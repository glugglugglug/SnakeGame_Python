import pyxel


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
    def __init__(self):
        self.tm = 0
        self.u = 0
        self.v = 0
        self.w = 192
        self.h = 128

    def draw(self):
        pyxel.bltm(0, 0, self.tm, self.u, self.v, self.w, self.h)