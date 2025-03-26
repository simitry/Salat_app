# from connect import create_table as ct
from salat_api import *
from datetime import datetime
import signal
from time import sleep
from plyer import notification

class SignalHandler:
    shutdown_requested =False
    
    def __init__(self):
        signal.signal(signal.SIGINT, self.request_shutdown)
        signal.signal(signal.SIGTERM , self.request_shutdown)
    
    def request_shutdown(self, *args):
        print("Request to shutdown, ........... stopping")
        self.shutdown_requested = True
        
    def can_run(self):
        return not self.shutdown_requested
    
    
def compare():
    salat_name = ["Fajr","Sunrise","Dhuhr","Asr","Maghrib","Isha"]

    # print(response)
    # print(timing)

    for elem in salat_name:
        if timing[elem] == datetime.now().strftime("%H:%M"): #strftime to customize output
        # if timing[elem] == "12:44" :
            notification.notify(
                title='Salat-App',
                message=f'time for {elem}',
                app_name ='Salat-App',
                # app_icon = 'icon.ico',
                timeout=10
            )
            sleep (60)
            
 
signal_handler = SignalHandler()    

print("Program running. Press Ctrl+C to stop.")

while signal_handler.can_run():  
    compare()
    sleep(2)
    
print("Program has stopped.")
