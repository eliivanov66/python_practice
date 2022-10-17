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
    print(f"====== Карточка контакта c псевдонимом {id} ======")
    print(f"Фамилия: {familie}")
    print(f"Имя: {name}")
    for i in range(len(phones)):
        num = str(i + 1) if i > 0 else ""
        print(f"Номер телефона {num}: {phones[i]}")
    print(f"Примечание: {description}")

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