# работа с файлами
# a- открытие и добавление данных
# r- открытие для чтения данных
# w- открытие для записи

#import hello as h #подключение другого файла, через псевдоним

# запись в файл
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) #
# data.write("Text 1")
# data.write("Text 2")
# data.close()

# запись в файл способ 2
# with open("d:/python/python_practice/file.txt", 'a') as data:
#     data.write("Text 1 \n")
#     data.write("Text 2 \n")
# чтение из файла
# with open("d:/python/python_practice/file.txt", 'r') as data:
#     for line in data:
#         print(line)

#метод
# def func(*param):
#     res=0
#     for item in param:
#         res += item
#     return res

# print(func(1, 3, -3, 7))

# кортеж, как список, но неизменный, элементы >1 или
# a, b = 3, 4 #простое присвоение
# с = (3,4,7, 10) #кортеж
# с = (3, ) #элементы >1 или (n,)
# t = tuple(colors) #преобразование листа в кортеж
# t = tuple - пустой кортеж
# red, blue, green = t #разложение кортежа

# словари - коллекции с ключом
# dictonary = {}
# dictonary =  {
#     'up': 'вверх',
#     'down' : 'вниз',
#     'left' : 'влево',
#     'right' : 'вправо'
#      }

#множества, изменяеммые или не изменяеммы
#colors = {"red", "green", "blue"} #изменяемые
#colors = frozenset({"red", "green", "blue"}) #неизменяемые
#colors = set()


#списки линкуются как = при этом, при изменении в одном, значения меняются и в другом, линкуются
# pop - удаление из списка
# insert - вставка из списка
# append - добавление значения в лист

#срез списка
#list[2:]

#dir(var_name)  - показывает все методы, которые возможны над ней