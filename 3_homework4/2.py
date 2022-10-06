# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59]

from librarium import *

# переменные
in_value = ""
in_value_int = 0
out_quality_bad = True
out_result = []

system('cls')
# обработка входных данных
while (out_quality_bad):
    out_quality_bad = False
    # ввод данных
    in_value = input("Введите целое число: ")
    # проверка является ли это числом с правающей запятой
    if not (in_value.isnumeric()) :
       out_quality_bad = True
    if out_quality_bad : 
        print("Некорректный ввод числа")

in_value_int = abs(int (in_value))

out_result = my_simple_mult(in_value_int)

print(f"Для числа {in_value_int} имеется следующий список простых множителей")
my_list_print(out_result)