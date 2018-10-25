import pygame
class Block(pygame.sprite.Sprite):
  
  def __init__(self, width, height, x_pos, y_pos, image):
    super().__init__()
    self.width = width
    self.height = height
    self.x_pos = x_pos
    self.y_pos = y_pos
    
    self.image = pygame.Surface([self.width, self.height])
    self.image.fill(image)
    self.rect = self.image.get_rect()
    self.rect.x = self.x_pos
    self.rect.y = self.y_pos
    
    
    
    