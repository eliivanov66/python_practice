# def sum(a,b):
#     """Сумма элементов"""
#     """a - int, b - int"""
#     return (a+b)
# print(sum(7,4))
# print(help(sum))
# print(dir(str))
# ctl + / - комментировать

#import librarium #импорт из библиотеки

# is - сравнивает два объекта 

from random import Random
import random
Result=[]
N = int(input("Введите число N: "))
for i in range(0, abs(N),1):
    Result.append(random.randint(-100,100))
print(f"Получена следующая последовательность {N}: {Result}")
