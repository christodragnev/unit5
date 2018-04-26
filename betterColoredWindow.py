#Christo Dragnev
#4/25/18
#betterColoredWindow.py

from random import randint
from ggame import *
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)
red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)

colors = [red, green, blue]

def mouseClick(event):
    num = randint(0,2)
    rectangle = RectangleAsset(800,800,blackOutline,colors[num])
    Sprite(rectangle)
    
App().listenMouseEvent('click',mouseClick)
App().run()