# This is our PetCity Game
# Written by Oakley and Evan
# Last modified 10/25/18
import pygame
from Character import *
from Block import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (105, 105, 105)

# pygame game setup
pygame.init()
pygame.display.set_caption('Pet City')


# Set the height and width of the screen
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# pygame set up the fps
fps = pygame.time.Clock()

done = False
all_sprites = pygame.sprite.Group()
testChar = Character(0, 0, 0, 0)
all_sprites.add(testChar)

"""
Build the bottom bar
"""
combat_bar = pygame.sprite.Group()
background = Block(900, 200, 0, 400, DARK_GRAY)
combat_bar.add(background)


# the game loop
while not done:
    
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    
    
    
    
    
    
    
    
    
    
    # Clear the screen
    screen.fill(WHITE)

    # Draw all the spites
    all_sprites.draw(screen)
    
    combat_bar.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 20 frames per second
    fps.tick(60)
    
pygame.quit()