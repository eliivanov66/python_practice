# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

#метод конвертации 10ого числа в 2ое
def my_conv_dec_to_bin(arg_input):
    #переменные
    temp_input = 0
    result = 0 
    position = 0
    temp_input = arg_input
    while (temp_input > 0) :
        result = result + int(((temp_input % 2) != 0)) * int( 10 ** position); 
        temp_input = temp_input // 2 
        position += 1
    return result

#переменные
in_value = ""
out_quality_bad = True
out_result = 0
in_clear = (",", ".", ";", ":", " ")

#обработка входных данных
while (out_quality_bad):
    in_value = input("Введите число: ")
    for i in range(len(in_clear)):                         #приведение чисел для конверсии в вещественные 
        in_value = in_value.replace(in_clear[i], "") 
    out_quality_bad = False
    if not (in_value.isnumeric()) :
        out_quality_bad = True
        print("Некорректный ввод числа")
        break

#калькуляция
out_result = int(in_value)

#вывод результата
print(f"Число {out_result} в двоичном виде имеет представление {my_conv_dec_to_bin(out_result)}")
