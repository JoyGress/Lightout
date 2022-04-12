import requests
import time
import json

while(1):
    r=requests.get("http://127.0.0.1:8000/")
    x=r.text
    json_acceptable_string = x.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    print(d.get("result"))
    time.sleep(10)