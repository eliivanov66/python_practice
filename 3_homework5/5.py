# 5*. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.

#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

from os import system

def my_data_extract(arg_value):
    '''метод извлечения исходной последовательности из строки'''
    out_quality_bad = False
    out_value = f"{arg_value}".split()
    for i in out_value:
        if not i.isnumeric():
            out_quality_bad = True
            break
        if i.isnumeric() and int(i) < 0:
            out_quality_bad = True
            break
    if len(out_value) < 2:
        out_quality_bad = True
    if not out_quality_bad:
        out_value = [int(x) for x in out_value]
    if out_quality_bad:
        return None
    return out_value

def my_sequence_build(arg_value):
    '''генератор всевозможных возрастающих последовательностей для списка чисел'''
    out_result = []
    for i in range(0, len(arg_value)):
        sub_result = []
        sub_result.append(arg_value[i])
        for j in range(i, len(arg_value)):
            if max(arg_value[j], sub_result[- 1]) == arg_value[j]:
                sub_result.append(arg_value[j])
        if (len(sub_result) > 2):
            sub_result.pop(0)
            out_result.append(sub_result)    
            # out_result.append(my_sequence_build(sub_result))
    for i in range(len(out_result)):
        if len(out_result[i]) > 2:
            temp_result = []
            for j in range(1, len(out_result[i])):    
                temp_result = out_result[i].copy()
                temp_result.pop(j)
                out_result.append(temp_result)
    temp_result = []
    [temp_result.append(a) for a in out_result if a not in temp_result ]
    return temp_result
    # return out_result

# переменные
filename_in = "C:\\Python\\Diagram_n_code\\python_practice\\3_homework5\\Data_5_In.txt" # файлик источник
filename_out = "C:\\Python\\Diagram_n_code\\python_practice\\3_homework5\\Data_5_Out.txt" # файлик результат
in_data = [] # исходный список
out_data = [] # результат список с последовательностями

system("cls")

# ввод данных
with open(filename_in, "r", encoding="utf-8") as file:
    temp_data = file.readline()
in_data = my_data_extract(temp_data)

if in_data != None:
    # показать результат ввода
    print("Получен следующий список: ")
    print(in_data)

    # получение всех возможных комбинаций последовательностей
    out_data = my_sequence_build(in_data)

    # вывод результата
    print("Получен список возможных комбинаций возрастающих последовательностей")
    for data in out_data:
        print(f"{out_data.index(data)}:{data}")

    with open(filename_out, "w", encoding="utf-8") as file:
        file.write(f"Исходная последовательность {in_data}\n")
        for data in out_data:
            file.write(f"{out_data.index(data)}:{data}\n")

else:
    print("Исходный файл не содержит последовательности целых положительных чисел")