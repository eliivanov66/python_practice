'''
Фамилия, Имя, Телефон, Описание
'''
from ast import Pass

def pack_data(data):
    '''метод упаковки данных в строку'''
    data_pack = ""
    (familie, name, phones, description) = data
    data_pack = f"_f_{familie};_n_{name};"
    for phone in phones:
        data_pack = f"{data_pack}_p_{phone};"
    data_pack = f"{data_pack}_d_{description};"
    return data_pack

def extract_data(data):
    ''''метод распаковки данных из строки'''
    bad_value = 0
    id = ""
    familie = ""
    name = ""
    phones = []
    description = ""
    markers = ["_i_", "_f_", "_n_", "_p_", "_d_"]
    data_extract = data.split(";")

    # проверка строки на содержание данных
    for marker in markers:
        if not (marker in data):
            bad_value = 1
            break
    if not bad_value:
    # извлечение данных из строки
        for item in data_extract:
            for marker in markers:
                if marker in item:
                    if marker == "_i_":
                        id = item.replace(marker, "")
                    if marker == "_f_":
                        familie = item.replace(marker, "")
                    if marker == "_n_":
                        name = item.replace(marker, "")
                    if marker == "_p_":
                        phones.append(item.replace(marker, ""))
                    if marker == "_d_":
                        description = item.replace(marker, "")
        return id, familie, name, phones, description
    else:
        print("Строка не содержит данных")
        # строка не содержит данных
        return -1

def write_data(id, data, file_name = "\data.csv", auto_rewrite = 0):
    familie, name, phones, description = data
    '''метод записи в хранилище'''
    with open(file_name, "r", encoding = "utf-8") as file:
        lines = file.readlines()
    # проверка есть id в записях
    for line in lines:
        if f"_i_{id}" in line:
            _id, _familie, _name, _phones, _description = (extract_data(line))
            phones_line = ""
            for phone in phones:
                phones_line = f"{phones_line} тел:{phone},"
            _phones_line = ""
            for phone in _phones:
                _phones_line = f"{_phones_line} тел:{phone},"
            
            if not auto_rewrite:
                print(f"Пользователь {_id}: {_familie}, {_name}, {_phones_line} {_description}, найден в базе")
                print(f"Заменить на новые данные {id}: {familie}, {name}, {phones_line} {description}")
            key = ""
            while (key.lower() != "n") and (key.lower() != "y") and not auto_rewrite:
                key = input("Перезаписать данные Y/N?:")
            if key.lower() == "y" or auto_rewrite:
                with open(file_name, "w", encoding = "utf-8") as file:
                    for i in lines:
                        if i != line:
                            file.write(f"{i}".lower())
                        else:
                            file.write(f"_i_{id};{pack_data(data)}\n".lower())
                    return 2 # запись найдена в базе, пользователь выбрал заменять данные
            else:
                return 3 # запись найдена в базе, но пользователь выбрал не заменять данные
    with open(file_name, "a", encoding = "utf-8") as file:
        file.write(f"_i_{id};{pack_data(data)}\n".lower())
        return 1 # создана новая запись

def read_data(id, file_name = "\data.csv"):
    '''метод чтения записи из хранилища'''
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line in lines:
        if f"{id}" in line:
            return extract_data(line)
    return -1

def delete_data(id, file_name = "\data.csv", auto_delete = 0):
    '''метод удаляющий запись из хранилища'''
    with open(file_name, "r", encoding = "utf-8") as file:
        lines = file.readlines()
    # проверка есть id в записях
    for line in lines:
        if f"_i_{id}" in line:
            _id, _familie, _name, _phones, _description = (extract_data(line))
            _phones_line = ""
            for phone in _phones:
                _phones_line = f"{_phones_line} тел:{phone},"
            if not auto_delete:
                print(f"Пользователь {_id}: {_familie}, {_name}, {_phones_line} {_description}, найден в базе")
            key = ""
            while (key.lower() != "n") and (key.lower() != "y") and not auto_delete:
                key = input("Удалить запись Y/N?:")
            if key.lower() == "y" or auto_delete:
                with open(file_name, "w", encoding = "utf-8") as file:
                    for i in lines:
                        if i != line:
                            file.write(f"{i}")
                    return 2 # запись найдена в базе, пользователь удалил запись
            else:
                return 3 # запись найдена в базе, но пользователь выбрал не удалять
    if not auto_delete:
        print("Запись не найдена в базе")
    return -1

def info_data(file_name = "\data.csv"):
    data_id = []
    '''метод возвращающий информацию о хранилище'''
    with open(file_name, "r", encoding = "utf-8") as file:
        lines = file.readlines()
        for line in lines:
            data_temp = extract_data(line)
            if data_temp != -1:
                _id, _familie, _name, _phones, _description = data_temp
                data_id.append(_id)
    return len(lines), data_id

def drop_data(file_name = "\data.csv"):
    '''Очистка хранилища'''
    with open(file_name, "w", encoding = "utf-8") as file:
        Pass