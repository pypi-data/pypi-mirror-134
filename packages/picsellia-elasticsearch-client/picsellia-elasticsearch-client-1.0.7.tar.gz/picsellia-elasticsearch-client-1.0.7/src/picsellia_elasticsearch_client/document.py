from datetime import datetime
from typing import Union

class PicselliaESDocument():

    def __init__(self, metric_type : str, data : dict) -> None:
        self.metric_type = metric_type

        if "_service" not in data:
            self.service = 'unknown'
        else:
            self.service = data["_service"]
            del data["_service"]
        
        if "_timestamp" not in data:
            self.timestamp = datetime.now()
        else:
            self.timestamp = data["_timestamp"]
            del data["_timestamp"]

        self.data = data

    def toBody(self):
        body = dict()
        body["_service"] = self.service
        body["_metric_type"] = self.metric_type
        body["_timestamp"] = self.timestamp

        for key in self.data:
            body[key] = self.data[key]
       
        return body