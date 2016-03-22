import smbus
import numpy as np
from time import sleep

buttons=[15,6,16,7,5,1,4,2,3,8]
bus = smbus.SMBus(1)

DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register A
IODIRB = 0x01 # Pin direction register B
GPIOA  = 0x12 # Register for inputs GPIOA
GPIOB  = 0x13 # Register for inputs GPIOB


def setup_buttons():
	bus.write_byte_data(DEVICE,IODIRA,0xFF) # Set all pins on GPIOA to inputs
	bus.write_byte_data(DEVICE,IODIRB,0xF8) # Set last 5 pins of GPIOB to inputs

def check_switch(number):
	if number < 8:
		state_a = bus.read_byte_data(DEVICE,GPIOA)
		a = 2**buttons[number] & state_a
		if a == 2**buttons[number]:
			return 1
	elif number > 7:
		state_b = bus.read_byte_data(DEVICE,GPIOB)
		b = 2**buttons[number] & state_b
		if b == 2**buttons[number]:
			return 1
	return 0
