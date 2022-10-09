# 5*. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.

#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

from os import system

def my_data_extract():
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

in_value = my_data_extract()

print(in_value)

