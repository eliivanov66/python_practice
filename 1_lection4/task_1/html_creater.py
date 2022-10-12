from user_interface import view_temperature
from user_interface import view_pressure
from user_interface import view_wind_speed

def html_create(device = 1):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, view_temperature(device))
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, view_pressure(device))
    html += '   <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, view_pressure(device))
    html += '   </body>\n</html>'

    with open("index.html", "w") as page:
        page.write(html)
    
    return html

def html_collection_create(data, device = 1):
    t, p, w = data
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, t)
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, p)
    html += '   <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, w)
    html += '   </body>\n</html>'

    with open("index_collection.html", "w") as page:
        page.write(html)
    
    return data