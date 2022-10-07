# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
from librarium import my_list_print
from os import system

def my_insert_data(arg_input):
    result = ""
    '''Метод формирующий строку многочлена'''
    for i in range(len(arg_input) - 1):
        if arg_input[i] <0 :
            sign = " - "
        else:
            sign = " + "
        if arg_input[i] == 0 :
            continue
        if result == "":
            if arg_input[i] <0 :
                sign = " - "
            else:
                sign = ""
            result = f"{sign} {abs(arg_input[i])} * (x ^ {len(arg_input) - i - 1})"
        else:
            result = f"{result} {sign} {abs(arg_input[i])} * (x ^ {len(arg_input) - i -1})"

    if arg_input[i + 1] !=0:
        if arg_input[i + 1] < 0 :
            sign = " - "
        else:
            sign = " + "
        result = f"{result} {sign} {abs(arg_input[i + 1])}"
    result = f"k={len(arg_input) - 1} => {result} = 0"
    return result
    
# переменные
in_value = ""
in_value_int = 0
out_quality_bad = True
data_input = []
out_result_str = ""
filename_1 = "C:\\Python\\Diagram_n_code\\python_practice\\3_homework4\\Data_1.txt"
filename_2 = "C:\\Python\\Diagram_n_code\\python_practice\\3_homework4\\Data_2.txt"
filename_result = ""

system('cls')
out_quality_bad = True

# выбор файла
while out_quality_bad:
    out_quality_bad = False
    in_value = input("В какой из файлов нужно производить запись 1 - Data_1.txt, 2 - Data_2.txt ")
    if in_value != "1" and in_value != "2" :
        out_quality_bad = True
        system('cls')

if in_value == "2":
    filename_result = filename_2
else:
    filename_result = filename_1

system('cls')
out_quality_bad = True

# обработка входных данных
while (out_quality_bad):
    out_quality_bad = False
    # ввод данных
    in_value = input("Введите натуральную степень k: ")
    # проверка является ли это числом с правающей запятой
    if not (in_value.isnumeric()) :
        out_quality_bad = True
    else:
        in_value_int = abs(int (in_value))
        if in_value_int < 1:
           out_quality_bad = True 
    if out_quality_bad : 
        print("Некорректный ввод числа")


print(f"Для числа натуральной степени к = {in_value_int} сформирован следующий многочлен: ")

# заполнение коэффицентов
for i in range(in_value_int, -1, -1):
    rand_int = randint(-50,50)
    data_input.append( rand_int )
my_list_print(data_input)

# формирование многочлена
out_result_str = my_insert_data(data_input)
print(out_result_str)
# запись многочлена в файл
with open(filename_result,"a", encoding="utf-8") as f:
    f.write(f"{out_result_str} \n")