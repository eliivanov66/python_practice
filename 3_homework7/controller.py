
import ui
import storage as db
import import_export as ie

from os import system

def control_logic(file_db):
    key = ""
    system('cls')
    while key.lower() != "q":
        print("================ Телефонная база TEST ================")
        print("1 - показать существующие записи")
        print("2 - добавить-редактировать запись")
        print("3 - найти запись")
        print("4 - удалить запись")
        print("5 - экспорт базы")
        print("6 - импорт базы")
        print("Q - Выход из приложения")
        key = input("Ваш выбор: ")
        if key == "1":
            system('cls')
            print("================ Телефонная база TEST ================")
            print("================ \существующие записи ===============")
            print("1 - вывести на экран")
            print("5 - экспортировать базу в файл целиком")
            print("0 - Назад")
            key = ""
            while key != "1" and key != "0" and key !="5":
                key = input("Ваш выбор: ")
                if key == "1":
                    data_count, data_id_collection = db.info_data(file_db)
                    if data_count != 0:
                        for data_id in data_id_collection:
                            data_for_display = db.read_data(f"_i_{data_id}", file_db)
                            if data_for_display != -1:
                                ui.data_display(data_for_display)
                    else:
                        print("База пуста, нужно добавить записи или импортировать")
            if key == "1" or key == "0":
                continue
        if key == "2":
            system('cls')
            print("================ Телефонная база TEST ================")
            print("================ \добавить-редактировать запись =====")
            print("1 - ввести данных вручную")
            print("6 - импортировать из файла базу целиком")
            print("0 - Назад")
            key = ""
            while key != "1" and key != "0" and key != "6":
                key = input("Ваш выбор: ")
                if key == "1":
                    id = str(ui.single_input(str, "псевдоним контакта")).lower()
                    db.write_data(id, ui.data_input(), file_db, 0)
            if key == "1" or key == "0":
                continue
        if key == "3":
            system('cls')
            print("================ Телефонная база TEST ================")
            print("================ \найти запись =====")
            print("1 - Перейти к вводу данных записи")
            print("0 - Назад")
            key = ""
            while key != "1" and key != "0":
                key = input("Ваш выбор: ")
                if key == "1":
                    data_id = str(ui.single_input(str, "псевдоним контакта")).lower()
                    data_for_display = db.read_data(f"_i_{data_id}", file_db)
                    if data_for_display != -1:
                        ui.data_display(data_for_display)
            continue
        if key == "4":
            system('cls')
            print("================ Телефонная база TEST ================")
            print("================ \удалить запись =====")
            print("1 - Перейти к вводу данных записи")
            print("0 - Назад")
            key = ""
            while key != "1" and key != "0":
                key = input("Ваш выбор: ")
                if key == "1":
                    id = str(ui.single_input(str, "псевдоним контакта")).lower()
                    db.delete_data(id, file_db, 0)
            continue
        if key == "5":
            system('cls')
            print("================ Телефонная база TEST ================")
            print("================ \экспорт базы =====")
            print("1 - экспорт базы в XML")
            print("2 - экспорт базы в HTML")
            print("0 - Назад")
            key = ""
            while key != "1" and key != "2" and key != "0":
                key = input("Ваш выбор: ")
                if key == "1":
                    data_collection = []
                    data_count, data_id_collection = db.info_data(file_db)
                    for data_id in data_id_collection:
                        data = db.read_data(data_id, file_db)
                        data_collection.append(data)
                    ie.xml_export(data_collection, file_db.replace(".csv", ".xml"))
                if key == "2":
                    data_collection = []
                    data_count, data_id_collection = db.info_data(file_db)
                    for data_id in data_id_collection:
                        data = db.read_data(data_id, file_db)
                        data_collection.append(data)
                    ie.html_export(data_collection, file_db.replace(".csv", ".html"))
            continue
        if key == "6":
            system('cls')
            print("================ Телефонная база TEST ================")
            print("================ \импорт базы =====")
            print("1 - импортировать базу из XML")
            print("2 - импортировать базу из HTML")
            print("0 - Назад")
            key = ""
            while key != "1" and key != "2" and key != "0":
                key = input("Ваш выбор: ")
                if key == "1":
                    data_set = ie.xml_import(file_db.replace(".csv", ".xml"))
                if key == "2":
                    data_set = ie.html_import(file_db.replace(".csv", ".html"))
                db.drop_data(file_db)
                for data in data_set:
                    data_id, data_body = data
                    db.write_data(data_id, data_body, file_db, 1)
            continue
