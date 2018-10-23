import pygame

class Player(Character):
    
    def __init__(self):
        super.__init__(self)
        self.points = 0
        return
        
    def get_points(self):
        return self.points
        
    def pick_move(self):
        i = 1
        for move in self.moves:
            print(str(i) + ": " + move.getName())
            i += 1
        
        choice = int(input("Which move do you want to pick? "))
        return self.moves[i - 1]
        
    def update(self):
        return
        
    def render(self):
        return
    