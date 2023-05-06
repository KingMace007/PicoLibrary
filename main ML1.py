from Lights import Light
from Buzzer import *
from Displays import *

import time

print("Hello, Pi Pico!")

led = Light(25, "Onboard LED")

led.on()
time.sleep(0.5)
led.off()
time.sleep(0.5)

blueled = Light(0, "Blue Light")

blueled.on()
time.sleep(0.5)
blueled.off()
time.sleep(0.5)

buzz = PassiveBuzzer(13)
buzz.play()
time.sleep(1)
buzz.stop()

display = LCDDisplay(sda=20, scl = 21, i2cid = 0)
display.showText("Life is Good")
