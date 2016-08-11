import json
from collections import OrderedDict

def print_power_rankings(teams):
    index = 1

    print '    TM  W-L  PWR  WV   PYTH   DIFF  PERC  O   D   TO'

    for id, team in sorted(teams.iteritems(), key=lambda (x, y): y['power_ranking'], reverse=True):
        print '%d. %s %d-%d %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f' % (index, team['id'], team['wins'], team['losses'], team['power_ranking'], team['win_value'], team['pythagorean_win_value'], team['point_differential_value'], team['win_percentage_value'], team['points_scored_value'], team['points_against_value'], team['turnover_differential_value'])
        index += 1

def export_to_json(teams, input_week, input_year):
    rankings = []

    input_year_str = str(input_year)
    input_week_str = str(input_week) if (input_week > 9) else ('0' + str(input_week))

    name = input_year_str + '_wk_' + input_week_str
    fileName = name + '.json'

    for id, team in sorted(teams.iteritems(), key=lambda (x, y): y['power_ranking'], reverse=True):
        rankings.append(team)

    output = OrderedDict([ ('_id', name), ('year', input_year), ('week', input_week), ('data', rankings) ])

    with open(fileName, 'w') as outfile:
        json.dump(output, outfile)
