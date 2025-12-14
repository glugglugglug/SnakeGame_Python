import pyxel
from game import labels, helpers
def draw_2boxtext(self, level_name, level_num, padding, shadow_col, back_col, text_col):

    highlight = labels.Colour.MID_BLUE

    #number box
    pyxel.rect(self.first_x - padding, self.first_y, len(str(level_num)) * pyxel.FONT_WIDTH + padding * 2 + 2, pyxel.FONT_HEIGHT + padding * 2, back_col)
    #shadow for box
    if self.menu_ind == level_num -1:
        pyxel.rect(self.first_x - padding, self.first_y + pyxel.FONT_HEIGHT + padding * 2 - 2, len(str(level_num)) * pyxel.FONT_WIDTH + padding * 2, 2, highlight)
        pyxel.rect(self.first_x - padding + len(str(level_num)) * pyxel.FONT_WIDTH + padding * 2 - 2 + 2, self.first_y, 2, pyxel.FONT_HEIGHT + padding * 2, highlight)
        pyxel.text(self.first_x + 1, self.first_y + padding, str(level_num), highlight)
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
        pyxel.text(self.first_text_x + 1, self.first_y + padding, level_name, highlight)
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
    shadow_col_title = labels.Colour.MID_BLUE
    back_col_title = labels.Colour.WHITE
    text_col_title = shadow_col_title
    pyxel.rect(self.game_name_x - padding, self.game_name_y, len(self.game_name) * pyxel.FONT_WIDTH + padding * 2, pyxel.FONT_HEIGHT + padding * 2, back_col_title)
    #shadow ig
    pyxel.rect(self.game_name_x - padding, self.game_name_y + pyxel.FONT_HEIGHT + padding * 2 - 2, len(self.game_name) * pyxel.FONT_WIDTH + padding * 2, 2, shadow_col_title)
    pyxel.rect(self.game_name_x - padding + len(self.game_name) * pyxel.FONT_WIDTH + padding * 2 - 2, self.game_name_y, 2, pyxel.FONT_HEIGHT + padding * 2 , shadow_col_title)
    pyxel.text(self.game_name_x, self.game_name_y + padding, self.game_name, text_col_title)


    #level buttons
    padding = 5 
    shadow_col = labels.Colour.BLUE
    back_col = labels.Colour.WHITE
    #text_col = labels.Colour.WHITE
    text_col = shadow_col
    self.space_bw_y = 20
    self.level_1 = "This is SNAKE "
    self.level_2 = "This is LADDER"
    self.level_3 = "This is LIFE  "

    self.first_x = helpers.center_text(self.level_1, self.w) - 17
    self.first_y = helpers.arrange_text_y(self.level_1, self.h, 8) * 3

    draw_2boxtext(self, self.level_1, 1, padding, shadow_col, back_col, text_col)

    #second button</3
    self.first_y += self.space_bw_y

    draw_2boxtext(self, self.level_2, 2, padding, shadow_col, back_col, text_col)

    #third button ;-;
    self.first_y += self.space_bw_y

    draw_2boxtext(self, self.level_3, 3, padding, shadow_col, back_col, text_col)
