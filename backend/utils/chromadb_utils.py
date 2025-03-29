import requests
from django.conf import settings

class ChromaDBUtils:
    def __init__(self):
        self.base_url = f"http://{settings.CHROMADB_HOST}:{settings.CHROMADB_PORT}/api"

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url)
        response.raise_for_status()
        return response.json()
