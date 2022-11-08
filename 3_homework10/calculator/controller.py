

from dataclasses import replace
import file_path
import mathemathic
import logger
from telebot import TeleBot
import telebot

file_log = file_path.file_log

def logic():
    bot = TeleBot("")
    global file_db
    @bot.message_handler(commands=['start'])
    def startup(msg: telebot.types.Message):
        bot.send_message(chat_id=msg.from_user.id , text=f"Кнопка 'Start' бесполезна калькулятору")

    @bot.message_handler(commands=['stop'])
    def shutdown(msg: telebot.types.Message):
        bot.send_message(chat_id=msg.from_user.id , text=f"Кнопка 'Stop' калькулятор не остановить")

    @bot.message_handler(commands=['info'])
    def info(msg: telebot.types.Message):
        bot.send_message(chat_id=msg.from_user.id , text=f"Бот с калькулятором действительных и комплексных чисел /nВведите строку для вычисления, для мнимой единицы используйте 'i'")
    
    @bot.message_handler(commands=['log'])
    def log(msg: telebot.types.Message):
        global file_log
        '''чтение лога из файла'''
        try:
            with open(file_log, "r", encoding="utf-8") as f_log:
                lines = f_log.readlines()
                for line in lines:
                    line = line.replace(";"," ")         
        except FileNotFoundError:
            bot.send_message(chat_id=msg.from_user.id , text=f"Бот с калькулятором, файл лога отсутсвует")
            bot.send_message(chat_id=msg.from_user.id , text=f"Бот с калькулятором действительных и комплексных чисел /nВведите строку для вычисления, для мнимой единицы используйте 'i'")
        else:
            for line in lines:
                bot.send_message(chat_id=msg.from_user.id , text=f"{line}")
        

    @bot.message_handler(content_types=['text'])
    def control_logic(msg: telebot.types.Message):
        global file_log
        input_value = msg.text
        temp_value = mathemathic.string_to_formula(input_value)   
        if not (temp_value is None):
            output_value = mathemathic.formula_calculate(temp_value)
            if not (output_value is None):
                bot.send_message(chat_id=msg.from_user.id , text=f"Результат {input_value} = {output_value}")
                logger.logger(file_log, f"Пользователь {msg.from_user.full_name}: Результат вычисления формулы {input_value}", output_value) 
            else:
                bot.send_message(chat_id=msg.from_user.id , text=f"Бот с калькулятором, Вы ввели некорректную формулу {input_value} - возможно деление на ноль")
                logger.logger(file_log, f"Пользователь {msg.from_user.full_name}: Попытка деления на ноль {input_value}", "")   
        else:
            bot.send_message(chat_id=msg.from_user.id , text=f"Бот с калькулятором, Вы ввели некорректную формулу {input_value}")
            logger.logger(file_log, f"Пользователь {msg.from_user.full_name}: Ввёл некорректную формулу {input_value}", "")
        bot.send_message(chat_id=msg.from_user.id , text=f"Бот с калькулятором действительных и комплексных чисел /nВведите строку для вычисления, для мнимой единицы используйте 'i'")
    bot.polling()
