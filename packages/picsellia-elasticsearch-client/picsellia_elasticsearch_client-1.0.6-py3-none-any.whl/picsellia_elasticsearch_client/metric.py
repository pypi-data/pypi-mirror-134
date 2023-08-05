from .document import PicselliaESDocument

class PicselliaESMetric(PicselliaESDocument):

    def __init__(self, data : dict) -> None:
        super().__init__(metric_type = 'metric', data=data)