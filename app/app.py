from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "DevOps Assignment Application",
        "status": "Running",
        "hostname": socket.gethostname()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route("/version")
def version():
    return jsonify({
        "version": "1.0.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)