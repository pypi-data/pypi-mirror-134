import os
from innocuous_api import InnocuousAPI

class InnocuousSDK:
    def __init__(self, token=None, **kwargs):
        self.version = "1.0.0"
        if token:
            self.token = token
        else:
            self.token = os.getenv("INNOCUOUSBOOK_TOKEN", "")

        self.api = InnocuousAPI(self.token, **kwargs)

    def get_experiment(self, id):
        return self.api.get_experiment(id)

    def get_endpoint(self, id):
        return self.api.get_endpoint(id)

    def list_experiments(self):
        return self.api.list_experiment()

    def list_endpoints(self):
        return self.api.list_endpoint()

    def get_experiment_id_by_name(self, name):
        result = [endpoint for endpoint in self.list_experiment() if endpoint["name"] == name]
        if len(result) != 0:
            return result[0]['id']
        else:
            return None

    def get_endpoint_id_by_name(self, name):
        result = [endpoint for endpoint in self.list_endpoint() if endpoint["name"] == name]
        if len(result) != 0:
            return result[0]['id']
        else:
            return None

    def predict(self, id, data):
        return self.api.call_endpoint_predict(id, data)

    def predict_file(self, id, files):
        return self.api.call_endpoint_predict_file(id, files)

    def continous_learning(self, id, dataset):
        return self.api.call_endpoint_continous_learning(id, dataset)
