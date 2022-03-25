#Maria Suarez 
#Learning Pygame
 
 #import all your libraries

import os, time
import pygame as pg        

WIDTH=600
HEIGHT=700
 #initialize pygame
pg.init()
#create your window/screen
screen=pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('My screen')
pg.display.update()
pg.time.delay(500)

#Create new colors
white=[255,255,255]
green=[0,255,0]
red=[255,0,0]
blueish=[102,153, 255]
screen.fill(white)
pg.display.update()
pg.time.delay(500)
#create rectangules
    #initial position
x=10
y=10
    #height and the width of rect
wbox=20
hbox=20

square=pg.Rect(x,y,wbox,hbox)

#Main Game loop 
run=True

while run:
    screen.fill(blueish)
    pg.draw.rect(screen,(green), square)
    pg.display.update()
    for event in pg.event.get():
        if event.type== pg.QUIT:
            run =False
    pg.time.delay(200)
    square.x +=5
    square.y +=5
    pg.draw.rect(screen,(green), square)
    pg.display.update()
    pg.time.delay(200)
