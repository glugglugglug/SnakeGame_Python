import pyxel
from game import helpers, levels, start




# handles drawing text and scores-
class Hud:
    def __init__(self):
        self.title_text = "SnakeGame :P"
        self.page_width = 192
        self.title_text_x = helpers.center_text(self.title_text, self.page_width)
        self.score_text = str(0)
        self.score_text_x = helpers.right_text(self.score_text, self.page_width)
        self.level_text = "lvl 0"
        self.level_text_x = 4
        self.padding = 4
        self.apples_text = "Apples "
        self.apples_text_x = helpers.right_text(self.apples_text, self.page_width)

    def draw_title(self, level):
        levels=[
            "This is SNAKE",
            "This is LADDER",
            "This is LIFE",
        ]
        self.title_text = levels[level-1]
        self.title_text_x = helpers.center_text(self.title_text, self.page_width)
        pyxel.rect(self.title_text_x - self.padding, 0, len(self.title_text) * pyxel.FONT_WIDTH +1 + self.padding * 2, pyxel.FONT_HEIGHT +1, 1)
        pyxel.text(self.title_text_x, 1, self.title_text, 12)

    def draw_score(self, score):
        self.score_text = str(score)
        self.score_text_x = helpers.right_text(self.score_text, 196)
        pyxel.rect(self.score_text_x - 2, 0, len(self.score_text) * pyxel.FONT_WIDTH +1, pyxel.FONT_HEIGHT +1, 1)
        pyxel.text(self.score_text_x -1, 1, self.score_text, 3)

    def draw_level(self, level):
        self.level_text = str(level)
        pyxel.rect(self.level_text_x - self.padding, 0, len(self.level_text) * pyxel.FONT_WIDTH +1 + self.padding - 2, pyxel.FONT_HEIGHT +1, 1)
        pyxel.text(self.level_text_x - self.padding + 2, 1, self.level_text, 3)

    def draw_apples(self, apples):
        self.apples_text = "Apples " + str(apples)
        self.apples_text_x = helpers.right_text(self.apples_text, self.page_width)
        pyxel.rect(self.apples_text_x + 2, 128 - pyxel.FONT_HEIGHT - 2, len(self.apples_text) * pyxel.FONT_WIDTH +1, pyxel.FONT_HEIGHT +1, 1)
        pyxel.text(self.apples_text_x + 3, 1 + 128 - pyxel.FONT_HEIGHT - 2, self.apples_text, 8)