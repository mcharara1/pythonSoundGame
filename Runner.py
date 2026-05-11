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
    pygame.image.load('graphics/dog1.png'),
    pygame.image.load('graphics/dog2.png'),
    pygame.image.load('graphics/dog2.png'),
    pygame.image.load('graphics/dog3.png'),
    pygame.image.load('graphics/dog3.png'),
    pygame.image.load('graphics/dog4.png'),
    pygame.image.load('graphics/dog4.png'),
]
def BlastSequence(number, canvas, X, Y):
    smallBlast = pygame.image.load("graphics/B.png")
    BigBlast = pygame.image.load("graphics/BB.png")
    if number == 1:
        canvas.blit(smallBlast, (X + 100,Y + 15))
    if number == 2:
        canvas.blit(BigBlast, (X + 100, Y + 15))
        number = 0
