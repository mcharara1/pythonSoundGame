import pygame
import sys
import random
import time
import sounddevice as sd
import numpy as np
import bar
import Runner

pygame.init()
#this here adjusts the size of the sprite. would change or get rid of this if we change the sprite
slimeOrig = pygame.image.load('graphics/slime1.png')
slimeSet = [
            pygame.image.load('graphics/slime1.png'),
            pygame.image.load('graphics/slime2.png'),
            pygame.image.load('graphics/slime3.png'),
            pygame.image.load('graphics/slime4.png'),
            pygame.image.load('graphics/slime5.png'), 
            ]
orig_width, orig_height = slimeOrig.get_size()
scale_factor = 3  # increase size by 300%
new_size = (int(orig_width * scale_factor), int(orig_height * scale_factor))
slime = pygame.transform.scale(random.choice(slimeSet), new_size)

#here we gotta make a transform position function so it looks like the dog is running to the obstacle, and also a detect collision function