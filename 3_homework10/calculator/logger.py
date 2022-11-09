from datetime import datetime as dt

def logger(filename, text, value):
    if value is None:
        value = ""
    time = dt.now()
    time = f"{time.year}/{time.month}/{time.day} {time.hour}:{time.minute}:{time.second}"
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{time}; {text}; {value}; \n")