# проверяет есть ли число в списке
def My_list_print(Arg_in):
    """ Метод выводящий на экран список с индексом"""
    print("{", end = "")
    for i in range(0, len(Arg_in) ):
        print(f" [{i}]={Arg_in[i]}", end = "")
    else:
        print(" }")

def My_clear_string(Arg_in, Arg_target):
    """ Метод чистящий строку от повторов и прочего перед split, с разделителем Arg_target"""
    # чистка исходных данных
    Temp_Arg_in = ""
    # удаление пустоты вначале
    for i in range(0, len(Arg_in) -1 ) :
        if (Arg_in[i] != Arg_target) :
            Temp_Arg_in = Arg_in[i: len(Arg_in)]
            break
    # удаление пустоты в конце
    for i in range(len(Temp_Arg_in) -1, 0, -1) :
        if (Temp_Arg_in[i] != Arg_target) :
            Temp_Arg_in = Temp_Arg_in[0: i + 1]
            break
    # удаление повторов разделителя
    while Arg_target*2 in Temp_Arg_in :
        Temp_Arg_in = Temp_Arg_in.replace(Arg_target*2,Arg_target)
    return Temp_Arg_in

#переменные
source_value = ""
_source_value = ""
count_value = -1

#ввод данных
source_value = input("Введите список, элементы разделены ПРОБЕЛОМ: ")
source_value = My_clear_string(source_value," ")
_source_value = source_value.split(" ")
print("Получен следующий список: ")
print(My_list_print(_source_value))

for i in range(len(_source_value)):
    if _source_value[i].isnumeric():
        count_value = i
        break

if count_value != -1:
    print("В списке: ")
    print(My_list_print(_source_value))
    print(f"Есть число {_source_value[count_value]} на позиции {count_value}")
    print(f"Находитя на  {i} позиции")
else:
    print("В списке: ")
    print(My_list_print(_source_value))
    print(f"Нет цифр")