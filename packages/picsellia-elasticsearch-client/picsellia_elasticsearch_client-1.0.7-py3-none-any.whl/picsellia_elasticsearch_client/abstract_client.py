from abc import ABC, abstractmethod
from .document import PicselliaESDocument


class AbstractPicselliaESClient(ABC):

    @abstractmethod
    def push(self, index : str, document : PicselliaESDocument) -> str:
        """Create a document into Elasticsearch client

        Args:
            index (str): name of the index where document should be pushed
            document (PicselliaElasticDocument): picsellia document to push

        Returns:
            str: id of the document inserted
        """
        pass

    @abstractmethod
    def read(self, index : str, id : str) -> dict:
        """Read a document from Elasticsearch client

        Args:
            index (str): index to search
            id (str): of the document

        Returns:
            dict: document retrieved
        """
        pass