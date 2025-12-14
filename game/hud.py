import pyxel
from game import helpers, labels, levels, start




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
        pyxel.rect(self.title_text_x - self.padding, 0, len(self.title_text) * pyxel.FONT_WIDTH +1 + self.padding * 2, pyxel.FONT_HEIGHT +1, labels.Colour.WHITE)
        pyxel.text(self.title_text_x, 1, self.title_text, labels.Colour.MID_BLUE)

    def draw_score(self, score):
        self.score_text = str(score)
        self.score_text_x = helpers.right_text(self.score_text, 196)
        pyxel.rect(self.score_text_x - 2, 0, len(self.score_text) * pyxel.FONT_WIDTH +1, pyxel.FONT_HEIGHT +1, labels.Colour.WHITE)
        pyxel.text(self.score_text_x -1, 1, self.score_text, labels.Colour.FANTA)

    def draw_level(self, level):
        self.level_text = str(level)
        pyxel.rect(self.level_text_x - self.padding, 0, len(self.level_text) * pyxel.FONT_WIDTH +1 + self.padding - 2, pyxel.FONT_HEIGHT +1, labels.Colour.WHITE)
        pyxel.text(self.level_text_x - self.padding + 2, 1, self.level_text, labels.Colour.FANTA)

    def draw_apples(self, apples):
        self.apples_text = "Apples " + str(apples)
        self.apples_text_x = helpers.right_text(self.apples_text, self.page_width)
        pyxel.rect(self.apples_text_x + 2, 128 - pyxel.FONT_HEIGHT - 2, len(self.apples_text) * pyxel.FONT_WIDTH +1, pyxel.FONT_HEIGHT +1, labels.Colour.WHITE)
        pyxel.text(self.apples_text_x + 3, 1 + 128 - pyxel.FONT_HEIGHT - 2, self.apples_text, labels.Colour.FANTA)
        
    def draw_game_over(self):
        self.gameover_text = "GAME OVER - SPACE TO START AGAIN"
        self.margins = 20
        self.width = 192 - 2 * self.margins
        self.height = 128 - 2 * self.margins
        self.gameover_text_x = helpers.center_text(self.gameover_text, self.width) + self.margins
        self.gameover_text_y = helpers.arrange_text_y(self.gameover_text_x, self.height, 2) + self.margins
        pyxel.rect(self.gameover_text_x -1, self.gameover_text_y -1, len(self.gameover_text) * pyxel.FONT_WIDTH +1, pyxel.FONT_HEIGHT +1, labels.Colour.BLUE)
        pyxel.text(self.gameover_text_x, self.gameover_text_y, self.gameover_text, labels.Colour.WHITE)