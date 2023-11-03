#Flappy Bird
#Gordon Mo, Jacky Wong, Sara Perera, Selina Cheng

import pygame, random

#initialize pygame
pygame.init()
clock = pygame.time.Clock()
fsp = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

running = True

#our main loop 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()