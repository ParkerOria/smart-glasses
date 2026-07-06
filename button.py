from gpiozero import Button
from signal import pause

button = Button(10)

def when_pressed():
    print("pressed")

button.when_pressed = when_pressed
