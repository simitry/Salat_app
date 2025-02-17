from connect import create_table as ct
from salat_api import *
from datetime import datetime

def compare():
    # ct("" , "test", "test3")
    salat_name = ["Fajr","Sunrise","Dhuhr","Asr","Maghrib","Isha"]

    print(response)
    print(timing)

    for elem in salat_name:
        if timing[elem] == datetime.now().strftime("%H:%M"): #strftime to customize output
            print(f'time for {elem}')
        else:
            print('no')

    print(datetime.today())
    
    
# compare()
ct("" , "test", "test4")