
import ui
import storage as db
import import_export as ie
import file_path

from telebot import TeleBot

import telebot

file_db = file_path.file_db
running = 0
navigation = 0
id = None
familie = None
name = None
phones = None
description = None

def init_data():
    global id
    global familie
    global name
    global phones
    global description
    id = None
    familie = None
    name = None
    phones = None
    description = None

def logic():
    bot = TeleBot("5551738625:AAFE5AXjwLN0Deu7YqhZCQITpeP-YcQDQ04")
    global file_db
    @bot.message_handler(commands=['start'])
    def startup(msg: telebot.types.Message):
        global navigation
        global id
        global familie
        global name
        global phones
        global description
        global running
        running = 1 
        init_data()
        navigation = 0
        bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))

    @bot.message_handler(commands=['stop'])
    def shutdown(msg: telebot.types.Message):
        global navigation
        global id
        global familie
        global name
        global phones
        global description 
        global running
        running = 0 
        init_data()
        navigation = 0
        bot.send_message(chat_id=msg.from_user.id , text=f"Приложение остановлено, запустите приложение командой 'Start'")

    @bot.message_handler(commands=['info'])
    def info(msg: telebot.types.Message):
        bot.send_message(chat_id=msg.from_user.id , text="Бот телефонной базы 'Test'")

    @bot.message_handler(commands=['log'])
    def log(msg: telebot.types.Message):
        bot.send_message(chat_id=msg.from_user.id , text=f"Логирование не ведётся")

    @bot.message_handler(content_types=['document','text'])
    def control_logic(msg: telebot.types.Message):
        
        global navigation
        global id
        global familie
        global name
        global phones
        global description 
        global file_db
        global running

        if running:
            key = msg.text
            value = msg.text
        else:
            bot.send_message(chat_id=msg.from_user.id , text=f"Приложение остановлено, запустите приложение командой 'Start'")
            return

        # проверка принадлежит ли ввод разрешённой навигации
        if not str(key).isnumeric() and not (navigation in ui.menu_special):
            bot.send_message(chat_id=msg.from_user.id , text="Некорректный ввод")
            return
        if str(key).isnumeric() and not (navigation in ui.menu_special):
            key = int(key)
            if key not in ui.menu_enable[navigation]:
                bot.send_message(chat_id=msg.from_user.id , text="Некорректный ввод")
                return
        # отрисовка навигации   
        if navigation != 0 and key == 0:
            navigation = 0
            bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
            return
        if navigation == 0 and key != 0:
            navigation = key
            bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
            return
        if navigation == 0 and key ==0:
            running = 0
            bot.send_message(chat_id=msg.from_user.id , text=f"Приложение остановлено, запустите приложение командой 'Start'")
            return
        if navigation == 1: # отображение существующих записей
            if value != str(navigation):
                bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
            if key in ui.menu_enable[navigation]:
                if key == 1:
                    data_count, data_id_collection = db.info_data(file_db)
                    if data_count != 0:
                        for data_id in data_id_collection:
                            data_for_display = db.read_data(f"_i_{data_id}", file_db)
                            if data_for_display != -1:
                                bot.send_message(chat_id=msg.from_user.id , text=ui.data_display(data_for_display))
                        bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                    else:
                        bot.send_message(chat_id=msg.from_user.id , text="База пуста, нужно добавить записи или импортировать")
                    return
                if key == 5:
                    navigation = 5
                    bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                    return
            else:
                bot.send_message(chat_id=msg.from_user.id , text="Некорректный ввод")
                bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))    
        if navigation == 2: # добавление/ редактирование записей
            if value != str(navigation):
                bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
            if key in ui.menu_enable[navigation]:
                if key == 1:
                    navigation = 21
                    init_data()
                    value = None
                if key == 6:
                    navigation = 6
                    bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                    return
            else:
                bot.send_message(chat_id=msg.from_user.id , text="Некорректный ввод")
                bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))  
        if navigation == 3: # поиск записи
            if value != str(navigation):
                bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
            if key in ui.menu_enable[navigation]:
                if key == 1:
                    navigation = 31
                    init_data()
                    value = None
            else:
                bot.send_message(chat_id=msg.from_user.id , text="Некорректный ввод")
                bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))  
        if navigation == 4: # удаление записи
            if value != str(navigation):
                bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
            if key in ui.menu_enable[navigation]:
                if key == 1:
                    navigation = 41
                    init_data()
                    value = None
            else:
                bot.send_message(chat_id=msg.from_user.id , text="Некорректный ввод")
                bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation)) 
        if navigation == 5: # экспорт записей
            if value != str(navigation):
                bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
            if key in ui.menu_enable[navigation]:
                if key == 1:
                    data_collection = []
                    data_count, data_id_collection = db.info_data(file_db)
                    for data_id in data_id_collection:
                        data = db.read_data(data_id, file_db)
                        data_collection.append(data)
                    ie.xml_export(data_collection, file_db.replace(".csv", ".xml"))
                    bot.send_message(chat_id=msg.from_user.id , text="Экспорт данных в xml завершён")
                    bot.send_document(chat_id=msg.from_user.id, document=open(file_db.replace(".csv", ".xml"), "rb"))
                    bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                if key == 2:
                    data_collection = []
                    data_count, data_id_collection = db.info_data(file_db)
                    for data_id in data_id_collection:
                        data = db.read_data(data_id, file_db)
                        data_collection.append(data)
                    ie.html_export(data_collection, file_db.replace(".csv", ".html"))
                    bot.send_message(chat_id=msg.from_user.id , text="Экспорт данных в html завершён")
                    bot.send_document(chat_id=msg.from_user.id, document=open(file_db.replace(".csv", ".html"), "rb"))
                    bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
            else:
                bot.send_message(chat_id=msg.from_user.id , text="Некорректный ввод")
                bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation)) 
        if navigation == 6: # импорт данных
            if value == "0":
                navigation = 0
                bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                return
            if not (msg.content_type == "document"):
                bot.send_message(chat_id=msg.from_user.id , text="Некорректный ввод")
                bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                return
            else:
                file = bot.get_file(msg.document.file_id)
                # получение данных
                downloaded_file = bot.download_file(file.file_path)
                with open(msg.document.file_name, 'wb') as f_out:
                    f_out.write(downloaded_file)

                if (".xml" not in msg.document.file_name) and (".html" not in msg.document.file_name):
                    bot.send_message(chat_id=msg.from_user.id , text="Файл не является файлом бэкапа базы")
                    bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                    return
                else:
                    if (".xml" in msg.document.file_name):
                        data_set = ie.xml_import(msg.document.file_name)
                        db.drop_data(file_db)
                        for data in data_set:
                            data_id, data_body = data
                            db.write_data(data_id, data_body, file_db, 1)
                        bot.send_message(chat_id=msg.from_user.id , text="Импорт данных из xml завершён")
                        bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                    if (".html" in msg.document.file_name):
                        data_set = ie.html_import(msg.document.file_name)
                        db.drop_data(file_db)
                        for data in data_set:
                            data_id, data_body = data
                            db.write_data(data_id, data_body, file_db, 1)
                        bot.send_message(chat_id=msg.from_user.id , text="Импорт данных из html завершён")
                        bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
        if navigation == 21: # диалог добавления новой записи
            if (id is None) and (value is None):
                bot.send_message(chat_id=msg.from_user.id , text=f"Добавление контакта. Введите псевдоним контакта: ")
            if (id is None) and not(value is None):
                id = str(value).lower()
                value = None
            if not (id is None) and (value is None):
                bot.send_message(chat_id=msg.from_user.id , text=f"Добавление контакта {id}. Введите фамилию контакта: ")
            if not (id is None) and (familie is None) and not (value is None):
                familie = str(value).lower()
                value = None
            if not (id is None) and not (familie is None) and (value is None):
                bot.send_message(chat_id=msg.from_user.id , text=f"Добавление контакта {id}. Введите имя контакта: ")
            if not (id is None) and not (familie is None) and (name is None) and not (value is None):
                name = str(value).lower()
                value = None
            if not (id is None) and not (familie is None) and not (name is None) and (value is None):
                bot.send_message(chat_id=msg.from_user.id , text=f"Добавление контакта {id}. Введите номера телефона контакта через ПРОБЕЛ: ")
            if not (id is None) and not (familie is None) and not (name is None) and (phones is None) and not (value is None):
                phones = str(value).split()
                for temp_phone in phones:
                    if not str(temp_phone).isnumeric():
                        bot.send_message(chat_id=msg.from_user.id , text=f"Добавление контакта {id}. Некорректный ввод. Введите номера телефона контакта через ПРОБЕЛ: ")
                        phones = None
                        return
                value = None
            if not (id is None) and not (familie is None) and not (name is None) and not (phones is None) and (value is None):
                bot.send_message(chat_id=msg.from_user.id , text=f"Добавление контакта {id}. Введите описание контакта: ")
            if not (id is None) and not (familie is None) and not (name is None) and not (phones is None) and (description is None) and not (value is None):
                description = value
                value = None
            if not (id is None) and not (familie is None) and not (name is None) and not (phones is None) and not (description is None):
                data_for_display = db.read_data(f"_i_{id}", file_db)
                if data_for_display == -1:
                    db.write_data(id, (familie, name, phones, description), file_db, 1)
                    bot.send_message(chat_id=msg.from_user.id , text=f"Добавление контакта. Cоздана новая запись {id}")
                    bot.send_message(chat_id=msg.from_user.id , text=ui.data_display((id, familie, name, phones, description)))
                    navigation = 2
                    bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                    return
                else:
                    if str(value).lower() != "y" and str(value).lower() != "n":
                        bot.send_message(chat_id=msg.from_user.id , text=f"Добавление контакта {id}. Запись  найдена в базе")
                        bot.send_message(chat_id=msg.from_user.id , text=f"Добавление контакта {id}. Cуществующая:")
                        bot.send_message(chat_id=msg.from_user.id , text=ui.data_display(data_for_display))
                        bot.send_message(chat_id=msg.from_user.id , text=f"Добавление контакта {id}. Изменения:")
                        bot.send_message(chat_id=msg.from_user.id , text=ui.data_display((id, familie, name, phones, description)))
                        bot.send_message(chat_id=msg.from_user.id , text=f"Добавление контакта {id}. Перезаписать Y/N?")
                    if str(value).lower() == "y":
                        db.write_data(id, (familie, name, phones, description), file_db, 1)
                        bot.send_message(chat_id=msg.from_user.id , text=f"Добавление контакта. Существующая запись {id} обновлена")
                        navigation = 2
                        bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                        return
                    if str(value).lower() == "n":
                        bot.send_message(chat_id=msg.from_user.id , text="Добавление контакта. Отменено")
                        navigation = 2
                        bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                        return
        if navigation == 31: # диалог поиска записи
            if (id is None) and (value is None):
                bot.send_message(chat_id=msg.from_user.id , text=f"Поиск контакта. Введите псевдоним контакта: ")
            if (id is None) and not (value is None):
                id = str(value).lower()
                data_for_display = db.read_data(f"_i_{id}", file_db)
                if data_for_display != -1:
                    bot.send_message(chat_id=msg.from_user.id , text=f"Запись найдена")
                    bot.send_message(chat_id=msg.from_user.id , text=ui.data_display(data_for_display))
                    navigation = 3
                    bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                    return
                else:
                    bot.send_message(chat_id=msg.from_user.id , text=f"Запись не найдена")
                    navigation = 3
                    bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                    return
        if navigation == 41: # диалог удаления записи
            if (id is None) and (value is None):
                bot.send_message(chat_id=msg.from_user.id , text=f"Удаление контакта. Введите псевдоним контакта: ")
            if (id is None) and not (value is None):
                id = str(value).lower()
                data_for_display = db.read_data(f"_i_{id}", file_db)
                if data_for_display != -1:
                    bot.send_message(chat_id=msg.from_user.id , text=f"Удаление контакта {id}. Запись найдена")
                    bot.send_message(chat_id=msg.from_user.id , text=ui.data_display(data_for_display))
                    bot.send_message(chat_id=msg.from_user.id , text=f"Удаление контакта {id}. Удалить Y/N?")
                    return
                else:
                    bot.send_message(chat_id=msg.from_user.id , text=f"Запись не найдена")
                    navigation = 4
                    bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                    return
            if not (id is None) and not (value is None):
                    if str(value).lower() != "y" and str(value).lower() != "n":
                        bot.send_message(chat_id=msg.from_user.id , text=f"Удаление контакта {id}. Запись найдена")
                        bot.send_message(chat_id=msg.from_user.id , text=ui.data_display(data_for_display))
                        bot.send_message(chat_id=msg.from_user.id , text=f"Удаление контакта {id}. Удалить Y/N?")
                    if str(value).lower() == "y":
                        db.delete_data(id, file_db, 1)
                        bot.send_message(chat_id=msg.from_user.id , text=f"Удаление контакта {id}. Контакт удалён")
                        navigation = 4
                        bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                        return
                    if str(value).lower() == "n":
                        bot.send_message(chat_id=msg.from_user.id , text=f"Удаление контакта {id}. контакта. Отменено")
                        navigation = 4
                        bot.send_message(chat_id=msg.from_user.id , text=ui.menu_navigation(navigation))
                        return

    bot.polling()