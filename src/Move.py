import pygame

class Move(Object):
  def __init__(self, name, damage):
    super.__init__(self)
    
    self.name = name
    self.damage = damage
    