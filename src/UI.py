import pygame

"""
Build the bottom bar
"""
combat_bar = pygame.sprite.Group()
background = Block(900, 200, 0, 400, DARK_GRAY)
combat_bar.add(background)

class UI(pygame.sprite.Sprite):