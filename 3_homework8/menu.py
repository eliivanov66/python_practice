from user_interface import login_dialog as login
from user_interface import int_checker
from user_interface import user_interface as interface


def menu():
    while True:
        menu_key = int_checker("Добро пожаловть\n1 - Вход\n0 - Завершение работы\n---->")
        if menu_key == 0:
            print("Всего доброго!")
            break
        elif menu_key == 1:
            user_data = -1
            while user_data == -1:
                user_data = login()
            interface(user_data)
        else:
            print("Введите корректные данные")
