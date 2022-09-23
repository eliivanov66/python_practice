#value=None
from operator import truediv
from pickle import FALSE, TRUE


value=43
print(type(value))
a=1
b=2.3
c="test"
print("{}  - {} - {}".format(a,b,c))  #форматирование
print(f"{a}/{b}/{c}") #форматирование
list = [1,2,3,4]
print(list)
d=int(input("Введите входную переменную"))
print(type(d))
print(d)
print(d//1) #//-целое деление, % - остаток деления
a=3
a=a+5
a+=5
print(a)
f=[1,2,3,4]
print(2 in f) #проверка нахождения числа в f
f.append=5 #Добавление

if FALSE:
    #
    #
    #
    print(FALSE)
elif TRUE:
    print('monkey')
else:
    #
    #
    #
    print(TRUE)

while TRUE: #цикл 
    print(TRUE)
else:
    print(FALSE)
print("Monkey 2")

for i in [1,2,3,4,5]: #цикл
    print(i)

r=range(10) #значения от 0 до 9
for i in range(10):
    print(i)
for i in range(1,10,2): #начало, конец и шаг
    print(i)

str="test string variable"
print(len(str))
print
#methods
def f(x):
    if x==1:
        return "Целое"
    elif x==2.3:
        return "Плавающая запятая"
    elif x=="Строка":
        return "Строка"