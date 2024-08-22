
from game_data_analyzer.datasets.steam_game_data import SteamGameData

games = SteamGameData()

print('Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma?')
answer1 = games.free_paid_games_percent()
print(f'Resposta: {answer1[0]: .2f}% dos jogos são gratuitos e {answer1[1]: .2f}% dos jogos são pagos\n')
print('\n')

print('Pergunta 2: Qual o ano com o maior número de novos jogos?')
answer2 = games.most_releases_year()
if type(answer2) is list:
  print(f'Resposta: os anos nos quais se lançaram mais jogos foram {answer2}')
else:
  print(f'Resposta: o ano no qual se lançaram mais jogos foi {answer2}')
print('\n')

print('Pergunta 1: Qual o percentual de jogos compatíveis com Linux?')
answer3 = games.linux_games_percent()
print(f'Resposta: {answer3: .2f}% dos jogos rodam em Linux\n')
