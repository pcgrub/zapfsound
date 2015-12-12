#!/usr/bin/python
# -*- coding: utf-8 -*-
""" """
from time import sleep
import RPi.GPIO as GPIO

def setting_pins_up(pins):
    # Init(GPIO and audio):
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pins=[11,9,4,14,15,18,17,27,22,23,24,10]
#pins = [9, 11, 4, 14, 15, 18, 17, 27, 22, 23, 24, 10] #pins for for soundboard buttons
setting_pins_up(pins)
while True:
    try:
        for i in range(len(pins)):
                if GPIO.input(pins[i]): #testing soundpins
                    print i+1
                    sleep(0.3)
    except KeyboardInterrupt:
        GPIO.cleanup()
	break

