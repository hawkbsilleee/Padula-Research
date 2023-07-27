import matplotlib.pyplot as plt
import numpy as np
import argparse
from matplotlib.animation import FuncAnimation
import time 
import keyboard 
import csv

OBJECT_SPEED = 0.00000001

# Graph Setup
plt.rcParams["figure.figsize"] = 10,10
# create a figure with an axes
fig, ax = plt.subplots()
# set the axes limits (SIZING)
ax.axis([-100,100,-100,100])
# Fixation point 
ax.plot(0,0, "k", marker="o")

# create a point in the axes
point, = ax.plot([],[], "r", marker="o")

input_dict = {}

def write_csv(patientID, color, meridian, x, y):
    with open('FCFTester_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(['patientID', 'color', 'meridian', 'x_coord', 'y_coord'])
        writer.writerow([patientID, color, meridian, x, y])

def update(x, y):
    point.set_data(x, y)
    return point,

def direction(meridian):
    i = 0
    x = 0
    y = 0
    update(x,y)
    while True:
        i += 1 
        if meridian == 0:
            x = i/10
            y = 0
        elif meridian == 45:
            x = i/10
            y = i/10
        elif meridian == 90:
            x = 0
            y = i/10
        update(x,y)
        plt.pause(OBJECT_SPEED) 
        if keyboard.is_pressed('space'):
            keyboard.release('space')
            print(f"Detection: ({x},{y})")
            input_dict[meridian] = [x, y]
            break 
        # try: 
        #     if keyboard.is_pressed('space'):
        #         print(f"Detection: ({x},{y})")
        #         debounce = False 
        #         break 
        # except:
        #     # debounce = False
        #     break    
    # write_csv('ES', 'red', meridian, x, y)
    print(input_dict)

direction(0)
direction(45)
direction(90)

plt.show()
