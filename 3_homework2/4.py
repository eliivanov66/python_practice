# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

# переменные
N =""
a = ""
b = ""
N_list = []
Temp_list = []
# пока пользователь не ввёл число
while not ( N.isdigit() ) :
    N = input("Введите число N: ")
# заполнение результата
for i in range( - int(N), int(N) + 1 ):
    N_list.append(i)
    Temp_list.append( len(N_list) - 1 )
# вывод результата
print("{", end = "")
for i in range(0, len(N_list) ):
    print(f" [{i}]={N_list[i]}", end = "")
else:
    print(" }")
# запрос первого индекса
while not ( a.isdigit() ) :
    a = input("Введите индекс первого элемента: ")
    if a.isdigit():
       if (int(a) < 0) or (int(a) > len(N_list) - 1):
        a=""
print(f"Первый элемент [{int(a)}] = {N_list[int(a)]}") 
# запрос второго индекса
while not ( b.isdigit() ) :
    b = input("Введите индекс второго элемента: ")
    if b.isdigit():
       if (int(b) < 0) or (int(b) > len(N_list) - 1):
        b=""
print(f"Второй элемент [{int(b)}] = {N_list[int(b)]}")
# вывод результата 
print(f"Произведение элемента [{int(a)}] = {N_list[int(a)]} и элемента [{int(b)}] = {N_list[int(b)]}, равно : {N_list[int(a)]* N_list[int(b)]}")