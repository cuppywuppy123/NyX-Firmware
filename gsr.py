import Adafruit_BBIO.ADC as ADC
import time
from display import display
ADC.setup()
def read_gsr_data():
    return int(ADC.read("P9_39")*1000)
if __name__=="__main__":
    while(True):
        if(read_gsr_data()>=threshold):
            display('Exhausted?',2)
