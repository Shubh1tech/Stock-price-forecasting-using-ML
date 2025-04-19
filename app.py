from flask import Flask, json, request
from pymongo import MongoClient

import requests


app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client.admin
collection = db.AmsterdamListings


@app.route("/getAllAmsterdamListings", methods=["GET"])
def getAllData():
    getAllData = list(collection.find({},{"name": 1, "id": 1, "host_name": 1, "minimum_nights": 1, "price": 1}))
    return json.dumps(getAllData, default = str)

@app.route("/byHostName", methods = ["POST"])
def getByHostName():
    getHostName = request.form.get("host_name")
    getAllDataByHost = list(collection.find({"host_name": {"$regex": f"^{getHostName}", "$options": "i"}}))
    return json.dumps(getAllDataByHost, default=str)


if __name__ == "__main__":
    app.run(debug=True, port=8080) 