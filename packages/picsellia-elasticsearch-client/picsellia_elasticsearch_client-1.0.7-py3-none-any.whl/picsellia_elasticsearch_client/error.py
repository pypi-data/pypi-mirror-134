from .document import PicselliaESDocument

class PicselliaESError(PicselliaESDocument):

    def __init__(self, data : dict) -> None:
        super().__init__(metric_type = 'error', data=data)