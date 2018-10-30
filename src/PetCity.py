# This is our PetCity Game
# Written by Oakley and Evan
# version 0.5
# Last modified 10/26/18
# This is the file for the game loop and core of PetCity
# this handles all of the logic and processing of the game
# it also includes instructions for how to play
"""
INSTRUCTIONS
Here are the instructions for our game, PetCity.
We have worked mostly from command line (Oakley is more comfortable there),
so our project might look a bit different than others.
PetCity is broken into Python files that reference each other.
It helps us keep our classes in check.
=============================================
The controls are as follow: either click your attack option, or press 1/2/3
(corresponds to the order on the bottom of the screen).
Punch beats special, special beats counter, and counter beats punch.
The results are tracked in the terminal,
as well as with the health bars above the characters.
This alpha is showing off the game logic. Sprites, music, more feedback,
and (hopefully some) animation is to come!
"""

import pygame
from Character import *
import time
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


def create_health_bars(health, max_health, x_pos, y_pos):
    """
    The health bars
    """
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
# special_bar = action_font.render('SPECIAL', False, (0, 0, 0))
# counter_bar = action_font.render('COUNTER', False, (0, 0, 0))

# the game loop
while not done:
    action = False
    attack = -1
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONUP and not game_over:
            action = True
            pos = pygame.mouse.get_pos()
            # within button area
            if pos[1] in range(450, 551):
                # punch
                if pos[0] in range(150, 251):
                    attack = 1
                # special
                elif pos[0] in range(400, 501):
                    attack = 2
                # counter
                elif pos[0] in range(650, 751):
                    attack = 3
        # keyboard input
        elif event.type == pygame.KEYDOWN and not game_over:
            action = True
            if event.key == pygame.K_1:
                attack = 1
            elif event.key == pygame.K_2:
                attack = 2
            elif event.key == pygame.K_3:
                attack = 3
                
    # player took an action
    if action:
        enemy_attack = thug.pick_move()
        if attack == enemy_attack:
            print("DRAW")
        elif attack == 1 and enemy_attack == 2:
            print("Player beats enemy: Punch v Special")
            thug.update_health(-1)
        elif attack == 1 and enemy_attack == 3:
            print("Enemy beats player: Counter v Punch")
            player.update_health(-1)
        elif attack == 2 and enemy_attack == 1:
            print("Enemy beats player: Punch v Special")
            player.update_health(-1)
        elif attack == 2 and enemy_attack == 3:
            print("Player beats enemy: Special v Counter")
            thug.update_health(-1)
        elif attack == 3 and enemy_attack == 1:
            print("Player beats enemy: Counter v Punch")
            thug.update_health(-1)
        elif attack == 3 and enemy_attack == 2:
            print("Enemy beats player: Special v Counter")
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
    screen.blit(punch_bar, (148, 550))
    screen.blit(special_bar, (388, 550))
    screen.blit(counter_bar, (630, 550))
    
    # draw health text
    create_health_bars(player.get_health(), 3, 15, 15)
    create_health_bars(thug.get_health(), 3, 800, 15)
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    fps.tick(60)

pygame.quit()
