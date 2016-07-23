from __future__ import division
import json
import sys
import init
import calculations

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

def calc_power_ranking(team):
    team['win_value'] = (team['wins'] * team['sov']) * 0.50
    team['point_differential_value'] = (team['point_differential_avg'] * team['sos']) * 0.25
    team['points_scored_value'] = team['points_scored_transformation'] * 0.10
    team['points_against_value'] = team['points_against_transformation'] * 0.10
    team['turnover_differential_value'] = team['turnover_differential_transformation'] * 0.05

    team['power_ranking'] = team['win_value'] + team['point_differential_value'] + team['points_scored_value'] + team['points_against_value'] + team['turnover_differential_value']

def print_power_rankings(teams):
    index = 1

    for id, team in sorted(teams.iteritems(), key=lambda (x, y): y['power_ranking'], reverse=True):
        print '%d. %s %d-%d %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f' % (index, team['id'], team['wins'], team['losses'], team['power_ranking'], team['sos'], team['sov'], team['win_value'], team['point_differential_value'], team['points_scored_value'], team['points_against_value'], team['turnover_differential_value'])
        index += 1

def export_to_json(teams):
    data = {}
    rankings = []
    name = str(input_year) + '_wk_' + str(input_week)
    fileName = name + '.json'

    for id, team in sorted(teams.iteritems(), key=lambda (x, y): y['power_ranking'], reverse=True):
        rankings.append(team)

    data['_id'] = name
    data['data'] = rankings

    with open(fileName, 'w') as outfile:
        json.dump(data, outfile)

global teams
global input_year
global input_week

input_year = int(sys.argv[1])
input_week = int(sys.argv[2])

teams = init.init_teams(input_year, input_week);
teams = calculations.init_calc_team_record_ranking(teams)

teams = calculations.calc_value_ranking(teams, 'points_scored_avg', 'points_scored_ranking', True)
teams = calculations.calc_value_ranking(teams, 'points_against_avg', 'points_against_ranking', False)
teams = calculations.calc_value_ranking(teams, 'turnover_differential', 'turnover_differential_ranking', True)
calc_value_transformation(teams, 'points_scored_avg', 'points_scored_transformation', True)
calc_value_transformation(teams, 'points_against_avg', 'points_against_transformation', False)
calc_value_transformation(teams, 'turnover_differential', 'turnover_differential_transformation', True)

for id, team in teams.iteritems():
    calc_power_ranking(team)

print_power_rankings(teams)
export_to_json(teams)
