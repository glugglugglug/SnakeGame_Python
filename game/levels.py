import pyxel
import random
from game import labels


#stores data for each level
class LevelData:
    def __init__(self, tm_id, tm_u, tm_v, snake, apple, speed):
         self.tm = tm_id
         self.tm_u = tm_u 
         self.tm_v =tm_v 
         self.snake = snake
         self.apple = apple
         self.speed = speed
         self.wall = []
         self.wall_tile = (3,0)
         

#spreadsheet for level info
LEVELS = [
        LevelData(tm_id=0, tm_u =0, tm_v =0, snake= (0,0), apple= (16,0), speed= 1.5),
        LevelData(tm_id=1, tm_u =0, tm_v =0 + 128 * random.randrange(0,4,1), snake= (0,16), apple= (32,16), speed= 1.5),
        LevelData(tm_id=0, tm_u =0, tm_v =0, snake= (0,32), apple= (32,32), speed= 1.5)
]

#handles the levels of a class
class Level:
    def __init__(self, leveldata):
        self.data = leveldata
        self.w = 192
        self.h = 128

    def draw(self):
        pyxel.bltm(0, 0, self.data.tm, self.data.tm_u, self.data.tm_v, self.w, self.h, labels.Colour.BLACK)

                
                
