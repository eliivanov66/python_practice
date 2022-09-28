str_a  = ""
str_b  = ""
result = 0

while (len(str_b)>=len(str_a)):
    str_a = input("Введите первую строку: ")
    str_b = input("Введите вторую строку: ")

for i in range(0, len(str_a)):
    if str_b == str_a[i:i + len(str_b)]:
        result+=1
    else:
        continue
print(f"Строка ({str_b}) входит {result} раз в строку ({str_a})")
