from __future__ import division
import sys
import init
import calculations
import output

def calc_rankings(input_year, input_week):
    teams = init.init_teams(input_year, input_week);
    teams = calculations.init_calc_team_record_ranking(teams)

    teams = calculations.calc_value_ranking(teams, 'points_scored_avg', 'points_scored_ranking', True)
    teams = calculations.calc_value_ranking(teams, 'points_against_avg', 'points_against_ranking', False)
    teams = calculations.calc_value_ranking(teams, 'turnover_differential', 'turnover_differential_ranking', True)
    teams = calculations.calc_value_transformation(teams, 'points_scored_avg', 'points_scored_transformation', True)
    teams = calculations.calc_value_transformation(teams, 'points_against_avg', 'points_against_transformation', False)
    teams = calculations.calc_value_transformation(teams, 'turnover_differential', 'turnover_differential_transformation', True)

    teams = calculations.calc_advanced_stats(teams)

    teams = calculations.calc_value_transformation(teams, 'pythagorean_wins', 'pythagorean_wins_transformation', True)
    teams = calculations.calc_value_transformation(teams, 'victory_value', 'victory_value_transformation', True)
    teams = calculations.calc_value_transformation(teams, 'point_differential_strength', 'point_differential_transformation', True)
    teams = calculations.calc_value_transformation(teams, 'win_percentage', 'win_percentage_transformation', True)

    teams = calculations.init_calc_power_ranking(teams)

    output.print_power_rankings(teams)
    output.export_to_json(teams, input_week, input_year)

def calc_multiple_weeks():
    beg_year = int(sys.argv[2])
    beg_week = int(sys.argv[3])
    end_year = int(sys.argv[4])
    end_week = int(sys.argv[5])

    first_archived_year = 2009
    weeks_in_a_season = 17

    year_iterations = (end_year - beg_year) + 1

    if year_iterations == 1:
        beg_year_week_iterations = (end_week - beg_week) + 1
        final_year_week_iterations = (end_week - beg_week) + 1
    else:
        beg_year_week_iterations = (weeks_in_a_season - beg_week) + 1
        final_year_week_iterations = end_week

    for year_index in range(year_iterations):
        year = beg_year + year_index

        if year == beg_year:
            week_iterations = beg_year_week_iterations
            initial_week = beg_week
        elif year == end_year:
            week_iterations = final_year_week_iterations
            initial_week = 1
        else:
            week_iterations = weeks_in_a_season
            initial_week = 1

        for week_index in range(week_iterations):
            week = initial_week + week_index

            calc_rankings(year, week)

def calc_single_week():
    input_year = int(sys.argv[2])
    input_week = int(sys.argv[3])
    calc_rankings(input_year, input_week)

def entry():
    calc_type = sys.argv[1]

    if calc_type == 'multiple':
        calc_multiple_weeks()
    elif calc_type == 'single':
        calc_single_week()

entry()
