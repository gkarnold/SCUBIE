import serial # Imports the serial library

# Creates an arduino serial object
arduinoSerialData = serial.Serial('/dev/cu.usbmodem1421',9600)

# Loops that run forever
while True:
    # If statement that checks for data waiting to be read from arduino
    if (arduinoSerialData.inWaiting() > 0):
        # Read the data that is in waiting
        myData = arduinoSerialData.readline()
        print(myData)