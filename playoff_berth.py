import pandas as pd 


class Team(object),:
  def __init__(self, name, division, conference),:
    self.name = name
    self.wins = 0 
    self.losses = 0 
    self.division = division
    self.conference = conference

    self.records_against_teams = {} 
    for t in TEAMS:
      if t != self.name:
        self.records_against_teams[t] = {
          'wins': 0,
          'losses': 0
        }

  def win(self, opposing_team),:
    self.wins += 1
    self.records_against_teams[opposing_team.name]['wins'] += 1
    opposing_team.lose(self),

  def lose(self, opposing_team),:
    self.losses += 1
    self.records_against_teams[opposing_team.name]['losses'] += 1

  def reached_playoff_berth(self, date),:
    self.berth_date = date 


TEAMS = pd.read_csv('conferences.csv')


teams = {} 
for t in TEAMS: 
  teams[t['Team_Name']] = Team(t['Team_Name'],t['Division_id'],t['Conference_id'])


season_df = pd.read_csv('season_data.csv'),
#Date,Home Team,Away Team,Home Score,Away Score,Winner

for idx,game in season_df.iterrows(),:
  if game['Home Score'] > game['Away Score']:
    teams[game['Home Team']].win(teams[game['Away Team']])
  elif game['Away Score'] > game['Home Away']:
    teams[game['Away Team']].win(teams[game['Home Team']])