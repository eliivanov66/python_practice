#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import librarium as lib
import os

#переменные
in_list = []
in_value = ""
out_list = []
out_quality_bad = True
out_result = 0.0
in_clear = (",", ".", ";", ":")
out_minimum = 0.0
out_maximum = 0.0

#обработка входных данных
while (out_quality_bad):
    in_value = input("Введите список чисел, разделённых через ПРОБЕЛ: ")
    in_value = lib.My_clear_string(in_value, " ")          #удаление лишних пробелов
    for i in range(len(in_clear)):                         #приведение чисел для конверсии в вещественные 
        in_value = in_value.replace(in_clear[i], ".") 
    in_list = in_value.split(" ")
    for i in range(len(in_list)):                          #проверка если пользователь ввёл не числовые значения
        out_quality_bad = False
        if not (in_list[i].replace(".","").isnumeric()) :
            out_quality_bad = True
            print("Введённый список содержит не цифровые значения")
            break
for i in range(len(in_list)):                              #получение списка вещественных чисел
    out_list.append(float(in_list[i]))
#вывод результата ввода
os.system("cls")
print("Получен следующий список чисел: ")
lib.My_list_print(out_list)

# калькуляция, поиск минимальной дробной и максимальной дробной части списка вещественных чисел
out_minimum = out_list[0] - float(int(out_list[0])) #минимальная дробная часть
out_maximum = out_list[0] - float(int(out_list[0])) #максимальныя дробная часть
out_minimum = round(out_minimum, 1)
out_maximum = round(out_maximum, 1)
for i in range(len(out_list)):
    #минимальная дробная часть
    if out_list[i] - float(int(out_list[i])) < out_minimum :
       out_minimum = out_list[i] - float(int(out_list[i]))
       out_minimum = round(out_minimum, 1)
    #максимальная дробная часть
    if out_list[i] - float(int(out_list[i])) > out_maximum :
       out_maximum = out_list[i] - float(int(out_list[i]))
       out_maximum = round(out_maximum, 1)
#вывод результата
print(f"Минимальная дробная часть равна: {out_minimum}, максимальная дробная часть равна: {out_maximum}")
print(f"Их разница равна: {out_maximum - out_minimum}")
