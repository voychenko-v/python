"""
    Реализуйте игру Magic (hw3/magic.py) с некоторыми дополнениями.

    1. При запуске, программа спрашивает имя игрока.

    2. В словаре player_data хранить данные игрока и актуализировать их после
    каждой сыгранной игры. Оперировать такими данными:
        name - имя игрока
        games - общее количество сыграных игр
        record - рекордное количество попыток (минимальное)
        avg_attempts - среднее количество попыток за игру

    3. При выходе из программы данные игрока записывать в файл (txt либо json).

    **4. При запуске программы, после ввода имени пользователем, читать файл,
    если данные об игроке есть в файле то загружать их в player_data.

"""
import random
from pathlib import Path


name_player = input('Enter your name: ')
player_data = {
    'name': name_player,
    'games': 0,
    'record': 0,
    'avg_attempts': 0
}
num_games = 0
record_game = 0
path = Path(__file__).resolve()
while True:
    random_number = random.randint(1, 10)
    num = int(input('Введите число: '))
    num_1 = 1

    while num != random_number:
        num_1 += 1
        if num > random_number:
            print('Загаданое число меньньше')
        else:
            print('Загаданое число больше')
        num = int(input('Введите число: '))
    print('Попыток: ', num_1)
    print('Вы угадали, загаданое число: ', random_number)
    num_games += 1
    player_data['games'] = num_games
    if record_game == 0:
        record_game = num_1
    elif num_1 < record_game:
        record_game = num_1
    player_data['record'] = record_game
    if num_games == 1:
        avg = num_1
    elif num_games > 1:
        avg = ((player_data['avg_attempts'] + num_1) / 2)
    player_data['avg_attempts'] = avg
    print(player_data)

    if input('Continue ? (Y/n) ') == 'n':
        with open('player_data.txt', 'a+') as f:
            print(player_data, file=f)
        print('Bye')
        break

