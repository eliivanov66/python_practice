# Ускоренная обработка данных

##################################
# Lambda методы (анонимные методы)
##################################
def f(x):
    return x ** 2

g = f # переменная, которая хранит ссылку на метод

print(g(4))
print(f(4))

def sum(x, y): # метод 1
    return x + y

def mult(x, y): # метод 2
    return x * y

def lambda_calc(operation, a, b): # метод с аргументом-ссылкой на метод
    return operation(a, b)

print(lambda_calc(mult ,3 , 6 )) # вызов метода

sum_l = lambda x, y : x + y # переменная - lambda метод
sub_l = lambda x, y : x - y # переменная - lambda метод
mul_l = lambda x, y : x * y # переменная - lambda метод
div_l = lambda x, y : x // y if y!=0 else 0  # переменная - lambda метод

print(lambda_calc(sum_l , 6 , 3 )) # вызов метода
print(lambda_calc(sub_l , 6 , 3 )) # вызов метода
print(lambda_calc(mul_l , 6 , 3 )) # вызов метода
print(lambda_calc(div_l , 6 , 3 )) # вызов метода

print(lambda_calc(lambda x, y : x + y , 6 , 3 )) # вызов метода
print(lambda_calc(lambda x, y : x - y , 6 , 3 )) # вызов метода
print(lambda_calc(lambda x, y : x * y , 6 , 3 )) # вызов метода
print(lambda_calc(lambda x, y : x // y if y!=0 else 0 , 6 , 3 )) # вызов метода
#############################

##################################
# быстрое создание листов
##################################

fast_list = [(i ** 2) for i in range(10) ] # простой вариант
print(fast_list)

fast_list = [(i ** 2) for i in range(10) if not (i % 2) ] # условный вариант
print(fast_list)

fast_list = [i ** 2 if i != 0 else -1 for i in range(10) if not (i % 2) ] # условный вариант c условием вначале
print(fast_list)

##################################
# практическое задание
##################################
def select(func, col):
    return [func(x) for x in col]

def where(func, col):
    return [x for x in col if func(x)]

data = "1 2 3 5 8 15 23 38".split(" ")

res = select(int, data) # извлечение всех чисел как int
print(f"select(int, data) = {res}")

res = where(lambda x :  not (x % 2) and (x != 0) , res) # извлечение всех чётных как int
print(f"where(lambda x : not (x % 2) and (x != 0)  , res) = {res}")

res = select(lambda x : (x, x ** 2), res) #создание кортежа (x , x^2)
print(f"select(lambda x : (x, x ** 2), res) = {res}")

##################################
# функция map - маппинг данных
##################################
# map(function, data for function) - результат мепа итератор - по нему можно пробежаться лишь 1 раз

li = [i for i in range(1, 20) ]
res = map(lambda x : (x, x ** 2), li)
res = list(res)
print(f"map(lambda x : (x, x ** 2), [1, 2 , 3, 4, 5]) = {res}")

data = input("Введите строку данных, разделённых через ПРОБЕЛ: ").split(" ")
data = list(map(int, data)) #получение листа переменных
print(data)
data = list(map(int, input("Введите строку данных, разделённых через ПРОБЕЛ: ").split(" "))) #получение листа переменных
print(data)

data = map(int, input("Введите строку данных, разделённых через ПРОБЕЛ: ").split(" ")) #получение мэпа переменных
for d in data:
    print(d)
print("По итератору можно пробежаться лишь 1 раз ----------")
for d in data: # в этом месте данных уже не будет
    print(d)

# в итоге функция select используемая ранее больше не нужна и ей можно заминить на map
data = "1 2 3 5 8 15 23 38".split(" ")
res = list(map(lambda x : (int(x), int(x) ** 2), data) ) #создание кортежа (x , x^2)
print(f"list(map(lambda x : (x, x ** 2), data) ) = {res}")

##################################
# функция filter - фильтр данных
##################################
# filter(function, data for function) - результат мепа итератор - по нему можно пробежаться лишь 1 раз
data = "1 2 3 5 8 15 23 38".split(" ")
res = list(filter(lambda x : not int(x) % 2 and int(x) != 0, data))
print(f"list(filter(lambda x : not int(x) % 2 and int(x) !=0, data)) = {res}")

##################################
# функция zip - получение набора кортежа данных на основе уже имеющихся
##################################
# zip(data1, data2, ... datan) - результат мепа итератор - по нему можно пробежаться лишь 1 раз
res = list(zip([1,2,3], ["a", "b", "c"]))
print(res)

res = list(zip([1,2,3], ["a", "b", "c"], ["+", "-"])) # кортеж формируется по минимальному набору данных
print(res)

##################################
# функция enumirate - получение набора кортежа данных на основе набора, нумеруя его
##################################
# enumirate(data) - результат мепа итератор - по нему можно пробежаться лишь 1 раз
res = list(enumerate (["a", "b", "c"]))
print(res)