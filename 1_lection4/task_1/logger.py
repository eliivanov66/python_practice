from datetime import datetime as dt

def logger_temperature(data):
    time = dt.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write("{};temperature;{}\n".format(time, data))

def logger_pressure(data):
    time = dt.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write("{};pressure;{}\n".format(time, data))

def logger_wind_speed(data):
    time = dt.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write("{};wind_speed;{}\n".format(time, data))

def logger_collection(data):
    t, p, w = data
    time = dt.now().strftime("%H:%M")
    with open("log_collection.csv", "a") as file:
        file.write("{};temperatue;{};pressure;{};wind_speed;{}\n".format(time, t, p, w))