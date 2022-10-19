from datetime import datetime as dt

default_filename = "C:\\Python\\Diagram_n_code\\python_practice\\3_homework8\\log.txt"


def logger(filename=default_filename, text="Действие", value=None):
    if value is None:
        value = ""
    time = dt.now().strftime("%H:%M")
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{time}; {text}; {value}; \n")
