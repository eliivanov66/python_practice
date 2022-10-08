#1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# файлы - исходный и после обработки и удаления слов

filename_in = "C:\\Python\\Diagram_n_code\\python_practice\\3_homework5\\Data_1_In.txt"
filename_out = "C:\\Python\\Diagram_n_code\\python_practice\\3_homework5\\Data_1_Out.txt"
punkt_symbols = (",", ".", ";", ":", "-")

# исходный текст
with open(filename_in, "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("Исходный текст : ")
    print(lines)
    lines = list(map(lambda x: x.replace("\n",""), lines)) # удаление знака перехода на новую строку
    for symbol in punkt_symbols:
        lines = list(map(lambda x: x.replace(symbol,f" {symbol}"), lines)) # чтобы знаки препинания не удалялись
    lines = list(map(lambda x: x.split(), lines)) # разбиение строк на отдельные слова

# получение искомого слова
in_target = input("Введите набор для удаления слов из текста: ")

# удаление слов, которые содержат искомое слово
for line in lines:
    #если в каком-то слове строки есть искомое, удаляем его из строки
    line = list(map( lambda word : line.remove(word) if in_target.lower() in word.lower() else word , line) ) 

# сборка строк
lines = list(map(" ".join, lines))

for symbol in punkt_symbols:
    lines = list(map(lambda x: x.replace(f" {symbol}", symbol), lines)) # удаление лишних пробелов у знаков припинания

# запись результата
with open(filename_out, "w", encoding="utf-8") as file:
    for line in lines:
        file.write(f"{line}\n")

# показать результат
with open(filename_out, "r", encoding="utf-8") as file:
    print("Текст после обработки : ")
    print(file.readlines())

