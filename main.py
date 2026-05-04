#import all required libraries or functions from other files here
import pygame
import sys
import random
import obstacle
import time
import sounddevice as sd
import numpy as np
import bar
import Runner

#Initialize pygame
pygame.init()

#Set up the display (screen)
width, height = 1300, 800 #width and hight of window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Python sound game")
clock = pygame.time.Clock()
i=0
#set up the game surface gwindow
#gwindow = pygame.Surface((width - 400,height - 200))
gborder = pygame.image.load('graphics/gborder.png')
gwindow = gborder
mask = pygame.image.load('graphics/mask.png')
#ground = pygame.image.load('graphics/ground.png') # do this when ground pic is set up
#set up the power up Bar surface bwindow
bwindow = pygame.Surface((200,height - 200))
bwindow.fill('white')
# Main loop (the game runs inside this while true loop.)
running = True
while running:
    for event in pygame.event.get(): #check for closing pygame prettymuch all the time lmao
        if event.type == pygame.QUIT:
            running = False

    screen.fill('grey32')
    bwindow.blit(bar.barGraphicSet[1], (0,0))
    i = i+1
    if i == 4:
        i = 0
    dogGraphic = Runner.dogGraphicSet[i]
    #gwindow.fill('white')
    #gwindow.blit(gborder, (0,0))
    screen.blit(dogGraphic, (300,500))
    screen.blit(obstacle.slime, (600,500))
    screen.blit(gwindow, (100, 100)) #put game window on screen
    screen.blit(mask, (0,0)) #mask to cover everything that spills out of gwindow
    screen.blit(bwindow, (1000, 100)) #put bar window on screen
    barGraphic = random.choice(bar.barGraphicSet)
    bwindow.blit(barGraphic, (0,0)) #put bar graphic (from bar.py)

    pygame.display.update()     # Update display (while running is set to true, until set to false aka game over or smthng.)
    clock.tick(15)    # cap framerate to 60 fps

# Quit pygame once while loop is broken
pygame.quit()
sys.exit()