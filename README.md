# OutBox
### by Laura Lytle
#### 🚫Timelines, Hate Speech, Ads, Jack🚫
#### ✅Baltic Birch, Webhooks, LEDs, Crispy PNG✅

## Concept
OutBox is a physical scanner for Twitter users who hate Twitter. With the push of a button, Outbox allows you to capture and tweet a photo of your latest project, handwritten note, or radiant selfie.

Contributing content and eyeballs to social media platforms is a necessary evil of modern life. Outbox responds to this reality by allowing users to give as little of themselves as they want to at any given time, without getting totally sucked in. 

In contrast to Twitter's official website and apps, which are designed for addiction and rage, **OutBox adheres to a principle I will call "Design for Disuse (D4D)."** D4D is the idea that harmful technologies (ex social media) should protect users by discouraging interaction. As such, posting a photo is inconvenient-- users must power on the device, manually arrange their subject under the camera without a viewfinder, and press a button to caputure an image. There is absolutely no feedback to the user or forced content consumption.

## System Overview & Operation
Outbox is composed of a 5V power supply, a Raspberry Pi 3 A+, a Logitech Quick Cam webcam, a toggle "arming" button, a momentary "shutter" button, and LEDs in a custom, laser-cut enclosure. During normal operation, the device captures a low-res photo of its interior area, compresses it into a PNG, uploads it to a remote fileserver using SCP, and then triggers a pre-configured IFTT webhook to post the image as a tweet. 

To take a photo, the user must place their subject inside the OutBox scanner, depress the small, metal "arming" button, and then press the large, red "shutter" button. After releaseing the shutter button, the user should wait for at least 10 seconds before removing their subject from the Outbox scanner.

## Software Setup

#### Note: Outbox is designed as an art piece and a tool for personal use. As such, it is not secure and should not be used to transmit sensitive information.
 
