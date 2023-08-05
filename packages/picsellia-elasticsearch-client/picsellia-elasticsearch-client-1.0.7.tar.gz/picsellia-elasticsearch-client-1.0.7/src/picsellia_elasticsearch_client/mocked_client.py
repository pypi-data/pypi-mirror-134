from typing import Any, List, Mapping, Union
from elasticmock import elasticmock
import elasticsearch

from picsellia_elasticsearch_client.client import PicselliaESClient
from .document import PicselliaESDocument
from .abstract_client import AbstractPicselliaESClient
import logging

class MockedPicselliaESClient(AbstractPicselliaESClient):

    @elasticmock
    def __init__(self, service : str) -> None:
        self.service = service

        self.client = PicselliaESClient(es_host="localhost", es_port=9200, service=service)

        logging.debug('Mocked client of ES for service {}'.format(service))

    @elasticmock
    def push(self, index : str, document : PicselliaESDocument) -> str:
        return self.client.push(index, document)

    @elasticmock
    def read(self, index : str, id : str) -> dict:
        return self.client.read(index, id)

    @elasticmock
    def search_document(self, body : Mapping[str, Any], index : Union[List[str], str], size : Union[int, None] = None, sort : Union[List[str], str, None] = None) -> dict:
        return self.client.search_document(body, index, size, sort)