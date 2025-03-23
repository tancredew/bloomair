from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

# Store the latest sensor data in memory
latest_data = {
    "co2": 0,
    "pm25": 0,
    "temp": 0,
    "humidity": 0,
    "noise": 0,
    "timestamp": ""
}

@app.route("/api/data", methods=["POST"])
def receive_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        latest_data["co2"] = data.get("co2", 0)
        latest_data["pm25"] = data.get("pm25", 0)
        latest_data["temp"] = data.get("temp", 0)
        latest_data["humidity"] = data.get("humidity", 0)
        latest_data["noise"] = data.get("noise", 0)
        latest_data["timestamp"] = datetime.datetime.utcnow().isoformat()
        return jsonify({"message": "Data received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/data/latest", methods=["GET"])
def get_latest_data():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run()
