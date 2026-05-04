import pygame
import sys
import random
import time
import sounddevice as sd
import numpy as np
import bar
import Runner

pygame.init()
slimeOrig = pygame.image.load('graphics/slime.png') 
orig_width, orig_height = slimeOrig.get_size()

scale_factor = 3  # increase size by 300%
new_size = (int(orig_width * scale_factor), int(orig_height * scale_factor))

slime = pygame.transform.scale(slimeOrig, new_size)