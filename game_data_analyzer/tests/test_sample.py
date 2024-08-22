from game_data_analyzer.datasets.steam_game_data import SteamGameData


def test_sample():
  games = SteamGameData(use_sample_data=True)
  free_paid_games_percent = games.free_paid_games_percent()
  most_releases_year = games.most_releases_year()
  linux_russian_games_percent = games.linux_russian_games_percent()
  assert free_paid_games_percent[0] == 9.523809523809524
  assert free_paid_games_percent[1] == 90.47619047619048
  assert most_releases_year == '2019'
  assert linux_russian_games_percent == 14.285714285714285