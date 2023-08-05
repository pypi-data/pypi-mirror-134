from datetime import datetime

class PicselliaESDocument():

    def __init__(self, metric_type : str, data : dict) -> None:
        self.metric_type = metric_type
        self.service = 'unknown'
        self.timestamp = datetime.now()
        self.data = data

    def toBody(self):
        body = dict()
        body["_service"] = self.service
        body["_metric_type"] = self.metric_type
        body["_timestamp"] = self.timestamp

        for key in self.data:
            body[key] = self.data[key]
       
        return body