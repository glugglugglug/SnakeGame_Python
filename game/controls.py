import pyxel
from game import labels

    

def check_input(self):
        #start menu controls
        if self.cur_game_state == labels.GameState.START_MENU:
            if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S) \
            or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_A):
                self.menu_ind = (self.menu_ind + 1) % self.menu_max
            if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W) \
            or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_Y):
                self.menu_ind = (self.menu_ind - 1) % self.menu_max
            if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_START):
                self.start_level(self.menu_ind + 1) 
            return

        #pause menu controls
        if pyxel.btnp(pyxel.KEY_P) or pyxel.btnp(pyxel.KEY_BACKSPACE) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_GUIDE):
            if self.cur_game_state == labels.GameState.RUNNING:
                self.cur_game_state = labels.GameState.PAUSE
            elif self.cur_game_state == labels.GameState.PAUSE:
                self.cur_game_state = labels.GameState.RUNNING
            return

        #if paused
        if self.cur_game_state == labels.GameState.PAUSE:
            if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S) \
            or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_A):
                self.pause_menu.index = (self.pause_menu.index + 1) % len(self.pause_menu.options)
            if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W) \
            or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_Y):
                self.pause_menu.index = (self.pause_menu.index - 1) % len(self.pause_menu.options)
            if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_START):
                self.handle_pause()
            return

        #info screen control
        if self.cur_game_state == labels.GameState.INFO:
            if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.KEY_X) or \
                  pyxel.btn(pyxel.GAMEPAD1_BUTTON_GUIDE) or pyxel.btnp(pyxel.KEY_BACKSPACE) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_START) :
                self.cur_game_state = labels.GameState.RUNNING
            return
        
        #start new game??
        if self.cur_game_state == labels.GameState.GAME_OVER:
            if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_START):
                self.start_new_game()
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D) \
            or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_B):
            if len(self.input_queue) == 0:
                if self.snake_direction != labels.Direction.LEFT and self.snake_direction != labels.Direction.RIGHT:
                    self.input_queue.append(labels.Direction.RIGHT)
            else:
                if self.input_queue[-1] != labels.Direction.LEFT and self.input_queue[-1] != labels.Direction.RIGHT:
                    self.input_queue.append(labels.Direction.RIGHT)
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A) \
            or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_X):
            if len(self.input_queue) == 0:
                if self.snake_direction != labels.Direction.RIGHT and self.snake_direction != labels.Direction.LEFT:
                    self.input_queue.append(labels.Direction.LEFT)
            else:
                if self.input_queue[-1] != labels.Direction.RIGHT and self.input_queue[-1] != labels.Direction.LEFT:
                    self.input_queue.append(labels.Direction.LEFT)
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S) \
            or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_A):
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