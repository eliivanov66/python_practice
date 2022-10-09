# 5*. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.

#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

from os import system

def my_data_extract():
    '''метод извлечения исходной последовательности из строки'''
    out_quality_bad = True
    in_value = ""
    while out_quality_bad:
        in_value = input("Введите числовую последовательность через ПРОБЕЛ: ")
        out_value = in_value.split()
        out_quality_bad = False
        for i in out_value:
            if not i.isnumeric():
                out_quality_bad = True
                break
            if i.isnumeric() and int(i) < 0:
                out_quality_bad = True
                break
        if not out_quality_bad:
            out_value = [int(x) for x in out_value]
        if out_quality_bad:
            system("cls")
            print("Некорректный ввод последовательности")
    return out_value

def my_sequence_build(arg_data):
    '''генератор всевозможных возрастающих последовательностей для списка чисел'''
    out_result = []
    for i in range(0, len(arg_data)):
        sub_result = []
        sub_result.append(arg_data[i])
        for j in range(i, len(arg_data)):
            if max(arg_data[j], sub_result[- 1]) == arg_data[j]:
                sub_result.append(arg_data[j])
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
in_data = [] # исходный список
out_data = [] # результат список с последовательностями

system("cls")

# ввод данных
in_data = my_data_extract()
# показать результат ввода
print("Получен следующий список: ")
print(in_data)

# получение всех возможных комбинаций последовательностей
out_data = my_sequence_build(in_data)

# вывод результата
print("Получен список возможных комбинаций возрастающих последовательностей")
for data in out_data:
    print(f"{out_data.index(data)}:{data}")