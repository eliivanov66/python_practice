# 2. Создайте программу для игры с конфетами человек против человека.

#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#     Первый ход определяется жеребьёвкой.
#     За один ход можно забрать не более чем 28 конфет.
#     Все конфеты оппонента достаются сделавшему последний ход.
#     Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#     a) Добавьте игру против бота
#     b) Подумайте как наделить бота "интеллектом"

from os import system
from random import randint

def my_user_enter(arg_text):
    out_quality_bad = True
    while (out_quality_bad):
        out_quality_bad = False
        # ввод данных
        in_value = input(f"Введите {str(arg_text)}: ")
        # проверка является ли это числом с правающей запятой
        if not (in_value.isnumeric()) :
            out_quality_bad = True
        if out_quality_bad : 
            print(f"Некорректный ввод {str(arg_text)}")
    return int(in_value)

def generate_ai_choise(arg_input, arg_min, arg_max):
    '''метод генерирующий выбор духа машин'''
    if arg_input < arg_max:
        return arg_input
    if arg_input - arg_max >= arg_max:
        return arg_max
    else:
        return arg_min


# переменные 
candy_count = 0 # количество конфет на столе
human_count = 0 # количество конфет у человека
ai_count = 0 # количество конфет у духа машин
move = 0 # ход, 0 - дух машин, 1 - человек
human_choise = 0 # количество конфет, которое хочет забрать человек
ai_choise = 0 # количество конфет, которое хочет забрать дух машин
choise_min = 1 # минимальное количество конфет, которое можно взять на 1 ходу
choise_max = 28 # максимальное количество конфет, которое можно взять на 1 ходу

system('cls')
while candy_count <= 0:
    candy_count = my_user_enter("количество конфет, которое лежит на столе")
system('cls')

# опредиление первого хода
move = randint(0, 1)

# играем пока конфеты на столе
while candy_count > 0:
    # system('cls')
    print(f"На столе лежит {candy_count} конфет(ы), у игрока {human_count} конфет(ы), у духа машин {ai_count} конфет(ы)")
    if move:
        while (human_choise > choise_max or human_choise < choise_min or human_choise > candy_count):
            human_choise = my_user_enter(f"количество конфет, которое вы хотите забрать ({choise_min} - {choise_max})")
        print(f"Вы взяли со стола {human_choise} конфет(ы)") 
        human_count += human_choise # у человек конфет прибавляется
        candy_count -= human_choise # на столе конфет убавляется
        human_choise = 0
        move = 0 # передать ход духу машин
    else : 
        while (ai_choise > choise_max or ai_choise < choise_min or ai_choise > candy_count):
            # ai_choise = randint(1, 29)
            ai_choise = generate_ai_choise(candy_count ,choise_min, choise_max)
        print(f"Дух машин взял со стола {ai_choise} конфет(ы)")
        ai_count += ai_choise # у духа машин конфет прибавляется
        candy_count -= ai_choise # на столе конфет убавляется
        ai_choise = 0 
        move = 1 # передать ход человеку

# после того как все конфеты на столе закончились, тот кто сделал последний ход
# 1 = последний ход сделала машина, 0 - сделал человек
system('cls')
if move:
    ai_count += human_count 
    print(f"Вы проиграли, у духа машин {ai_count} конфет(ы)")
else:
    human_count += ai_count
    print(f"Вы победили у вас {human_count} конфет(ы)")
