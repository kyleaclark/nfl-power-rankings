from __future__ import division

def init_calc_team_record_ranking(tms):
    global teams

    teams = tms

    for id, team in teams.iteritems():
        calc_team_record_ranking(team)

    return teams

def calc_team_record_ranking(team):
    for opp in team['opponents']:
        team['opponent_games'] += teams[opp]['games']
        team['opponent_wins'] += teams[opp]['wins']

    for opp in team['game_win_opponents']:
        team['game_win_opponents_games'] += teams[opp]['games']
        team['game_win_opponents_wins'] += teams[opp]['wins']

    team['points_scored_avg'] = team['points_scored'] / team['games']
    team['points_against_avg'] = team['points_against'] / team['games']
    team['point_differential_avg'] = team['point_differential'] / team['games']

    if team['opponent_wins'] > 0:
        team['sos'] = team['opponent_wins'] / team['opponent_games']
    else:
        team['sos'] = 0

    if team['game_win_opponents_wins']:
        team['sov'] = team['game_win_opponents_wins'] / team['game_win_opponents_games']
    else:
        team['sov'] = 0

    team['win_percentage'] = team['wins'] / team['games']

def calc_value_ranking(teams, valueKey, rankingKey, reverse):
    prevAvg = None
    index = 32
    indexSeries = 0

    for id, team in sorted(teams.iteritems(), key=lambda (x, y): y[valueKey], reverse=reverse):
        if prevAvg == team[valueKey]:
            indexSeries += 1
        elif indexSeries > 0:
            indexSeries = 0

        prevAvg = team[valueKey]
        team[rankingKey] = index + indexSeries
        index -= 1

    return teams

def calc_value_transformation(teams, valueKey, transformationKey, reverse):
    index = 0
    transformationValue = 10

    for id, team in sorted(teams.iteritems(), key=lambda (x, y): y[valueKey], reverse=reverse):
        if index == 0:
            baselineAvg = team[valueKey]
            team[transformationKey] = transformationValue
        else:
            if reverse == True:
                team[transformationKey] = (team[valueKey] / baselineAvg) * transformationValue
            else:
                team[transformationKey] = (baselineAvg / team[valueKey]) * transformationValue

        index += 1

    return teams
