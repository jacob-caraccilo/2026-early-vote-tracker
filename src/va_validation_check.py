"""
Virginia early-vote source columns:

county       - locality name
cd           - congressional district of locality
sdl          - Virginia House of Delegates district of locality
sdu          - Virginia Senate district of locality
request_all  - number of mail-in ballots requested
accept_all   - number of accepted mail-in ballots
inperson_all - number of in-person ballots cast
voted_all    - total early votes cast | accept_all + ineprson_all
return_rate  - portion of mail-in ballots returned | accept_all / request_all
"""

import pandas as pd
import numpy as np

csv_url = 'https://election.lab.ufl.edu/data-downloads/earlyvote/2026/VA_county.csv'

df = pd.read_csv(csv_url)

# the following code conducts validation testing on the new csv file to ensure
# data quality and accuracy

# checks that votes_all = accept_all + inperson_all
votes_all_test = (df['voted_all'] == df['accept_all'] + df['inperson_all'])

votes_all_result = votes_all_test.all()

# checks that all counties only have one row

unique_localities_test = df['county'].duplicated().any()

unique_localities_result = not unique_localities_test

# checks that length of csv to confirm all localities are present
# Virginia contains 133 counties and county-level equivalents

complete_localities_result = (len(df) == 133)

# checks that return_rate reflects the true returned ratio

print(df['return_rate'].dtype)


