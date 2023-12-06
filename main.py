#Flappy Bird
#Gordon Mo, Jacky Wong, Sara Perera, Selina Cheng

#import libraries
import pygame, random

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    K_h,
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
    def purple(self):
        self.surf = pygame.image.load("purple.png").convert_alpha()

    def update(self, pressed_keys):
        if pressed_keys[K_SPACE]:
            self.rect.move_ip(0, -8)
        else:
            self.rect.move_ip(0, +3)

    #keep player on screen
        if self.rect.top <= -100:
            self.rect.top = -100
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Pipes(pygame.sprite.Sprite):
    def __init__(self):
        super(Pipes, self).__init__()
        self.surf = pygame.image.load("lower_pipe.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                #random.randint(75, SCREEN_HEIGHT-25)
                SCREEN_WIDTH, random.randint(500,800) #SCREEN_HEIGHT+200
            ))
    def top(self, lower):
        super(Pipes, self).__init__()
        self.surf = pygame.image.load("upper_pipe.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        #print(lower.rect.x)
        self.rect = self.surf.get_rect(
            bottomleft=(
                lower.rect.x, lower.rect.y-160  
            ))
    def update(self):
        self.rect.move_ip(-2, 0)
        if self.rect.right < 0:
            self.kill()

#initialize pygame
pygame.init()

#set the clock for a decent framerate
clock = pygame.time.Clock()

#Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

#variable to keep main loop running
running = True

move = False

#create custom events for adding a new pipe
ADDPIPE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDPIPE, 2500)

#group the pipes together
pipes = pygame.sprite.Group()

#create our bird
bird = Bird()
#our main loop 
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #if escape key is pressed, quit game
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_SPACE:
                move = True
            if event.key == K_h:
                bird.purple()
        #exiting window, quits game
        elif event.type == QUIT:
            running = False
        
        elif event.type == ADDPIPE:
            lower_pipe = Pipes()
            upper_pipe = Pipes()
            upper_pipe.top(lower_pipe)
            pipes.add(lower_pipe)
            pipes.add(upper_pipe)

    if move:
        pressed_keys = pygame.key.get_pressed()
        bird.update(pressed_keys)
    
    #screen.fill((255,255,255))
    screen.blit(bg,(0,0))
    screen.blit(bird.surf, bird.rect)
    
    for entity in pipes:
        screen.blit(entity.surf, entity.rect)

    pipes.update()
    #if bird touches floor, end game
    if bird.rect.bottom == SCREEN_HEIGHT:
        running = False
    #flip everything to the display
    pygame.display.flip()
    #60 frames per second
    clock.tick(60)

    if pygame.sprite.spritecollideany(bird, pipes):
        bird.kill()
        running = False 
    
#adding sound effects
#sound source: https://www.101soundboards.com/boards/10178-flappy-bird-sounds 
pygame.mixer.music.load("jump sound.mp3")
pygame.mixer.music.load("game over sound.mp3")

move_up_sound = pygame.mixer.Sound("jump sound.mp3")
gameover_sound = pygame.mixer.Sound("game over sound.mp3")

def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            move_up_sound.play()
        if bird.rect.bottom == SCREEN_HEIGHT:
            gameover_sound.play()
            
pygame.quit()
