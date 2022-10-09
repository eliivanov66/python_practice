# 3. Создайте программу для игры в "Крестики-нолики".
#  1 | 2 | 3
# -----------
#  X |   |
# ---------
#   |   |

from os import system
from random import randint

def my_field_display(arg_field):
    print("     0    1    2 ")
    print("--------------------")
    for i in range(len(arg_field)) :
        print(f"{i}| {arg_field[i]} |")
    print("--------------------")

def my_coord_get(arg_text): # 
    out_quality_bad = True
    out_result = []
    while (out_quality_bad):
        out_quality_bad = False
        # ввод данных
        in_value = input(f"{arg_text}")
        # извлечение данных
        for i in range(len(in_value)):
            if in_value[i].isdigit():
                out_result.append(int(in_value[i]))
        # проверка является ли это координатами
        if (len(out_result) != 2) or (out_result[0] > 2) or (out_result[0] < 0) or (out_result[1] > 2) or (out_result[1] < 0) :
            out_quality_bad = True
        if out_quality_bad : 
            print(f"Некорректный ввод {str(arg_text)}")
    return out_result

def my_check_empty(arg_field, arg_input):
    if arg_field[arg_input[1]][arg_input[0]] != " ":
        return False
    else:
        return True

def my_set_field(arg_field, arg_input, arg_value):
    arg_field[arg_input[1]][arg_input[0]] = arg_value

def my_game_over(arg_field, arg_value):
    out_value = False
    for i in range(0,3):
        if arg_field[i][0] == arg_field[i][1] == arg_field[i][2] == arg_value:
            out_value = True
        if arg_field[0][i] == arg_field[1][i] == arg_field[2][i] == arg_value:
            out_value = True
        if arg_field[0][0] == arg_field[1][1] == arg_field[2][2] == arg_value:
            out_value = True
        if arg_field[2][0] == arg_field[1][1] == arg_field[0][2] == arg_value:
            out_value = True
    return out_value

def my_check_field(arg_field):
    count = 0
    for i in arg_field:
        for j in i:
            if j == " ":
                count += 1
    return count == 0


# переменные 

move = 1 # ход, 1 - игрок 1, 2 - игрок 2
player_1_choise = [-1,-1] # выбор точки для фигуры игрока 1
player_2_choise = [-1,-1] # выбор точки для фигуры игрока 2
field_value = [[" " for i in range(3)] for j in range(3)] # поле для игры
game_over = 0


# опредиление первого хода
move = randint(1, 2)

# играем пока игра не завершится
while game_over == 0:
    system('cls') # очистка экрана
    my_field_display(field_value) # показать текущее состояние поля
    if move == 1: # ход игрока 1
        player_1_choise = my_coord_get("Игрок 1 выберите точку в формате (x,y) для своей фигуры: ") # выбор координаты игроком
        while not my_check_empty(field_value, player_1_choise): # проверка заполнена ли выбранная координата
            print(f"Заданные координаты {player_1_choise} уже заняты")
            player_1_choise = my_coord_get("Игрок 1 выберите точку в формате (x,y) для своей фигуры: ")
        print(f"Игрок 1 выбрал точку {player_1_choise}")
        my_set_field(field_value, player_1_choise, "x") # размещение на поле
        if my_game_over(field_value, "x"): # проверка победил ли игрок
            game_over = 1
            break
        if my_check_field(field_value): # проверка есть ли ещё свободные места на поле
            game_over = 3
            break   
        move = 2 # передать ход человеку 2
    else : # ход игрока 2
        player_2_choise = my_coord_get("Игрок 2 выберите точку в формате (x,y) для своей фигуры: ") # выбор координаты игроком
        while not my_check_empty(field_value, player_2_choise): # проверка заполнена ли выбранная координата
            print(f"Заданные координаты {player_2_choise} уже заняты")
            player_2_choise = my_coord_get("Игрок 2 выберите точку в формате (x,y) для своей фигуры: ")
        print(f"Игрок 2 выбрал точку {player_2_choise}")
        my_set_field(field_value, player_2_choise, "o") # размещение на поле
        if my_game_over(field_value, "o"): # проверка победил ли игрок
            game_over = 2
            break
        if my_check_field(field_value): # проверка есть ли ещё свободные места на поле
            game_over = 3
            break   
        move = 1 # передать ход человеку 2

# игра окончена, вывод результата
system('cls')
my_field_display(field_value)
if game_over == 1:
    print("Игрок 1 победил")
if game_over == 2:
    print("Игрок 2 победил")
if game_over == 3:
    print("Партия закончилась ничьей")