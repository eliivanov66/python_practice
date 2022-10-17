#data = a + b
#data = (ar, ai) + (br, bi)

def checker(data):
    operations = ["+", "-", "/", "*"]
    data = data.split() #out = list
    if len(data) == 1 and str(data[0]).replace(".", "", 1).isnumeric():
        return 1, float(data[0]), 0.0
    
    elif len(data) == 2 and str(data[0]).replace(".", "", 1).isnumeric() and str(data[1]).replace(".", "", 1).isnumeric():
        return 2, float(data[0]), float(data[1])
    
    elif len(data) == 1 and (data[0] in operations):
        return 3, 0.0, 0.0
    else:
        return -1, 0.0, 0.0
