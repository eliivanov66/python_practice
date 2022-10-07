# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.

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

def my_data_analyzer(arg_input):
    data_list = []
    clearing_list = ["(x ^ ", ")", "+ "]
    data_start = 0
    result_data = []
    '''Метод извлекающий данные из строки с многочленом'''
    # поиск начала / конца записи данных
    for i in range(0, len(arg_input)): 
        if arg_input[i] == ">":
            data_start = i + 1
            break
    data_temp = str(arg_input[data_start:(len(arg_input) - 5)]) #срез многочлена
    data_temp = f"{data_temp}*0"
    # удаление мусора
    for i in range(len(clearing_list)):
        data_temp = data_temp.replace(clearing_list[i], "")
    # корректировка знаков чисел
    for i in range(0, len(data_temp)):
        data_temp = data_temp.replace("+ ", "+")
        data_temp = data_temp.replace("- ", "-")
        data_temp = data_temp.replace(" * ", "*")
    
    # удаление пустоты вначале
    for i in range(0, len(data_temp) -1 ) :
        if (data_temp[i] != " ") :
            data_temp = data_temp[i: len(data_temp)]
            break
    # удаление пустоты в конце
    for i in range(len(data_temp) -1, 0, -1) :
        if (data_temp[i] != " ") :
            data_temp = data_temp[0: i + 1]
            break
    # удаление повторов разделителя
    while " "*2 in data_temp :
        data_temp = data_temp.replace(" "*2," ")

    # выделение отдельных сегментов многочлена
    data_list = data_temp.split(" ")
    for i in range(len(data_list)):
        k, n = data_list[i].split("*")
        
        #создание результирующего листа
        if i == 0: # результирующий лист начинает заполнение
           for j in range(int(n) + 1):
                result_data.append(0)

        result_data[ - int(n) - 1] = int(k)
        
    return result_data

# переменные
data_lines_1 = [] #данные из первого файла, служебная информация
data_lines_2 = [] #данные из второго файла, служебная информация
data_result  = [] #данные для результирующего файла, служебная информация
filename_1 = "C:\\Python\\Diagram_n_code\\python_practice\\3_homework4\\Data_1.txt" # исходная информация 1, сгенерирования 4.Py
filename_2 = "C:\\Python\\Diagram_n_code\\python_practice\\3_homework4\\Data_2.txt" # исходная информация 2, сгенерирования 4.Py
filename_result = "C:\\Python\\Diagram_n_code\\python_practice\\3_homework4\\Data_result.txt" # результирующая информация

system('cls')

with open(filename_1, "r") as f:
    lines_1 = len(f.readlines())

with open(filename_2, "r") as f:
    lines_2 = len(f.readlines())

# служебная информация и ритуалы извлечения данных из файло
print(f"Первый файл {filename_1}")
print(f"Первый файл содержит {lines_1} записей")
print(f"Второй файл {filename_2}")
print(f"Второй файл содержит {lines_2} записей")

# извлечение данных из первого файла
with open(filename_1, "r") as f:
    for i in range(lines_1):
        line_1 = f.readline().replace("\n", "")
        data_lines_1.append (my_data_analyzer(line_1))

# извлечение данных из второго файла
with open(filename_2, "r") as f:
    for i in range(lines_2):
        line_2 = f.readline().replace("\n", "")
        data_lines_2.append (my_data_analyzer(line_2))

# выравнивание размеров числа записей в данных
while len(data_lines_1) != len (data_lines_2):
    if len(data_lines_1) > len (data_lines_2):
        data_lines_2.append([])
    if len(data_lines_1) < len (data_lines_2):
        data_lines_1.append([])

# выравнивание размеров записей, теперь число записей равно
for i in range(len(data_lines_1)):
    while len(data_lines_1[i]) != len (data_lines_2[i]):
        if len(data_lines_1[i]) > len (data_lines_2[i]):
            data_lines_2[i].insert(0, 0)
        if len(data_lines_1[i]) < len (data_lines_2[i]):
            data_lines_1[i].insert(0,0)
print("Данные из первого файла")
print(data_lines_1)
print("Данные из второго файла")
print(data_lines_2)

# формирование результироующих записей для выходного файла
for i in range(len(data_lines_1)):
    data_result.append([])
    for j in range(len(data_lines_1[i])):
        data_result[i].append( data_lines_1[i][j] + data_lines_2[i][j] )

print("Данные для результирующего файла")
print(data_result)

# запись результирующих данных в файл
with open(filename_result, "w") as f:
    for i in range(len(data_result)):
        f.write(f"{my_insert_data(data_result[i])} \n")

# if lines_1 >= lines_2: #файл один содержит больше записей чем второй
#     # в файлах хранится разное число записей
#     for i in range( abs (lines_1 - lines_2) ):
#         data_lines_2.append([]) # пустая запись в конце
#     for i in range(lines_1):
#         data_1_len = len(data_lines_1[i])
#         print(f"Debug data_1_len {data_1_len}")
#         data_2_len = len(data_lines_2[i])
#         print(f"Debug data_2_len {data_2_len}")
#         # многочлены разной длины
#         if data_1_len >= data_2_len:
#             for i in range(abs (data_1_len - data_2_len) ):
#                 print(f"Debug i {i}")
#                 data_lines_2[i].append([]) # пустая запись в конце
#         else:
#             for i in range(abs (data_1_len - data_2_len) ):
#                 data_lines_1[i].append([]) # пустая запись в конце
#         data_result.append (data_lines_1[i] + data_lines_2[i])
#         print(f"Debug data_result {data_result}")
# else:
#     # в файлах хранится разное число записей
#     for i in range(abs (lines_1 - lines_2)):
#         data_lines_1.append([]) # пустая запись в конце
#     for i in range(lines_2):
#         data_1_len = len(data_lines_1[i])
#         data_2_len = len(data_lines_2[i])
#         # многочлены разной длины
#         if data_1_len >= data_2_len:
#             for i in range(abs (data_1_len - data_2_len) ):
#                 data_lines_2[i].append([]) # пустая запись в конце
#         else:
#             for i in range(abs (data_1_len - data_2_len) ):
#                 data_lines_1[i].append([]) # пустая запись в конце
#         data_result.append (data_lines_1[i] + data_lines_2[i])
# print("Результирующие данные")
# print(data_result)

        