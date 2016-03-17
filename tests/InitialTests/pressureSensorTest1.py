# Simple application that will read the pressure from the ardunio pressure sensor

from time import sleep
import serial

# Sets up the connection with the Arduino over the
arduino = serial.Serial('/dev/cu.usbmodem1421',9600)


while True:
    # Reads and outputs the pressure from the arduino pressure sensor
    print('Current Pressure: {}'.format(arduino.readline()))