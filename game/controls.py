import pyxel
from game import labels

def check_input(self):
        #start menu controls
        if self.cur_game_state == labels.GameState.START_MENU:
            if pyxel.btnp(pyxel.KEY_1):
                self.start_level(1)
            if pyxel.btnp(pyxel.KEY_2):
                self.start_level(2)
            if pyxel.btnp(pyxel.KEY_3):
                self.start_level(3)
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.menu_ind = (self.menu_ind + 1) % self.menu_max
            if pyxel.btnp(pyxel.KEY_UP):
                self.menu_ind = (self.menu_ind - 1) % self.menu_max
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.start_level(self.menu_ind + 1) 


            return
        #start new game??
        if self.cur_game_state == labels.GameState.GAME_OVER:
            if pyxel.btn(pyxel.KEY_SPACE):
                self.start_new_game()
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            if len(self.input_queue) == 0:
                if self.snake_direction != labels.Direction.LEFT and self.snake_direction != labels.Direction.RIGHT:
                    self.input_queue.append(labels.Direction.RIGHT)
            else:
                if self.input_queue[-1] != labels.Direction.LEFT and self.input_queue[-1] != labels.Direction.RIGHT:
                    self.input_queue.append(labels.Direction.RIGHT)
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
            if len(self.input_queue) == 0:
                if self.snake_direction != labels.Direction.RIGHT and self.snake_direction != labels.Direction.LEFT:
                    self.input_queue.append(labels.Direction.LEFT)
            else:
                if self.input_queue[-1] != labels.Direction.RIGHT and self.input_queue[-1] != labels.Direction.LEFT:
                    self.input_queue.append(labels.Direction.LEFT)
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            if len(self.input_queue) == 0:
                if self.snake_direction != labels.Direction.UP and self.snake_direction != labels.Direction.DOWN:
                    self.input_queue.append(labels.Direction.DOWN)
            else:
                if self.input_queue[-1] != labels.Direction.UP and self.input_queue[-1] != labels.Direction.DOWN:
                    self.input_queue.append(labels.Direction.DOWN)
        elif pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W):
            if len(self.input_queue) == 0:
                if self.snake_direction != labels.Direction.DOWN and self.snake_direction != labels.Direction.UP:
                    self.input_queue.append(labels.Direction.UP)
            else:
                if self.input_queue[-1] != labels.Direction.DOWN and self.input_queue[-1] != labels.Direction.UP:
                    self.input_queue.append(labels.Direction.UP)