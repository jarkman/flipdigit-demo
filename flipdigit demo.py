
# Demo code for driving the Alfazeta Flipdigit 7-segment display (with RS485 interface board) 
# https://flipdots.com/en/products-services/small-7-segment-displays/
# I used a cheap USB RS485 adapter from eBay
# 
# Wiring - my adapter was labelled A and B, the Flipdigit data sheet has +RS and -RS
# I wired +RS to A and -RS to B. I also connected USB ground to Flipdigit ground.

# I ran the Flipdigit from 24V DC

# The vendor's web page says
#   At these coil drive parameters, the duty cycle for driving the same segment must be less than 5% (on/off time)
#   therefore allow at least 900msec before driving the same segment again. 
#   This will ensure that the segment coil will not accumulate heat.
# This code pays no attention to this limit. Please do not blame me if you melt your display.

import serial # from https://pyserial.readthedocs.io
import time

import serial.rs485

# Segment layout (not obvious which way is meant to be up, I made an arbitrary choice)

    #     1
    # 32     2
    #     64
    # 16     4
    #     8


digits = [ 1+2+4+8+16+32, 2+4, 1+2+64+16+8, 1+2+64+4+8,32+64+2+4,1+32+64+4+8,32+64+16+4+8,1+2+4,1+2+4+8+16+32+64,1+2+4+32+64]    
    
def setFlaps(ser, num):
    command = 0x89  # send one byte and show it
    address = 0xff   # shipping default, use their PIX_ONE tool to change a digit's address 
    data = num  # MSB is neglected, the following bits B6 – B0 are setting dots from top to bottom respectively.

    


    packet = bytearray([0x80, command, address, data, 0x8f ])

     
    #for b in packet:
    #    print("Sending...", hex(b))

    ser.write(packet)

    ser.flush()
    print(); # empty line

def interactiveTester(ser):

    while True:

        # Taking input from user
        num = int(input("Enter a number (0 - 255): "))
        setFlaps(ser, num)

def looper(ser):

    loop = [1, 2, 4, 8, 16, 32]
    i = 0
    while True:
        i = i + 1
        if i >= len(loop):
            i = 0
        
        setFlaps(ser, loop[i])

        time.sleep(0.01)


def flasher(ser):
     t = 0.5

     while True:
        
        
        setFlaps(ser, 127)

        time.sleep(t)

        setFlaps(ser, 0)

        time.sleep(t)

        t = 0.9 * t

def showDigit(ser, digit):
    setFlaps(ser,digits[digit])

def counter(ser):
    t = 0.5
    digit = 0

    while True:
        
        
        showDigit(ser,digit)

        time.sleep(t)

        t = 0.97 * t            
        digit = digit +1
        if digit>9:
            digit = 0


ser = serial.Serial(port='COM3', baudrate=9600, timeout=10) # 9600 is the shipping default baud rate, use their PIX_ONE tool to change it
ser.rs485_mode= serial.rs485.RS485Settings()

#looper(ser)
#flasher(ser)
counter(ser)



