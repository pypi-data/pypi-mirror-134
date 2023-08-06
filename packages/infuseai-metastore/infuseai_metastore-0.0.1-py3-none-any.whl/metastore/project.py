import json
import configparser
from typing import Dict

from kafka import KafkaConsumer
from kafka import KafkaProducer

from metastore import create_logger, handlers
from metastore.artifacts import Record
from metastore.storage import Storage
from metastore.database import Database


class Project(object):

    def __init__(self, name: str, **kwargs):
        self.logger = create_logger('project')
        self.name = name

        kafka_config = dict()
        db_config = dict()

        # Load SDK profile
        profile = kwargs.get('profile', 'local')
        if profile == 'local' or profile == 'default':
            kafka_config['bootstrap_servers'] = '127.0.0.1:9092'
            db_config['hasura_server'] = 'http://127.0.0.1:8080'
            db_config['hasura_admin_secret'] = None
        else:
            config = configparser.ConfigParser()
            try:
                with open(f'{profile}.ini') as f:
                    config.read_file(f)
            except IOError:
                raise Exception(f'unknown profile {profile}')

            if 'kafka' in config.sections():
                kafka_config['bootstrap_servers'] = config['kafka']['bootstrap_servers']
                kafka_config['security_protocol'] = 'SASL_SSL'
                kafka_config['sasl_mechanism'] = 'SCRAM-SHA-256'
                kafka_config['sasl_plain_username'] = config['kafka']['sasl_plain_username']
                kafka_config['sasl_plain_password'] = config['kafka']['sasl_plain_password']
            if 'Hasura' in config.sections():
                db_config['hasura_server'] = config['Hasura']['Server']
                db_config['hasura_admin_secret'] = config['Hasura']['AdminSecret']

        self.kafka_config = kafka_config
        self.producer = KafkaProducer(**self.kafka_config)
        self.consumer = KafkaConsumer(**self.kafka_config)
        self.database = Database(db_config)

    def create(self, type: str, name: str, metadata: object = {}):
        record = Record()
        record.project = self
        record.storage = Storage()
        record.database = self.database
        record.type = type
        record.uid = record.generate_uuid()
        record.name = name
        record.metadata = metadata
        record.create()
        return record

    def get(self, type: str, uid_or_name: str):
        record = Record()
        record.project = self
        record.storage = Storage()
        record.database = self.database
        record.type = type
        return record.reload(uid_or_name)

    def find(self, type: str, contains: Dict = {}):
        where = {"type": {"_eq": type}, "metadata": {"_contains": contains}}
        records = self.database.get_nodes(where)
        return records

    def send_event(self, event: Dict):
        self.logger.info(f'send event => {self.name} {event}')
        future = self.producer.send(self.name, value=json.dumps(event).encode('utf-8'))
        future.get(timeout=10)

    def start_consumer(self):
        self.logger.info(f'wait events from {self.name}')
        self.consumer.subscribe([self.name])

    def run(self):
        self.start_consumer()

        for m in self.consumer:
            content = m.value
            try:
                incoming_event = json.loads(content.decode('utf-8'))
                if 'type' in incoming_event and 'event' in incoming_event and 'filters' in incoming_event:
                    self._invoke_handler_if_matches(incoming_event)
                else:
                    self.logger.warning(f'bad content {content}')
            except BaseException as e:
                self.logger.exception(f'cannot not handle the incoming event {content}')

    def _invoke_handler_if_matches(self, incoming_event):
        for h in handlers:
            if h['type'] != incoming_event['type']:
                continue

            cfg = h['configurations']
            if cfg['event'] != incoming_event['event']:
                continue

            matches = []
            for k, v in cfg.get('filter', {}).items():
                if k not in incoming_event['filters']:
                    matches.append(False)
                    continue
                if v != incoming_event['filters'][k]:
                    matches.append(False)
                    continue
                matches.append(True)

            if list(set(matches)) == [True] or list(set(matches)) == []:
                self.logger.info(f'invoke by {incoming_event}')
                h['handler']()
                continue
            else:
                self.logger.info(
                    f'skip by mismatching filter {cfg["filter"]} => {incoming_event}')
                continue

        self.logger.warning(f'no handlers match with {incoming_event}')
