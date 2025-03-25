import requests
import json
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)
VARIANTS = [
    "bullet", "blitz", "rapid", "classical", "chess960", "crazyhouse",
    "antichess", "atomic", "horde", "kingOfTheHill", "racingKings", "threeCheck"
]

LICHESS_API = "https://lichess.org/api/users"
BOTS_LIST = ["ToromBot", "AnotherBot", "Khanh_Bot"]  # Danh sách bot cần lấy Elo (có thể tự động cập nhật)

def fetch_all_bots():
    url = "https://lichess.org/api/player"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        bots = [player["id"] for player in data if player.get("title") == "BOT"]
        return bots
    print("Error fetching bot list:", response.status_code)
    return []

def fetch_bot_rankings():
    rankings = {variant: [] for variant in VARIANTS}
    bots = fetch_all_bots() if not BOTS_LIST else BOTS_LIST
    
    chunk_size = 100  # Lichess API giới hạn 300 người mỗi request, chia nhỏ để tránh lỗi
    for i in range(0, len(bots), chunk_size):
        chunk = bots[i:i + chunk_size]
        response = requests.post(LICHESS_API, json=chunk)
        if response.status_code == 200:
            bot_data = response.json()
            for bot in bot_data:
                username = bot["id"]
                for variant in VARIANTS:
                    if variant in bot["perfs"]:
                        rating = bot["perfs"][variant].get("rating", 0)
                        rankings[variant].append({"bot": username, "rating": rating})
        else:
            print("Error fetching bot data:", response.status_code)
    
    # Sắp xếp thứ hạng theo Elo giảm dần
    for variant in VARIANTS:
        rankings[variant].sort(key=lambda x: x["rating"], reverse=True)
    return rankings

def save_rankings(data):
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    with open("bot_rankings.json", "w", encoding="utf-8") as f:
        json.dump({"timestamp": timestamp, "data": data}, f, indent=4)

def main():
    rankings = fetch_bot_rankings()
    save_rankings(rankings)
    print("Rankings updated successfully!")

@app.route("/")
def home():
    return jsonify({"message": "Lichess Bot Rankings API is running!", "usage": "/rankings"})

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
