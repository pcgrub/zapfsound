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
    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # killswitch pin 8
    GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # special pin 7
    GPIO.setup(0, GPIO.OUT)  # pin for green LED
    GPIO.setup(1, GPIO.OUT)  # pin for yellow LED
    GPIO.output(0, 0)
    GPIO.output(1, 1)

pins = [18, 17, 21, 22, 23, 24, 10, 9, 11, 25, 8, 7] #pins for for soundboard buttons
setting_pins_up(pins)
while True:
    try:
        for i in range(len(pins)):
                if GPIO.input(pins[i]): #testing soundpins
                    print i
                    sleep(0.3)
    except KeyboardInterrupt:
        GPIO.cleanup()