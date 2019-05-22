#Outbox for Raspberry Pi
#by Laura Lytle
#Email: laura_lytle@aol.com
#Website: laura.dev
#Captures images with a USB webcam and posts them to twitter
#via IFTT. Controlled by button input.
#May 20, 2019
from gpiozero import LED, Button
import time
import urllib.request

#image capture parameters
imgFormat = "png" #format for caputured images
imgComp = "6" #image compression factor (0-9)
camPort = "/etc/video0" #camera port

#misc variable initialization
piclist = []
imgName = ""
isArmed = False
numPics = 0

#initializes GPIO
shutLED = LED(pin="GPIO19") #LED in shutter button
armLED = LED(pin="GPIO16") #LED in arm button
arm = Button(pin = "GPIO26", bounce_time = 0.25)#arm button
shutter = Button(pin = "GPIO20", bounce_time = 0.25) #shutter button

arm.when_pressed = armCam
arm.when_released = disarmCam
shutter.when_pressed = shutPress

while(True)
    loop = "Keep rockin'"
