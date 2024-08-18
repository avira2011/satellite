'''
1. Import the actors and draw them
2. Get a background
3. Draw lines between the satellites as per their serial no.
4. Add a timer 
5. Get the timer to stop when the connection is built
6. Build connection between the satellites and incase player miss clicks the connection gets intrrupted
 '''

import pgzrun
from random import randint 
from time import time

WIDTH = 700
HEIGHT = 500

satellites = []
lines = []
next_satellite = 0

start_time = 0
total_time = 0

number_of_satellite = 8
next_satellite = 0

galaxy = Actor('galaxy')

def create_satellite():
    global start_time
    for count in range(0, number_of_satellite):
        satellite = Actor('satellite')
        satellite.pos = randint(40,670), randint(40,460)
        satellites.append(satellite)

number = 1

def draw():
    galaxy.draw()
    for i in range(8):
        satellites[i].draw()
        screen.draw.text(str(number +i), (satellites[i].pos[0], satellites[i].pos[1]))
    for line in lines:
        screen.draw.line(line[0], line[1], 'white')

def update():
    pass

create_satellite()

def on_mouse_down(pos):
    global next_satellite, lines
    if next_satellite < number_of_satellite:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite != 0:
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))

                next_satellite +=1
            else:
                lines = []
                next_satellite = 0




pgzrun.go()
