import nfldb
import team_data

global teams
global weeks

def init():
    'Initialize nfldb connection'

    global db

    db = nfldb.connect()

def generate_query(team):
    'Generate a base query to the NFLDB'

    weeks = range(1, (input_week + 1))

    team_query = nfldb.Query(db)
    team_query.game(season_year=input_year, season_type='Regular', team=team['id'], week=weeks)

    for game in team_query.as_games():
        team['games'] += 1

        if game.home_team == team['id']:
            team['points_scored'] += game.home_score
            team['points_against'] += game.away_score
            team['point_differential'] += (game.home_score - game.away_score)
            team['turnover_differential'] += (game.home_turnovers - game.away_turnovers)
            team['opponents'].append(game.away_team)

            if game.winner == game.home_team:
                team['wins'] += 1
                team['game_win_opponents'].append(game.away_team)
            else:
                team['losses'] += 1

        else:
            team['points_scored'] += game.away_score
            team['points_against'] += game.home_score
            team['point_differential'] += (game.away_score - game.home_score)
            team['turnover_differential'] += (game.away_turnovers - game.home_turnovers)
            team['opponents'].append(game.home_team)

            if game.winner == game.away_team:
                team['wins'] += 1
                team['game_win_opponents'].append(game.home_team)
            else:
                team['losses'] += 1

def init_teams(year, week):
    init()

    global input_year
    global input_week

    input_year = year
    input_week = week

    if input_year > 2016:
        teams = team_data.get_post_2016_data()
    elif input_year == 2016:
        teams = team_data.get_2016_data()
    else:
        teams = team_data.get_pre_2016_data()

    for id, team in teams.iteritems():
        team['games'] = 0
        team['wins'] = 0
        team['losses'] = 0
        team['points_scored'] = 0
        team['points_against'] = 0
        team['point_differential'] = 0
        team['turnover_differential'] = 0
        team['opponents'] = []
        team['opponent_games'] = 0
        team['opponent_wins'] = 0
        team['game_win_opponents'] = []
        team['game_win_opponents_games'] = 0
        team['game_win_opponents_wins'] = 0
        generate_query(team)

    return teams
