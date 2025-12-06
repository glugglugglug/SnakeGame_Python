import pyxel
from game import labels, levels

#handles drawing parts of the snake, head orientation
#also checking intersections(crashed into itself)
class SnakeSec:
    def __init__(self, x, y, sprite, is_head = False):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        self.sprite = sprite
        self.is_head = is_head

    def draw(self, direction):
        # temp value so it can be manipulated
        width = self.w
        height = self.h
        sprite_x, sprite_y = self.sprite
        #if its head section, then sprite must be changed/flipped depending on direction
        if self.is_head:
            if direction == labels.Direction.RIGHT:
                sprite_x = 8
                sprite_y = 0
            if direction == labels.Direction.LEFT:
                sprite_x = 8
                sprite_y = 0
                #by making the value negative, draw func will draw it flipped
                width *= -1
            if direction == labels.Direction.DOWN:
                sprite_x = 0
                sprite_y = 8
            if direction == labels.Direction.UP:
                sprite_x = 0
                sprite_y = 8
                #by making the value negative, draw func will draw it flipped
                height *= -1
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, width, height, labels.Colour.BLACK)

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