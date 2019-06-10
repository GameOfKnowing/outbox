# OutBox
### by Laura Lytle
#### 🚫Timelines, Hate Speech, Ads, Jack🚫
#### ✅Baltic Birch, Webhooks, LEDs, Some Semblance of Control✅

## Concept
OutBox is a physical scanner for Twitter users who hate Twitter. With the push of a button, Outbox allows users to capture and tweet a photo of their latest project, handwritten note, or radiant smile.

Contributing content and eyeballs to social media platforms is a necessary evil of modern life. OutBox responds to this reality by allowing users to give as little of themselves as they want to at any given time, without getting totally sucked in. 

In contrast to Twitter's official website and apps, which are designed for addiction and rage, **OutBox adheres to a principle I will call "Design for Disuse (D4D)."** D4D is the idea that harmful technologies (ex social media) should protect users by *discouraging* interaction. As such, posting a photo with OutBox is inconvenient-- users must power on the device, manually arrange their subject under the camera without a viewfinder, and press a button to capture an image. There is absolutely no feedback to the user or forced content consumption.

## System Overview & Operation
OutBox is composed of a 5V power supply, a Raspberry Pi 3 A+, a Logitech Quick Cam webcam, a toggle "arming" button, a momentary "shutter" button, and LEDs in a custom, laser-cut enclosure. During normal operation, the device captures a low-res photo of its interior area, compresses it into a PNG, uploads it to a remote fileserver using SCP, and then triggers a pre-configured IFTTT webhook to post the image as a tweet. While all images are stored locally with unique filenames, OutBox will send them to the same location on the fileserver every time, overwriting the previous image.

To take a photo, the user must place their subject inside the OutBox scanner, depress the small, metal "arming" button, and then press the large, red "shutter" button. After releasing the shutter button, the user should wait for 10 seconds before removing their subject or the OutBox scanner.

## Hardware Setup
For an overview of the build process, check out my project video at [Link coming soon]

A 3D model of the enclosure and ready-to-cut illustrator files can be found [here on Thingiverse.](https://www.thingiverse.com/thing:3682624)

## Software Setup (see note below)
To start OutBox, run "OutBox.py" or use systemd to run it automatically when your computer starts up. If you have multiple camera peripherals or any camera connection issues, you may need to modify the variable "camPort" (line 19) the the appropriate port address for the camera you would like to use. 

To upload photos to your fileserver and post them using your IFTTT webhook, you will need to provide login and path information in a file called "secr.et" located in the same directory as "OutBox.py" . "secr.et" should be formatted as follows:

```
{YOUR_FILESERVER_IP}
{YOUR_FILESERVER_USERNAME}
{YOUR_FILESERVER_PASSWORD}
{YOUR_FILESERVER_IMAGE_DESTINATION_PATH}
{YOUR_IFTTT_WEBHOOK_URL}
{YOUR_IMAGE_URL_ON_FILESERVER}
```

An example "secr.et" might look like:

```
123.123.6.3
suniverse
beachcity
/home/suniverse/images/smokyQuartz.png
maker.ifttt.com/trigger/fusionPics/dklfajksdlfj
rosequartz.io/blog/smokyQuartz.png
```

#### Note: OutBox is designed as an art piece and a tool for personal use. As such, it is not secure and should not be used to transmit sensitive information or connect to important servers. As a general rule, you should not store IP addresses or login credientials in plain text. Most importantly, please take the time to understand your personal threat model, and be smart about using this and any other code you find online.
 
