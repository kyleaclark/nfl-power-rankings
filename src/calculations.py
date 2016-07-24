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
    transformationValue = 100

    for id, team in sorted(teams.iteritems(), key=lambda (x, y): y[valueKey], reverse=reverse):
        if index == 0:
            baselineAvg = team[valueKey]
            team[transformationKey] = transformationValue
        else:
            if reverse == True:
                team[transformationKey] = transformative_divide(team[valueKey], baselineAvg) * transformationValue
            else:
                team[transformationKey] = transformative_divide(baselineAvg, team[valueKey]) * transformationValue

        index += 1

    return teams

def transformative_divide(numerator, denominator):
    if denominator == 0:
        return 0

    val = numerator / denominator

    if val > 1:
        return 1
    elif val < -1:
        return -1
    else:
        return val

def calc_advanced_stats(teams):
    for id, team in teams.iteritems():
        points_scored = team['points_scored_transformation']
        points_scored_divisor = points_scored + team['points_against_transformation']
        team['pythagorean_wins'] = (points_scored / points_scored_divisor) * team['games']

        team['victory_value'] = (team['wins'] * team['sov'])
        team['point_differential_strength'] = team['point_differential_avg'] * team['sos']

    return teams

def init_calc_power_ranking(tms):
    global teams

    teams = tms

    for id, team in teams.iteritems():
        calc_power_ranking(team)

    return teams

def calc_power_ranking(team):
    team['win_value'] = team['victory_value_transformation'] * 0.25
    team['point_differential_value'] = team['point_differential_transformation'] * 0.25
    team['pythagorean_win_value'] = team['pythagorean_wins_transformation'] * 0.25

    team['win_percentage_value'] = team['win_percentage_transformation'] * 0.10
    team['points_scored_value'] = team['points_scored_transformation'] * 0.05
    team['points_against_value'] = team['points_against_transformation'] * 0.05
    team['turnover_differential_value'] = team['turnover_differential_transformation'] * 0.05

    team['power_ranking'] = team['win_value'] + team['point_differential_value'] + team['pythagorean_win_value'] + team['win_percentage_value'] + team['points_scored_value'] + team['points_against_value'] + team['turnover_differential_value']
