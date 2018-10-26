from Character import *

class Player(Character):
    
    def __init__(self):
        super().__init__()
        self.points = 0
        self.image.fill((0,0,255))
        self.rect.x = 200
        self.rect.y = 250
        return
        
    def get_points(self):
        return self.points
        
    def set_points(self, new_points):
        self.points = new_points
    
    def update_points(self, change):
        self.points += change
        
    def pick_move(self, choice):
        return
           
    def update(self):
        return
        
    def render(self):
        return
    