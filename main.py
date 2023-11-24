#Flappy Bird
#Gordon Mo, Jacky Wong, Sara Perera, Selina Cheng

#import libraries
import pygame, random
fsp = 60

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    MOUSEBUTTONDOWN,
    KEYDOWN,
    QUIT,
)

#set screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

#load background 
bg = pygame.image.load("background.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super(Bird, self).__init__()
        self.surf = pygame.image.load("bird.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2
            ))
    def update(self, num):
        if num == 1:
            self.rect.move_ip(0, -25)

    #keep player on screen
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

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
        if event.type == KEYDOWN:
            #if escape key is pressed, quit game
            if event.key == K_ESCAPE:
                running = False
        #exiting window, quits game
        elif event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                bird.update(1)
    #screen.fill((255,255,255))
    screen.blit(bg,(0,0))
    screen.blit(bird.surf, bird.rect)
    #flip everything to the display
    pygame.display.flip()
    #60 frames per second
    clock.tick(60)

pygame.quit()