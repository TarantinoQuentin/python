list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

players_count = len(list_players)
list_half = players_count // 2
first_team = list_players[:list_half]
second_team = list_players[list_half:]

print(f'{first_team}\n{second_team}')
