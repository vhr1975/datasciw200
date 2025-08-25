import pandas as pd
from os import path, listdir
import re
import numpy as np

data_dir = path.join(path.dirname(path.abspath(__file__)), 'data')
games = pd.read_csv(path.join(data_dir, 'games.csv'))
plays = pd.read_csv(path.join(data_dir, 'plays.csv'))

players = pd.read_csv(path.join(data_dir, 'players.csv'))
week_fns = [path.join(data_dir, f) for f in listdir(data_dir) if f.startswith('week')]
tracking = pd.concat(map(pd.read_csv, week_fns))
tracking = tracking.loc[tracking['position'] == 'QB'][['gameId', 'playId', 'nflId', 'route']]
tracking = tracking.drop_duplicates()

players_in_game = tracking.merge(players, how='left', on='nflId')

full_df = games.merge(plays, how='right', on='gameId').merge(players_in_game, how='left', on=['gameId', 'playId'])

qb_duplicated = full_df.duplicated(subset=['gameId', 'playId'], keep=False)
qb_duplicates = full_df.loc[qb_duplicated]

full_df = full_df.loc[~qb_duplicated]

qb_duplicates = qb_duplicates[qb_duplicates.apply(lambda x: bool(
    re.match(f".*[A-Z]+\.{x['displayName'].split()[1]} (pass|sack).*", x['playDescription'])), axis=1)]

full_df = pd.concat([full_df, qb_duplicates])

full_df['birthDate'] = pd.to_datetime(full_df['birthDate'])
full_df['gameDate'] = pd.to_datetime(full_df['gameDate'])

full_df['player_age'] = (full_df['gameDate']-full_df['birthDate'])/np.timedelta64(1, 'Y')
full_df.to_csv(path.join(data_dir, 'plays_merged_with_all_files.csv'), index=False)
