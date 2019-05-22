#Assorted Functions for the Outbox project
#by Laura Lytle
#Email: laura_lytle@aol.com
#Website: laura.dev
#May 21, 2019

import os
import paramiko
import urllib.request

#arms the device
def armCam ():
    global isArmed
    isArmed = True;
    print("Armed")

#disarms the device
def disarmCam ():
    global isArmed
    isArmed = False;
    print("Disarmed")

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
    print(imgFormat)
    if (isArmed):
        print("shutter pressed")
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
        picList = os.listdir("./images")
        #waits for new image file to be created
        while (numPics != len(picList)):
            picList = os.listdir("./images")
            time.sleep(1)
        print("going to press")    
        posterBoi(imgName)

#Tweets image via iftt
#Note: This isn't very secure
def posterBoi (fName):
    
    #brings in global variables
    global imgFormat
    
    if (200 == urllib.request.urlopen("http://www.twitter.com").getcode()): #checks if Twitter is up
        #reads server info from external file
        with open(secr.et, 'r') as input:
            server = input[0]
            user = input[1]
            password = input[2]
            fPath = input[3] + "image." + imgFormat
            wHook = input[4]
            fURL = input[5] + "image." + imgFormat

        #creates ssh/scp clients for server 
        sshCon = makeSSHClient(server, user, password)
        scpCon = SCPClient(sshCon.get_transport())
        #scp's image to server
        scp.put(fName, fPath)
        
        #send tweet with webhook
        r = requests.post("https://maker.ifttt.com/trigger/outbox/with/key/c2EyNgpusRaaVUzjI3aQEy", data={'value1': fURL})


#creates an SSH client        
def makeSSHClient(server, user, password):
        client = paramiko.SSHClient()
        client.connect(server, 22, user, password)
        return client
