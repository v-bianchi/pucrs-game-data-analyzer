from game_data_analyzer.datasets.steam_game_data import SteamGameData


def test_sample():
  games = SteamGameData(use_sample_data=True)
  free_paid_games_percent = games.free_paid_games_percent()
  most_releases_year = games.most_releases_year()
  linux_games_percent = games.linux_games_percent()
  assert free_paid_games_percent[0] == 9.523809523809524
  assert free_paid_games_percent[1] == 90.47619047619048
  assert most_releases_year == '2019'
  assert linux_games_percent == 23.809523809523807