import pyxel
from game import labels, helpers
def draw_2boxtext(self, level_name, level_num, padding, shadow_col, back_col, text_col):

    highlight = labels.Colour.WHITE

    #number box
    pyxel.rect(self.first_x - padding, self.first_y, len(str(level_num)) * pyxel.FONT_WIDTH + padding * 2 + 2, pyxel.FONT_HEIGHT + padding * 2, back_col)
    #shadow for box
    if self.menu_ind == level_num -1:
        pyxel.rect(self.first_x - padding, self.first_y + pyxel.FONT_HEIGHT + padding * 2 - 2, len(str(level_num)) * pyxel.FONT_WIDTH + padding * 2, 2, highlight)
        pyxel.rect(self.first_x - padding + len(str(level_num)) * pyxel.FONT_WIDTH + padding * 2 - 2 + 2, self.first_y, 2, pyxel.FONT_HEIGHT + padding * 2, highlight)
    else:
        pyxel.rect(self.first_x - padding, self.first_y + pyxel.FONT_HEIGHT + padding * 2 - 2, len(str(level_num)) * pyxel.FONT_WIDTH + padding * 2, 2, shadow_col)
        pyxel.rect(self.first_x - padding + len(str(level_num)) * pyxel.FONT_WIDTH + padding * 2 - 2 + 2, self.first_y, 2, pyxel.FONT_HEIGHT + padding * 2, shadow_col)
    pyxel.text(self.first_x + 1, self.first_y + padding, str(level_num), text_col)


    #text box
    self.first_text_x = self.first_x + 30

    pyxel.rect(self.first_text_x - padding, self.first_y, len(level_name) * pyxel.FONT_WIDTH + padding * 2 + 2, pyxel.FONT_HEIGHT + padding * 2, back_col)
    #shadow for box
    if self.menu_ind == level_num -1:
        pyxel.rect(self.first_text_x - padding, self.first_y + pyxel.FONT_HEIGHT + padding * 2 - 2, len(level_name) * pyxel.FONT_WIDTH + padding * 2, 2, highlight)
        pyxel.rect(self.first_text_x - padding + len(level_name) * pyxel.FONT_WIDTH + padding * 2 - 2 + 2, self.first_y, 2, pyxel.FONT_HEIGHT + padding * 2, highlight)
    else:
         pyxel.rect(self.first_text_x - padding, self.first_y + pyxel.FONT_HEIGHT + padding * 2 - 2, len(level_name) * pyxel.FONT_WIDTH + padding * 2, 2, shadow_col)
         pyxel.rect(self.first_text_x - padding + len(level_name) * pyxel.FONT_WIDTH + padding * 2 - 2 + 2, self.first_y, 2, pyxel.FONT_HEIGHT + padding * 2, shadow_col)
    pyxel.text(self.first_text_x + 1, self.first_y + padding, level_name, text_col)


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
    self.game_name_y = helpers.arrange_text_y(self.game_name, self.h, 6) 
    
    padding = 5
    pyxel.rect(self.game_name_x - padding, self.game_name_y, len(self.game_name) * pyxel.FONT_WIDTH + padding * 2, pyxel.FONT_HEIGHT + padding * 2, labels.Colour.LIGHT_BLUE)
    #shadow ig
    pyxel.rect(self.game_name_x - padding, self.game_name_y + pyxel.FONT_HEIGHT + padding * 2 - 2, len(self.game_name) * pyxel.FONT_WIDTH + padding * 2, 2, labels.Colour.MID_BLUE)
    pyxel.rect(self.game_name_x - padding + len(self.game_name) * pyxel.FONT_WIDTH + padding * 2 - 2, self.game_name_y, 2, pyxel.FONT_HEIGHT + padding * 2 , labels.Colour.MID_BLUE)
    pyxel.text(self.game_name_x, self.game_name_y + padding, self.game_name, labels.Colour.WHITE)

    #pyxel.text(60, 30, "SNAKE GAME", labels.Colour.BLACK)

    #level buttons

    shadow_col = labels.Colour.ORANGE
    back_col = labels.Colour.YELLOW
    text_col = labels.Colour.WHITE
    self.space_bw_y = 20
    self.level_1 = "This is SNAKE"
    self.level_2 = "This is LADDER"
    self.level_3 = "This is LIFE"

    self.first_x = helpers.center_text(self.level_1, self.w) - 17
    self.first_y = helpers.arrange_text_y(self.level_1, self.h, 8) * 3

    """
    pyxel.rect(self.first_x - padding, self.first_y, len("1") * pyxel.FONT_WIDTH + padding * 2 + 2, pyxel.FONT_HEIGHT + padding * 2, back_col)
    #shadow for box
    if self.menu_ind == 0:
        pyxel.rect(self.first_x - padding, self.first_y + pyxel.FONT_HEIGHT + padding * 2 - 2, len("1") * pyxel.FONT_WIDTH + padding * 2, 2, labels.Colour.WHITE)
        pyxel.rect(self.first_x - padding + len("1") * pyxel.FONT_WIDTH + padding * 2 - 2 + 2, self.first_y, 2, pyxel.FONT_HEIGHT + padding * 2, labels.Colour.WHITE)
    else:
        pyxel.rect(self.first_x - padding, self.first_y + pyxel.FONT_HEIGHT + padding * 2 - 2, len("1") * pyxel.FONT_WIDTH + padding * 2, 2, shadow_col)
        pyxel.rect(self.first_x - padding + len("1") * pyxel.FONT_WIDTH + padding * 2 - 2 + 2, self.first_y, 2, pyxel.FONT_HEIGHT + padding * 2, shadow_col)
    pyxel.text(self.first_x + 1, self.first_y + padding, "1", text_col)
    """

    draw_2boxtext(self, self.level_1, 1, padding, shadow_col, back_col, text_col)

    #second button</3
    self.first_y += self.space_bw_y

    draw_2boxtext(self, self.level_2, 2, padding, shadow_col, back_col, text_col)

    #third button ;-;
    self.first_y += self.space_bw_y

    draw_2boxtext(self, self.level_3, 3, padding, shadow_col, back_col, text_col)


    #pyxel.text(70, 60, "1 - LEVEL 1", pyxel.COLOR_WHITE)
    #pyxel.text(70, 75, "2 - LEVEL 2", pyxel.COLOR_WHITE)
    #pyxel.text(70, 90, "3 - LEVEL 3", pyxel.COLOR_WHITE)