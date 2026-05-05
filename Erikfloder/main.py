#import all required libraries or functions from other files here
import pygame
import sys
import random
import obstacle
import time
import sounddevice as sd
import numpy as np
import pythonSoundGame.Erikfloder.bar as bar
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
    
    #load things that appear in game window here
    dogGraphic = Runner.dogGraphicSet[i] #this loads the propper dog pic in the animation
    screen.blit(dogGraphic, (300,500)) #this places the dog on the screen
    screen.blit(obstacle.slime, (600,500)) #this places the slime on screen

    screen.blit(mask, (0,0)) #mask to cover everything that spills out of gwindow, such as ground or whatever
    
    screen.blit(gwindow, (100, 100)) #put game window on screen (the red border)
    #load things that appear outside the game window here
    screen.blit(bwindow, (1000, 100)) #put bar window on screen
    bar_level = bar.get_bar_level() #randomly select a bar image here                  # call the function to get 0–10
    bwindow.blit(bar.barGraphicSet[bar_level], (0,0))  # use that number to pick the image ✅
    pygame.display.update()     # Update display (while running is set to true, until set to false aka game over or smthng.)
    clock.tick(15)    # cap framerate to 60 fps

# Quit pygame once while loop is broken
pygame.quit()
bar.stream.stop()
sys.exit()