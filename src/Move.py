import pygame

class Move(Object):
  def __init__(self, name, damage):
    super.__init__(self)
    
    self.name = name
    self.damage = damage
    
  def get_name(self):
    return self.name
    
  def get_damage(self):
    return self.damage
    
  def update(self):
    return
    
  def render(self):
    return
    
  
    