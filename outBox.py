#Outbox for Raspberry Pi
#by Laura Lytle
#Email: laura_lytle@aol.com
#Website: laura.dev
#Captures images with a USB webcam and posts them to twitter
#via IFTT. Controlled by button input.
#May 20, 2019
from gpiozero import LED, Button
from time import sleep
import urllib.request
import requests
import time
import os
import paramiko
import scp

#image capture parameters
imgFormat = "png" #format for caputured images
imgComp = 6 #image compression factor (0-9)
camPort = "/dev/video0" #camera port

#misc variable initialization
piclist = []
imgName = ""
isArmed = False
numPics = 0

#arms the device
def armCam ():
    global isArmed
    isArmed = True
    print("Armed")
    shutLED.on()
    armLED.on()

#disarms the device
def disarmCam ():
    global isArmed
    isArmed = False
    print("Disarmed")
    shutLED.off()
    armLED.off()

#captures & posts image  on shutter press    
def shutPress ():
    
    #brings in global variables
    global isArmed
    global picList
    global numPics
    global camPort
    global imgFormat
    global imgComp
    global imgName
    print("Shutter pressed, may not be armed")
    if (isArmed):
        print("shutter pressed, armed")
        #gets image count if images dir exists, else creates it
        if (os.path.isdir("./images")):
            picList = os.listdir("./images")
            numPics = len(picList)
        else:
            os.system("mkdir ./images")
            numPics = 0
        imgName = "./images/cap" + str(numPics) + "." + imgFormat
        #captures & saves an image using paramters specified above    
        os.system("fswebcam --device %s --no-banner --%s %d --save %s" % (camPort, imgFormat, imgComp, imgName))
        print("going to press")    
        posterBoi(imgName)

#Tweets image via iftt
#Note: This isn't very secure
def posterBoi (fName):
    
    #brings in global variables
    global imgFormat
    
    if (200 == urllib.request.urlopen("http://www.twitter.com").getcode()): #checks if Twitter is up
        #reads server info from external file
        with open("secr.et", 'r') as input:
            fLines = []
            for line in input:
                fLines.append(line[:-1])
        print(fLines)
        server = fLines[0]
        user = fLines[1]
        password = fLines[2]
        fPath = fLines[3] + "image." + imgFormat
        wHook = fLines[4]
        fURL = fLines[5] + "image." + imgFormat

        #creates ssh/scp clients for server
        sshCon = paramiko.SSHClient()
        sshCon.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
        sshCon.connect(server, 22, user, password)
        scpCon = scp.SCPClient(sshCon.get_transport())
        #scp's image to server
        scpCon.put(fName, fPath)
       
        time.sleep(5)

        #send tweet with webhook
        r = requests.post("https://maker.ifttt.com/trigger/outbox/with/key/c2EyNgpusRaaVUzjI3aQEy")

#initializes GPIO
shutLED = LED(pin="GPIO19") #LED in shutter button
armLED = LED(pin="GPIO5") #LED in arm button
arm = Button(pin = "GPIO6", bounce_time = 0.25)#arm button
shutter = Button(pin = "GPIO26", bounce_time = 0.25) #shutter button

arm.when_pressed = disarmCam
arm.when_released = armCam
shutter.when_pressed = shutPress


#Main loop
#(not much here because all of the 
#image capture and upload is happening
#in interrupt-like events)
while(True):
    loop = "Keep rockin'"

