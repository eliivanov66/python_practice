# Задание 5 Реализуйте алгоритм перемешивания списка.
from random import Random
import random
# методы
def My_list_print(Arg_in):
    """ Метод выводящий на экран список с индексом"""
    print("{", end = "")
    for i in range(0, len(Arg_in) ):
        print(f" [{i}]={Arg_in[i]}", end = "")
    else:
        print(" }")

def My_clear_string(Arg_in, Arg_target):
    """ Метод чистящий строку от повторов и прочего перед split, с разделителем Arg_target"""
    # чистка исходных данных
    Temp_Arg_in = ""
    # удаление пустоты вначале
    for i in range(0, len(Arg_in) -1 ) :
        if (Arg_in[i] != Arg_target) :
            Temp_Arg_in = Arg_in[i: len(Arg_in)]
            break
    # удаление пустоты в конце
    for i in range(len(Temp_Arg_in) -1, 0, -1) :
        if (Temp_Arg_in[i] != Arg_target) :
            Temp_Arg_in = Temp_Arg_in[0: i + 1]
            break
    # удаление повторов разделителя
    while Arg_target*2 in Temp_Arg_in :
        Temp_Arg_in = Temp_Arg_in.replace(Arg_target*2,Arg_target)
    return Temp_Arg_in

def My_List_Mix(Arg_in):
    """Метод перемешивающий список"""
    Temp_arg_in = []
    for i in range(0, len(Arg_in) ) :
        Temp_arg_in.append(None)

    for i in range(0, len(Arg_in) ) :
        while True:
            Rand_int=random.randint(0,len(Arg_in) - 1)
            if Temp_arg_in[Rand_int] == None:
                Temp_arg_in[Rand_int] = Arg_in[i]
                break
    return Temp_arg_in
# переменные
N_list = []
N = ""
# получение данных от пользователя
N = input("Введите список через ПРОБЕЛ: ")
# чистка списка
N = My_clear_string(N, " ")
print(N)
# разбивка строки на список
N_list=N.split(" ")  
# вывод результата
print("Получен следующий список: ")
My_list_print(N_list)
# перемешивание
N_list=My_List_Mix(N_list)
print("Список после перемешивания: ")
My_list_print(N_list)