# Flappy Bird CS 127
## Gordon Mo, Jacky Wong, Sara Perera, Selina Cheng
### Final Project

import pygame
import random

pygame.init()
clock = pygame.time.Clock()
fsp = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')
