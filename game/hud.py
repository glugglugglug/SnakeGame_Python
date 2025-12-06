import pyxel
from game import helpers




# handles drawing text and scores-
class Hud:
    def __init__(self):
        self.title_text = "SnakeGame :P"
        self.title_text_x = helpers.center_text(self.title_text,196)
        self.score_text = str(0)
        self.score_text_x = helpers.right_text(self.score_text,196)
        self.level_text = "lvl 0"
        self.level_text_x = 10
        self.apples_text = "Apples "
        self.apples_text_x = len(self.level_text) * pyxel.FONT_WIDTH + self.level_text_x + 10

    def draw_title(self):
        pyxel.rect(self.title_text_x -1, 0, len(self.title_text) * pyxel.FONT_WIDTH +1, pyxel.FONT_HEIGHT +1, 1)
        pyxel.text(self.title_text_x, 1, self.title_text, 12)

    def draw_score(self, score):
        self.score_text = str(score)
        self.score_text_x = helpers.right_text(self.score_text, 196)
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