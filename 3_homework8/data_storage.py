# База пользователя 

''''''
'''login; password; familie; name; status; description'''

'''lesson; login; homework'''
import logger as log

default_username = "None"
default_filename = "C:\Python\Diagram_n_code\python_practice\\2_practice_8\\users.txt"


def data_read(filename=default_filename, id="", actual_user=default_username):
    '''чтение строки записи из файла'''
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        log.logger(filename=log.default_filename, text=f"Файл {filename} не существует", value="")
        print("Файл не существует")
        return -1
    else:
        if len(lines) == 0:
            log.logger(filename=log.default_filename, text=f"пользователь {actual_user} ошибка - файл {filename} пуст",
                       value="")
            print("Данные отсувуют в таблице")
            return -1
    # поиск нужной нам строки в файле
    for line in lines:
        # строка найдена
        if id in line:
            # разбиение строки на отдельные стролбцы
            line_data = str(line.replace(";\n", "")).split(";")
            log.logger(filename=log.default_filename,
                       text=f"пользователь {actual_user} извлёк из файла {filename} записи {id}", value=line_data)
            return line_data
    log.logger(filename=log.default_filename,
               text=f"пользователь {actual_user} ошибка - в файле {filename} нет записи {id}", value="")
    print("Данные отсувуют в таблице")
    return -1


def data_change(filename=default_filename, id="", par=0, value="", actual_user=default_username):
    ''''изменение поля в строке записи'''
    ''''id - ключ для поиска записи в таблице, par - номер столбца в таблице, value - чем заменяем'''
    temp_output = ""  # изменённая строка
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        log.logger(filename=log.default_filename, text=f"Файл {filename} не существует", value="")
        print("Файл не существует")
        return -1
    else:
        if len(lines) == 0:
            log.logger(filename=log.default_filename, text=f"пользователь {actual_user} ошибка - файл {filename} пуст",
                       value="")
            print("Данные отсувуют в таблице")
            return -1

    # проверка - присутсвует ли изменяемая строка в файле
    for line in lines:
        # строка в файле найдена
        if id in line:
            target_line = line
            line_data = str(line.replace(";\n", "")).split(";")
            # номер столбца задан не корректно
            if par not in range(len(line_data)):
                log.logger(filename=log.default_filename,
                           text=f"пользователь {actual_user} ошибка - в файле {filename} в записи {id} нет поля {par}",
                           value="")
                print("ошибка в файле нет указанного столца")
                return -1
            # модификация столбца записи
            line_data[par] = value
            # формирование строки для вставки
            for i in line_data:
                temp_output = f"{temp_output}{i};"
            break
    # пересброрка файла с изменённой строкой
    with open(filename, "w", encoding="utf-8") as file:
        for i in lines:
            if i != target_line:
                file.write(i)
            else:
                file.write(f"{temp_output}\n")
        log.logger(filename=log.default_filename,
                   text=f"пользователь {actual_user} изменил в файле {filename} запись {id} поле {par} на {value}",
                   value="")
        return 1


def data_insert(filename=default_filename, id="", data=[], actual_user=default_username):
    '''Вставка строки записи целиком'''
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        log.logger(filename=log.default_filename, text=f"Файл {filename} не существует", value="")
        print("Файл не существует")
        return -1
    else:
        # проверка данных
        if len(data) == 0:
            log.logger(filename=log.default_filename,
                       text=f"пользователь {actual_user} ошибка добавления записи в файл {filename}",
                       value="пустые данные")
            print("Входные данные нулевого размера")
            return -1
        # проверка совпадает ли данные для вставки с данными в таблице
        if len(lines) > 0:
            line_data = str(lines[0].replace(";\n", "")).split(";")
            if (len(data) + 1) != (len(line_data)):
                log.logger(filename=log.default_filename,
                           text=f"пользователь {actual_user} ошибка добавления записи в файл {filename}",
                           value="длина данных не соотвествует файлу")
                print("Размер входных данных и данных в таблице не совпадают")
                return -1
    # строка для вставки в таблицу
    line_data_insert = f"{id};"
    for i in data:
        line_data_insert = f"{line_data_insert}{i};"

    # проверка, существует ли запись уже в таблице
    for line in lines:
        line_data = str(line.replace(";\n", "")).split(";")
        # присутсвует
        if id in line_data:
            line_target = line
            line_data_old = ""
            for i in line_data:
                line_data_old = f"{line_data_old}{i};"
            # запрос на перезапись       
            key = ""
            while key.lower() != "y" and key.lower() != "n":
                print(f"В таблице присутсвует запись ({line_data_old})")
                print(f"В заменить её на ({line_data_insert})")
                key = input("Заменить Y/N?")
            if key.lower() == "n":
                log.logger(filename=log.default_filename,
                           text=f"пользователь {actual_user} отмена записи {line_data_old} на {line_data_insert} в файл {filename}",
                           value="")
                return 0  # пользователь не заменил запись
            if key.lower() == "y":
                with open(filename, "w", encoding="utf-8") as file:
                    for i in lines:
                        if i != line_target:
                            file.write(i)
                        else:
                            file.write(f"{line_data_insert}\n")
                    log.logger(filename=log.default_filename,
                               text=f"пользователь {actual_user} замена записи {line_data_old} на {line_data_insert} в файл {filename}",
                               value="")
                    return 1  # пользователь заменил запись
    # запись отсуствует в таблице, просто создаём новую запись
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{line_data_insert}\n")
        log.logger(filename=log.default_filename,
                   text=f"пользователь {actual_user} добавил новую запись {line_data_insert} в файл {filename}",
                   value="")
        return 2


def data_remove(filename=default_filename, id="", actual_user=default_username):
    '''удаление строки записи из файла'''
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        log.logger(filename=log.default_filename, text=f"Файл {filename} не существует", value="")
        print("Файл не существует")
        return -1

    # поиск записи в таблице
    for line in lines:
        # запись найдена
        line_data = str(line.replace(";\n", "")).split(";")
        if str(id).lower() == line_data[0]:
            with open(filename, "w", encoding="utf-8") as file:
                # запись всех строк, кроме той что должна быть удалена
                for i in lines:
                    if i != line:
                        file.write(i)
                log.logger(filename=log.default_filename,
                           text=f"пользователь {actual_user} удалил в файле {filename} запись {id}", value="")
                return 1
    print("Запись не найдена в таблице")
    log.logger(filename=log.default_filename,
               text=f"пользователь {actual_user} ошибка - в файле {filename} нет записи {id}", value="")
    return -1


def info_data(filename=default_filename, actual_user=default_username):
    data_id = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        log.logger(filename=log.default_filename, text=f"Файл {filename} не существует", value="")
        print("Файл не существует")
        return -1
    else:
        for line in lines:
            line_data = str(line.replace(";\n", "")).split(";")
            data_temp = data_read(filename, line_data[0], actual_user)
            if data_temp != -1:
                data_id.append(data_temp[0])
    return len(lines), data_id
