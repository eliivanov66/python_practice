#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

#Возможны 2**3 комбинаций
LogicList = [
                [0,0,0],
                [1,0,0],
                [1,1,0],
                [1,1,1],
                [0,1,1],
                [0,0,1],
                [1,0,1],
                [0,1,0]
            ]
for i in range(0, len(LogicList)-1):
    x = LogicList[i][0]
    y = LogicList[i][1]
    z = LogicList[i][2]
    print(f"Комбинация [x:{x},y:{y},z:{z}]")
    LeftPart = not(x or y or z)
    print(f"Левая часть выражения: ¬(X ⋁ Y ⋁ Z) {LeftPart}")
    RightPart = not x and not y and not z
    print(f"Правая часть выражения: ¬X ⋀ ¬Y ⋀ ¬Z {RightPart}")
    if (LeftPart==RightPart):
        print("Левая часть эквивалента правой")
    else:
        print("Левая часть НЕ эквивалента правой")