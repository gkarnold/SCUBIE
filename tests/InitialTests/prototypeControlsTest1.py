# Application that will take a joystick input command from an xBox controller and send the information to Arduino.
# Arduino will then send the information back and use the value to control the intensity of an LED
import pygame, sys, time, math, serial
from pygame.locals import *

# Initializes pygame
pygame.init()

# Sets up the connection with the Arduino
arduino = serial.Serial('/dev/cu.usbmodem1421',9600)


joystick_count = pygame.joystick.get_count()
print("There were ", joystick_count, " joystick(s) found.")
if joystick_count == 0:
    print("Please connect a joystick and try again.")
else:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

keepLooping = True

while keepLooping:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            keepLooping = False

    # Sets a header value to send to arduino to be ignored
    header = 0;

     # Gets Left Vertical Controller Axis
    v_L = math.floor(my_joystick.get_axis(1)*100)*-1

     # Gets Right Vertical Controller Axis
    v_R = math.floor(my_joystick.get_axis(3)*100)*-1

    # Gets Trigger Axes
    trigger_L = math.floor(my_joystick.get_axis(4)*100)
    trigger_R = math.floor(my_joystick.get_axis(5)*100)

    # Combines the two triggers into a single trigger value for vertical control
    trigger = -(trigger_L+1)/2+(trigger_R+1)/2

    # Checks the values of the joysticks and triggers and zeros them if they are close to zero or axes them if they are close to max
    if v_L < 10 and v_L > -10:
        v_L = 0
    if v_L > 95:
        v_L = 100
    if v_L < -95:
        v_L = -100

    if v_R < 10 and v_R > -10:
        v_R = 0
    if v_R > 95:
        v_R = 100
    if v_R < -95:
        v_R = -100

    if trigger < 10 and trigger > -10:
        trigger = 0
    if trigger > 95:
        trigger = 100
    if trigger < -95:
        trigger = -100

    axesString = str(header)+'H'+str(v_L)+'L'+str(v_R)+'R'+str(trigger)+'V'
    # axesString = str('100L10R53V')
    # Outputs the value of the left vertical controller axis for comparision
    print('Controller Axis (v_L, v_R, trigger): {}'.format(axesString))
    # Reads the return information from Arduino
    print('Left Vertical Controller Axis (Arduino): {}'.format(arduino.readline()))
    print('-------------------------------------------------------')

    # Sends the value of the controller axes to Arduino
    arduino.write(str(axesString))