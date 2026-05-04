from flask import Flask, request, jsonify, send_from_directory
from pyatem import ATEM

app = Flask(__name__)

# 🔧 WPISZ IP SWOJEGO ATEM MINI PRO
ATEM_IP = "192.168.1.50"

atem = ATEM()
atem.connect(ATEM_IP)

PRESETS = {
    "youtube": {
        "url": "rtmp://a.rtmp.youtube.com/live2",
        "key": "WPISZ-SWOJ-KLUCZ"
    },
    "facebook": {
        "url": "rtmp://live-api-s.facebook.com:80/rtmp/",
        "key": "WPISZ-SWOJ-KLUCZ"
    },
    "rtmp1": {
        "url": "rtmp://192.168.1.10/live",
        "key": "stream1"
    }
}

@app.route("/set-stream", methods=["POST"])
def set_stream():
    data = request.json
    url = data["url"]
    key = data["key"]

    atem.set_stream(url, key)
    return jsonify({"status": "OK", "message": "Stream updated"})

@app.route("/preset/<name>", methods=["POST"])
def preset(name):
    if name not in PRESETS:
        return jsonify({"status": "ERROR", "message": "Preset not found"}), 404

    p = PRESETS[name]
    atem.set_stream(p["url"], p["key"])
    return jsonify({"status": "OK", "message": f"Preset {name} ustawiony"})

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

app.run(host="0.0.0.0", port=3000)
