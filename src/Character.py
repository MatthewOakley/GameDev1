import pygame

PINK = (255,105,180)

class Character(pygame.sprite.Sprite):
    
    def __init__(self, health, skin, special_name, moves):
        super().__init__()
        self.health = health
        self.skin = skin
        self.special_name = special_name
        self.moves = moves
        self.image = pygame.Surface([20, 15])
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 100
        
        #self.moves_len = len(moves)
        
    def update(self):
        return
    
    def render(self):
        return
    
    