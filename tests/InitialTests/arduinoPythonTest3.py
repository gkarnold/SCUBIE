# Simple application that will send ASCII characters to an Arduino board and then ahve the board send them back

from time import sleep
import serial

# Sets up the connection with the Arduino over the
ser = serial.Serial('/dev/cu.usbmodem1421',9600)

counter = 32 # Below 32 everything is gibberish

while True:
    counter += 1
    ser.write(str(chr(counter))) # Convers the number to ASCII and then send it to the Arduino board
    print ser.readline() #Reads the newest output from the Arduino board
    sleep(.1) # Waits for 1/10 of a second
    if counter == 255:
        counter = 32