# Author: Thomas Trinh
# File: backup.py
# Purpose: Initial implementation of analytics.py.

import requests
from bs4 import BeautifulSoup

# Define the base URL of the API
base_url = "http://localhost:3001"  # Assuming the API is running locally on port 3001

# Define the endpoint URLs
live_score_endpoint = "/match/live_score"


# Make requests to the API endpoints
def get_live_score():
    response = requests.get(base_url + live_score_endpoint)
    return response.json()


# Pull entire JSON object from API
if __name__ == "__main__":
    live_score = get_live_score()

    # Declare empty array to store match URLs
    match_page_urls = []

    # Fix the match_page URLs by appending '/' after '.gg'
    for segment in live_score['data']['segments']:
        segment['match_page'] = segment['match_page'].replace('vlr.gg', 'vlr.gg/')
        match_page_url = segment['match_page']
        match_page_urls.append(match_page_url)

    # Print entire JSON object containing live score data
    print("Fixed Live Score:", live_score)

    # Print entire array containing match URLs
    print("Total Match URLs:", match_page_urls)

    # Iterate over match page URLs and retrieve betting odds and scores
    for i, url in enumerate(match_page_urls, start=1):
        # Send a GET request to the URL and parse the HTML content
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the <span> elements containing the betting odds
        betting_odds_1 = soup.find("span", class_="match-bet-item-odds mod- mod-1")
        betting_odds_2 = soup.find("span", class_="match-bet-item-odds mod- mod-2")

        # Find the <div> elements containing the scores
        score_1 = soup.find("div", class_="team1-score")
        score_2 = soup.find("div", class_="team2-score")

        # Extract the scores if available
        team_1_score = score_1.text.strip() if score_1 else "N/A"
        team_2_score = score_2.text.strip() if score_2 else "N/A"

        # Extract the team names from the URL
        team_1_name = live_score['data']['segments'][i-1]['team1']
        team_2_name = live_score['data']['segments'][i-1]['team2']

        # If betting odds are found, extract the odds value
        if betting_odds_1 and betting_odds_2:
            betting_odds_1 = betting_odds_1.text.strip()
            betting_odds_2 = betting_odds_2.text.strip()
            print(f"Match {i} URL:", url)
            print(f"{team_1_name} Betting Odds:", betting_odds_1)
            print(f"{team_2_name} Betting Odds:", betting_odds_2)
        else:
            print(f"Match {i} URL:", url)
            print("Betting odds not found on the page.")

        # Print scores
        print(f"{team_1_name} Score:", team_1_score)
        print(f"{team_2_name} Score:", team_2_score)

        print()  # Add a newline for better readability




