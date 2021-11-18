# %%
"""
This file has to do with all data preprocessing needed for data.
Then import corresping dataframe to required file.
"""
import pandas as pd
import numpy as np

# %%
points_table = pd.read_csv('../data/merged/points_table.csv')
season_batting_card = pd.read_csv('../data/merged/season_batting_card.csv')
season_bowling_card = pd.read_csv('../data/merged/season_bowling_card.csv')
season_details = pd.read_csv('../data/merged/season_details.csv', low_memory = False)
season_summary = pd.read_csv('../data/merged/season_summary.csv')

# %%
points_table_df = pd.DataFrame(points_table)
season_batting_card_df = pd.DataFrame(season_batting_card)
season_bowling_card_df = pd.DataFrame(season_bowling_card)
season_details_df = pd.DataFrame(season_details)
season_summary_df = pd.DataFrame(season_summary)

# %%
points_table_df.replace('KXIP', 'PBKS', inplace=True, regex=True)
season_batting_card_df.replace('KXIP', 'PBKS', inplace=True, regex=True)
season_bowling_card_df.replace('KXIP', 'PBKS', inplace=True, regex=True)
season_details_df.replace('KXIP', 'PBKS', inplace=True, regex=True)
season_summary_df.replace('KXIP', 'PBKS', inplace=True, regex=True)

points_table_df.replace('Kings XI Punjab', 'Punjab Kings', inplace=True, regex=True)
season_batting_card_df.replace('Kings XI Punjab', 'Punjab Kings', inplace = True,regex=True)
season_bowling_card_df.replace('Kings XI Punjab', 'Punjab Kings', inplace = True, regex=True)
season_details_df.replace('Kings XI Punjab', 'Punjab Kings', inplace = True, regex=True)
season_summary_df.replace('Kings XI Punjab', 'Punjab Kings', inplace = True, regex=True)

# %%
points_table.to_csv('../data/processed/points_table.csv', index=False)
season_batting_card.to_csv('../data/processed/season_batting_card.csv', index=False)
season_bowling_card.to_csv('../data/processed/season_bowling_card.csv', index=False)
season_details.to_csv('../data/processed/season_details.csv', index=False)
season_summary.to_csv('../data/processed/season_summary.csv', index=False)


