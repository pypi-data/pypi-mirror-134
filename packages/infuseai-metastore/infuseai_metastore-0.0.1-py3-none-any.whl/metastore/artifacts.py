import json
import uuid
from typing import Dict


class Record(object):
    """
    Record is a metadata file related to the real resources in the metastore

    /{artifact}/{uid}/metadata.json
    /{artifact}/{uid}/store/...

    When the metadata changed, it should create an event to the event-stream.
    """

    def __init__(self, **kwargs):
        self.storage = None
        self.database = None
        self.name = None
        self.uid = None
        self.type = None
        self.metadata = {}

    def generate_uuid(self):
        return str(uuid.uuid4())

    def reload(self, uid_or_name):
        content = self.database.get_node_by_uid(uid_or_name) or \
                  self.database.get_node_by_type_and_name(self.type, uid_or_name) or \
                  None
        if content is None:
            return None

        for k, v in content.items():
            if hasattr(self, k):
                setattr(self, k, v)
        return self

    def create(self):
        self._check_state()
        self.database.add_node(self._build_graphql_input())
        self.project.send_event(self.event('created', filters={'name': self.name}))

    def update(self):
        self._check_state()
        self.database.update_node(self._build_graphql_input())
        self.project.send_event(self.event('updated', filters={'name': self.name}))

    def _build_graphql_input(self):
        return {
            'uid': self.uid,
            'type': self.type,
            'name': self.name,
            'metadata': self._build_metadata(dict(self.metadata))
        }

    # loop over nested dictionary and replace Record with uid
    def _build_metadata(self, metadata: Dict):
        for k, v in metadata.items():
            if isinstance(v, Dict):
                self._build_metadata(v)
            elif isinstance(v, Record):
                metadata[k] = v.uid
        return metadata

    def exists(self):
        self._check_state()
        return self.has_metadata() and self.has_name_mapping()

    def event(self, event_type, filters: Dict = None):
        self._check_state()
        return dict(uid=self.uid, type=self.type, event=event_type, filters=filters if filters else {})

    def _check_state(self):
        if self.type is None:
            raise ValueError('type cannot be None')
        if self.uid is None:
            raise ValueError('uid cannot be None')
        if self.name is None:
            raise ValueError('name cannot be None')

    def annotate(self, key: str, value: str):
        self.metadata[key] = value
