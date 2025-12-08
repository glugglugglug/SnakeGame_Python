import pyxel
from game import labels, helpers


class PauseMenu:
    def __init__(self):
        self.options = ["Resume", 
                        "Restart",
                        "Home",
                        "Info",
                        "Exit"
                        ]
        self.index = 0

    def draw(self, selected_ind):
        self.margins = 20
        self.width = 192 
        self.height = 128
        self.pop_w = (self.width - 2 * self.margins) 
        self.pop_h = (self.height - 2 * self.margins)
        pyxel.rect(self.margins, self.margins, self.pop_w, self.pop_h, labels.Colour.WHITE)
        pyxel.rectb(self.margins, self.margins, self.pop_w, self.pop_h, labels.Colour.GREY)

        
        self.padding = 10
        self.text = self.options[0]
        self.space = helpers.arrange_text_y(self.text,self.pop_h, len(self.options) +1) -2
        self.text_y = self.space + self.margins - 4
        for i in self.options:
            self.text = i
            if len(self.text) == 7:
                self.padding = 4
            elif len(self.text) == 6:
                self.padding = 6
            else:
                self.padding = 10
            self.text_x = helpers.center_text(self.text, self.pop_w) + self.margins
            
            pyxel.rect(self.text_x - self.padding, self.text_y, len(self.text) * pyxel.FONT_WIDTH + self.padding * 2 -2, pyxel.FONT_HEIGHT + 2 , labels.Colour.YELLOW)
            
            #shadow
            if selected_ind == self.options.index(i):
                pyxel.rect(self.text_x - self.padding, self.text_y + pyxel.FONT_HEIGHT + 2, len(self.text) * pyxel.FONT_WIDTH + self.padding * 2 - 2, 1, labels.Colour.LIGHT_BLUE )
                pyxel.rect(self.text_x - self.padding + len(self.text) * pyxel.FONT_WIDTH + self.padding * 2 - 2 -1, self.text_y, 1, pyxel.FONT_HEIGHT + 2, labels.Colour.LIGHT_BLUE )
            else:
                pyxel.rect(self.text_x - self.padding, self.text_y + pyxel.FONT_HEIGHT + 2, len(self.text) * pyxel.FONT_WIDTH + self.padding * 2 - 2, 1, labels.Colour.ORANGE )
                pyxel.rect(self.text_x - self.padding + len(self.text) * pyxel.FONT_WIDTH + self.padding * 2 - 2 -1, self.text_y, 1, pyxel.FONT_HEIGHT + 2, labels.Colour.ORANGE )
            #text
            pyxel.text(self.text_x, self.text_y + 2, self.text, labels.Colour.WHITE)
            self.text_y += self.space + 4

class InfoPopup:
    def __init__(self):
        self.visible = False

    def draw(self, level_data):
        self.margins = 20 
        self.width = 192 
        self.height = 128
        self.pop_w = (self.width - 2 * self.margins) 
        self.pop_h = (self.height - 2 * self.margins)
        pyxel.rect(self.margins, self.margins, self.pop_w, self.pop_h, labels.Colour.YELLOW)
        pyxel.rectb(self.margins, self.margins, self.pop_w, self.pop_h, labels.Colour.ORANGE)

        self.level_info = [
            "a classic implementation of the\nsnake game, with regular\nsprites and rules.\neat more apples\nto gain a higher score.",
            "a play on the name of the game\n'snake and ladders'\nalthough it doesn't have\n much to do with it.\nThe walls placed mid scene\n make it harder to consume apples",
            "a miscallaneous level,\nwith random changes,\n because this is life.\nand life isn't always fair.\ntry your luck at the game of life"
        ]

        self.text = self.level_info[level_data - 1]
        lines = self.text.split("\n")

        total_h = len(lines) * (pyxel.FONT_HEIGHT + 2)
        start_y = self.margins + (self.pop_h - total_h) //2

        self.text_y = start_y
        for i in lines:
            self.text_x = self.margins  + helpers.center_text(i,self.pop_w)
            pyxel.text(self.text_x, self.text_y, i, labels.Colour.WHITE)
            self.text_y += pyxel.FONT_HEIGHT + 2
       
         
