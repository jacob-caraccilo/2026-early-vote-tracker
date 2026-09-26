import pandas as pd
import requests
from bs4 import BeautifulSoup

# url of Virginia Public Access Project page showing daily 2026 early vote totals
url = "https://election.lab.ufl.edu/early-vote/2026-early-voting/2026-general-election-early-vote-virginia/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

html = response.text

with open("data/raw/virginia_sample.html", "w", encoding="utf-8") as file:
    file.write(html)