import pyxel
from game import labels, levels


#class for apple that handles drawing and moving it
#also checks if anything is on apple (snake eating it)
class Apple:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        self.sprite = sprite

    def draw(self):
        sprite_x, sprite_y = self.sprite
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h, labels.Colour.BLACK)

    def intersects(self, u, v, w, h):
        is_intersected = False
        #checking if given coordinates are inside apple
        if ( 
             u + w > self.x
             and self.x + self.w > u
             and v + h > self.y
             and self.y + self.h > v
        ):
            is_intersected = True
        
        return is_intersected

    def move(self, new_x, new_y):
        self.x = new_x 
        self.y = new_y