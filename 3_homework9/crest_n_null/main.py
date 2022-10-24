# Игра в крестики нолики через Telegram бота

from random import randint
from telebot import TeleBot
import telebot

def my_field_display(arg_field):
    ms_text ="."
    ms_text =f"{ms_text}  0   1   2 \n"
    ms_text =f"{ms_text} --------------------\n"
    for i in range(len(arg_field)) :
        line = ""
        for j in range(len(arg_field[i])):
            if arg_field[i][j] == " ":
                line = f"{line} {arg_field[i][j]}|"
            else:
                line = f"{line}{arg_field[i][j]}|"
        ms_text = f"{ms_text}{i}|{line} \n"
    ms_text =f"{ms_text}--------------------"
    return ms_text

def my_coord_get(arg_text):
    out_result = []
    for i in arg_text:
        if not str(i).isnumeric() and str(i) != " ":
            arg_text = arg_text.replace(i)
    out_temp = str(arg_text).split()
    if len(out_temp) != 2:
        return -1
    else:
        for i in out_temp:
            if not str(i).isnumeric():
                return -1
        for i in out_temp:
            out_result.append(int(i))
        if (out_result[0] > 2) or (out_result[0] < 0) or (out_result[1] > 2) or (out_result[1] < 0):
            return -1
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

def machine_spirit(arg_field):
    out_value = [0, 0]
    while True:
        if my_check_empty(arg_field, out_value):
            return out_value
        else:
            out_value = [randint(0,2), randint(0,2)]



move = 0 # ход, 1 - игрок 1, 2 - игрок 2
player_1_choise = [-1,-1] # выбор точки для фигуры игрока 1
player_2_choise = [-1,-1] # выбор точки для фигуры игрока 2
field_value = [[" " for i in range(3)] for j in range(3)] # поле для игры
game_over = 0
game_running = 0


bot = TeleBot("5551738625:AAFE5AXjwLN0Deu7YqhZCQITpeP-YcQDQ04")

@bot.message_handler(commands=['start'])
def startup(msg: telebot.types.Message):
    global move
    global player_1_choise
    global player_2_choise
    global field_value
    global game_over
    global game_running

    game_over = 0
    game_running = 1
    move = randint(0,1)
    field_value = [[" " for i in range(3)] for j in range(3)] # поле для игры
    bot.send_message(chat_id=msg.from_user.id , text=f"Игрок {msg.from_user.full_name} запустил игру")
    if move:
        bot.send_message(chat_id=msg.from_user.id , text=my_field_display(field_value)) # показать текущее состояние поля
        bot.send_message(chat_id=msg.from_user.id , text=f"Ход игрока {msg.from_user.full_name}, выберите координату для '+' в формате x y" )  
        return
    else:
        player_2_choise = machine_spirit(field_value)
        my_set_field(field_value, player_2_choise, "o") # размещение на поле
        bot.send_message(chat_id=msg.from_user.id , text=f"Ход копьютера, он выбрал координату {player_2_choise}" )
        bot.send_message(chat_id=msg.from_user.id , text=my_field_display(field_value)) # показать текущее состояние поля
        move = 1 # передать ход человеку 1
        bot.send_message(chat_id=msg.from_user.id , text=f"Ход игрока {msg.from_user.full_name}, выберите координату для '+' в формате x y" )
        return

@bot.message_handler(commands=['stop'])
def shutdown(msg: telebot.types.Message):
    global move
    global player_1_choise
    global player_2_choise
    global field_value
    global game_over
    global game_running

    game_over = 0
    game_running = 0
    move = randint(0,1)
    field_value = [[" " for i in range(3)] for j in range(3)] # поле для игры
    bot.send_message(chat_id=msg.from_user.id , text=f"Игрок {msg.from_user.full_name} остановил игру")

@bot.message_handler(commands=['info'])
def info(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id , text=f"Бот для игры в крестики - нолики, задавайте координаты для '+' в формате координаты по горизонтали пробел по вертикали")

@bot.message_handler(commands=['log'])
def log(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id , text=f"Логирование не ведётся")

@bot.message_handler()
def logic(msg: telebot.types.Message):
    global move
    global player_1_choise
    global player_2_choise
    global field_value
    global game_over
    global game_running

    if not game_running:
        bot.send_message(chat_id=msg.from_user.id , text="Игра в крестики нолики, для начала выберите 'Start'") # показать текущее состояние поля
    if move and game_running and not game_over: # ход игрока 1
        player_1_choise = my_coord_get(msg.text) # выбор координаты игроком
        if player_1_choise == -1:
            bot.send_message(chat_id=msg.from_user.id , text=f"Ход игрока {msg.from_user.full_name}, Координаты должны быть в формате x y")
            bot.send_message(chat_id=msg.from_user.id , text=f"Ход игрока {msg.from_user.full_name}, выберите координату для '+' в формате x y" )
            return
        else:
            if not my_check_empty(field_value, player_1_choise): # проверка заполнена ли выбранная координата
                bot.send_message(chat_id=msg.from_user.id , text=f"Ход игрока {msg.from_user.full_name}, указанная координата {player_1_choise} занята")
                bot.send_message(chat_id=msg.from_user.id , text=f"Ход игрока {msg.from_user.full_name}, выберите координату для '+' в формате x y" )
                return 
            if my_check_empty(field_value, player_1_choise):
                bot.send_message(chat_id=msg.from_user.id , text=f"Ход игрока {msg.from_user.full_name}, игрок выбрал точку {player_1_choise}")
                my_set_field(field_value, player_1_choise, "+") # размещение на поле
                bot.send_message(chat_id=msg.from_user.id , text=my_field_display(field_value)) # показать текущее состояние поля
                move = 0 # передать ход машине
                # проверка закончилась ли игра
                if my_game_over(field_value, '+'): # проверка победил ли игрок
                    game_over = 1
                if my_check_field(field_value): # проверка есть ли ещё свободные места на поле
                    game_over = 3
    if not move and game_running and not game_over: # ход компьютера
        player_2_choise = machine_spirit(field_value)
        my_set_field(field_value, player_2_choise, "o") # размещение на поле
        bot.send_message(chat_id=msg.from_user.id , text=f"Ход копьютера, он выбрал координату {player_2_choise}" )
        bot.send_message(chat_id=msg.from_user.id , text=my_field_display(field_value)) # показать текущее состояние поля
        move = 1 # передать ход человеку 1
        # проверка закончилась ли игра
        if my_game_over(field_value, 'o'): # проверка победил ли игрок
            game_over = 2
        if my_check_field(field_value): # проверка есть ли ещё свободные места на поле
            game_over = 3
        if game_over == 0:
            bot.send_message(chat_id=msg.from_user.id , text=f"Ход игрока {msg.from_user.full_name}, выберите координату для '+' в формате x y" )
            return 
    # cообщение о результатах  
    if game_running:
        if game_over == 1:
            bot.send_message(chat_id=msg.from_user.id , text=f"Игрок {msg.from_user.full_name} победил") # игрок 1
            game_running = 0
        elif game_over == 2:
            bot.send_message(chat_id=msg.from_user.id , text=f"Компьютер победил") # игрок 2
            game_running = 0
        else:
            bot.send_message(chat_id=msg.from_user.id , text=f"Партия закончилась ничьей") # игрок 2
            game_running = 0
bot.polling()