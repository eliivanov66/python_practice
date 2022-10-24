import logger

special_symbols = ["*", "/", "+", "-", "(", ")"]

def string_to_formula(arg_input):
    global special_symbols
    arg_input = str(arg_input)
    
    # разделяем значимые данные пробелом
    arg_input = arg_input.replace(",", ".")
    for i in special_symbols:
        arg_input = arg_input.replace(i, f" {i} ")
    
    while "  " in arg_input:
        arg_input = arg_input.replace("  ", " ")

    arg_input = arg_input.split()

    for i in arg_input:
        if not i.replace(".","").isnumeric() and (i not in special_symbols):
            return -1

    # анализ скобок, их количество, тот факт что направления скобок не совпадают
    temp_count_open = 0
    temp_count_close = 0
    for i in arg_input:
        if i == "(":
            temp_count_open += 1
        if i == ")":
            temp_count_close += 1
        if temp_count_close > temp_count_open:
            return -1
    if temp_count_open != temp_count_close:
        return -1

    # вывод результата
    arg_input = [float(i) if i not in special_symbols else str(i) for i in arg_input]
    return arg_input

def formula_calculate(arg_input):
    global special_symbols
    start = None
    end = None
    out_result = 0.0
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
    
    print(arg_input)
    range_high = len(arg_input)
    while ("*" in arg_input) or ("/" in arg_input):
        for i in range(1, range_high): 
            if arg_input[i] == "*":
                out_result = arg_input[i - 1] * arg_input[i + 1]
                arg_input[i] = out_result
                arg_input.pop(i + 1)
                arg_input.pop(i - 1)
                range_high = len(arg_input)
                break
            if arg_input[i] == "/":
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
                out_result = arg_input[i - 1] + arg_input[i + 1]
                arg_input[i] = out_result
                arg_input.pop(i + 1)
                arg_input.pop(i - 1)
                range_high = len(arg_input)
                break
            if arg_input[i] == "-":
                out_result = arg_input[i - 1] - arg_input[i + 1]
                arg_input[i] = out_result
                arg_input.pop(i + 1)
                arg_input.pop(i - 1)
                range_high = len(arg_input)
                break
    return round(out_result, 5)
