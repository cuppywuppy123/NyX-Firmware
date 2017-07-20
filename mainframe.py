import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import Adafruit_SSD1306
import subprocess as subprocess
#from PIL import image
from pymongo import MongoClient
from security import check
from display import display
#from servo import rotate
from gsr import read_gsr_data
if __name__=="__main__":
    response=check()
    while(response=='Pin not recognised'):
        response=check()
        display(response,4)
    display(response,4)
    #display('Welcome to CAR-e',4)
