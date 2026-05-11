import pygame
import random

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

#slimeDeath = pygame.image.load('graphics/1i.png')
#slime1Death2 = pygame.image.load('graphics/1is.png')

#slime2Death1 = pygame.image.load('graphics/2i.png')
#slime2Death2 = pygame.image.load('graphics/2is.png')

#slime3Death1 = pygame.image.load('graphics/3i.png')
#slime3Death2 = pygame.image.load('graphics/3is.png')

#slime4Death1 = pygame.image.load('graphics/4i.png')
#slime4Death2 = pygame.image.load('graphics/4is.png')

#slime5Death1 = pygame.image.load('graphics/5i.png')
#slime5Death2 = pygame.image.load('graphics/5is.png')



orig_width, orig_height = slimeOrig.get_size()
scale_factor = 3  # increase size by 300%
new_size = (int(orig_width * scale_factor), int(orig_height * scale_factor))
slime = pygame.transform.scale(random.choice(slimeSet), new_size)

class Obstacle:
    def __init__(self, screen_width, screen_height, speed=5):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = speed
        self.reset()


    def reset(self):
        min_y = 100
        max_y = self.screen_height - 100 - new_size[1]
        self.y = random.randint(min_y, max_y)  # Spawn anywhere inside the window margins
        self.x = self.screen_width  # Start off-screen to the right
        self.image = pygame.transform.scale(random.choice(slimeSet), new_size)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


    def update(self):
        self.x -= self.speed
        self.rect.x = self.x
        if self.x + self.rect.width < 0:
            self.reset()  # Spawn a new obstacle when off-screen


    def draw(self, screen):
        screen.blit(self.image, self.rect)

