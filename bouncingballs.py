# 3 bouncing balls

# Make two circles that move around the screen and bounce off the edges of the window.  If they collide, one of them (or both) goes to a random location.

import pgzrun
import math

WIDTH = 800
HEIGHT = 600
c1Xpos = 100
c1Ypos = 100

c2Xpos = 400
c2Ypos = 400

c3Xpos = 500
c3Ypos = 100

speed = 2
x1 = -speed
y1 = speed
x2 = speed
y2 = -speed
x3 = speed
y3 = speed


def draw():
    global c1Xpos, c1Ypos, c2Xpos, c2Ypos, x1, y1, x2, y2
    screen.draw.filled_circle((c1Xpos, c1Ypos), 50, "blue")
    screen.draw.filled_circle((c2Xpos, c2Ypos), 50, "red")
    screen.draw.filled_circle((c3Xpos, c3Ypos), 50, "purple")


def update():
    global c1Xpos, c1Ypos, c2Xpos, c2Ypos, c3Xpos, c3Ypos, x1, y1, x2, y2, x3, y3, speed
    c1Xpos += x1
    c1Ypos += y1
    c2Xpos += x2
    c2Ypos += y2
    c3Xpos += x3
    c3Ypos += y3

    if c1Xpos > 750 or c1Xpos < 50:
        x1 *= -1
    if c1Ypos > 550 or c1Ypos < 50:
        y1 *= -1
    if c2Xpos > 750 or c2Xpos < 50:
        x2 *= -1
    if c2Ypos > 550 or c2Ypos < 50:
        y2 *= -1
    if c3Xpos > 750 or c3Xpos < 50:
        x3 *= -1
    if c3Ypos > 550 or c3Ypos < 50:
        y3 *= -1

    distance = ((c1Xpos-c2Xpos)**2 + (c1Ypos-c2Ypos)**2)**0.5
    if distance <= 100:
        slope = (c1Ypos-c2Ypos)/(c1Xpos-c2Xpos)
        if (slope == 0):
            slope = 0.0000000001
        x1 = -1/slope*speed/slope
        y1 = -slope*speed/slope
        x2 = 1/slope*speed/slope
        y2 = slope*speed/slope

    distance = ((c1Xpos-c3Xpos)**2 + (c1Ypos-c3Ypos)**2)**0.5
    if distance <= 100:
        slope = (c1Ypos-c3Ypos)/(c1Xpos-c3Xpos)
        if (slope == 0):
            slope = 0.0000000001
        x1 = -1/slope*speed/slope
        y1 = -slope*speed/slope
        x3 = 1/slope*speed/slope
        y3 = slope*speed/slope

    distance = ((c3Xpos-c2Xpos)**2 + (c3Ypos-c2Ypos)**2)**0.5
    if distance <= 100:
        slope = (c3Ypos-c2Ypos)/(c3Xpos-c2Xpos)
        if (slope == 0):
            slope = 0.0000000001
        x3 = -1/slope*speed/slope
        y3 = -slope*speed/slope
        x2 = 1/slope*speed/slope
        y2 = slope*speed/slope

    screen.clear()


pgzrun.go()
