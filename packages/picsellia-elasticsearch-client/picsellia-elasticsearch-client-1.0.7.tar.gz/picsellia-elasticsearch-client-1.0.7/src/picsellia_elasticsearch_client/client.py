from typing import Any, List, Mapping, Union
import elasticsearch
from .alert import PicselliaESAlert
from .error import PicselliaESError
from .metric import PicselliaESMetric
from .document import PicselliaESDocument
from .abstract_client import AbstractPicselliaESClient
import logging

class PicselliaESClient(AbstractPicselliaESClient):

    def __init__(self, service : str, es_host: str, es_port : int, username : str = None, password : str = None,) -> None:
        self.service = service

        hosts = [{ 'host' : es_host, 'port' : es_port}]
        if username != None and password != None:
            http_auth=(username, password)
            self.elasticsearch_client = elasticsearch.Elasticsearch(hosts=hosts, http_auth=http_auth)
        else:
            self.elasticsearch_client = elasticsearch.Elasticsearch(hosts=hosts)
        
        

        logging.debug('Connected to ES at {}:{}'.format(es_host, es_port))

    def push(self, index : str, document : PicselliaESDocument) -> str:
        
        document.service = self.service

        object = self.elasticsearch_client.index(index=index, body=document.toBody())

        id = object.get('_id')

        logging.debug('Pushed object with id {} to ES'.format(id))

        return id

    def read(self, index : str, id : str) -> PicselliaESDocument:

        object = self.elasticsearch_client.get(index=index, id=id)

        return self.__from_source_to_document(object.get('_source'))

    def search_document(self, body : Mapping[str, Any], index : Union[List[str], str], size : Union[int, None] = None, sort : Union[List[str], str, None] = None) -> List[PicselliaESDocument]:
        documents = []

        objects = self.elasticsearch_client.search(body=body, index=index, size=size, sort=sort)
        if objects == None or objects['hits']['total']['value'] == 0:
            return []

        for object in objects["hits"]['hits']:
            documents.append(self.__from_source_to_document(object['_source']))

        return documents


    def __from_source_to_document(self, data : dict) -> PicselliaESDocument:
        if "_metric_type" not in data:
            return PicselliaESDocument('unknown', data)
    
        metric_type = data["_metric_type"]
        if metric_type == "error":
            return PicselliaESError(data)
        elif metric_type == "alert":
            return PicselliaESAlert(data)
        elif metric_type == "metric":
            return PicselliaESMetric(data)
        else:
            return PicselliaESDocument(metric_type, data)
