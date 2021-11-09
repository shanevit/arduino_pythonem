import time
from pymata4 import pymata4

arduino = pymata4.Pymata4()

tlacitko_pin = 8

zelena_pin = 2
zluta_pin = 3
cervena_pin = 4

arduino.set_pin_mode_digital_output(zelena_pin)
arduino.set_pin_mode_digital_output(zluta_pin)
arduino.set_pin_mode_digital_output(cervena_pin)

def cervena():
    arduino.digital_write(zelena_pin,0)
    arduino.digital_write(zluta_pin,0)
    arduino.digital_write(cervena_pin,1)    

def zluta():
    arduino.digital_write(zelena_pin,0)
    arduino.digital_write(zluta_pin,1)
    arduino.digital_write(cervena_pin,0) 

def zelena():
    arduino.digital_write(zelena_pin,1)
    arduino.digital_write(zluta_pin,0)
    arduino.digital_write(cervena_pin,0)
    
# kdyz zmacknu tlacitko, tak sos zelena zluta cervena


def zmacknuto(data):
    global tlacitko_stav
    tlacitko_stav = data[2]
    print(f'zmacknuto - stav: {tlacitko_stav}')

arduino.set_pin_mode_digital_input_pullup(tlacitko_pin, callback=zmacknuto)

while True:
    pass