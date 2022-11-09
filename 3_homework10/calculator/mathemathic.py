import logger

special_symbols = ["*", "/", "+", "-", "(", ")", "j"]

def string_to_formula(arg_input):
    global special_symbols
    arg_input = str(arg_input)
    
    # разделяем значимые данные пробелом
    arg_input = arg_input.replace(" ", "")
    arg_input = arg_input.replace(",", ".")
    arg_input = arg_input.replace("i", "j")
    arg_input = arg_input.replace("*j", "j")
    
    while ("--" in arg_input):
        arg_input = arg_input.replace("--", "+")

    while ("-+" in arg_input):
        arg_input = arg_input.replace("-+", "-")
    
    for i in special_symbols:
        while i*2 in arg_input and (i != "j"):
            arg_input = arg_input.replace(i*2, i)

    for i in special_symbols:
        if i != "j":
            arg_input = arg_input.replace(i, f" {i} ")
    
    if arg_input[0:2] == " +" or arg_input[0:2] == " *" or arg_input[0:2] == " /":
        arg_input = f"1.0 *{arg_input[2:len(arg_input)]}"
    if arg_input[0:2] == " -":
        arg_input = f"-1.0 *{arg_input[2:len(arg_input)]}"

    arg_input = arg_input.split()

    for i in range(1, len(arg_input)):
        if arg_input[i] == "(" and (arg_input[i - 1].replace(".","").replace("-","").isnumeric() or "j" in arg_input[i - 1]):
            arg_input.insert(i, "*")
    for i in range(1, len(arg_input)):
        if arg_input[i - 1] == ")" and (arg_input[i].replace(".","").replace("-","").isnumeric() or "j" in arg_input[i]):
            arg_input.insert(i, "*")

    if arg_input[0] == "(" and arg_input[-1] == ")":
        arg_input.pop(0)
        arg_input.pop(-1)

    for i in arg_input:
        if not i.replace(".","").replace("-","").isnumeric() and (i not in special_symbols) and ("j" not in i):
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

def split_string_to_complex(arg_input):
    
    out_real = 0.0
    out_image = 0.0

    if type(arg_input) is complex:
        return arg_input
    else:
        if not ("j" in str(arg_input)):
            out_real = float(arg_input)
            out_image = 0.0      
        else:
            temp_var = str(arg_input)
            
            if  temp_var == "j":
                out_real = 0
                out_image = 1
            else:
                temp_var = temp_var.split("j")
                if temp_var[1] == "":
                    temp_var[1] = 0
                    out_real = float(temp_var[1])
                    out_image = float(temp_var[0])

                if temp_var[0] == "":
                    temp_var[0] = 0
                    out_real = float(temp_var[0])
                    out_image = float(temp_var[1])
        return complex(out_real, out_image)

def formula_calculate(arg_input):
    print(arg_input)
    global special_symbols
    start = None
    end = None
    out_result = 0.0
    
    i_number = 0
    for i in str(arg_input):
        if "j" in str(i):
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
                    arg_input[i - 1] = split_string_to_complex(arg_input[i - 1])
                    arg_input[i + 1] = split_string_to_complex(arg_input[i + 1])
                    out_result = arg_input[i - 1] * arg_input[i + 1]
                    arg_input[i] = out_result
                    arg_input.pop(i + 1)
                    arg_input.pop(i - 1)
                    range_high = len(arg_input)
                    break
                if arg_input[i] == "/":
                    if str(arg_input[i + 1]) == "0.0" or str(arg_input[i + 1]) == "0.0j":
                        return None
                    else:
                        arg_input[i - 1] = split_string_to_complex(arg_input[i - 1])
                        arg_input[i + 1] = split_string_to_complex(arg_input[i + 1])
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
                    arg_input[i - 1] = split_string_to_complex(arg_input[i - 1])
                    arg_input[i + 1] = split_string_to_complex(arg_input[i + 1])
                    out_result = arg_input[i - 1] + arg_input[i + 1]
                    arg_input[i] = out_result
                    arg_input.pop(i + 1)
                    arg_input.pop(i - 1)
                    range_high = len(arg_input)
                    break
                if arg_input[i] == "-":
                    arg_input[i - 1] = split_string_to_complex(arg_input[i - 1])
                    arg_input[i + 1] = split_string_to_complex(arg_input[i + 1])
                    out_result = arg_input[i - 1] - arg_input[i + 1]
                    arg_input[i] = out_result
                    arg_input.pop(i + 1)
                    arg_input.pop(i - 1)
                    range_high = len(arg_input)
                    break
        return out_result