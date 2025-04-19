from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route("/getAllStudentDetails", methods=["GET"])
def test_json():
    api_response = {
        "firstName": "Shubh",
        "lastName": "Singh",
        "age": 24,
        "college": {
            "name":"Chandigarh University",
            "city":"Mohali",
            "branch": "CSE"
        },
        "time": datetime.datetime.now()
    } 
    return jsonify(api_response)

if __name__ == "__main__":
    app.run(port=8080)