from urllib import response
from fastapi import FastAPI
import requests
import json

app = FastAPI()

def get_json(urlVar):
    response = requests.get(urlVar)
    return response.json()

def create_json(singleJson):
    return {
        "id": singleJson["slug"],
        "title": singleJson["title"],
        "description": singleJson["description"]
    }


@app.get("/job")
def list_jobs():
    return jobs

json_list
