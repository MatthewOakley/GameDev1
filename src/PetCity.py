# This is our PetCity Game
# Written by Oakley and Evan
# version 0.5
# Last modified 10/26/18
#
import pygame
import os
import datetime
import time
from Character import *
from Block import *
from Player import *
from Thug import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (105, 105, 105)

# pygame game setup
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
action_font = pygame.font.SysFont('Trebuchet MS', 30)
pygame.display.set_caption('Pet City')
game_over_text = my_font.render('Game Over', False, (0, 0, 0))
game_over = False


# Set the height and width of the screen
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# setup the needed images
full_health = pygame.image.load("../content/full_heart.png")
empty_health = pygame.image.load("../content/empty_heart.png")


# pygame set up the fps and flags
fps = pygame.time.Clock()
done = False


"""
Setup player
"""
all_sprites = pygame.sprite.Group()
player = Player()
thug = Thug()
all_sprites.add(player)
all_sprites.add(thug)

"""
Build the bottom bar
"""
combat_bar = pygame.sprite.Group()
background = Block(900, 200, 0, 400, DARK_GRAY)
# background of combat bar
combat_bar.add(background)

# the moves buttons
# 3 moves
punch = Block(100, 100, 150, 450, BLUE)
punch_bar = my_font.render('PUNCH', False, (0, 0, 0))
special = Block(100, 100, 400, 450, GREEN)
special_bar = my_font.render('SPECIAL', False, (0, 0, 0))
counter = Block(100, 100, 650, 450, RED)
counter_bar = my_font.render('COUNTER', False, (0, 0, 0))
combat_bar.add(punch)
combat_bar.add(special)
combat_bar.add(counter)

# The health bars
def create_health_bars(health, max_health, x_pos, y_pos):
    i = 0
    shift = 0
    while i < health:
        screen.blit(full_health, (x_pos + shift, y_pos))
        shift += 20
        i += 1
    while i < max_health:
        screen.blit(empty_health, (x_pos + shift, y_pos))
        shift += 20
        i += 1
# the timer

"""
Build the visual actions
"""
# the moves over the characters
punch_text = action_font.render('PUNCH', False, (0, 0, 0))
special_bar = action_font.render('SPECIAL', False, (0, 0, 0))
counter_bar = action_font.render('COUNTER', False, (0, 0, 0))





# the game loop
while not done:
    action = False
    attack = -1
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONUP:
            action = True
            pos = pygame.mouse.get_pos()
            # within button area
            if pos[1] >= 450 and pos[1] <= 550:
                # punch
                if pos[0] >= 150 and pos[0]<= 250:
                    attack = 1
                    print("PUNCH")
                # special
                elif pos[0] >= 400 and pos[0]<= 500:
                    attack = 2
                    print("SPECIAL")
                # counter
                elif pos[0] >= 650 and pos[0]<= 750:
                    attack = 3
                    print("COUNTER")
        # keyboard input
        elif event.type == pygame.KEYDOWN:
            action = True
            if event.key == pygame.K_1:
                attack = 1
                print("PUNCH")
            elif event.key == pygame.K_2:
                attack = 2
                print("SPECIAL")
            elif event.key == pygame.K_3:
                attack = 3
                print("COUNTER")
                
    # player took an action
    if action:
        enemy_attack = thug.pick_move()
        print("Enemy:", enemy_attack)
        if attack == enemy_attack:
            print("DRAW")
        elif attack == 1 and enemy_attack == 2:
            print("Player beats enemy: P v S")
            thug.update_health(-1)
        elif attack == 1 and enemy_attack == 3:
            print("Enemy beats player: C v P")
            player.update_health(-1)
        elif attack == 2 and enemy_attack == 1:
            print("Enemy beats player: P v S")
            player.update_health(-1)
        elif attack == 2 and enemy_attack == 3:
            print("Player beats enemy: S v C")
            thug.update_health(-1)
        elif attack == 3 and enemy_attack == 1:
            print("Player beats enemy: C v P")
            thug.update_health(-1)
        elif attack == 3 and enemy_attack == 2:
            print("Enemy beats player: S v C")
            player.update_health(-1)
    
    # Clear the screen
    screen.fill(WHITE)   
    
    
    
    if (player.get_health() == 0 or thug.get_health() == 0) and game_over == False:
        game_over = True
        start_time = time.time()
    
    if game_over:
        if time.time() - start_time < 3:
            screen.blit(game_over_text, (300, 100))
        else:
            done = True
    

    # Draw all the spites
    all_sprites.draw(screen)
    
    # draw the UI
    combat_bar.draw(screen)
    
    # draw moves text
    screen.blit(punch_bar,(148,550))
    screen.blit(special_bar,(388,550))
    screen.blit(counter_bar,(630,550))
    
    # draw health text
    create_health_bars(player.get_health(), 3, 15, 15)
    create_health_bars(thug.get_health(), 3, 800, 15)
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    fps.tick(60)
    
pygame.quit()