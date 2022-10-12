# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import librarium as lib
import os

###########################################################################################
###################################     Было     ##########################################
###########################################################################################

#переменные
in_list = []
in_value = ""
out_list = []
out_quality_bad = True
out_result = 0

#обработка входных данных
while (out_quality_bad):
    in_value = input("Введите список чисел, разделённых через ПРОБЕЛ: ")
    in_value = lib.My_clear_string(in_value, " ")
    in_list = in_value.split(" ")
    for i in range(len(in_list)):
        out_quality_bad = False
        if not in_list[i].isdecimal() :
            out_quality_bad = True
            print("Введённый список содержит не цифровые значения")
            break
#вывод результата ввода
os.system("cls")
print("Получен следующий список чисел: ")
lib.My_list_print(in_list)

# калькуляция
for i in range(len(in_list)):
    if (i % 2 != 0) : #проверка на чётность, согласно условию задачи нумерация индексов с 1
        out_list.append(in_list[i])
        out_result += int(in_list[i]) #суммирование чётных элементов

#вывод результата
print("Нечётные числа списка: ")
lib.My_list_print(out_list)
print(f"Их сумма равна {out_result}")

###########################################################################################
###################################     Стало           ###################################
################################### map list comprehension ################################
out_quality_bad = True
while (out_quality_bad):
    in_value = input("Введите список чисел, разделённых через ПРОБЕЛ: ")
    in_value = list(map(lambda x: int(x) if x.isnumeric() else "", in_value.replace("  ", " ").split()))
    out_quality_bad = len(in_value) == 0
print(in_value)
in_value = [in_value[i] for i in range(len(in_value)) if (i % 2)]
print(f"Нечётные числа списка: {in_value}")
print(f"Их сумма равна {sum(in_value)}")