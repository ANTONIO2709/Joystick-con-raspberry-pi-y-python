#!/usr/bin/env python3
#############################################################################
# Filename    : Joystick.py
# Description : Read Joystick state
# Author      : Antonio2709
# modification: 2019/12/27
########################################################################
import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus=smbus.SMBus(1)
cmd=0x40
Z_Pin = 12      # definir Pin Z
def analogRead(chn):        # leer valor ADC
    bus.write_byte(address,cmd+chn)
    value = bus.read_byte(address)
    value = bus.read_byte(address)
    # value = bus.read_byte_data(address,cmd+chn)
    return value
    
def analogWrite(value):
    bus.write_byte_data(address,cmd,value)  

def setup():
    GPIO.setmode(GPIO.BOARD)        
    GPIO.setup(Z_Pin,GPIO.IN,GPIO.PUD_UP)   # poner pin Z a modo pull-up 
def loop():
    while True:     
        val_Z = GPIO.input(Z_Pin)       # leer valor digital de Z
        val_Y = analogRead(0)           # leer valor analogico de  X e Y
        val_X = analogRead(1)
        print ('value_X: %d ,\tvlue_Y: %d ,\tvalue_Z: %d'%(val_X,val_Y,val_Z))
        time.sleep(1)

def destroy():
    bus.close()
    GPIO.cleanup()
    
if __name__ == '__main__':
    print ('El Programa esta arrancando ... ') # Arrancar programa
    print ('Presionar control + c para finalizar programa ')
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Presionar control + c para finalizar programa
        destroy()
