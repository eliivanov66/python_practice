import data_provider as prov
import logger as log

def view_temperature(sensor):
    data = prov.data_temperature(sensor)
    log.logger_temperature(data)
    return data

def view_pressure(sensor):
    data = prov.data_pressure(sensor)
    log.logger_pressure(data)
    return data

def view_wind_speed(sensor):
    data = prov.data_wind_speed(sensor)
    log.logger_wind_speed(data)
    return data

def view_collection(sensor):
    data = prov.data_collector(sensor)
    log.logger_collection(data)
    return data