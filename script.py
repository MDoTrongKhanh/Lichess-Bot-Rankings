import requests
import json
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

def fetch_bot_rankings():
    url = "https://lichess.org/api/player/top/10/bot"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching rankings:", response.status_code)
        return None

def save_rankings(data):
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    with open("bot_rankings.json", "w", encoding="utf-8") as f:
        json.dump({"timestamp": timestamp, "data": data}, f, indent=4)

def main():
    rankings = fetch_bot_rankings()
    if rankings:
        save_rankings(rankings)
        print("Rankings updated successfully!")
    else:
        print("Failed to update rankings.")

@app.route("/rankings", methods=["GET"])
def get_rankings():
    try:
        with open("bot_rankings.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "No rankings available"}), 404

if __name__ == "__main__":
    main()
    app.run(host='0.0.0.0', port=5000)
