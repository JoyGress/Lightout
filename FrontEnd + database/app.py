from operator import methodcaller
from aiohttp import request
from flask import Flask, render_template, url_for, request, redirect
from math import floor
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
    minutelist = []
    hourlist = []
    for i in range(len(alarmlist)):
        tmp = str(floor((alarmlist[i] % 3600 ) / 60 ))
        if(len(tmp) == 1):
            tmp = '0' + tmp
        minutelist.append(tmp)
        hourlist.append(floor(alarmlist[i] / 3600))
    return render_template('index.html', minute = minutelist, hour = hourlist, listlen = len(hourlist))

@app.route("/addalarm", methods = ['POST'])
def addalarm():
    hour = request.form["hour"]
    minute = request.form["minute"]
    add = requests.post(f"http://127.0.0.1:8000/newalarm/{hour}/{minute}")
    return redirect(request.referrer)

@app.route("/delalarm", methods = ['POST'])
def delalarm():
    hour = request.form["hour"]
    minute = request.form["minute"]
    add = requests.delete(f"http://127.0.0.1:8000/deletealarm/{hour}/{minute}")
    return redirect(request.referrer)

if __name__ == "__main__":
    app.run(debug=True)