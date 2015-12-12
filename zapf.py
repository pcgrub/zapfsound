#!/usr/bin/python
# -*- coding: utf-8 -*-
""" """
import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
import subprocess


def setting_pins_up(pins):
    # Init(GPIO and audio):
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # killswitch pin 24
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # special pin 10
    GPIO.setup(0, GPIO.OUT)  # pin for green LED
    GPIO.setup(1, GPIO.OUT)  # pin for yellow LED
    GPIO.output(0, 0)
    GPIO.output(1, 1)

def reading_in(pins):
    # reading in the sound file names from config and creating the sounds:
    soundfile = open('sounds.txt', 'r')
    adresses = soundfile.read().splitlines()
    soundlist = []
    for i in range(len(adresses)-1):
        if adresses[i][0] != '#':
            print str(adresses[i])
            temp = pygame.mixer.Sound(str(adresses[i]))
            if (temp.get_length() >= 5 or temp.get_length() <= 0.1):
                temp = pygame.mixer.Sound("WilhelmScream.wav")
            soundlist.append(temp)
    if len(soundlist) < 10:
        for i in range(len(soundlist),len(pins)):
            soundlist.append(pygame.mixer.Sound("WilhelmScream.wav"))
    return soundlist


def main():
    # switch detection and playing sounds:
    pygame.mixer.init(48000, -16, 1, 1024)
    Channel0 = pygame.mixer.Channel(0)
    pins=[11, 9, 4, 14, 15, 18, 17, 27, 22, 23]
    setting_pins_up(pins)
    soundlist = reading_in(pins)
    print "fertig"
    GPIO.output(0,1) #switching on green LED when ready
    while True:
        try:
            for i in range(len(pins)):
                if GPIO.input(pins[i]): #testing soundpins
                    Channel0.play(soundlist[i])
                    sleep(soundlist[i].get_length())
                if GPIO.input(10):
                    try:
                        subprocess.call(['git pull'])
                        reading_in(pins)
                    except:
                        pass
                if GPIO.input(24):  #testing killswitch pin 24
                    raise KeyboardInterrupt
        except KeyboardInterrupt:
            GPIO.cleanup()
            #GPIO.setup(1, GPIO.OUT) #pin for yellow LED
            #GPIO.output(1,1)


if __name__=="__main__":
    main()
