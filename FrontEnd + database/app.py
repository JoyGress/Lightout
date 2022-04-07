from operator import methodcaller
from aiohttp import request
from flask import Flask, render_template, url_for, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    r=requests.get("http://127.0.0.1:8000/")
    x=r.text
    json_acceptable_string = x.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    alarmlist = d.get("result")
    return render_template('index.html', alarm = alarmlist)

@app.route("/addalarm", methods = ['POST'])
def addalarm():
    hour = request.form["hour"]
    minute = request.form["minute"]
    add = requests.post(f"http://127.0.0.1:8000/newalarm/{hour}/{minute}")

    r=requests.get("http://127.0.0.1:8000/")
    x=r.text
    json_acceptable_string = x.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    alarmlist = d.get("result")
    return render_template('index.html', alarm = alarmlist)

if __name__ == "__main__":
    app.run(debug=True)