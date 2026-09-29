import pandas as pd
import requests
from bs4 import BeautifulSoup
'''
# url of Virginia Public Access Project page showing daily 2026 early vote totals
url = "https://election.lab.ufl.edu/early-vote/2026-early-voting/2026-general-election-early-vote-virginia/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

html = response.text

with open("data/raw/virginia_sample.html", "w", encoding="utf-8") as file:
    file.write(html)
'''

csv_url = 'https://election.lab.ufl.edu/data-downloads/earlyvote/2026/VA_county.csv'

df = pd.read_csv(csv_url)

print(df.head(10))

test = (df['inperson_all'] + df['accept_all'] == df['voted_all'])

print(df['county'].duplicated().any())