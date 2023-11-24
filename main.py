#Flappy Bird
#Gordon Mo, Jacky Wong, Sara Perera, Selina Cheng

import pygame, random
fsp = 60

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super(Bird, self).__init__()
        self.surf = pygame.image.load("bird.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2
            ))

#initialize pygame
pygame.init()
clock = pygame.time.Clock()

#Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

#variable to keep main loop running
running = True

#create our bird
bird = Bird()

#our main loop 
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.fill((255,255,255))

    screen.blit(bird.surf, bird.rect)
    #flip everything to the display
    pygame.display.flip()
    #60 frames per second
    clock.tick(60)

pygame.quit()