#HELLO THIS IS PYTHON

import subprocess
import time
import string
from gpiozero import Button
from signal import pause

button = Button(17) # double check which gpio attached to

def pressed():
        response = True

response = False

recording = False

button.pressed = pressed

while(True):
        while(not recording):
                # response = str(input("Do you want to take a picture?"))
                # if response == '1' or response.lower() == 'true' or response.lower() == 'yes' or response.lower() == 'y':
                if response:
                        recording = True
                else: recording == False

        while(recording):
                currtime = time.time_ns()
                outputfile = str(currtime)
                outputfile += '.jpg'
                result = subprocess.run(['rpicam-still', '-t', '10', '-o', outputfile], text=True)
                recording = False
