import smbus
from time import sleep
import numpy as np

#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register A
IODIRB = 0x01 # Pin direction register B
GPIOA  = 0x12 # Register for inputs GPIOA
GPIOB  = 0x13 # Register for inputs GPIOB
OLATA  = 0x14 # Alternative to GPIOA
OLATB  = 0x15 # Alternative to GPIOB

bus.write_byte_data(DEVICE,IODIRA,0xFF) # Set all pins on GPIOA to inputs
bus.write_byte_data(DEVICE,IODIRB,0xF8) # Set first 5 pins of GPIOB to inputs

while True:
    try:
        overall_switch_state_a = bus.read_byte_data(DEVICE,GPIOA)
        overall_switch_state_b = bus.read_byte_data(DEVICE,GPIOB)
        for i in range(8):
            a = 2**i & overall_switch_state_a
            if a == 2**i:
                print str(np.log2(a)+1) + " pressed"
        for d in range(8):
            b = 2**d & overall_switch_state_b
            if b == 2**d:
                print str(np.log2(b)+9) + " pressed"
        sleep(0.1)
    except KeyboardInterrupt:
        break
