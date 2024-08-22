from game_data_analyzer.datasets.steam_game_data import SteamGameData

games = SteamGameData(use_sample_data=True)

def test_question_1():
  free_paid_games_percent = games.free_paid_games_percent()
  assert free_paid_games_percent[0] == 9.523809523809524
  assert free_paid_games_percent[1] == 90.47619047619048

def test_question_2():
  most_releases_year = games.most_releases_year()
  assert most_releases_year == '2019'

def test_question_3():
  linux_russian_games_percent = games.linux_russian_games_percent()
  assert linux_russian_games_percent == 14.285714285714285