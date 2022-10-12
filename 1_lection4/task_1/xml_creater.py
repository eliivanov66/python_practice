from user_interface import view_temperature
from user_interface import view_pressure
from user_interface import view_wind_speed

def xml_create(device = 1):
    xml = '<xml>\n'
    xml += '   <temperature units = "c">{}</temperature>\n'\
        .format(view_temperature(device))
    xml += '   <pressure units = "mmHg">{}</pressure>\n'\
        .format(view_pressure(device))
    xml += '   <wind_speed units = "m/s">{}</wind_speed>\n'\
        .format(view_wind_speed(device))
    xml += '   </xml>'

    with open("index.xml", "w") as page:
        page.write(xml)
    
    return xml

def xml_collection_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32 #Фаренгейты
    xml = '<xml>\n'
    xml += '   <temperature units = "f">{}</temperature>\n'\
        .format(t)
    xml += '   <pressure units = "mmHg">{}</pressure>\n'\
        .format(p)
    xml += '   <wind_speed units = "m/s">{}</wind_speed>\n'\
        .format(w)
    xml += '   </xml>'

    with open("index_collection.xml", "w") as page:
        page.write(xml)
    
    return data