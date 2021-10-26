from pymata4 import pymata4
import time

arduino = pymata4.Pymata4()

zelena_pin = 2
zluta_pin = 3
cervena_pin = 4

arduino.set_pin_mode_digital_output(zelena_pin)
arduino.set_pin_mode_digital_output(zluta_pin)
arduino.set_pin_mode_digital_output(cervena_pin)

while True:
    arduino.digital_write(zelena_pin,0)
    arduino.digital_write(zluta_pin,0)
    arduino.digital_write(cervena_pin,0)
    time.sleep(1)
    arduino.digital_write(zelena_pin,1)
    arduino.digital_write(zluta_pin,1)
    arduino.digital_write(cervena_pin,1)
    time.sleep(1)

