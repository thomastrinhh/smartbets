## Betting Odds Scraper

This repository contains a Python script that scrapes betting odds for Valorant matches from vlr.gg and calculates odds ratios for potential betting opportunities. Additionally, it utilizes a FastAPI-based REST API to retrieve live match scores and other data related to Valorant esports.

## Getting Started

To use this script, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the FastAPI server by executing `python main.py` in the `api` directory.
4. Run the Python script `betting_odds_scraper.py` to fetch live match scores and corresponding betting odds.

## Prerequisites

- Python 3.x
- FastAPI
- BeautifulSoup
- Requests

## Usage

The `analytics.py` script retrieves live match scores from the FastAPI server and extracts betting odds from vlr.gg for each match. It then calculates odds ratios for potential betting opportunities.

To run the script:

```bash
1. python main.py
2. python analytics.py

## Acknowledgments

The FastAPI server used in this project is based on the vlrggapi repository, an unofficial REST API for vlr.gg created by axsddlr. Special thanks to axsddlr for providing the unofficial REST API for vlr.gg.

## License
This project is licensed under the MIT License.
