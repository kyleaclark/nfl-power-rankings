from __future__ import division
import sys
import init
import calculations
import output

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
teams = calculations.calc_value_transformation(teams, 'points_scored_avg', 'points_scored_transformation', True)
teams = calculations.calc_value_transformation(teams, 'points_against_avg', 'points_against_transformation', False)
teams = calculations.calc_value_transformation(teams, 'turnover_differential', 'turnover_differential_transformation', True)

teams = calculations.init_calc_power_ranking(teams)

output.print_power_rankings(teams)
output.export_to_json(teams, input_week, input_year)
