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

        #checking if ladder or not
        self.is_Ladder = False
        if self.sprite == levels.LEVELS[1].snake:
            self.is_Ladder = True

        #direction tracking
        self.prev_dir = None
        self.next_dir = None

    def draw(self, direction):
        # temp value so it can be manipulated
        width = self.w
        height = self.h
        sprite_x, sprite_y = self.sprite
        #if its head section, then sprite must be changed/flipped depending on direction
        if self.is_head:
            if direction == labels.Direction.RIGHT:
                sprite_x += 8
                sprite_y += 0
            if direction == labels.Direction.LEFT:
                sprite_x += 8
                sprite_y += 0
                #by making the value negative, draw func will draw it flipped
                width *= -1
            if direction == labels.Direction.DOWN:
                sprite_x += 0
                sprite_y += 8
            if direction == labels.Direction.UP:
                sprite_x += 0
                sprite_y += 8
                #by making the value negative, draw func will draw it flipped
                height *= -1
        elif self.is_Ladder == True:
            if self.prev_dir != None and self.next_dir != None and self.prev_dir != self.next_dir:
                sprite_x, sprite_y = 16, 16
                if (self.prev_dir == labels.Direction.RIGHT and self.next_dir == labels.Direction.DOWN) or \
                    (self.prev_dir == labels.Direction.UP and self.next_dir == labels.Direction.LEFT):
                    sprite_x += 8
                    sprite_y += 0
                if (self.prev_dir == labels.Direction.LEFT and self.next_dir == labels.Direction.DOWN) or \
                    (self.prev_dir == labels.Direction.UP and self.next_dir == labels.Direction.RIGHT):
                    sprite_x += 0
                    sprite_y += 0
                if (self.prev_dir == labels.Direction.RIGHT and self.next_dir == labels.Direction.UP) or \
                    (self.prev_dir == labels.Direction.DOWN and self.next_dir == labels.Direction.LEFT):
                    sprite_x += 8
                    sprite_y += 8
                if (self.prev_dir == labels.Direction.LEFT and self.next_dir == labels.Direction.UP) or \
                    (self.prev_dir == labels.Direction.DOWN and self.next_dir == labels.Direction.RIGHT):
                    sprite_x += 0
                    sprite_y += 8
            else:
                if self.prev_dir == labels.Direction.UP or self.prev_dir == labels.Direction.DOWN:
                    sprite_x += 8
                    sprite_y += 8
                if self.prev_dir == labels.Direction.RIGHT or self.prev_dir == labels.Direction.LEFT:
                    sprite_x += 0
                    sprite_y += 0   
            """ elif direction == labels.Direction.DOWN:
                sprite_x += 8
                sprite_y += 8
            elif direction == labels.Direction.UP:
                sprite_x += 8
                sprite_y += 8 """

    
        print(sprite_x, sprite_y)
        
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