import pyxel
import enum
import time

#snake direction labels
class Direction(enum.Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


#class for apple that handles drawing and moving it
#also checks if anything is on apple (snake eating it)
class Apple:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 0, self.w, self.h)


#handles drawing parts of the snake, head orientation
#also checking intersections(crashed into itself)
class SnakeSec:
    def __init__(self,x,y,is_head = False):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        self.is_head = is_head

    def draw(self, direction):
        # temp value so it can be manipulated
        width = self.w
        height = self.h
        sprite_x = 0
        sprite_y = 0
        #if its head section, then sprite must be changed/flipped depending on direction
        if self.is_head:
            if direction == Direction.RIGHT:
                sprite_x = 8
                sprite_y = 0
            if direction == Direction.LEFT:
                sprite_x = 8
                sprite_y = 0
                #by making the value negative, draw func will draw it flipped
                width *= -1
            if direction == Direction.DOWN:
                sprite_x = 0
                sprite_y = 8
            if direction == Direction.UP:
                sprite_x = 0
                sprite_y = 8
                #by making the value negative, draw func will draw it flipped
                height *= -1
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, width, height)

                
            
class App():
    #constructor of the class
    def __init__(self):
        scale = 4
        pyxel.init(192, 128, display_scale=scale, capture_scale=scale, title="Snake Game :P", fps=60)
        pyxel.load("assets/resources.pyxres")
        self.apple = Apple(64,32)

        #Store the snake sections
        self.snake = []

        #adding some sections
        self.snake.append(SnakeSec(32,32,is_head = True))
        self.snake.append(SnakeSec(24,32))
        self.snake.append(SnakeSec(16,32))
        
        #setting direction of snake
        self.snake_direction: Direction = Direction.RIGHT

        #timing and speed
        self.speed = 1.5
        self.time_last_frame = time.time()
        self.delta_time = 0
        self.time_since_last_move = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        #doing time stuff before moving snake
        time_this_frame = time.time()
        self.delta_time = time_this_frame - self.time_last_frame
        self.time_last_frame = time_this_frame
        self.time_since_last_move += self.delta_time
        
        #check if enough time has passed
        if self.time_since_last_move >= 1 / self.speed:
            self.time_since_last_move = 0
            self.move_snake()

    def draw(self):
        pyxel.cls(0)
        self.apple.draw()
        
        #going through each peice of snake and drawing them
        for s in self.snake:
            s.draw(self.snake_direction)
    
    def move_snake(self):
        # move the head
        prev_loc_x = self.snake[0].x
        prev_loc_y = self.snake[0].y
        if self.snake_direction == Direction.RIGHT:
            self.snake[0].x += self.snake[0].w
        if self.snake_direction == Direction.LEFT:
            self.snake[0].x -= self.snake[0].w
        if self.snake_direction == Direction.DOWN:
            self.snake[0].x += self.snake[0].h
        if self.snake_direction == Direction.UP:
            self.snake[0].x -= self.snake[0].h

        # move the tail
        for s in self.snake:
            if s == self.snake[0]:
                continue
            cur_loc_x = s.x
            cur_loc_y = s.y
            s.x = prev_loc_x
            s.y = prev_loc_y
            prev_loc_x = cur_loc_x
            prev_loc_y = cur_loc_y




#kickstarting the program
App()