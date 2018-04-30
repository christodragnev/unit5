#Christo Dragnev
#4/30/18
#antsDemo.py - using lists with graphics

from ggame import *
from random import randint

ANTS = 30
WIDTH = 900
HEIGHT = 400

#move each ant randomly up/down and left/right
def step():
    for ant in data['antList']:
        ant.x += randint(-4,3)
        ant.y += randint(-4,3)

#putting fire ants randomly on the screen
if __name__ == '__main__':
    
    data = {}
    data['antList'] = []
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(10,LineStyle(1,red),red)
    
    for i in range(ANTS):
        data['antList'].append(Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT))))
        
    
    App().run(step)
