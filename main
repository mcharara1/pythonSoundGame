#import all required libraries or functions from other files here
import pygame
import sys
import random
import obstacle1
import time
import sounddevice as sd
import numpy as np
import bar
#Initialize pygame
pygame.init()

#Set up the display (screen)
width, height = 1300, 800 #width and hight of window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Python sound game")
clock = pygame.time.Clock()
screen.fill('white')

#set up the game surface gwindow
#gwindow = pygame.Surface((width - 400,height - 200))
gwindow = pygame.image.load('graphics/gborder.png')

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
    screen.blit(gwindow, (100, 100)) #put game window on screen
    screen.blit(bwindow, (1000, 100)) #put bar window on screen
    bwindow.blit(bar.barGraphic, (0,0))
    pygame.display.update()     # Update display (while running is set to true, until set to false aka game over or smthng.)
    clock.tick(60)    # cap framerate to 60 fps

# Quit pygame once while loop is broken
pygame.quit()
sys.exit()