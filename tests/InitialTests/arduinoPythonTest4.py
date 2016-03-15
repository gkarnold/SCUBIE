# Simple application that will send a command from python to Arduino to change which light is illuminated in a series of lights

## Imports
# Build in functions
import time
import serial

# Sets up the arduino serial connection
arduino = serial.Serial('/dev/cu.usbmodem1421',9600)
time.sleep(2)
# Sets a loop that runs forever
while True:
    arduino.write(str(0))
    time.sleep(.25)
    print arduino.readline()
    arduino.write(str(1))
    time.sleep(.25)
    print arduino.readline()
    arduino.write(str(2))
    time.sleep(.25)
    print arduino.readline()
    arduino.write(str(3))
    time.sleep(.25)
    print arduino.readline()
    arduino.write(str(4))
    time.sleep(.25)
    print arduino.readline()