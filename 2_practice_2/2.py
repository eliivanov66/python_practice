Result=[]
N = int(input("Введите число N: "))
for i in range(1, abs(N),1):
    Result.append(3 * i + 1)
print(f"Получена следующая последовательность {N}: {Result}")