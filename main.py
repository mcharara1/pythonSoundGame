#import all required libraries or functions from other files here
import turtle

import keyboard
import pygame
import sys
import os
import keyboard
import random
import obstacle
import time
import sounddevice as sd
import numpy as np
import bar
import Runner
import Background

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
#bground = pygame.image.load('graphics/Background.png')
gborder = pygame.image.load('graphics/gborder.png')
gwindow = gborder
mask = pygame.image.load('graphics/mask.png')
#ground = pygame.image.load('graphics/ground.png') # do this when ground pic is set up
#set up the power up Bar surface bwindow
bwindow = pygame.Surface((200,height - 200))
bwindow.fill('white')
# Main loop (the game runs inside this while true loop.)

# Create obstacle speed function first
start_ticks = pygame.time.get_ticks()

def get_obstacle_speed():
    seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
    base_speed = 7 + (seconds_passed * 0.08)
    random_bonus = random.uniform(0, 2)
    return min(base_speed + random_bonus, 16)

# Create obstacle instance
obstacle_instance = obstacle.Obstacle(width, height)
obstacle_instance.speed = get_obstacle_speed()
obstacle_level = random.randint(1, 5)
prev_obstacle_x = obstacle_instance.x


GROUND = 580
obstacles = []
onstacle_timer = 0
score = 0
difficulty = 0.0
font = pygame.font.SysFont(None, 36)
started = False
dogPosX = 300
dogPosY = 500
speed = 5
running = True
game_over = False
obstacle_level = random.randint(1, 5)
prev_obstacle_x = width
bar_was_zero = True

start_ticks = pygame.time.get_ticks()

def get_obstacle_speed():
    seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
    base_speed = 9 + (seconds_passed * 0.12)   # gets faster over time
    random_bonus = random.uniform(0, 2)        # keeps it random
    return min(base_speed + random_bonus, 12)  # maximum speed

while running:
    for event in pygame.event.get():  # check for closing window
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and started == False:
                started = True

    screen.fill('grey32')
    
    if game_over:
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text, (550, 350))
        pygame.display.update()
        clock.tick(15)
        continue
    if started == False:
        bar_level = bar.get_bar_level()
        print("Bar (before start):", bar_level)  # <-- ADD HERE

        start_text = font.render("Press SPACE to start", True, (255, 255, 255))
        screen.blit(start_text, (500, 350))
        pygame.display.update()
        clock.tick(60)
        continue

    i = i + 1
    if i == 4:
        i = 0

    obstacle_instance.update()
 
    dogGraphic = Runner.dogGraphicSet[i]
    screen.blit(Background.bground, (100, 100))
    screen.blit(dogGraphic, (dogPosX, dogPosY))

    if keyboard.is_pressed('up'):
        dogPosY -= 5
    elif keyboard.is_pressed('down'):
        dogPosY += 5

    dog_rect = dogGraphic.get_rect(topleft=(dogPosX, dogPosY))


    obstacle_instance.draw(screen)

    if dog_rect.colliderect(obstacle_instance.rect):
        game_over = True

    screen.blit(mask, (0, 0))
    screen.blit(gwindow, (100, 100))

    score_text = font.render(f"score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (50, 50))

    screen.blit(bwindow, (1000, 100))
    bwindow.blit(pygame.image.load('graphics/bar0.png'), (0, 0))

    bar_level = bar.get_bar_level()
    bwindow.blit(bar.barGraphicSet[bar_level], (0, 0))

    # Map bar (0-10) down to match obstacle levels (1-5)
    mapped_level = (bar_level // 2) + 1

    # If obstacle scrolled off naturally, assign new level and speed
    if obstacle_instance.x > prev_obstacle_x:
        obstacle_level = random.randint(1, 5)
        obstacle_instance.speed = get_obstacle_speed()
    prev_obstacle_x = obstacle_instance.x

    # Only trigger if mic is actually picking up sound (bar_level above resting noise)
    if bar_level == 0:
        bar_was_zero = True

    if bar_level > 0 and bar_was_zero and abs(mapped_level - obstacle_level) <= 1:
        obstacle_instance.reset()
        obstacle_level = random.randint(1, 5)
        obstacle_instance.speed = get_obstacle_speed()
        score += 1
        bar_was_zero = False  # must return to 0 before next destroy

    pygame.display.update()
    clock.tick(15)
    # cap framerate to 60 fps
    
    #os.execv(sys.executable, ['python'] + sys.argv)
# Quit pygame once while loop is broken
pygame.quit()
bar.stream.stop()
sys.exit()    