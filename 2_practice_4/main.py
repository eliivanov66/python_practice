filename = "D:\\Python\python_practice\\2_practice_4\\file.txt"
f=open(filename,"a", encoding="utf-8")
f.write(f"{input('Введите текст для файла: ')} \n")
f.close
with open(filename,"r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
f.close
