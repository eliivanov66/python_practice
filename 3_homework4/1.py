# 1 Вычислить число π c заданной точностью d
# *Пример:* 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from librarium import *

# переменные
in_value = ""
out_quality_bad = True
out_result = 0.0

system('cls')
# обработка входных данных
while (out_quality_bad):
    out_quality_bad = False
    # ввод данных
    in_value = input("Введите точность для вычисления Пи: ")
    # проверка является ли это числом с правающей запятой
    if not (in_value.replace(".","").isnumeric()) :
       out_quality_bad = True
    for i in range (len(in_value)):
        if (in_value[i].isdigit()) and (in_value[i] != "0") and (in_value[i] != "1"):
            out_quality_bad = True
            break
    if out_quality_bad : 
        print("Некорректный ввод точности  ")

out_result = float (in_value)
print(f"Задана точность : {out_result}")
print(f"Расчитанное число Пи : {my_pi(out_result)}")
print(f"Проверочное число Пи : {pi}")