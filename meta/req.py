import requests
from pprint import pprint

endpoint = "http://127.0.0.1:8000/fetchMeta"
res = requests.get(endpoint)
pprint(res.json())