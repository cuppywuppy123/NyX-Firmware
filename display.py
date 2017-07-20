import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Image
import ImageDraw
import ImageFont
import Adafruit_BBIO.GPIO as GPIO
import subprocess as sp 
#Beaglebone Black Pin Configuration
RST='P9_12'
#For SPI OLED Devices
DC='P9_15'
SPI_PORT=1
SPI_DEVICE=0
#########Setup for OLED##########################
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST,dc=DC,sclk='P9_22',din='P9_18',cs='P9_17')
disp.begin()
disp.clear()
disp.display()
width=128
height=64
image=Image.new('1',(width,height))
draw=ImageDraw.Draw(image)
padding=0
shape_width=200
top=0
bottom=height
font=ImageFont.load_default()
def display(str,delay):
    	draw.text((0,10),str,font=font,fill=255)
	disp.image(image)
	disp.display()
	time.sleep(delay)
	disp.clear()
	disp.display()
