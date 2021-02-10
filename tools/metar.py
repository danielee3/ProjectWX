import csv, requests, datetime
from bs4 import BeautifulSoup


'''
This app helps generating a csv file of METAR data from Iowa State University's Iowa Environmental Mesonet website (https://mesonet.agron.iastate.edu/).
'''

def mk_station(station_list):
    stations = ""
    for st in station_list:
        stations = stations+"station="+st+"&"
    return stations

def mk_start_date(date):
    return "year1="+date.strftime("%Y")+"&" + "month1="+date.strftime("%m")+"&" + "day1="+date.strftime("%d")+"&"

#The end date is exclusive
def mk_end_date(date):
    return "year2="+date.strftime("%Y")+"&" + "month2="+date.strftime("%m")+"&" + "day2="+date.strftime("%d")+"&"

def mk_metar_types(metar_type):
    if metar_type==1:
        return "report_type=1"
    elif metar_type==2:
        return "report_type=2"
    else:
        return "report_type=1&report_type=2"

def mk_link(station_list, start_date, end_date, metar_type):
    base = "https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?"
    data_all = "data=all&"
    default_settings = "tz=Etc%2FUTC&format=onlycomma&latlon=yes&elev=no&missing=M&trace=0.0001&direct=no&"
    return base+mk_station(station_list)+data_all+mk_start_date(start_date)+mk_end_date(end_date)+default_settings+mk_metar_types(metar_type)

stations = ["ITH"]
start_date = datetime.datetime(2021, 1, 1)
end_date = datetime.datetime(2021, 2, 1)
link = mk_link(["ITH"], start_date, end_date, 2)

mpw_stations = ["ITH"]
mpw_date = datetime.datetime.now()
metar_past_week = mk_link(mpw_stations, mpw_date-datetime.timedelta(days=7), mpw_date, 2)

print(link)
print(metar_past_week)
