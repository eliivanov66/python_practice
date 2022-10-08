# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# aaaaaaaaaaaaaaaaaaaaaabbb222aaabbwwwwcc
# 9a9a5a3b3a222b4w2c
# aaaaaaaabbbaaabbwwwwcc

def my_rle_coding(arg_input):
    '''Метод сжимающий строку по RLE алгоритму'''
    count = 1
    out_value = ""
    for i in range(len(arg_input)):
        if (i + 1) < len(arg_input):
            if (arg_input[i + 1] == arg_input[i]) and count<9:
                count += 1
            else:
                out_value = f"{out_value}{count}{arg_input[i]}"
                count = 1
        else:
            out_value = f"{out_value}{count}{arg_input[i]}" 
    return out_value

def my_rle_decoding(arg_input):
    '''Метод восстанавливающий строку по RLE алгоритму'''
    out_value = ""
    if (len(arg_input) % 2) :
        out_value="Введённая строка не закодирована RLE методом"
        return out_value
    else:
        for i in range(0, len(arg_input), 2):
            if not arg_input[i].isdigit():
                out_value="Введённая строка не закодирована RLE методом"
                return out_value
            else:
                out_value = f"{out_value}{int(arg_input[i]) * arg_input[i+1]}"
    return out_value    

def rle(arg_method, arg_filename_in, arg_filename_out):
    '''Метод сжатия / разжатия данных по RLE в файле'''
    # исходные данные
    with open(arg_filename_in, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # сжатие строк по-методу RLE
    lines = [arg_method(line) for line in lines]
    # запись результата
    with open(arg_filename_out, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(f"{line}")

# переменные
input_value = "" # исходная строка
decripted_value = "" # строка сжатая
encripted_value = "" # строка восстановленная
filename_in = "C:\\Python\\Diagram_n_code\\python_practice\\3_homework5\\Data_4_In.txt"
filename_temp = "C:\\Python\\Diagram_n_code\\python_practice\\3_homework5\\Data_4_Temp.txt"
filename_out = "C:\\Python\\Diagram_n_code\\python_practice\\3_homework5\\Data_4_Out.txt"

# исходные данные  
in_value = input("Введите произвольную строку: ")
print("Исходная строка:")
print(in_value)

# сжатие
decripted_value = my_rle_coding(in_value)
print("Сжатая строка:")
print(decripted_value)

# восстановление
encripted_value = my_rle_decoding(decripted_value)
print("Восстановленная строка:")
print(encripted_value)

# сжатие данных в файле
rle(my_rle_coding, filename_in, filename_temp)
# извлечение данных в файле
rle(my_rle_decoding, filename_temp, filename_out)

