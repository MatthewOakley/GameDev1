import pygame

class Character(pygame.sprite.Sprite):
    
    def __init__(self, health, skin, special_name, moves):
        self.health = health
        self.skin = skin
        self.special_name = special_name
        self.moves = moves
        
        self.moves_len = len(moves)
        
    def update(self):
        return
    
    def render(self):
        return
    
    