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

bgroundOrig = pygame.image.load('graphics/Grass.png')
#orig_width, orig_height = bgroundOrig.get_size()
#scale_factor = 1.2
#new_size = (int(orig_width * scale_factor), int(orig_height * scale_factor))
bground = bgroundOrig#pygame.transform.scale(bgroundOrig, new_size)
