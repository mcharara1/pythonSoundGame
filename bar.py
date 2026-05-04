import pygame
import sys
import random
import obstacle1
import time
import sounddevice as sd
import numpy as np
pygame.init()

#here is where we should make a sound level checker and adjust bar image based on the level. create a threshold for each level.
#not required: a great feature that we could add is if the threshold can be adjusted with just one variable.
#create array that stores thresholds and maybe applies the multiplier to them, which are then used in a big if else else else statement.
# the if statement returns the propper bar image, and also would initiate the propper obstacle defeat sequence. 

barGraphicSet = [
    pygame.image.load('graphics/bar0.png'),
    pygame.image.load('graphics/bar1.png'),
    pygame.image.load('graphics/bar2.png'),
    pygame.image.load('graphics/bar3.png'),
    pygame.image.load('graphics/bar4.png'),
    pygame.image.load('graphics/bar5.png'),
    pygame.image.load('graphics/bar6.png'),
    pygame.image.load('graphics/bar7.png'),
    pygame.image.load('graphics/bar8.png'),
    pygame.image.load('graphics/bar9.png'),
    pygame.image.load('graphics/bar10.png')
]
#simply set barGraphic to whatever numb:    ↓     from 0-10  in each if else thingy
barGraphic = random.choice(barGraphicSet)

