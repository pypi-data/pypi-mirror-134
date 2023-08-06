import requests
from typing import Dict, List

from metastore.utils import create_logger, is_valid_uuid4

logger = create_logger('database')


class Database(object):

    def __init__(self, config):
        self.base_url = config.get('hasura_server', 'http://localhost:8080')
        self.hasura_admin_secret = config.get('hasura_admin_secret', None)
        self.graphql_endpoint = self.base_url + '/v1/graphql'
        # Hasura only
        self._create_default_database()
        self._create_default_tables()

    def get_nodes(self, where: Dict = {}):
        return self._query_nodes(where)

    def get_edges(self, where: Dict = {}):
        return self._query_edges(where)

    def get_node_by_uid(self, uid: str):
        if not is_valid_uuid4(uid):
            return None

        nodes = self._query_nodes_by_uid(uid)
        return nodes[0]

    def get_node_by_type_and_name(self, type: str, name: str):
        nodes = self._query_nodes_by_type_and_name(type, name)
        return nodes[0]

    def add_node(self, node: Dict):
        self._insert_nodes(node)
        uid = node['uid']

        # Search and add edges
        edges = []
        for k, v in node['metadata'].items():
            if is_valid_uuid4(v):
                edges.append({'n1_uid': v,'n2_uid': uid, 'type': k})
        self._insert_edges(edges)

    def update_node(self, node: Dict):
        self._update_nodes(node)

    def _generate_headers(self):
        if self.hasura_admin_secret:
            return {'x-hasura-admin-secret': self.hasura_admin_secret}
        else:
            return None

    def post(self, path, data=None, json=None):
        headers = self._generate_headers()
        return requests.post(self.base_url + path, headers=headers, data=data, json=json)

    def graphql(self, data=None, json=None):
        headers = self._generate_headers()
        return requests.post(self.graphql_endpoint, headers=headers, data=data, json=json)

    # Hasura only
    def _fetch_sources(self):
        data = {"type": "export_metadata", "args": {}}
        res = self.post('/v1/metadata', json=data)
        if res.status_code != 200:
            logger.error('Failed to fetch source list')
            raise
        sources =  res.json()['sources']
        return sources

    # Hasura only
    def _fetch_tablenames(self):
        data = {
          "type": "run_sql",
          "args": {
            "source": "default",
            "sql": "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema'"
          }
        }
        res = self.post('/v2/query', json=data)
        if res.status_code != 200:
            logger.error('Failed to fetch tablenames')
            raise
        tablenames = res.json()['result']
        return tablenames

    # Hasura only
    def _create_default_database(self):
        sources = self._fetch_sources()
        for source in sources:
            if source['name'] == 'default':
                return

        data = {
            "type": "pg_add_source",
            "args": {
                "name": "default",
                "configuration": {
                    "connection_info": {
                        "database_url": {
                            "from_env": "PG_DATABASE_URL"
                        },
                        "pool_settings": {
                            "retries": 1,
                            "idle_timeout": 180,
                            "max_connections": 50
                        }
                    }
                }
            }
        }

        logger.info('Add default source')
        res = self.post('/v1/metadata', json=data)
        if res.status_code != 200:
            logger.error('Failed to add default source')
            raise

    # Hasura only
    def _create_default_tables(self):
        tablenames = self._fetch_tablenames()
        if ['nodes'] in tablenames and ['edges'] in tablenames:
            return

        self._create_tables()
        self._track_tables()


    # Hasura only
    def _create_tables(self):
        data = {
          "type": "run_sql",
          "args": {
            "source": "default",
            "sql": "CREATE TABLE nodes(uid UUID PRIMARY KEY NOT NULL, type TEXT NOT NULL, name TEXT NOT NULL, created_at TIMESTAMP DEFAULT NOW(), updated_at TIMESTAMP DEFAULT NOW(), metadata JSONB)"
          }
        }

        res = self.post('/v2/query', json=data)
        if res.status_code != 200:
            logger.error('Failed to create table nodes')
            raise

        data['args']['sql'] = "CREATE TABLE edges(n1_uid UUID NOT NULL, n2_uid UUID NOT NULL, created_at TIMESTAMP DEFAULT NOW(), updated_at TIMESTAMP DEFAULT NOW(), type TEXT, metadata JSONB)"
        res = self.post('/v2/query', json=data)
        if res.status_code != 200:
            logger.error('Failed to create table edges')
            raise
        return res.json()

    # Hasura only
    def _track_tables(self):
        data = {
          "type": "pg_track_table",
          "args": {
            "source": "default",
            "schema": "public",
            "name": "nodes"
          }
        }

        res = self.post('/v1/metadata', json=data)
        if res.status_code != 200:
            logger.error('Failed to track table nodes')
            raise

        data['args']['name'] = 'edges'
        res = self.post('/v1/metadata', json=data)
        if res.status_code != 200:
            logger.error('Failed to track table edges')
            raise
        return res.json()

    # Hasura only
    def _query_nodes(self, where: Dict):
        query = """
        query query_nodes($where: nodes_bool_exp!, $order_by: [nodes_order_by!]) {
          nodes(where: $where, order_by: $order_by) {
            updated_at
            uid
            name
            type
            created_at
            metadata
          }
        }
        """

        variables = {
            'where': where,
            'order_by': {
                'created_at': "desc"
            }
        }
        res = self.graphql(json={"query": query, "variables": variables})
        if res.status_code != 200:
            logger.error('Failed to query_nodes')
            raise

        res_json = res.json()
        if 'errors' in res_json:
            logger.info(res.text)
            return None

        nodes = res_json['data']['nodes']
        if nodes:
            return nodes
        return None

    # Hasura only
    def _query_nodes_by_uid(self, uid: str):
        where = {"uid": {"_eq": uid}}
        return self._query_nodes(where)

    # Hasura only
    def _query_nodes_by_type_and_name(self, type: str, name: str):
        where = {"type": {"_eq": type}, "name": {"_eq": name}}
        return self._query_nodes(where)

    # Hasura only
    def _insert_nodes(self, node: Dict):
        query = """
        mutation insert_nodes($object: [nodes_insert_input!]!) {
          insert_nodes(objects: $object) {
            returning {
              uid
              type
              name
              metadata
              created_at
              updated_at
            }
          }
        }
        """

        variables = {'object': [node]}
        res = self.graphql(json={"query": query, "variables": variables})
        if res.status_code != 200:
            logger.error('Failed to insert_nodes')
            raise

        res_json = res.json()
        if 'errors' in res_json:
            logger.info(res.text)
            return None

        logger.info(res.text)
        return res_json['data']['insert_nodes']['returning']

    # Hasura only
    def _update_nodes(self, node: Dict):
        query = """
        mutation update_nodes($_set: nodes_set_input!, $where: nodes_bool_exp!) {
          update_nodes(_set: $_set, where: $where) {
            returning {
              uid
              type
              name
              metadata
              created_at
              updated_at
            }
          }
        }
        """

        variables = {'_set': node, 'where': {"uid": {"_eq": node["uid"]}}}
        res = self.graphql(json={"query": query, "variables": variables})
        if res.status_code != 200:
            logger.error('Failed to update_nodes')
            raise

        res_json = res.json()
        if 'errors' in res_json:
            logger.info(res.text)
            return None

        return res_json['data']['update_nodes']['returning']

    # Hasura only
    def _query_edges(self, where: Dict):
        query = """
        query query_edges($where: edges_bool_exp!) {
          edges(where: $where) {
            n1_uid
            n2_uid
            type
            metadata
            created_at
            updated_at
          }
        }
        """

        variables = {'where': where}
        res = self.graphql(json={"query": query, "variables": variables})
        if res.status_code != 200:
            logger.error('Failed to query_edges')
            raise

        res_json = res.json()
        if 'errors' in res_json:
            logger.info(res.text)
            return None

        edges = res_json['data']['edges']
        if edges:
            return edges
        return None

    # Hasura only
    def _insert_edges(self, edges: List):
        query = """
        mutation insert_edges($object: [edges_insert_input!]!) {
          insert_edges(objects: $object) {
            returning {
              n1_uid
              n2_uid
              type
              metadata
              created_at
              updated_at
            }
          }
        }
        """

        variables = {'object': edges}
        res = self.graphql(json={"query": query, "variables": variables})
        if res.status_code != 200:
            logger.error('Failed to insert_edges')
            raise

        res_json = res.json()
        if 'errors' in res_json:
            logger.info(res.text)
            return None

        logger.info(res.text)
        return res_json['data']['insert_edges']['returning']

