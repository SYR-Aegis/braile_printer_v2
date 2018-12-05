import RPi.GPIO as GPIO
from motor import *

GPIO.setmode(GPIO.BCM)

m = Motor()
m.speed = 1500
m.Set_Input(6,13,19,26)

while True:
    m.Counter_Clockwise()
