
from telebot import TeleBot
import telebot
from random import randint

def generate_ai_choise(arg_input, arg_min, arg_max):
    '''метод генерирующий выбор духа машин'''
    if arg_input <= arg_max:
        return arg_input
    if arg_input - arg_max >= arg_max:
        return arg_max
    else:
        return arg_min

candy_count = 2020
human_count = 0
human_choise = 0
ai_choise = 0
ai_count = 0
game_running = 0

move = randint(0,1)
bot = TeleBot("5551738625:AAFE5AXjwLN0Deu7YqhZCQITpeP-YcQDQ04")

@bot.message_handler()
def echo(msg: telebot.types.Message):
    global candy_count
    global human_count
    global human_choise
    global ai_choise
    global ai_count
    global move
    global game_running

    if msg.text.lower() == "играть":
        move = randint(0,1)
        candy_count = randint(100, 300)
        game_running = 1
        ai_count = 0
        human_count = 0
        if move:
            bot.send_message(chat_id=msg.from_user.id , text=f"На столе лежит {candy_count} конфет")
            bot.send_message(chat_id=msg.from_user.id , text=f"Ваш ход, введите количество конфет которое хотите взять со стола в диапазоне 1..28 конфет" )  
            return
        else:
            bot.send_message(chat_id=msg.from_user.id , text=f"На столе лежит {candy_count} конфет")

    if move == 1 and game_running and candy_count > 0:
        if not str(msg.text).isnumeric() and len(msg.text)>0:
            bot.send_message(chat_id=msg.from_user.id , text="Вы ввели не число")
            bot.send_message(chat_id=msg.from_user.id , text=f"На столе лежит {candy_count} конфет")
            bot.send_message(chat_id=msg.from_user.id , text=f"Ваш ход, введите количество конфет которое хотите взять со стола в диапазоне 1..28 конфет" )
        else:
            human_choise = int(msg.text)
            if human_choise > 28 or human_choise < 1:
                bot.send_message(chat_id=msg.from_user.id , text="Значение должно быть в диапазоне 1..28 конфет")
                bot.send_message(chat_id=msg.from_user.id , text=f"На столе лежит {candy_count} конфет")
                bot.send_message(chat_id=msg.from_user.id , text=f"Ваш ход, введите количество конфет которое хотите взять со стола в диапазоне 1..28 конфет" ) 
            elif human_choise > candy_count:
                human_choise = candy_count
            else:
                human_count += human_choise # у человек конфет прибавляется
                candy_count -= human_choise # на столе конфет убавляется
                bot.send_message(chat_id=msg.from_user.id , text=f"Вы взяли {human_choise} конфет, теперь у вас {human_count} конфет")
                bot.send_message(chat_id=msg.from_user.id , text=f"На столе лежит {candy_count} конфет")
                human_choise = 0
                move = 0
    if move == 0 and game_running and candy_count > 0: # передать ход духу машин
        ai_choise = generate_ai_choise(candy_count ,1 , 28)
        ai_count += ai_choise # у духа машин конфет прибавляется
        candy_count -= ai_choise # на столе конфет убавляется
        bot.send_message(chat_id=msg.from_user.id , text=f"Бот взял {ai_choise} конфет, теперь у него {ai_count} конфет")
        bot.send_message(chat_id=msg.from_user.id , text=f"На столе лежит {candy_count} конфет")
        if candy_count >0:
            bot.send_message(chat_id=msg.from_user.id , text=f"Ваш ход, введите количество конфет которое хотите взять со стола в диапазоне 1..28 конфет" ) 
        ai_choise = 0 
        move = 1 # передать ход человеку
        
    if candy_count <= 0 and game_running:
    # 1 = последний ход сделала машина, 0 - сделал человек
        if move:
            ai_count += human_count 
            bot.send_message(chat_id=msg.from_user.id , text=f"Вы проиграли, у духа машин {ai_count} конфет(ы) (он забрал ваши конфеты)")
        else:
            human_count += ai_count
            bot.send_message(chat_id=msg.from_user.id , text=f"Вы победили у вас {human_count} конфет(ы) (вы забрали конфеты бота)")
        game_running = 0
bot.polling()

