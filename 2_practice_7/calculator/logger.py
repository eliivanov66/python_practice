
from datetime import datetime as dt

def logger(text="Действие", value = None, file_name = "log.csv"):
    if value is None:
        value = ""
    time = dt.now().strftime("%H:%M")
    with open(file_name, "a") as file:
        file.write(f"{time}; {text}; {value}; \n")