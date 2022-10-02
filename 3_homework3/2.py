# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import librarium as lib
import os

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
for i in range(len(in_list) // 2 ):
    out_list.append( int(in_list[i]) * int(in_list[len(in_list) - 1 - i]) )
else: #элемент, у которого нет пары умножаем сам на себя
    if len(in_list) % 2 != 0:
        out_list.append(int(in_list[len(in_list)// 2]) * int(in_list[len(in_list)// 2]))

#вывод результата
print("Произведеление пар чисел равна: ")
lib.My_list_print(out_list)