import logger

special_symbols = ["*", "/", "+", "-", "(", ")", "i"]

def string_to_formula(arg_input):
    global special_symbols
    arg_input = str(arg_input)
    
    # разделяем значимые данные пробелом
    arg_input = arg_input.replace(" ", "")
    arg_input = arg_input.replace(",", ".")
    arg_input = arg_input.replace("*i", "i")
    
    while ("--" in arg_input):
        arg_input = arg_input.replace("--", "+")

    while ("-+" in arg_input):
        arg_input = arg_input.replace("-+", "-")
    
    for i in special_symbols:
        while i*2 in arg_input and (i != "i"):
            arg_input = arg_input.replace(i*2, i)

    for i in special_symbols:
        if i != "i":
            arg_input = arg_input.replace(i, f" {i} ")
    
    if arg_input[0:2] == " +" or arg_input[0:2] == " *" or arg_input[0:2] == " /":
        arg_input = f"1.0 *{arg_input[2:len(arg_input)]}"
    if arg_input[0:2] == " -":
        arg_input = f"-1.0 *{arg_input[2:len(arg_input)]}"

    arg_input = arg_input.split()

    for i in arg_input:
        if not i.replace(".","").replace("-","").isnumeric() and (i not in special_symbols) and ("i" not in i):
            return None

    # анализ скобок, их количество, тот факт что направления скобок не совпадают
    temp_count_open = 0
    temp_count_close = 0
    for i in arg_input:
        if i == "(":
            temp_count_open += 1
        if i == ")":
            temp_count_close += 1
        if temp_count_close > temp_count_open:
            return None
    if temp_count_open != temp_count_close:
        return None 

    # вывод результата
    arg_input = [float(i) if i.replace(".","").replace("-","").isnumeric() else str(i) for i in arg_input]
    return arg_input

def formula_calculate(arg_input):
    global special_symbols
    start = None
    end = None
    out_result = 0.0
    
    i_number = 0
    for i in str(arg_input):
        if "i" in str(i):
            i_number = 1
            break

    if not i_number: # реальное число
        if len(arg_input) == 1:
            out_result = arg_input[0]
            return round(out_result, 5)

        for i in range(len(arg_input)):
            if arg_input[i] == "(":
                start = i + 1
            if arg_input[i] == ")" and not (start is None):
                end = i - 1
                break

        while start != end and not (start is None) and not (end is None):
            temp = formula_calculate(arg_input[start: end + 1])  
            for i in range(start - 1, end + 2):
                arg_input.pop(start - 1)
            arg_input.insert(start - 1, temp)

            start = None
            end = None
            for i in range(len(arg_input)):
                if arg_input[i] == "(":
                    start = i + 1
                if arg_input[i] == ")" and not (start is None):
                    end = i - 1
                    break

        range_high = len(arg_input)
        while ("*" in arg_input) or ("/" in arg_input):
            for i in range(1, range_high): 
                if arg_input[i] == "*":
                    arg_input[i - 1] = float(arg_input[i - 1])
                    arg_input[i + 1] = float(arg_input[i + 1]) 
                    out_result = arg_input[i - 1] * arg_input[i + 1]
                    arg_input[i] = out_result
                    arg_input.pop(i + 1)
                    arg_input.pop(i - 1)
                    range_high = len(arg_input)
                    break
                if arg_input[i] == "/":
                    arg_input[i - 1] = float(arg_input[i - 1])
                    arg_input[i + 1] = float(arg_input[i + 1]) 
                    if arg_input[i + 1] == 0:
                        return None
                    else:
                        out_result = arg_input[i - 1] / arg_input[i + 1]
                        arg_input[i] = out_result
                        arg_input.pop(i + 1)
                        arg_input.pop(i - 1)
                        range_high = len(arg_input)
                        break

        range_high = len(arg_input)
        while ("+" in arg_input) or ("-" in arg_input):
            for i in range(1, range_high): 
                if arg_input[i] == "+":
                    arg_input[i - 1] = float(arg_input[i - 1])
                    arg_input[i + 1] = float(arg_input[i + 1]) 
                    out_result = arg_input[i - 1] + arg_input[i + 1]
                    arg_input[i] = out_result
                    arg_input.pop(i + 1)
                    arg_input.pop(i - 1)
                    range_high = len(arg_input)
                    break
                if arg_input[i] == "-":
                    arg_input[i - 1] = float(arg_input[i - 1])
                    arg_input[i + 1] = float(arg_input[i + 1]) 
                    out_result = arg_input[i - 1] - arg_input[i + 1]
                    arg_input[i] = out_result
                    arg_input.pop(i + 1)
                    arg_input.pop(i - 1)
                    range_high = len(arg_input)
                    break

        return round(out_result, 5)
    else: # мнимое число
        if len(arg_input) == 1:
            out_result = arg_input[0]
            return out_result
     
        for i in range(len(arg_input)):
            if arg_input[i] == "(":
                start = i + 1
            if arg_input[i] == ")" and not (start is None):
                end = i - 1
                break

        while start != end and not (start is None) and not (end is None):
            temp = formula_calculate(arg_input[start: end + 1])  
            for i in range(start - 1, end + 2):
                arg_input.pop(start - 1)
            arg_input.insert(start - 1, temp)

            start = None
            end = None
            for i in range(len(arg_input)):
                if arg_input[i] == "(":
                    start = i + 1
                if arg_input[i] == ")" and not (start is None):
                    end = i - 1
                    break
        
        range_high = len(arg_input)
        while ("*" in arg_input) or ("/" in arg_input):
            for i in range(1, range_high): 
                if arg_input[i] == "*":
                    i_count = 0
                    if ("i" in str(arg_input[i - 1])) and ("i" in str(arg_input[i + 1])):
                        i_count += str(arg_input[i - 1]).count("i")
                        i_count += str(arg_input[i + 1]).count("i")
                        arg_input[i - 1] = float(str(arg_input[i - 1]).replace("i",""))
                        arg_input[i + 1] = float(str(arg_input[i + 1]).replace("i",""))
                        out_result =f"{str(arg_input[i - 1] * arg_input[i + 1])} {'i' * i_count}"
                    elif ("i" in str(arg_input[i - 1])) and not ("i" in str(arg_input[i + 1])):
                        # arg_input[i - 1] = str(arg_input[i - 1])
                        
                        # # умножается лишь верхняя часть
                        # sep_arg_input = arg_input[i - 1][0: (str(arg_input[i - 1]).find("/") if str(arg_input[i - 1]).find("/") != -1 else len(arg_input[i - 1]))]
                        # print(sep_arg_input)
                        i_count += str(arg_input[i - 1]).count("i")
                        i_count += str(arg_input[i + 1]).count("i")

                        arg_input[i - 1] = float(str(arg_input[i - 1]).replace("i",""))
                        arg_input[i + 1] = float(str(arg_input[i + 1]).replace("i",""))
                        out_result =f"{str(arg_input[i - 1] * arg_input[i + 1])} {'i' * i_count}"
                    else:
                        arg_input[i - 1] = float(str(arg_input[i - 1]).replace("i",""))
                        arg_input[i + 1] = float(str(arg_input[i + 1]).replace("i",""))
                        out_result = arg_input[i - 1] * arg_input[i + 1]
                    arg_input[i] = out_result
                    arg_input.pop(i + 1)
                    arg_input.pop(i - 1)
                    range_high = len(arg_input)
                    break
                if arg_input[i] == "/":
                    i_count = 0
                    if arg_input[i + 1] == "0" or arg_input[i + 1] == "0i":
                        return None
                    else:
                        if ("i" in str(arg_input[i - 1])) and ("i" in str(arg_input[i + 1])):
                            i_count += str(arg_input[i - 1]).count("i")
                            i_count -= str(arg_input[i + 1]).count("i")
                            arg_input[i - 1] = float(str(arg_input[i - 1]).replace("i",""))
                            arg_input[i + 1] = float(str(arg_input[i + 1]).replace("i",""))
                            out_result = f"{str(arg_input[i - 1] / arg_input[i + 1])} {'i' * i_count}"
                        elif ("i" in str(arg_input[i - 1])) and not ("i" in str(arg_input[i + 1])):
                            i_count += str(arg_input[i - 1]).count("i")
                            i_count -= str(arg_input[i + 1]).count("i")
                            arg_input[i - 1] = float(str(arg_input[i - 1]).replace("i",""))
                            arg_input[i + 1] = float(str(arg_input[i + 1]).replace("i",""))
                            out_result = f"{str(arg_input[i - 1] / arg_input[i + 1])} {'i' * i_count}"
                        elif not ("i" in str(arg_input[i - 1])) and ("i" in str(arg_input[i + 1])):
                            out_result = f"{str(arg_input[i - 1])} / {arg_input[i + 1]}"
                        else:
                            out_result = arg_input[i - 1] / arg_input[i + 1]
                        arg_input[i] = out_result
                        arg_input.pop(i + 1)
                        arg_input.pop(i - 1)
                        range_high = len(arg_input)
                        break

        range_high = len(arg_input)
        while ("+" in arg_input) or ("-" in arg_input):
            for i in range(1, range_high): 
                if arg_input[i] == "+":
                    i_count_1 = str(arg_input[i - 1]).count("i") 
                    i_count_2 = str(arg_input[i + 1]).count("i")
                    
                    arg_input[i - 1] = float(str(arg_input[i - 1]).replace("i",""))
                    arg_input[i + 1] = float(str(arg_input[i + 1]).replace("i",""))

                    if (i_count_1 == i_count_2) and (i_count_1 !=0):
                        out_result = f"{str(arg_input[i - 1] + arg_input[i + 1])} {'i' * i_count_1}"
                    elif  (i_count_1 != i_count_2):
                        out_result = f"{str(arg_input[i - 1])}{'i' * i_count_1} + {str(arg_input[i + 1])} {'i' * i_count_2}"
                    else:
                        out_result = arg_input[i - 1] + arg_input[i + 1]

                    arg_input[i] = out_result
                    arg_input.pop(i + 1)
                    arg_input.pop(i - 1)
                    range_high = len(arg_input)
                    break
                if arg_input[i] == "-":
                    i_count_1 = str(arg_input[i - 1]).count("i") 
                    i_count_2 = str(arg_input[i + 1]).count("i")

                    arg_input[i - 1] = float(str(arg_input[i - 1]).replace("i",""))
                    arg_input[i + 1] = float(str(arg_input[i + 1]).replace("i",""))

                    if (i_count_1 == i_count_2) and (i_count_1 !=0):
                        out_result = f"{str(arg_input[i - 1] + arg_input[i + 1])} {'i' * i_count_1}"
                    elif  (i_count_1 != i_count_2):
                        out_result = f"{str(arg_input[i - 1])}{'i' * i_count_1} - {str(arg_input[i + 1])} {'i' * i_count_2}"
                    else:
                        out_result = arg_input[i - 1] - arg_input[i + 1]

                    arg_input[i] = out_result
                    arg_input.pop(i + 1)
                    arg_input.pop(i - 1)
                    range_high = len(arg_input)
                    break
        return out_result

tes = "(4i+5/7i) * 3"
tes = string_to_formula(tes)
print(tes)
print(formula_calculate(tes))