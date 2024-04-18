import requests
from bs4 import BeautifulSoup

# Define the base URL of the API
base_url = "http://localhost:3001"  # Assuming the API is running locally on port 3001

# Define the endpoint URLs
live_score_endpoint = "/match/live_score"


# Make requests to the API endpoints
def get_live_matches():
    response = requests.get(base_url + live_score_endpoint)
    return response.json()


# Parse vlr.gg site containing live matches using BeautifulSoup library
def getOdds(url, live_score, index):
    # Send a GET request to the URL and parse the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the <span> elements containing the betting odds
    betting_odds_1 = soup.select_one("#wrapper > div.col-container > div.col.mod-3 > div:nth-child(2) > a > "
                                     "div:nth-child(1) > div:nth-child(2) > span.match-bet-item-odds.mod-down.mod-1")
    betting_odds_2 = soup.select_one("#wrapper > div.col-container > div.col.mod-3 > div:nth-child(2) > a >"
                                     " div:nth-child(3) > div:nth-child(1) > span.match-bet-item-odds.mod-up.mod-2")

    # Extract the odds value if available
    odds_1 = betting_odds_1.text.strip() if betting_odds_1 else "N/A"
    odds_2 = betting_odds_2.text.strip() if betting_odds_2 else "N/A"

    # Get the team names from the live_score JSON object based on the index
    team_1_name = live_score['data']['segments'][index]['team1']
    team_2_name = live_score['data']['segments'][index]['team2']

    return odds_1, odds_2, team_1_name, team_2_name


def printOdds(urls, scores):

    # Print entire JSON object containing data about current live matches
    print(scores)
    print()

    # Iterate over match page URLs and print betting odds
    for i, url in enumerate(urls, start=1):
        odds_1, odds_2, team_1_name, team_2_name = getOdds(url, scores, i - 1)
        print(f"Match {i} URL:", url)
        print(f"{team_1_name} Betting Odds:", odds_1)
        print(f"{team_2_name} Betting Odds:", odds_2)

        # Calculate odds ratio
        # NOTE: Higher odds yield higher payouts, Lower odds yield lower payouts
        if odds_1 != "N/A" and odds_1 != "N/A":
            # Cast betting odds from string to float
            odds_1 = float(odds_1)
            odds_2 = float(odds_2)
            if odds_1 > odds_2:
                ratio = odds_1/odds_2
            elif odds_1 < odds_2:
                ratio = odds_2/odds_1
            else:
                ratio = "N/A"
        else:
            ratio = "N/A"

        print("Ratio: ", ratio)
        print()  # Add a newline for better readability


# Pull entire JSON object from API
if __name__ == "__main__":
    live_score = get_live_matches()
    match_page_urls = []

    # Fix the match_page URLs by appending '/' after '.gg' and add to match_page_urls
    for segment in live_score['data']['segments']:
        segment['match_page'] = segment['match_page'].replace('vlr.gg', 'vlr.gg/')
        match_page_url = segment['match_page']
        match_page_urls.append(match_page_url)

    # Call the printOdds function to print the odds for each match
    printOdds(match_page_urls, live_score)
