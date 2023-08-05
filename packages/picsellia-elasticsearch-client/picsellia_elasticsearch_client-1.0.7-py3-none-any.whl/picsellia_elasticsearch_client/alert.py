from .document import PicselliaESDocument

class PicselliaESAlert(PicselliaESDocument):

    def __init__(self, data : dict) -> None:
        super().__init__(metric_type = 'alert', data=data)