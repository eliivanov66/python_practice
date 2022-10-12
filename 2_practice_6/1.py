# Строкой матиматическое выражение
#2*4 + 5

from unittest import result


in_value = "1 * 33/3 - 11 * 1" # = "4 * 11/4 - 13 * 1" =  - 11
list_digits = []
list_operations = []
list_math_law = ["*", "/" , "+", "-"]
list_result = []
out_result = 0.0

in_value = in_value.replace(" ","")

for i in range(len(in_value)):
    if not in_value[i].isdigit():
       list_operations.append(in_value[i])

for i in list_operations:
    in_value = in_value.replace(i, " ")

list_digits = in_value.split()
list_digits = [int(a) for a in list_digits]

print(f"Исходная строка {in_value}")
print(f"Исходные цифры {list_digits}")
print(f"Исходнаые операции {list_operations}")

for i in range(len(list_math_law)):
    for j in range(len(list_operations)):
        if list_math_law[i] == list_operations[j]:
            if  list_operations[j] == list_math_law[0]:
                out_result = list_digits[j] * list_digits[j + 1]
                list_digits[j] = out_result
                list_digits[j + 1] = out_result
            elif  list_operations[j] == list_math_law[1]:
                out_result = list_digits[j] / list_digits[j + 1]
                list_digits[j] = out_result
                list_digits[j + 1] = out_result 
            elif  list_operations[j] == list_math_law[2]:
                out_result = list_digits[j] + list_digits[j + 1]
                list_digits[j] = out_result
                list_digits[j + 1] = out_result 
            elif  list_operations[j] == list_math_law[3]:
                out_result = list_digits[j] - list_digits[j + 1]
                list_digits[j + 1] = out_result

    print(out_result)
print(f"Результат математической операций {out_result}")                 
           
    

