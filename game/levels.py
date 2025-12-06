import pyxel
from game import labels


#stores data for each level
class LevelData:
    def __init__(self, tm_id, snake, apple, speed):
         self.tm = tm_id
         self.snake = snake
         self.apple = apple
         self.speed = speed

#spreadsheet for level info
LEVELS = [
        LevelData(tm_id=0, snake= (0,0), apple= (16,0), speed= 1.5)
]

#handles the levels of a class
class Level:
    def __init__(self, leveldata):
        self.data = leveldata
        self.w = 192
        self.h = 128

    def draw(self):
        pyxel.bltm(0, 0, self.data.tm, 0, 0, self.w, self.h, labels.Colour.BLACK)