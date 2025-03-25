import requests
import json
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)
VARIANTS = [
    "bullet", "blitz", "rapid", "classical", "chess960", "crazyhouse",
    "antichess", "atomic", "horde", "kingOfTheHill", "racingKings", "threeCheck"
]

def fetch_bot_rankings():
    rankings = {}
    for variant in VARIANTS:
        url = f"https://lichess.org/api/player/top/10/{variant}"
        response = requests.get(url)
        if response.status_code == 200:
            rankings[variant] = response.json()
        else:
            print(f"Error fetching {variant} rankings:", response.status_code)
            rankings[variant] = []
    return rankings

def save_rankings(data):
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    with open("bot_rankings.json", "w", encoding="utf-8") as f:
        json.dump({"timestamp": timestamp, "data": data}, f, indent=4)

def main():
    rankings = fetch_bot_rankings()
    save_rankings(rankings)
    print("Rankings updated successfully!")

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
