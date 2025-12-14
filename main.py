import pyxel
from game import labels, levels, snake, apple, hud, controls, start, pause
import time
import collections
import random


class App():
    #constructor of the class
    def __init__(self):
        scale = 3
        self.page_w = 192
        self.page_h = 128
        pyxel.init(self.page_w, self.page_h, display_scale=scale, capture_scale=scale, title="Snake Game :P", fps=60)
        pyxel.load("assets/resources.pyxres")

        #pause var
        self.pause_menu = pause.PauseMenu()
        self.info_pop = pause.InfoPopup()

        #menu selection variables
        self.menu_ind = 0
        self.menu_max = 3

        #quantifying vars score levels apples etc
        self.score = 0
        self.apples_eaten_this_level = 0
        self.apples_eaten_total = 0
        self.cur_level = 1

        self.level_data = levels.LEVELS[self.cur_level - 1]
        

        self.sprite_apple = self.level_data.apple
        self.apple = apple.Apple(64, 32, self.sprite_apple)

        #gamestate variables
        self.cur_game_state = labels.GameState.START_MENU

        #level     
        self.level = levels.Level(self.level_data)

        #texts
        self.hud = hud.Hud()

        #Store the snake sections
        self.sprite_snake = self.level_data.snake
        self.snake = []

        #adding some sections
        self.snake.append(snake.SnakeSec(32, 32, self.level_data.snake, is_head = True))
        self.snake.append(snake.SnakeSec(24, 32, self.level_data.snake))
        self.snake.append(snake.SnakeSec(16, 32, self.level_data.snake))
        
        #setting direction of snake
        self.snake_direction: labels.Direction = labels.Direction.RIGHT

        #sections to add
        self.sec_to_add = 0

        #timing and speed
        self.speed = self.level_data.speed
        self.time_last_frame = time.time()
        self.delta_time = 0
        self.time_since_last_move = 0

        #quantifying vars score levels apples etc
        self.score = 0
        self.apples_eaten_this_level = 0
        self.apples_eaten_total = 0
        self.cur_level = 1

        #level 3 randomizing variables
        self.apple_timeout = random.uniform(4, 9)
        self.apple_timer = 0
        
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
        controls.check_input(self)
    
        #check game state first and then see if its time to move
        if self.cur_game_state == labels.GameState.RUNNING:
            if self.time_since_last_move >= 1 / self.speed:
                self.time_since_last_move = 0
                self.move_snake()
                self.check_collision()
                self.score += len(self.snake) * self.apples_eaten_total + 1

        #for level 3
        self.apple_timer += self.delta_time

        if self.cur_level == 3:
            if int(self.apple_timer) >= self.apple_timeout:
                self.move_apple()
                self.apple_timer = 0
                if random.randrange(1,10,1) % 3 == 0:
                        self.snake.pop()
                elif random.randrange(1,10,1) % 4 == 0:
                        self.sec_to_add += random.randrange(1,4,1)
                elif len(self.snake) > 20 and random.randrange(1,10,1) == 1:
                        while len(self.snake) > 4:
                            self.snake.pop()

                        
    def start_new_game(self):
        self.cur_game_state = labels.GameState.RUNNING
        self.snake.clear()

        self.what_i_drew_last = tuple()

        #Add the initial snake sections again
        self.snake.append(snake.SnakeSec(32, 32, self.sprite_snake, is_head = True, app=self))
        self.snake.append(snake.SnakeSec(24, 32, self.sprite_snake, app=self))
        self.snake.append(snake.SnakeSec(16, 32,self.sprite_snake, app=self))
        self.snake.append(snake.SnakeSec(8,32,self.sprite_snake, app=self))

        #setting direction of snake
        self.snake_direction: labels.Direction = labels.Direction.RIGHT

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


    def start_level(self, level_num):
        self.cur_level = level_num
        self.level_data = levels.LEVELS[level_num - 1]

        self.sprite_snake = self.level_data.snake
        self.sprite_apple = self.level_data.apple

        self.apple.sprite = self.sprite_apple

        self.level = levels.Level(self.level_data)


        self.start_new_game()
        self.cur_game_state = labels.GameState.INFO

    def draw(self):
        
        #drawing start menu
        if self.cur_game_state == labels.GameState.START_MENU:
            start.start_menu(self)
            return
        
        #if game paused-
        if self.cur_game_state ==  labels.GameState.PAUSE:
            self.pause_menu.draw(self.pause_menu.index)
            return
        
        #info pop up
        if self.cur_game_state == labels.GameState.INFO:
            self.info_pop.draw(self.cur_level)
            return  
         
        #if game over
        if self.cur_game_state == labels.GameState.GAME_OVER:
            self.hud.draw_game_over()
            return
        
        #if game is running
        pyxel.cls(labels.Colour.BLACK)
        pyxel.bltm(0, 0, 0, 192 * 8, 0, self.page_w, self.page_h)
        self.level.draw()
        #self.level.get_wall_coords()
        self.apple.draw()
        
        #going through each peice of snake and drawing them
        for s in self.snake:
            s.draw(self.snake_direction)

        #draw title and other text
        self.hud.draw_title(self.cur_level)
        self.hud.draw_score(self.score)
        self.hud.draw_level(self.cur_level)
        self.hud.draw_apples(self.apples_eaten_total)

        #show game over _ debug
        # pyxel.text(10, 114, str(self.cur_game_state), 12)


    def handle_pause(self):
        choice = self.pause_menu.index

        if choice == 0:
            self.cur_game_state = labels.GameState.RUNNING
        elif choice == 1:
            self.start_new_game()
        elif choice == 2:
            self.cur_game_state = labels.GameState.START_MENU
        elif choice == 3:
            self.cur_game_state = labels.GameState.INFO
        elif choice == 4:
            pyxel.quit()



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
                self.cur_game_state = labels.GameState.GAME_OVER

        #snake wall intersection

        #debug
        #tx = self.snake[0].x // 8
        #ty = self.snake[0].y // 8
        #tile_value = pyxel.tilemaps[0].pget(tx, ty)  #needed to show value as a tuple ;-;
        #print(f"Snake at ({tx}, {ty}), tile={tile_value}")

        if pyxel.tilemaps[self.cur_level - 1].pget(self.snake[0].x / 8, self.snake[0].y / 8) == (3,0):
            self.cur_game_state = labels.GameState.GAME_OVER

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
            if pyxel.tilemaps[self.cur_level - 1].pget(new_x / 8, new_y / 8) == (3,0):
                good_posn = False
            
            #if posn is good, move the apple
            if good_posn:
                self.apple.move(new_x, new_y)

    def move_snake(self):
        #change direction???
        if len(self.input_queue) > 0:
            self.snake_direction = self.input_queue.popleft()
        #grow snake??
        if self.sec_to_add > 0:
            self.snake.append(snake.SnakeSec(self.snake[-1].x, self.snake[-1].y, self.sprite_snake, app=self))
            self.sec_to_add -= 1
        # move the head
        prev_loc_x = self.snake[0].x
        prev_loc_y = self.snake[0].y
        if self.snake_direction == labels.Direction.RIGHT:
            self.snake[0].x += self.snake[0].w
        if self.snake_direction == labels.Direction.LEFT:
            self.snake[0].x -= self.snake[0].w
        if self.snake_direction == labels.Direction.DOWN:
            self.snake[0].y += self.snake[0].h
        if self.snake_direction == labels.Direction.UP:
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

        #tracking direction
        for i in range(len(self.snake)):
            if i > 0:
                delta_x = self.snake[i].x - self.snake[i-1].x
                delta_y = self.snake[i].y - self.snake[i-1].y
                self.snake[i].prev_dir = self._dir_from_delta(delta_x, delta_y)
            if i < len(self.snake) -1:
                delta_x = self.snake[i+1].x - self.snake[i].x
                delta_y = self.snake[i+1].y - self.snake[i].y
                self.snake[i].next_dir = self._dir_from_delta(delta_x, delta_y)

    
    def _dir_from_delta(self, dx, dy):
        if dx > 0: return labels.Direction.RIGHT
        if dx < 0: return labels.Direction.LEFT
        if dy > 0: return labels.Direction.DOWN
        if dy < 0: return labels.Direction.UP
        return None
    




#kickstarting the program
App()