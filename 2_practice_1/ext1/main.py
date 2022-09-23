#1 Проверка являются ли числа квадратами
a = (int)(input("Введите первое число: "))
b = (int)(input("Введите второе число: "))

if (a ** 2 == b) or (b ** 2 == a):
    print(f"Числа {a} и {b} являются числом и квадратом")
else:
    print(f"Числа {a} и {b} не являются числом и квадратом")

#2 Нахождение максимального числа в массиве
list=[0,0,0,0,0]
for i in range (0, len(list)):
    list[i] = (int)(input(f"Введите число {i + 1}/{len(list)}: "))

maximal = list[0]
for i in range (0, len(list)):
    if (list[i] > maximal): 
        maximal = list[i]
print(f"Максимальное число из ряда {list}: {maximal}")

#3 Нахождение составных чисел числа
a = (int)(input("Введите число: "))
result = []
for i in range(2, a//2 + 1):
    while (a % i == 0):
        result.append(i)
        a = a // i
print(result)
