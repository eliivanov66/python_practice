# Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# метод факториал
def My_factorial(In_arg) :
    if In_arg!=0 :
        return In_arg * My_factorial(In_arg - 1)
    else:
        return 1

###########################################################################################
###################################     Было     ##########################################
###########################################################################################
 
# переменные
N =""
N_list = []
# пока пользователь не ввёл число
while not (N.isdigit()) :
    N = input("Введите число N: ")
# заполнение результата
for i in range(1, int(N) + 1 ) :
    N_list.append(My_factorial(i))
# вывод результата
print(f"Для числа N={N} получен следующий набор значений: {N_list}")

###########################################################################################
###################################     Стало     #########################################
###############################  list comprehension  ######################################

while not (N.isdigit()) :
    N = input("Введите число N: ")
N_list = [My_factorial(i) for i in range(1, int(N) + 1)]
print(f"Для числа N={N} получен следующий набор значений: {N_list}")