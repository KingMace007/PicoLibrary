from Displays import * 
from Button import *
from Buzzer import *
import time
""" This is a counter class that willl implement basic
increment reset and show count on a display """

class Counter:
    def __init__(self):
        print("Counter: Contstructor")
        self._number = 0
        self._display = LCDDisplay(sda = 20, scl = 21, i2cid = 0)
        self._greenButton = Button(17, "increase", buttonhandler = self, lowActive=True)
        self._redButton = Button(16, "reset", buttonhandler = self, lowActive=True) 
        self._buzzer = PassiveBuzzer(13)    

    def increment(self):
        print("Counter: Increment")
        self._number = self._number + 1
        self._buzzer.beep()

    
    def reset(self):
        print("Counter: reset")
        self._number = 0
        self._display.reset()

    def buttonPressed(self,name):
        if name == "increase":
            self.increment()
        elif name == "reset":
            self.reset()

    def buttonReleased(self,name):
        pass

    def show(self):
        while True:
            self._display.showNumber(self._number)
            time.sleep(0.1)

    



    