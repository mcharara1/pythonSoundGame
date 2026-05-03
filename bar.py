import pygame
import sys
import random
import obstacle1
import time
import sounddevice as sd
import numpy as np
#here is where we should make a sound level checker and adjust bar image based on the level. create a threshold for each level.
#not required: a great feature that we could add is if the threshold can be adjusted with just one variable.
#create array that stores thresholds and maybe applies the multiplier to them, which are then used in a big if else else else statement.
# the if statement returns the propper bar image, and also would initiate the propper obstacle defeat sequence. 


#simply set barGraphic to whatever numb:    ↓     from 0-10  in each if else thingy
barGraphic = pygame.image.load('graphics/bar7.png')

