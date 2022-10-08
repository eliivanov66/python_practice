# 1 2 3 4 6 7 8 9

# 1. В файле находится N натуральных чисел, записанных через пробел. 
#    Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1] + 1. 
#    Найдите это число.


# 2. Напишите программу, удаляющую из текста все слова, содержащие "абв". <- filter


# 3. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
#    Порядок элементов менять нельзя.
    
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

with open( "Data_1.txt", "w") as file:
    file.write(input("Введите последовательность чисел через ПРОБЕЛ:"))

with open( "Data_1.txt", "r") as file:
    list_ = [int(i) for i in file.readline().split() ]

print("Исходный лист")
print(list_)

list_result = [item for item in list_]

for i in range(len(list_)):
    if list_[i] != list_[i - 1] + 2 and (i - 1 > 0):
       list_result.insert(i + 1, list_[i - 1] + 2)
       print(f"i = {i}, list_result = {list_result[i]}")

print("Получен следующий ")
print(list_result)

