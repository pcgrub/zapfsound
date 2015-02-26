import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17,0)
pygame.mixer.init(48000, -16, 1, 1024)


Sound0 = pygame.mixer.Sound("applause.wav")
Sound1 = pygame.mixer.Sound("WilhelmScream.wav")
Sound2 = pygame.mixer.Sound("buzzer.wav")
Sound3 = pygame.mixer.Sound ("CastleThunder.wav")
Sound4 = pygame.mixer.Sound("clap.wav")
Sound5 = pygame.mixer.Sound("applause.wav")
Sound6 = pygame.mixer.Sound("applause.wav")
Sound7 = pygame.mixer.Sound("applause.wav")
Sound8 = pygame.mixer.Sound("applause.wav")
Sound9 = pygame.mixer.Sound("applause.wav")

Channel0 = pygame.mixer.Channel(0)
Channel1 = pygame.mixer.Channel(1)
Channel2 = pygame.mixer.Channel(2)
Channel3 = pygame.mixer.Channel(3)
Channel4 = pygame.mixer.Channel(4)
Channel5 = pygame.mixer.Channel(5)
Channel6 = pygame.mixer.Channel(6)
Channel7 = pygame.mixer.Channel(7)
#Channel8 = pygame.mixer.Channel(8)
#Channel9 = pygame.mixer.Channel(9)


print "fertig"
GPIO.output(17,1)
while True:
	try:
		if GPIO.input(25):
			print "0"
			Channel0.play(Sound0)
			sleep(Sound0.get_length())
		if GPIO.input(24):
			print "1"
			Channel0.play(Sound1)
			sleep(Sound1.get_length())
		if GPIO.input(23):
			print "2"
			Channel0.play(Sound2)
			sleep(Sound2.get_length())
		if GPIO.input(18):
			print "3"#
			Channel0.play(Sound3)
			sleep(Sound3.get_length())
		if GPIO.input(15):
			print "4"
			Channel0.play(Sound4)
			sleep(Sound4.get_length())
	except KeyboardInterrupt:
		GPIO.cleanup()
