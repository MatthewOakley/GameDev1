import pygame
import random
from Character import *

class Thug(Character):
    
    def __init__(self):
        super().__init__()
        self.image.fill((255,0,0))
        self.rect.x = 500
        self.rect.y = 250
        return
          
    def pick_move(self):
        num = random.randint(1,3)
        return num
           
    def update(self):
        return
        
    def render(self):
        return
    
    