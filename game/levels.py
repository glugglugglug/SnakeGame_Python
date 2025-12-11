import pyxel
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
        LevelData(tm_id=1, tm_u =0, tm_v =0, snake= (0,16), apple= (32,16), speed= 1.5),
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


    """
    def get_wall_coords(self):
        self.tm_width = self.data.tm_u + self.w
        self.tm_height = self.data.tm_v + self.h

        for i in range(self.data.tm_u, self.tm_width):
            for j in range(self.data.tm_v, self.tm_height):
                tile = pyxel.tilemaps[0].pget(i, j)
                print(type(tile))
                col_tile = pyxel.images[0].pget(tile[0]*8, tile[1]*8)
                

                if tile == self.data.wall_tile:
                    self.data.wall.append((i,j))

        print(self.data.wall)
    """
                
                
