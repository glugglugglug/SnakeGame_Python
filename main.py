import pyxel
import enum
import time
import random
import collections



#snake direction labels
class Direction(enum.Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

#game state labels
class GameState(enum.Enum):
    RUNNING = 0
    GAME_OVER = 1


# level class that handles drawing the level(walls)
class Level:
    def __init__(self):
        self.tm = 0
        self.u = 0
        self.v = 0
        self.w = 192
        self.h = 128

    def draw(self):
        pyxel.bltm(0, 0, self.tm, self.u, self.v, self.w, self.h)


#class for apple that handles drawing and moving it
#also checks if anything is on apple (snake eating it)
class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 0, self.w, self.h)

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



#handles drawing parts of the snake, head orientation
#also checking intersections(crashed into itself)
class SnakeSec:
    def __init__(self, x, y, is_head = False):
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



#helper func for calc start x value for centred text
def center_text(text, page_width, char_width = pyxel.FONT_WIDTH):
    text_width = len(text) * char_width
    return (page_width - text_width) / 2


#helper func for calc start x value for right aligned text
def right_text(text, page_width, char_width = pyxel.FONT_WIDTH):
    text_width = len(text) * char_width
    return page_width - (text_width + char_width) 

# handles drawing text and scores-
class Hud:
    def __init__(self):
        self.title_text = "SnakeGame :P"
        self.title_text_x = center_text(self.title_text,196)
        self.score_text = str(0)
        self.score_text_x = right_text(self.score_text,196)
        self.level_text = "lvl 0"
        self.level_text_x = 10
        self.apples_text = "Apples "
        self.apples_text_x = len(self.level_text) * pyxel.FONT_WIDTH + self.level_text_x + 10

    def draw_title(self):
        pyxel.rect(self.title_text_x -1, 0, len(self.title_text) * pyxel.FONT_WIDTH +1, pyxel.FONT_HEIGHT +1, 1)
        pyxel.text(self.title_text_x, 1, self.title_text, 12)

    def draw_score(self, score):
        self.score_text = str(score)
        self.score_text_x = right_text(self.score_text, 196)
        pyxel.rect(self.score_text_x - 11, 0, len(self.score_text) * pyxel.FONT_WIDTH +1, pyxel.FONT_HEIGHT +1, 1)
        pyxel.text(self.score_text_x - 10, 1, self.score_text, 3)

    def draw_level(self, level):
        self.level_text = "Level " + str(level)
        pyxel.rect(self.level_text_x -1, 0, len(self.level_text) * pyxel.FONT_WIDTH +1, pyxel.FONT_HEIGHT +1, 1)
        pyxel.text(self.level_text_x, 1, self.level_text, 3)

    def draw_apples(self, apples):
        self.apples_text = "Apples " + str(apples)
        pyxel.rect(self.apples_text_x -1, 0, len(self.apples_text) * pyxel.FONT_WIDTH +1, pyxel.FONT_HEIGHT +1, 1)
        pyxel.text(self.apples_text_x, 1, self.apples_text, 8)

    
            
class App():
    #constructor of the class
    def __init__(self):
        scale = 4
        pyxel.init(192, 128, display_scale=scale, capture_scale=scale, title="Snake Game :P", fps=60)
        pyxel.load("assets/resources.pyxres")
        self.apple = Apple(64, 32)

        #gamestate variables
        self.cur_game_state = GameState.RUNNING

        #level 
        self.level = Level()

        #texts
        self.hud = Hud()

        #Store the snake sections
        self.snake = []

        #adding some sections
        self.snake.append(SnakeSec(32, 32, is_head = True))
        self.snake.append(SnakeSec(24, 32))
        self.snake.append(SnakeSec(16, 32))
        
        #setting direction of snake
        self.snake_direction: Direction = Direction.RIGHT

        #sections to add
        self.sec_to_add = 0

        #timing and speed
        self.speed = 1.5
        self.time_last_frame = time.time()
        self.delta_time = 0
        self.time_since_last_move = 0

        #quantifying vars score levels apples etc
        self.score = 0
        self.apples_eaten_this_level = 0
        self.apples_eaten_total = 0
        self.cur_level = 1
        
        #for input queue - using a deque, pop from front and back - stores direction changes
        self.input_queue = collections.deque()

        pyxel.run(self.update, self.draw)

    def update(self):
        #doing time stuff before moving snake
        time_this_frame = time.time()
        self.delta_time = time_this_frame - self.time_last_frame
        self.time_last_frame = time_this_frame
        self.time_since_last_move += self.delta_time
        
        #queue-ing up player moves
        self.check_input()
    
        #check game state first and then see if its time to move
        if self.cur_game_state == GameState.RUNNING:
            if self.time_since_last_move >= 1 / self.speed:
                self.time_since_last_move = 0
                self.move_snake()
                self.check_collision()
                self.score += len(self.snake) * self.apples_eaten_total + 1
                
    def start_new_game(self):
        self.cur_game_state = GameState.RUNNING
        self.snake.clear()

        #Add the initial snake sections again
        self.snake.append(SnakeSec(32, 32, is_head = True))
        self.snake.append(SnakeSec(24, 32))
        self.snake.append(SnakeSec(16, 32))

        #setting direction of snake
        self.snake_direction: Direction = Direction.RIGHT

        #sections to add
        self.sec_to_add = 0

        #timing and speed
        self.speed = 1.5
        self.time_last_frame = time.time()
        self.delta_time = 0
        self.time_since_last_move = 0

        #reset input queue
        self.input_queue.clear()

        #move apple again
        self.move_apple() 

        #quantifying vars score levels apples etc
        self.score = 0
        self.apples_eaten_this_level = 0
        self.apples_eaten_total = 0
        self.cur_level = 1



    def draw(self):
        pyxel.cls(0)
        self.level.draw()
        self.apple.draw()
        
        #going through each peice of snake and drawing them
        for s in self.snake:
            s.draw(self.snake_direction)

        #draw title and other text
        self.hud.draw_title()
        self.hud.draw_score(self.score)
        self.hud.draw_level(self.cur_level)
        self.hud.draw_apples(self.apples_eaten_total)

        #show game over
        pyxel.text(10, 114, str(self.cur_game_state), 12)
    
    #checks all collisions
    def check_collision(self):
        #apple and snakehead intersection
        if self.apple.intersects(self.snake[0].x, self.snake[0].y, self.snake[0].w, self.snake[0].h):
            self.speed += (self.speed * 0.1)
            self.sec_to_add += 4
            self.move_apple()
            self.apples_eaten_total += 1
            self.apples_eaten_this_level += 1

        #snakehead into snake intersection
        for s in self.snake:
            if s == self.snake[0]:
                continue
            if s.intersects(self.snake[0].x, self.snake[0].y, self.snake[0].w, self.snake[0].h):
                #end the game
                self.cur_game_state = GameState.GAME_OVER

        #snake wall intersection

        #debug
        #tx = self.snake[0].x // 8
        #ty = self.snake[0].y // 8
        #tile_value = pyxel.tilemaps[0].pget(tx, ty)  #needed to show value as a tuple ;-;
        #print(f"Snake at ({tx}, {ty}), tile={tile_value}")

        if pyxel.tilemaps[0].pget(self.snake[0].x / 8, self.snake[0].y / 8) == (3,0):
            self.cur_game_state = GameState.GAME_OVER

    def move_apple(self):
        #select new random location for apple
        #make sure its not in a wall or snake
        good_posn = False
        while not good_posn:
            new_x = random.randrange(8, 184, 8)        
            new_y = random.randrange(8, 120, 8)        
            good_posn = True
            #check for collision w snake
            for s in self.snake:
                if (
                    new_x + 8 > s.x
                    and s.x + s.w > new_x
                    and new_y + 8 > s.y
                    and s.y + s.w >new_y
                ):
                    good_posn = False
                    break
            #check for collision w wall 
            
            #if posn is good, move the apple
            if good_posn:
                self.apple.move(new_x, new_y)

    def move_snake(self):
        #change direction???
        if len(self.input_queue) > 0:
            self.snake_direction = self.input_queue.popleft()
        #grow snake??
        if self.sec_to_add > 0:
            self.snake.append(SnakeSec(self.snake[-1].x, self.snake[-1].y))
            self.sec_to_add -= 1
        # move the head
        prev_loc_x = self.snake[0].x
        prev_loc_y = self.snake[0].y
        if self.snake_direction == Direction.RIGHT:
            self.snake[0].x += self.snake[0].w
        if self.snake_direction == Direction.LEFT:
            self.snake[0].x -= self.snake[0].w
        if self.snake_direction == Direction.DOWN:
            self.snake[0].y += self.snake[0].h
        if self.snake_direction == Direction.UP:
            self.snake[0].y -= self.snake[0].h

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
    
    def check_input(self):
        #start new game??
        if self.cur_game_state ==GameState.GAME_OVER:
            if pyxel.btn(pyxel.KEY_SPACE):
                self.start_new_game()
        if pyxel.btn(pyxel.KEY_RIGHT):
            if len(self.input_queue) == 0:
                if self.snake_direction != Direction.LEFT and self.snake_direction != Direction.RIGHT:
                    self.input_queue.append(Direction.RIGHT)
            else:
                if self.input_queue[-1] != Direction.LEFT and self.input_queue[-1] != Direction.RIGHT:
                    self.input_queue.append(Direction.RIGHT)
        elif pyxel.btn(pyxel.KEY_LEFT):
            if len(self.input_queue) == 0:
                if self.snake_direction != Direction.RIGHT and self.snake_direction != Direction.LEFT:
                    self.input_queue.append(Direction.LEFT)
            else:
                if self.input_queue[-1] != Direction.RIGHT and self.input_queue[-1] != Direction.LEFT:
                    self.input_queue.append(Direction.LEFT)
        elif pyxel.btn(pyxel.KEY_DOWN):
            if len(self.input_queue) == 0:
                if self.snake_direction != Direction.UP and self.snake_direction != Direction.DOWN:
                    self.input_queue.append(Direction.DOWN)
            else:
                if self.input_queue[-1] != Direction.UP and self.input_queue[-1] != Direction.DOWN:
                    self.input_queue.append(Direction.DOWN)
        elif pyxel.btn(pyxel.KEY_UP):
            if len(self.input_queue) == 0:
                if self.snake_direction != Direction.DOWN and self.snake_direction != Direction.UP:
                    self.input_queue.append(Direction.UP)
            else:
                if self.input_queue[-1] != Direction.DOWN and self.input_queue[-1] != Direction.UP:
                    self.input_queue.append(Direction.UP)




#kickstarting the program
App()