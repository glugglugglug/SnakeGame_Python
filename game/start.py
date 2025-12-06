import pyxel
from game import labels, helpers

def start_menu(self):
    pyxel.cls(labels.Colour.BLACK)

    #drawing the background
    self.u = 1792
    self.v = 0
    self.w = 192
    self.h = 128
    self.tm = 0
    pyxel.bltm(0, 0, self.tm, self.u, self.v, self.w, self.h)

    #the text for the name 
    self.game_name = "SNAKE :3"
    self.game_name_x = helpers.center_text(self.game_name, self.w)
    self.game_name_y = helpers.center_text_y(self.game_name, self.h)
    
    padding = 5
    pyxel.rect(self.game_name_x - padding, self.game_name_y, len(self.game_name) * pyxel.FONT_WIDTH + padding * 2, pyxel.FONT_HEIGHT + padding * 2, labels.Colour.WHITE)
    #shadow ig
    pyxel.rect(self.game_name_x - padding, self.game_name_y + pyxel.FONT_HEIGHT + padding * 2 - 2, len(self.game_name) * pyxel.FONT_WIDTH + padding * 2, 2, labels.Colour.GREY)
    pyxel.rect(self.game_name_x - padding + len(self.game_name) * pyxel.FONT_WIDTH + padding * 2 - 2, self.game_name_y , 2, pyxel.FONT_HEIGHT + padding * 2 , labels.Colour.GREY)
    pyxel.text(self.game_name_x, self.game_name_y + padding, self.game_name, labels.Colour.PINK)

    #pyxel.text(60, 30, "SNAKE GAME", labels.Colour.BLACK)

    pyxel.text(70, 60, "1 - LEVEL 1", pyxel.COLOR_WHITE)
    pyxel.text(70, 75, "2 - LEVEL 2", pyxel.COLOR_WHITE)
    pyxel.text(70, 90, "3 - LEVEL 3", pyxel.COLOR_WHITE)