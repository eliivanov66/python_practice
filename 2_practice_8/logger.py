from datetime import datetime as dt

default_filename = "c:\\Users\\nikkl\\OneDrive\\Рабочий стол\\GeekBrains\\Python\\Семинары\\L8\\log.txt"


def logger(filename=default_filename, text="Действие", value=None):
    if value is None:
        value = ""
    time = dt.now().strftime("%H:%M")
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{time}; {text}; {value}; \n")
