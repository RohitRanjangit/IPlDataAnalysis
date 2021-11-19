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
points_table_df.replace('Deccan Chargers', 'Sunrisers Hyderabad', inplace=True, regex=True)
season_batting_card_df.replace('Deccan Chargers', 'Sunrisers Hyderabad', inplace = True,regex=True)
season_bowling_card_df.replace('Deccan Chargers',  'Sunrisers Hyderabad', inplace = True, regex=True)
season_details_df.replace('Deccan Chargers', 'Sunrisers Hyderabad', inplace = True, regex=True)
season_summary_df.replace('Deccan Chargers', 'Sunrisers Hyderabad', inplace = True, regex=True)

# %%
points_table_df.replace('Delhi Daredevils', 'Delhi Capitals', inplace=True, regex=True)
season_batting_card_df.replace('Delhi Daredevils', 'Delhi Capitals', inplace = True,regex=True)
season_bowling_card_df.replace('Delhi Daredevils',  'Delhi Capitals', inplace = True, regex=True)
season_details_df.replace('Delhi Daredevils', 'Delhi Capitals', inplace = True, regex=True)
season_summary_df.replace('Delhi Daredevils', 'Delhi Capitals', inplace = True, regex=True)

# %%
points_table_df.replace('Rising Pune Supergiants', 'Rising Pune Supergiant', inplace=True, regex=True)
season_batting_card_df.replace('Rising Pune Supergiants', 'Rising Pune Supergiant', inplace = True,regex=True)
season_bowling_card_df.replace('Rising Pune Supergiants',  'Rising Pune Supergiant', inplace = True, regex=True)
season_details_df.replace('Rising Pune Supergiants', 'Rising Pune Supergiant', inplace = True, regex=True)
season_summary_df.replace('Rising Pune Supergiants', 'Rising Pune Supergiant', inplace = True, regex=True)

# %%
team_code_dict = dict(zip(points_table_df['name'], points_table_df['short_name']))
team_name_dict = dict(zip(points_table_df['short_name'], points_table_df['name']))

# %%
season_summary_df['short_name'] = season_summary_df['name'].apply(lambda x: ' v '.join([team_code_dict[t] for t in x.split(' v ')]))
season_summary_df['home_team'] = season_summary_df['short_name'].apply(lambda x: x.split(' v ')[0])
season_summary_df['away_team'] = season_summary_df['short_name'].apply(lambda x: x.split(' v ')[1])

# %%
season_details_df.columns

# %%
# for row in season_details_df.itertuples():
#     if row.match_name != season_summary_df[season_summary_df['id'] == row.match_id]['short_name'].values[0]:
#         print(row.match_name, season_summary_df[season_summary_df['id'] == row.match_id]['short_name'].values[0])
season_details_df['match_name'] = season_details_df['match_id'].apply(lambda x: season_summary_df[season_summary_df['id'] == x]['short_name'].values[0])
season_details_df['home_team'] = season_details_df['match_id'].apply(lambda x: season_summary_df[season_summary_df['id'] == x]['home_team'].values[0])
season_details_df['away_team'] = season_details_df['match_id'].apply(lambda x: season_summary_df[season_summary_df['id'] == x]['away_team'].values[0])

# %%
season_batting_card_df.columns

# %%
# for row in season_batting_card_df.itertuples():
#     if row.match_name != season_summary_df[season_summary_df['id'] == row.match_id]['short_name'].values[0]:
#         print(row.match_name, season_summary_df[season_summary_df['id'] == row.match_id]['short_name'].values[0])
season_batting_card_df['match_name'] = season_batting_card_df['match_id'].apply(lambda x: season_summary_df[season_summary_df['id'] == x]['short_name'].values[0])
season_batting_card_df['home_team'] = season_batting_card_df['match_id'].apply(lambda x: season_summary_df[season_summary_df['id'] == x]['home_team'].values[0])
season_batting_card_df['away_team'] = season_batting_card_df['match_id'].apply(lambda x: season_summary_df[season_summary_df['id'] == x]['away_team'].values[0])

# %%
# for row in season_bowling_card.itertuples():
#     if row.match_name != season_summary_df[season_summary_df['id'] == row.match_id]['short_name'].values[0]:
#         print(row.match_name, season_summary_df[season_summary_df['id'] == row.match_id]['short_name'].values[0])
season_bowling_card['match_name'] = season_bowling_card['match_id'].apply(lambda x: season_summary_df[season_summary_df['id'] == x]['short_name'].values[0])
season_bowling_card['home_team'] = season_bowling_card['match_id'].apply(lambda x: season_summary_df[season_summary_df['id'] == x]['home_team'].values[0])
season_bowling_card['away_team'] = season_bowling_card['match_id'].apply(lambda x: season_summary_df[season_summary_df['id'] == x]['away_team'].values[0])

# %%
points_table.to_csv('../data/processed/points_table.csv', index=False)
season_batting_card.to_csv('../data/processed/season_batting_card.csv', index=False)
season_bowling_card.to_csv('../data/processed/season_bowling_card.csv', index=False)
season_details.to_csv('../data/processed/season_details.csv', index=False)
season_summary.to_csv('../data/processed/season_summary.csv', index=False)


