# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

from librarium import *

#переменные
in_list = []
in_value = ""
out_list = []
out_quality_bad = True
out_result = 0

system("cls")
#обработка входных данных
while (out_quality_bad):
    in_value = input("Введите последовательность чисел, разделённых через ПРОБЕЛ: ")
    in_value = my_clear_string(in_value, " ")
    in_list = in_value.split(" ")
    for i in range(len(in_list)):
        out_quality_bad = False
        if not in_list[i].isdecimal() :
            out_quality_bad = True
            print("Введённый список содержит не цифровые значения")
            break
#вывод результата ввода
system("cls")
print("Получен следующая последовательность чисел: " )
my_list_print(in_list)

for i in range (len(in_list)):
    if in_list.count(in_list[i]) == 1:
        out_list.append(in_list[i])

if len(out_list) > 0:
    print("Она содержит неповторяющиеся значения: " )
    my_list_print(out_list)
else:
    print("Все числа последовательности повторяются" )
