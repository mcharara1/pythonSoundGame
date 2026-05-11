#import all required libraries or functions from other files here
import keyboard
import pygame
import sys
import os
import keyboard
import random
import obstacle
import bar
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
gborder = pygame.image.load('graphics/gborder.png')
gwindow = gborder
mask = pygame.image.load('graphics/mask.png')
#set up the power up Bar surface bwindow
bwindow = pygame.Surface((200,height - 200))
bwindow.fill('white')
bground = pygame.image.load('graphics/Grass.png')
# Main loop (the game runs inside this while true loop.)

# Create obstacle speed function first
start_ticks = pygame.time.get_ticks()

#define obstacle speed and make each obstacle slightly different

def get_obstacle_speed():
    seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
    base_speed = 9 + (seconds_passed * 0.12)   # gets faster over time
    random_bonus = random.uniform(0, 2)        # keeps it random
    return min(base_speed + random_bonus, 12)  # maximum speed

#load a different image in the even tof defeating an obstacle
death_animations = {
    i: pygame.transform.scale(
        pygame.image.load(f"graphics/{i}i.png").convert_alpha(),
        (128, 128)
    ) 
    for i in range(1, 6)
}

def defanimation(screen, level, x, y):
    screen.blit(death_animations[level], (x,y))

# Create obstacle instance
obstacle_instance = obstacle.Obstacle(width, height)
obstacle_instance.speed = get_obstacle_speed()
obstacle_level = random.randint(1, 5)
prev_obstacle_x = obstacle_instance.x

#variables and constants
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
game_over_text = font.render("GAME OVER", True, (255, 0, 0))
restart_text = font.render("Press R to restart", True, (255, 255, 255))
start_ticks = pygame.time.get_ticks()

bgSecPast = (pygame.time.get_ticks() - start_ticks) / 1000

bg_pos_x = 100

bg_pos_increment = -10
B_Inc = 0
obstacle_defeat = False

#main game loop. this runs at a certain amount per second
while running:
    for event in pygame.event.get():  # check for closing window
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and started == False:
                started = True

            if event.key == pygame.K_r and game_over == True:
                os.execl(sys.executable, sys.executable, *sys.argv)

    screen.fill('grey32')
    
    if game_over:
        #game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text, (550, 350))
        screen.blit(restart_text, (527, 400))
        pygame.display.update()
        clock.tick(15)
        
        continue
    if started == False:
        bar_level = bar.get_bar_level()
        #print("Bar (before start):", bar_level)  # <-- ADD HERE

        start_text = font.render("Press SPACE to start", True, (255, 255, 255))
        screen.blit(start_text, (500, 350))
        pygame.display.update()
        clock.tick(60)
        continue

    i = i + 1
    if i == 8:
        i = 0

    obstacle_instance.update()
 
    dogGraphic = Runner.dogGraphicSet[i]

    screen.blit(bground, (bg_pos_x, 0))
    screen.blit(bground, (bg_pos_x + 400, 0))
    screen.blit(bground, (bg_pos_x + 800, 0))


    bg_pos_x = bg_pos_x + bg_pos_increment
    if bg_pos_x == -100:
        bg_pos_x = 100

    screen.blit(dogGraphic, (dogPosX, dogPosY))

    if keyboard.is_pressed('up'):
        dogPosY -= 10
    elif keyboard.is_pressed('down'):
        dogPosY += 10

    dog_rect = dogGraphic.get_rect(topleft=(dogPosX, dogPosY))

    if obstacle_defeat == False:
        obstacle_instance.draw(screen)
    else:
        obstacle_defeat = False

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

    current_obstacle_x = obstacle_instance.x
    current_obstacle_y = obstacle_instance.y

         # If obstacle scrolled off naturally, assign new level and speed
    if obstacle_instance.x > prev_obstacle_x:
        obstacle_level = random.randint(1, 5)
        obstacle_instance.speed = get_obstacle_speed()
        
    prev_obstacle_x = obstacle_instance.x

    # Only trigger if mic is actually picking up sound (bar_level above resting noise)
    if bar_level == 0:
        bar_was_zero = True

    if bar_level > 0 and abs(mapped_level - obstacle_level) <= 1 and abs(current_obstacle_y - dogPosY) <= 90 and abs(current_obstacle_x < 1000):
            defanimation(screen, obstacle_level, obstacle_instance.x, obstacle_instance.y)
            obstacle_instance.reset()
            obstacle_level = random.randint(1, 5)
            obstacle_instance.speed = get_obstacle_speed()
            score += 1
            B_Inc = 1
            obstacle_defeat = True
            bar_was_zero = False  # must return to 0 before next destroy
    if  B_Inc == 2: 
        Runner.BlastSequence(2, screen, dogPosX, dogPosY)
    else:
        if B_Inc == 1:
            Runner.BlastSequence(1, screen, dogPosX, dogPosY)
            B_Inc = 2

    pygame.display.update()
    clock.tick(15)
    B_Inc += 1
    # cap framerate to 60 fps

# Quit pygame once while loop is broken
pygame.quit()
bar.stream.stop()
sys.exit()    