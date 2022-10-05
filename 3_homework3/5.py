#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# метод генерирующий числа в ряде Фибоначчи
from math import sqrt
import librarium as lib

def generate_fibonacci(arg_input) :
    Fi = (1 + sqrt(5.0))/ 2.0; 
    result = int ( ((Fi ** arg_input) - (- Fi) ** (- arg_input)) / (2.0 * Fi - 1.0) )
    return result

mem = {0:0, 1:1, 2:1}
def new_generate_fibonacci(arg_input): 
    if arg_input not in mem:
       mem[arg_input]=new_generate_fibonacci(arg_input-1) + new_generate_fibonacci(arg_input-2)
    return mem[arg_input]

# переменные
in_value = ""
out_quality_bad = True
out_value = 0
out_result = []
in_clear = (",", ".", ";", ":", " ")


# обработка входных данных
while (out_quality_bad):
    in_value = input("Введите число: ")
    for i in range(len(in_clear)):                         #приведение чисел для конверсии в вещественные 
        in_value = in_value.replace(in_clear[i], "") 
    out_quality_bad = False
    if not (in_value.isnumeric()) :
        out_quality_bad = True
        print("Некорректный ввод числа")
        break
out_value = int(in_value)

# калькуляция
for i in range( - out_value, out_value + 1) :
    #out_result.append( new_generate_fibonacci(i))
    out_result.append( generate_fibonacci(i) )

# вывод результата
print(f"Для числа {out_value} получен следующий ряд Фибоначчи: ")
lib.My_list_print(out_result)
