from datetime import datetime as dt

def logger(filename, text, value):
    if value is None:
        value = ""
    time = dt.now().strftime("%H:%M")
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{time}; {text}; {value}; \n")
