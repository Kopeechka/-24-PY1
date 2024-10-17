list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(first_team)
print(second_team)

#работа была сделана изначально в пайчарме
#увидев то, как здесь использовалось положение middle_index для индексации,
#это вдохновило сделать первую работу так, как она представлена выше
