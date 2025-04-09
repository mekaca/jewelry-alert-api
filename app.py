from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
latest_alert = {}

@app.route("/")
def home():
    return "✅ Jewelry Alert API çalışıyor"

@app.route("/alert", methods=["POST"])
def alert():
    global latest_alert
    data = request.json
    latest_alert = {
        "camera_id": data.get("camera_id"),
        "location": data.get("location"),
        "timestamp": datetime.utcnow().isoformat()
    }
    return jsonify({"status": "ok", "received": latest_alert})

@app.route("/latest", methods=["GET"])
def latest():
    if latest_alert:
        return jsonify(latest_alert)
    return jsonify({"message": "Henüz veri yok."})