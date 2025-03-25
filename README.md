# Lichess Bot Rankings

## Introduction
This repository collects bot rankings on Lichess for all chess variants. The data is automatically updated daily via GitHub Actions.

## Usage
### Run the script manually
1. Install Python 3 and the required libraries:
   ```sh
   pip install flask requests
   ```
2. Run the script to update the rankings:
   ```sh
   python script.py
   ```
3. Start the API to fetch data:
   ```sh
   python script.py
   ```
   Access `http://localhost:5000/rankings` to view the data.

## Repository Structure
- `script.py`: Fetches data from the Lichess API and runs the Flask API.
- `bot_rankings.json`: Stores the latest bot rankings.
- `.github/workflows/update_rankings.yml`: Automates daily updates of rankings.

## API
- `GET /rankings`: Returns bot rankings for each chess variant.

## Automatic Updates
GitHub Actions runs the script daily to update bot rankings and commits the `bot_rankings.json` file to the repository.

## Contributing
If you want to improve this repository, feel free to open a pull request or an issue!

