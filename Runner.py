import pygame
import sys
import random
import obstacle
import time
import sounddevice as sd
import numpy as np
import bar

pygame.init()

dogGraphicSet = [
    pygame.image.load('graphics/dog1.png'),
    pygame.image.load('graphics/dog2.png'),
    pygame.image.load('graphics/dog3.png'),
    pygame.image.load('graphics/dog4.png'),
]
