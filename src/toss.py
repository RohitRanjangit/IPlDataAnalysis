import pandas as pd
import numpy as np
from data_process import *
from metadata import *
import matplotlib.pyplot as plt
import plotly.express as px
import cufflinks as cf
from plotly.offline import plot, iplot, download_plotlyjs, init_notebook_mode
import seaborn as sns


def toss_win_to_win_count():
    """
    Return the Dataframe with match win to toss win percentage
    """
    toss_match_df = season_summary_df[['toss_won', 'winner']].dropna()
    toss_match_df['win'] = toss_match_df['toss_won'] == toss_match_df['winner']
    toss_match_df['win'] = toss_match_df['win'].astype(int)
    
    toss_match_df['toss'] = 1
    toss_match_df = toss_match_df.groupby(['winner']).sum().reset_index() 
    toss_match_df['toss_win_percentage'] = toss_match_df['win']*100/toss_match_df['toss']
    
    toss_match_df = toss_match_df[toss_match_df['winner'] != 'No Result']
    return toss_match_df
    

toss_win_to_win_count().iplot(kind='bar', x='winner', y='toss_win_percentage', title='Toss Win to Win Percentage',  barmode = 'group')


def ground_toss_decision():
    """
    This function will return the dataframe for every ground % of BAT FIRST and BOWL FIRST
    """
    venue_toss_df = season_summary_df[['venue_id','venue_name', 'decision']].dropna()
    venue_toss_df['bat_first'] = venue_toss_df['decision'].str.contains('BAT').astype(int)
    venue_toss_df['toss'] = 1
    venue_toss_df = venue_toss_df.groupby(['venue_id', 'venue_name']).sum().reset_index()
    venue_toss_df['bat_first_percentage'] = venue_toss_df['bat_first']*100/venue_toss_df['toss']
    venue_toss_df['bowl_first_percentage'] = 100 - venue_toss_df['bat_first_percentage']
    return venue_toss_df

ground_toss_decision().iplot(kind='barh', x='venue_name', y=['bat_first_percentage','bowl_first_percentage'], title='Ground Toss Decision', size=10)


def toss_won_by_team():
    """
    Toss won by team
    """
    toss_df = season_summary_df['toss_won'].dropna()
    toss_df = toss_df.groupby(toss_df).count()
    toss_df =  toss_df.to_dict()
    toss_df_keys = list(toss_df.keys())
    toss_df_values = list(toss_df.values())
    ax = sns.barplot(x=toss_df_keys, y=toss_df_values)
    #set figure size to (10, 6)
    ax.figure.set_size_inches(10, 6)
    ax.set_title("Toss Won", fontsize=14, fontweight='bold')
    ax.set_xlabel("Team", fontsize=12, fontweight='bold')
    ax.set_ylabel("Count", fontsize=12, fontweight='bold')
    ax.bar_label(container=ax.containers[0])
toss_won_by_team()


def final_win_toss_to_win():
    final_df = season_summary_df[['winner', 'toss_won', 'description']].dropna()
    final_df['stage'] = final_df['description'].apply(lambda x: x.split(',')[0].title().split(' ')[0])
    final_df = final_df[final_df['stage'] == 'Final']
    final_df['toss_won_to_won'] = final_df['winner'] == final_df['toss_won']
    final_df = final_df['toss_won_to_won'].dropna()
    final_df = final_df.groupby(final_df).count()
    final_df =  final_df.to_dict()
    final_df_values = list(final_df.values())
    plt.pie(final_df_values, labels=['final won', 'final lost'], autopct='%1.1f%%')
    plt.show()

final_win_toss_to_win()