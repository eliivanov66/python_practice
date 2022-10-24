import storage as db

def single_input(data_type, text_in):
    value_bad = 1

    while value_bad:
        try:
            temp_out = data_type(input(f"Введите {str(text_in).lower()}: "))
        except:
            value_bad = 1
            print("Некорректный ввод")
        else:
            print(f"Введён {str(text_in).lower()}: {temp_out} " )
            key = ""
            while (key.lower() != "n") and (key.lower() != "y"):
                key = input("Скорректировать ввод Y/N? :")
            if key.lower() == "n":
                value_bad = 0
            else:
                value_bad = 1
    return temp_out

def data_display(data):
    id, familie, name, phones, description = data
    out_value = "" 
    out_value =(f"{out_value}====== Карточка контакта c псевдонимом {id} ======\n")
    out_value =(f"{out_value}Фамилия: {familie}\n")
    out_value =(f"{out_value}Имя: {name}\n")
    for i in range(len(phones)):
        num = str(i + 1) if i > 0 else ""
        out_value =(f"{out_value}Номер телефона {num}: {phones[i]}\n")
    out_value =(f"{out_value}Примечание: {description}")
    return out_value

def data_input():
    key = "y"
    familie = ""
    name = ""
    phones = []
    description = ""
    familie = single_input(str, "фамилию")
    name = single_input(str, "имя")
    phones.append(abs(single_input(int, "телефон")))
    while key == "y":
        key = input("Добавить доп. номер ввод Y/N? :")
        if key == "y":
            phones.append(str(single_input(int, "телефон")))
    description = single_input(str, "примечание")
    return familie, name, phones, description

menu_enable = [[0,1,2,3,4,5,6], [1,5,0], [1,6,0], [1,0], [1,0], [1,2,0], [1,2,0]]
menu_special = [6, 21, 31, 41]
def menu_navigation(arg_input):
    arg_input = str(arg_input)
    if arg_input == "0":
        out_value = f""
        out_value = f"{out_value}================ Телефонная база TEST ================\n"
        out_value = f"{out_value}1 - показать существующие записи\n"
        out_value = f"{out_value}2 - добавить-редактировать запись\n"
        out_value = f"{out_value}3 - найти запись\n"
        out_value = f"{out_value}4 - удалить запись\n"
        out_value = f"{out_value}5 - экспорт базы\n"
        out_value = f"{out_value}6 - импорт базы\n"
        out_value = f"{out_value}0 - Выход из приложения\n"
        out_value = f"{out_value}Ваш выбор: "
    if arg_input == "1":
        out_value = f""
        out_value = f"{out_value}================ Телефонная база TEST ================\n"
        out_value = f"{out_value}================ \существующие записи ===============\n"
        out_value = f"{out_value}1 - вывести на экран\n"
        out_value = f"{out_value}5 - экспортировать базу в файл целиком\n"
        out_value = f"{out_value}0 - Назад"
    if arg_input == "2":
        out_value = f""
        out_value = f"{out_value}================ Телефонная база TEST ================\n"
        out_value = f"{out_value}================ \добавить-редактировать запись =====\n"
        out_value = f"{out_value}1 - ввести данных вручную\n"
        out_value = f"{out_value}6 - импортировать из файла базу целиком\n"
        out_value = f"{out_value}0 - Назад"
    if arg_input == "3":
        out_value = f""
        out_value = f"{out_value}================ Телефонная база TEST ================\n"
        out_value = f"{out_value}================ \найти запись =====\n"
        out_value = f"{out_value}1 - Перейти к вводу данных записи\n"
        out_value = f"{out_value}0 - Назад"
    if arg_input == "4":
        out_value = f""
        out_value = f"{out_value}================ Телефонная база TEST ================\n"
        out_value = f"{out_value}================ \удалить запись =====\n"
        out_value = f"{out_value}1 - Перейти к вводу данных записи\n"
        out_value = f"{out_value}0 - Назад"
    if arg_input == "5":
        out_value = f""
        out_value = f"{out_value}================ Телефонная база TEST ================\n"
        out_value = f"{out_value}================ \экспорт базы =====\n"
        out_value = f"{out_value}1 - экспорт базы в XML\n"
        out_value = f"{out_value}2 - экспорт базы в HTML\n"
        out_value = f"{out_value}0 - Назад"
    if arg_input == "6":
        out_value = f""
        out_value = f"{out_value}================ Телефонная база TEST ================\n"
        out_value = f"{out_value}================ \импорт базы =====\n"
        out_value = f"{out_value}прикрепить файл базы в xml - импортировать базу из XML\n"
        out_value = f"{out_value}прикрепить файл базы в html - импортировать базу из HTML\n"
        out_value = f"{out_value}0 - Назад"
    return out_value