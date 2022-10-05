# 1 Вычислить число π c заданной точностью d
# *Пример:* 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from librarium import *

def my_pi_calc_v1(arg_input):
    result = 0.0
    i = 0.0
    while abs(float(int(result)) - result) <= arg_input :
        result = result + my_fctrl(6 * i) * (13591409 + 545140134 * i) / (my_fctrl(3 * i) * (my_fctrl(i)) ** 3 * (-640320) ** (3 * i))
        result = 1 / (result * 1 / ( 426880 * sqrt(10005) ) )
        i += 1.0
        print(result)
    return result

def my_pi_calc_v2(arg_input):
    an = 1.0
    bn = 1 / sqrt(2)
    tn = 1 / 4
    pn = 1.0
    while True:
        print(an, bn, tn, pn, (an + bn)**2 / (4*tn))
        an_1 = (an + bn) /2
        bn_1 = sqrt (an * bn)
        tn_1 = tn - pn * ((an  - an_1)**2)
        pn_1 = 2*pn

        an = an_1
        bn = bn_1
        tn = tn_1
        pn = pn_1

        result = (an + bn)**2 / (4*tn)

        if abs(float (int (result)) - result) < arg_input:
           break

    return result

def my_pi_calc_v3(arg_input):
    result = 0.0
    n = 0.0
    for n in range(arg_input): 
        result = result + 1/( (2*n + 1) * ((-3)**n) )
        n += 1.0
    return 4*result

def my_pi(arg_input):
    result = 0.0
    n = 0.0
    while ( result - float (int (result)) ) > arg_input:
        result = result + ((-1) ** n) / (2 * n + 1 )
        n += 1.0
    return 4 * result
#переменные
in_value = ""
out_quality_bad = True
out_result = 0.0
in_clear = (",", ".", ";", ":", " ", "+", "-")

#обработка входных данных
while (out_quality_bad):
    in_value = input("Введите точность для вычисления Пи: ")
    for i in range(len(in_clear)):                         #приведение чисел для конверсии в вещественные 
        in_value = in_value.replace(in_clear[i], ".") 
    out_quality_bad = False
    if not (in_value.replace(".","").isnumeric()) :
        out_quality_bad = True
        print("Некорректный ввод точности")
        break
out_result = float (in_value)

print(my_pi(out_result))