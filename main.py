#Flappy Bird
#Gordon Mo, Jacky Wong, Sara Perera, Selina Cheng

#import libraries
import pygame, random

from pygame.locals import (
    RLEACCEL,
    K_ESCAPE,
    K_SPACE,
    K_h,
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
        self.load_images()
        self.rect = self.surf.get_rect(
            center = (SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2)
        )
        
    def load_images(self):
        self.surf = pygame.image.load("bird.png").convert_alpha()
        self.surf.set_colorkey(pygame.Color("white"), RLEACCEL)

    #load in purple version of the bird
    def purple(self):
        self.surf = pygame.image.load("purple.png").convert_alpha()

    #controls vertical movement
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
                lower.rect.x, lower.rect.y-180  
            ))

    def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.kill()

class Score(object):
    def __init__(self):
        self.black = 0,0,0
        self.count = 0
        pygame.font.init()
        self.font = pygame.font.SysFont("comicsans",50, True , True)
        self.text = self.font.render(str(self.count),1,self.black)

    def show_score(self, screen):
        screen.blit(self.text, (SCREEN_WIDTH/2,SCREEN_HEIGHT/2-200))

    def score_up(self):
        self.count += 1
        self.text = self.font.render(str(self.count),1,self.black)

#create Score object
score = Score()

#initialize pygame
pygame.init()

#set the clock for a decent framerate
clock = pygame.time.Clock()

#Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

#variable to keep main loop running
running = True

#keep the bird from moving
move = False

#game over state flag
game_over = False

#create custom events for adding a new pipe
ADDPIPE = pygame.USEREVENT + 1
PIPE_ADD_INTERVAL = 5000
pygame.time.set_timer(ADDPIPE, PIPE_ADD_INTERVAL)

#group the pipes together
pipes = pygame.sprite.Group()
uP = pygame.sprite.Group()

#create our bird
bird = Bird()

#game over function
def display_game_over_screen():
    #clear screen
    screen.fill((255, 255, 255))

    #display game over text
    font1 = pygame.font.SysFont("comicsans", 50, True)
    game_over_text = font1.render("Game Over", 1, (0, 0, 0))
    game_over_text_rect = game_over_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 40))
    screen.blit(game_over_text, game_over_text_rect)
    
    #display final score
    score_text = font1.render(f"Final Score: {score.count}", 1, (0, 0, 0))
    score_text_rect = score_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(score_text, score_text_rect)

    #reset game instructions
    font2 = pygame.font.SysFont("comicsans", 30, False, True)
    reset_instruction_text = font2.render("press space to replay", 1, (0, 0, 0))
    reset_instruction_text_rect = reset_instruction_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 40))
    screen.blit(reset_instruction_text, reset_instruction_text_rect)

#reset game after game over function
def reset_game():
    global game_over
    game_over = False

    #reset game variables
    score.count = 0

    #reset bird position
    bird.rect.x = SCREEN_WIDTH/2 - 100
    bird.rect.y = SCREEN_HEIGHT/2

    #remove existing pipes
    pipes.empty()
    uP.empty()
    pygame.time.set_timer(ADDPIPE, PIPE_ADD_INTERVAL)

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
            uP.add(upper_pipe)

    if move:
        pressed_keys = pygame.key.get_pressed()
        bird.update(pressed_keys)

    #clear the screen
    screen.blit(bg, (0, 0))
    screen.blit(bird.surf, bird.rect)
    
    for entity in pipes:
        screen.blit(entity.surf, entity.rect)

    #score increment when game in-progress
    if not game_over:
        for pipe in uP:
            if bird.rect.left == pipe.rect.right:
                score.score_up()

    pipes.update()

    score.show_score(screen)

    #if bird touches floor, end game
    if bird.rect.bottom == SCREEN_HEIGHT:
        game_over = True
    
    #if bird collides into any pipes, end game
    if pygame.sprite.spritecollideany(bird, pipes):
        bird.kill()
        game_over = True

    if game_over:
        pygame.event.get()

        #display game over screen
        display_game_over_screen()

        #restart input
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    reset_game()

    #flip everything to the display
    pygame.display.flip()

    #60 frames per second
    clock.tick(60)
    
#sound effects
#sound source: https://www.101soundboards.com/boards/10178-flappy-bird-sounds 
pygame.mixer.music.load("jump sound.mp3")
pygame.mixer.music.load("game over sound.mp3")
move_up_sound = pygame.mixer.Sound("jump sound.mp3")
gameover_sound = pygame.mixer.Sound("game over sound.mp3")

#keying sound effects to pressed keys
def update(self, pressed_keys):
        if pressed_keys[K_SPACE]:
            move_up_sound.play()
        if bird.rect.bottom == SCREEN_HEIGHT:
            gameover_sound.play()
            
pygame.quit()