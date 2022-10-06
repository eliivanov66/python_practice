from math import *
from os import *
from random import *

def my_list_print(arg_in):
    """ Метод выводящий на экран список с индексом"""
    print("{", end = "")
    for i in range(0, len(arg_in) ):
        print(f" [{i}]={arg_in[i]}", end = "")
    else:
        print(" }")

def my_clear_string(arg_in, arg_target):
    """ Метод чистящий строку от повторов и прочего перед split, с разделителем Arg_target"""
    # чистка исходных данных
    temp_arg_in = ""
    # удаление пустоты вначале
    for i in range(0, len(arg_in) -1 ) :
        if (arg_in[i] != arg_target) :
            temp_arg_in = arg_in[i: len(arg_in)]
            break
    # удаление пустоты в конце
    for i in range(len(temp_arg_in) -1, 0, -1) :
        if (temp_arg_in[i] != arg_target) :
            temp_arg_in = temp_arg_in[0: i + 1]
            break
    # удаление повторов разделителя
    while arg_target*2 in temp_arg_in :
        temp_arg_in = temp_arg_in.replace(arg_target*2,arg_target)
    return temp_arg_in

def my_list_mix(arg_in):
    """Метод перемешивающий список"""
    temp_arg_in = []
    for i in range(0, len(arg_in) ) :
        temp_arg_in.append(None)

    for i in range(0, len(arg_in) ) :
        while True:
            rand_int=Random.randint(0,len(arg_in) - 1)
            if temp_arg_in[rand_int] == None:
                temp_arg_in[rand_int] = arg_in[i]
                break
    return temp_arg_in

def my_conv_dec_to_bin(arg_input):
    """Метод конверсии десятичного числа в двоичное"""
    temp_input = 0
    result = 0 
    position = 0
    temp_input = arg_input
    while (temp_input > 0) :
        result = result + int(((temp_input % 2) != 0)) * int( 10 ** position); 
        temp_input = temp_input // 2 
        position += 1
    return result

def my_generate_fibonacci(arg_input) :
    Fi = (1 + sqrt(5.0))/ 2.0; 
    result = int ( ((Fi ** arg_input) - (- Fi) ** (- arg_input)) / (2.0 * Fi - 1.0) )
    return result

def my_fctrl(arg_input):
    if arg_input <=1:
        return 1
    else:
        return arg_input * my_fctrl(arg_input - 1)

# метод расчёта ПИ до знака
def my_pi(arg_input):
    """Метод использует познаковое вычисление символа числа ПИ (взято с википедии формула Бэйли — Боруэйна — Плаффа)"""
    result = 0.0
    if (arg_input > 0.1):
        result = 3.0
        return result

    iteration = int(round (log ((arg_input) ** (-1.0) , 10.0) ) ) #вычисляем количество знаков, которое нам нужно найти в Пи
    for i in range(iteration) :
        result = result + 16 ** (-i) * (4 / (8 * i + 1) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))
    result = float( int( result * (10 ** iteration) ) / (10 ** iteration) ) 
    return result 

def my_simple_mult(arg_input):
    """Метод возвращающий простые множители целого числа"""
    i = 2
    out_result = []
    temp_arg_input = arg_input
    while i < arg_input:
        if (temp_arg_input % i) == 0 :
            out_result.append(i)
            temp_arg_input =  temp_arg_input // i
        else:
            i += 1
            if i >= arg_input:
                break
    return out_result