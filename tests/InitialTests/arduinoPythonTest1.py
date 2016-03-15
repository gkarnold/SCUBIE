import serial, time
arduino = serial.Serial('/dev/cu.usbmodem1421',9600,timeout=.1)
while True:
    data = arduino.readline()[:-2] # The last bit gets rid of the new-line chars

    # Checks if data is blank or not and then outputs it if it is not blank
    if data:
        print(data)
