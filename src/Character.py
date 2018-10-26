import pygame

PINK = (255,105,180)

class Character(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.health = 3
        self.image = pygame.Surface([40, 70])
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        
    def get_health(self):
        return self.health
        
    def set_health(self, new_health):
        self.health = new_health
        
    def update_health(self, change):
        self.health += change
        
    def update(self):
        return
    
    def render(self):
        return
    
    