#curl -i -H "Content-Type: application/json" -X POST -d '{"x": 10,"y": 20,"zoom": 17}' http://localhost:5000/yamap/api/v1.0/fromGlobalPixels

import json
import requests

url = 'http://localhost:5000/yamap/api/v1.0/fromGlobalPixels'
payload = {"x": 10,"y": 20,"zoom": 17}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)
r_json = r.json()
print(r_json)
