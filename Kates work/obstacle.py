import pygame
import sys
import random
import time
import sounddevice as sd
import numpy as np


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
def update_obstacles(screen, obstacles, obstacle_timer, score, difficulty):
    obstacle_timer += 1

    # Spawn interval shrinks as difficulty rises, capped at 20 frames minimum
    spawn_interval = max(20, 60 - int(difficulty * 10))
    if obstacle_timer > random.randint(spawn_interval, spawn_interval + 40):
        obs_height = random.randint(int(30 + difficulty * 8), int(60 + difficulty * 12))
        obs_width = random.randint(int(20 + difficulty * 5), int(35 + difficulty * 8))
        obs = pygame.Rect(1400, 520 - obs_height, obs_width, obs_height)
        obstacles.append(obs)
        obstacle_timer = 0

    # Move, draw, and cull obstacles
    for obs in obstacles[:]:
        obs.x -= 6
        screen.blit(slime, obs.topleft)
        if obs.x < -obs.width:
            obstacles.remove(obs)
            score += 1

    return obstacle_timer, score