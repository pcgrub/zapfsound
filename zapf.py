#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit
from numpy import loadtxt

"""Init(GPIO and audio):"""
pins=[25,24,23,18,15,14,4,17,27,22] #pins for for soundboard buttons
GPIO.setmode(GPIO.BCM)
for d in range(len(pins)):
    GPIO.setup(pins[d], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setuo(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #killswitch pin 8
GPIO.setup(17, GPIO.OUT) #pin for green LED
GPIO.output(17,0)					
pygame.mixer.init(48000, -16, 1, 1024)
Channel0 = pygame.mixer.Channel(0)


"""reading in the sound file names from config and creating the sounds:"""
soundfile = open('sounds.txt', 'r')	
adresses = soundfile.read().splitlines()
soundlist = []				
for i in range(0, len(adresses)-1):
	if adresses[i][0] != '#':
		print str(adresses[i])
		temp = pygame.mixer.Sound(str(adresses[i]))
		if temp.get_length() >= 5:
			temp = pygame.mixer.Sound("WilhelmScream.wav")
		soundlist.append(temp)


"""switch detection and playing sounds:"""
print "fertig"
GPIO.output(17,1) #switching on green LED when ready
while True:
	try:
        for i in range(len(pins)):
            if GPIO.input(pins[i]): #testing soundpins
            print i
            Channel0.play(soundlist[i])
            sleep(soundlist[i].get_length())
        if GPIO.inpit(8):  #testing killswitch pin 8
            raise KeyboardInterrupt
	except KeyboardInterrupt:
		GPIO.cleanup()
