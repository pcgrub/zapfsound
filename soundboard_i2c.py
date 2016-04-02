import smbus
from time import sleep
import subprocess
import pygame.mixer

buttons=[14,5,15,6,4,0,3,1,2,7]
bus = smbus.SMBus(1)

DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register A
IODIRB = 0x01 # Pin direction register B
GPIOA  = 0x12 # Register for inputs GPIOA
GPIOB  = 0x13 # Register for inputs GPIOB
OLATB  = 0x15 # Register for outputs on B

def setup_buttons():
	bus.write_byte_data(DEVICE,IODIRA,0xFF) # Set all pins on GPIOA to inputs
	bus.write_byte_data(DEVICE,IODIRB,0xF8) # Set last 5 pins of GPIOB to inputs
 	bus.write_byte_data(DEVICE,OLATB,0)
def check_switch(number):
	try:
		number //= 1
	except TypeError:
		print 'Only numbers, please!'
	if buttons[number] < 8:
		state_a = bus.read_byte_data(DEVICE,GPIOA)
		actual = buttons[number]
		a = 2**actual & state_a
		if a == 2**actual:
			return 1
	elif buttons[number] > 7:
		state_b = bus.read_byte_data(DEVICE,GPIOB)
		actual = buttons[number]-8
		b = 2**actual & state_b
		if b == 2**actual:
			return 1
	return 0

def reading_in(pins):
    # reading in the sound file names from config and creating the sounds:
    soundfile = open('sounds.txt', 'r')
    adresses = soundfile.read().splitlines()
    soundlist = []
    path = '/home/pi/wavsounds/'
    for i in range(len(adresses)-1):
        if adresses[i][0] != '#':
            print str(adresses[i])
            temp = pygame.mixer.Sound(path+str(adresses[i]))
            if (temp.get_length() >= 5 or temp.get_length() <= 0.1):
                temp = pygame.mixer.Sound(path+"WilhelmScream.wav")
            soundlist.append(temp)
    if len(soundlist) < 10:
        for i in range(len(soundlist),len(pins)):
            soundlist.append(pygame.mixer.Sound(path+"WilhelmScream.wav"))
    soundfile.close()
    return soundlist

def main():
    # switch detection and playing sounds:
    pygame.mixer.init(48000, -16, 1, 1024)
    Channel0 = pygame.mixer.Channel(0)
    buttons=[14,5,15,6,4,0,3,1,2,7]
    soundlist = reading_in(buttons)
    print "fertig"
    bus.write_byte_data(DEVICE,OLATB,1) # switching on green LED
    while True:
        try:
            for i in range(len(buttons)):
                if check_switch(i): #testing soundpins
                    Channel0.play(soundlist[i])
                    sleep(soundlist[i].get_length())
               # if check_switch(13):
               #     try:
               #         subprocess.call('git pull', shell=True)
               #         reading_in(buttons)
               #     except:
               #         pass
               # if check_switch(12):  #testing killswitch button
               #     raise KeyboardInterrupt
        except KeyboardInterrupt:
            bus.write_byte_data(DEVICE,OLATB,4)
	    break

if __name__=="__main__":
    main()

