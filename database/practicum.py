from pymongo import MongoClient
from fastapi import FastAPI, HTTPException, Query, Request
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from math import floor
import random
import time

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = MongoClient('mongodb://localhost', 27017)
db = client["practicum"]
alarm_collection = db["alarm"]

@app.get("/")
def alarmtime():
    result = alarm_collection.find({},{"_id":0})
    my_res = []
    for r in result:
        my_res.append(r["time"])
    my_res.sort()
    return{
        "result": my_res
    }

@app.get("/isalarm/")
def alarmtime():
    result = alarm_collection.find({},{"_id":0})
    my_res = False
    curtime = int(time.time()+ 7*3600) % 86400
    for r in result:
        if( floor(r["time"] / 60) == floor(curtime / 60)):
            my_res = True
    if(my_res):
        return{
            "result": "True"
        }
    else:
        return{
            "result": "False"
        }

@app.post("/newalarm/{hour}/{minute}")
def newalarm(hour : int , minute : int):
    if(hour > 24 or hour < 0 or minute > 60 or minute < 0):
        return{
            "result" : "invalid value of hour or minute"
        }
    time = hour * 3600 + minute * 60
    newentry = {
        "time" : time
    }
    test = alarm_collection.find_one(newentry)
    if test == None:
        alarm_collection.insert_one(newentry)
        return{
            "result" : "success"
        }
    else:
        return{
            "result" : "duplicate entry"
        }

@app.delete("/deletealarm/{hour}/{minute}")
def deletealarm(hour : int, minute : int):
    if(hour > 24 or hour < 0 or minute > 60 or minute < 0):
        return{
            "result" : "invalid value of hour or minute"
        }
    time = hour * 3600 + minute * 60
    query = {
        "time" : time
    }
    test = alarm_collection.find_one(query)
    if test == None:
        return{
            "result" : "not found"
        }
    else:
        alarm_collection.delete_one(query)
        return{
            "result" : "success"
        }

@app.delete("/deleteall")
def deletealarm():
    alarm_collection.delete_many({})
    return{
        "result" : "success"
    }