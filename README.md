# Lichess Bot Rankings

This is an API that ranks Lichess bots based on their Elo ratings across different chess variants.

## 🚀 Main Features
- Ranks bots based on actual Elo instead of just fetching the top 10 from Lichess API.
- Supports multiple chess variants: Bullet, Blitz, Rapid, Classical, Chess960, etc.
- Automatically updates the bot list.
- No need for `/player/top/10/variant` API, only uses `/users` API.

## 🔧 Usage

### 1. Run the API
Install the required dependencies:
```bash
pip install flask requests
```
Then start the server:
```bash
python app.py
```
The API will run at `http://localhost:5000/`

### 2. Endpoints
- `GET /rankings` → Retrieves the bot rankings by Elo.
- `GET /` → Checks if the API is running.

## 🛠 Structure
- `app.py` → Main API code.
- `bot_rankings.json` → Stores ranking data.
- `requirements.txt` → Lists required dependencies.

## 📌 Notes
- If a bot is missing from the list, add it manually in `BOTS_LIST` inside `app.py`.
- To automatically fetch bot names, update `BOTS_LIST = fetch_all_bots()` to retrieve them from Lichess.

Happy coding! 🚀
