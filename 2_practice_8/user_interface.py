from data_storage import data_change as change
from data_storage import data_read as read
from data_storage import info_data

file_users = "c:\\Users\\nikkl\\OneDrive\\Рабочий стол\\GeekBrains\\Python\\Семинары\\L8\\users.txt"
file_marks = "c:\\Users\\nikkl\\OneDrive\\Рабочий стол\\GeekBrains\\Python\\Семинары\\L8\\marks.txt"
file_ht = "c:\\Users\\nikkl\\OneDrive\\Рабочий стол\\GeekBrains\\Python\\Семинары\\L8\\home_tasks.txt"


def int_checker(input_text):
    while True:
        try:
            return int(input(f"{input_text}"))
        except ValueError:
            print("Введите корректное число")


def student_interface(user_data):
    print(f"Доброе пожаловать {user_data[2]} {user_data[3]}\n {user_data[6]}")
    info = info_data(file_ht)
    if info != -1:
        lenght_of_subjects, subjects_list = info
        menu_text = "Выберете предмет:\n0.Выход\n"
        for i in range(len(subjects_list)):
            menu_text = f"{menu_text} {i + 1}.{subjects_list[i]}\n"
        while True:
            ui_button = int_checker(
                'Выберете действие:\n0.Выход\n1.Показать Домашнее задание\n2.Таблица успеваемости\n---->')
            if ui_button == 0:
                return print("Всего хорошего!")
            elif ui_button == 1:
                while True:
                    subject_key = int_checker(f"{menu_text}----> ")
                    if subject_key == 0:
                        return print("Всего хорошего!")
                    if subject_key in range(1, lenght_of_subjects + 1):
                        task = read(
                            file_ht,
                            subjects_list[subject_key - 1])
                        print(task[1])
                        break
                    else:
                        print("\nВведите корректные данные\n")
            elif ui_button == 2:
                marks = read(
                    file_marks,
                    user_data[0])
                if marks != -1:
                    for el in range(1, len(marks), 2):
                        print(f"{marks[el]}: {marks[el + 1]}")
            else:
                print("\nВведите корректные данные\n")
            while True:
                ui_button = int_checker("------------\nЖелаете продолжить?\n0 - Да\n1 - Нет\n---->")
                if ui_button == 1:
                    return print("Всего хорошего!")
                elif ui_button == 0:
                    break
                else:
                    print("\nВведите корректные данные\n")


def teacher_interface(user_data):
    print(f"Доброе пожаловать {user_data[2]} {user_data[3]}\n {user_data[6]}")
    while True:
        subject_key = int_checker(
            "Выберете действие:\n9.Выход\n1.Изменить домашнее задание\n2.Изменить табель успеваемости\n---->")
        if subject_key == 9:
            return print("Всего хорошего!")
        if subject_key == 1:
            task = read(
                file_ht,
                user_data[5])
            print(f"Текущее домашнее задание: {task[1]}")
            while True:
                subject_key = int_checker("Хотите изменить уже имеющееся задание?\n1 - Да\n0 - Нет\n---->")
                if subject_key == 1:
                    task = input("Задание: ")
                    change(file_ht,
                           user_data[5], 1, task)
                    print("Готово")
                elif subject_key == 0:
                    break
                else:
                    print("Введите корректные данные")
                break
        elif subject_key == 2:
            names = info_data(file_marks)
            if names != -1:
                lenght_of_names, names_list = names
                list_of_names = "Выберете ученика:\n0.Выход\n"
                for i in range(len(names_list)):
                    temp_data = read(
                        file_users,
                        names_list[i], user_data[0])
                    list_of_names = f"{list_of_names} {i + 1}.{temp_data[2]} {temp_data[3]}\n"
                ui_button = int_checker(f"{list_of_names}----> ")
                if ui_button == 0:
                    return print("Всего хорошего!")
                elif ui_button in range(1, lenght_of_names + 1):
                    marks = read(
                        file_marks,
                        names_list[ui_button - 1])
                    for i in range(len(marks)):
                        temp_data = read(
                            file_users,
                            names_list[ui_button - 1], user_data[0])
                        if marks[i] == user_data[5]:
                            print(f'Оценка ученика {temp_data[2]} {temp_data[3]}: {marks[i + 1]}')
                            while True:
                                mark_button = int_checker("Хотите изменить оценку?\n0.Нет\n1.Да\n---->")
                                if mark_button == 0:
                                    break
                                elif mark_button == 1:
                                    mark = 0
                                    while mark not in range(1, 6):
                                        mark = int_checker("Новая оценка: ")
                                    print(names_list[ui_button - 1])
                                    change(
                                        file_marks,
                                        names_list[ui_button - 1], i + 1, str(mark), user_data[0])
                                    break
                                else:
                                    print("Введите корректные данные")
        else:
            print("Введите корректные данные")
        while True:
            ui_button = int_checker("------------\nЖелаете продолжить?\n0 - Да\n1 - Нет\n---->")
            if ui_button == 1:
                return print("Всего хорошего!")
            elif ui_button == 0:
                break
            else:
                print("\nВведите корректные данные\n")


def login_dialog():
    login = input("Введите ваш логин:")
    passw = input("Введите ваш пароль:")
    data_read_req = read(
        "c:\\Users\\nikkl\\OneDrive\\Рабочий стол\\GeekBrains\\Python\\Семинары\\L8\\users.txt",
        id=login, actual_user=login)
    if data_read_req != -1:
        if data_read_req[1] == passw:
            ret_value = data_read_req
        else:
            print(f"Неверный пароль")
            ret_value = -1
    else:
        print("Пользователь не найден")
        ret_value = -1
    return ret_value


def user_interface(user_data: list):
    if int(user_data[4]):
        student_interface(user_data)
    else:
        teacher_interface(user_data)
