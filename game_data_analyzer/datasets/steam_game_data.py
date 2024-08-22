import csv
from os.path import dirname, join

current_path = dirname(__file__)

class SteamGameData:
  def __init__(self, use_sample_data=False):
    filename = 'steam_games_sample.csv' if use_sample_data else 'steam_games.csv'
    self._file_path = join(current_path, 'data', filename)

    with open(self._file_path, 'r') as file:
      reader =  csv.reader(file)
      count = 0
      for row in reader:
        count += 1
      self.games_total = count

  def _games_percent(self, games_quantity):
    """Dada uma quantidade de jogos, calcula o quanto essa quantidade representa do total, em porcentagem.

    Args:
        games_quantity (int): quantidade de jogos

    Returns:
        float: porcentagem da quantidade total de jogos
    """
    if games_quantity < 0:
      raise ValueError('Quantidade de jogos deve ser positiva')
    return (games_quantity / self.games_total) * 100

  def free_paid_games_percent(self):
    """Calcula quantos % dos jogos do dataset são gratuitos e quantos % são pagos

    Returns:
        (float, float): Tupla contendo a porcentagem de jogos gratuitos e a porcentagem de jogos pagos
    """
    with open(self._file_path, 'r') as file:
      reader =  csv.DictReader(file)
      free_games_count = 0
      for row in reader:
        if row['Price'] == '0.0':
          free_games_count += 1
      free_games_percent = self._games_percent(free_games_count)
      return (free_games_percent, (100.0 - free_games_percent))

  def most_releases_year(self):
    """Mostra o(s) ano(s) no(s) qual(is) foram lançados mais jogos.

    Returns:
        string | string[]: ano no qual foram lançados mais jogos. Em caso de empate, retorna uma lista de anos
    """
    with open(self._file_path, 'r') as file:
      reader =  csv.DictReader(file)
      yearly_releases_dict = {}
      for row in reader:
        year = row['Release date'][-4:]
        if year in yearly_releases_dict:
          yearly_releases_dict[year] += 1
        else:
          yearly_releases_dict[year] = 1
      max_yearly_releases = max(yearly_releases_dict.values())
      top_years = [k for k, v in yearly_releases_dict.items() if v == max_yearly_releases]
      if len(top_years) == 1:
        return top_years[0]
      else:
        return top_years

  def linux_russian_games_percent(self):
    """Quantos % dos jogos disponíveis em língua russa rodam no sistema operacional Linux

    Returns:
        float: porcentagem da quantidade total de jogos
    """
    with open(self._file_path, 'r') as file:
      reader =  csv.DictReader(file)
      games_count = 0
      for row in reader:
        if row['Linux'] == 'True' and 'Russian' in row['Supported languages']:
          games_count += 1
      return self._games_percent(games_count)