import pygame, sys, time, math
from pygame.locals import *

pygame.init()


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

    # Left joystick axes
    h_L = math.floor(my_joystick.get_axis(0)*1000)
    v_L = math.floor(my_joystick.get_axis(1)*1000)

    # Trigger axes
    trigger = math.floor(my_joystick.get_axis(2)*1000)

    # Right joystick axes
    h_R = math.floor(my_joystick.get_axis(3)*1000)
    v_R = math.floor(my_joystick.get_axis(4)*1000)

    # Checks the values of the joysticks and triggers and zeros them if they are close to zero
    if h_L < 10 and h_L > -10:
        h_L = 0
    if v_L < 10 and v_L > -10:
        v_L = 0
    if trigger < 10 and trigger > -10:
        trigger = 0
    if h_R < 10 and h_R > -10:
        h_R = 0
    if v_R < 10 and v_R > -10:
        v_R = 0


    ##### PS 3 CONTROLLER
    # # Gets the current button state
    # button_x = my_joystick.get_button(0)
    # button_circle = my_joystick.get_button(1)
    # button_square = my_joystick.get_button(2)
    # button_triangle = my_joystick.get_button(3)
    # button_left_index = my_joystick.get_button(4)
    # button_right_index = my_joystick.get_button(5)
    # button_select = my_joystick.get_button(6)
    # button_start = my_joystick.get_button(7)
    # button_left_joystick = my_joystick.get_button(8)
    # button_right_joystick = my_joystick.get_button(9)
    #
    # # Prints the status of the controller
    # print('Joysticks')
    # print(h_L,v_L,trigger,h_R,v_R)
    # print('Buttons:')
    # print(button_x,button_circle,button_square,button_triangle,button_left_index,button_right_index,button_select,
    #     button_start,button_left_joystick,button_right_joystick)

    print('------------------------')
    print(my_joystick.get_axis(0))
    print(my_joystick.get_axis(1))
    print(my_joystick.get_axis(2))
    print(my_joystick.get_axis(3))
    print(my_joystick.get_axis(4))
    print(my_joystick.get_axis(5))

    time.sleep(1)