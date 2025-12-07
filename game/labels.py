import pyxel
import enum


#snake direction labels
class Direction(enum.Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


#game state labels
class GameState(enum.Enum):
    RUNNING = 0
    GAME_OVER = 1
    START_MENU = 2
    PAUSE = 3
    INFO = 4


#colour labels
class Colour:
    BLACK = 0
    YELLOW = 10
    WHITE = 7
    PINK = 8
    GREY = 13
    ORANGE = 9
    BLUE = 1
    LIGHT_BLUE = 6
    MID_BLUE = 12
    BROWN = 4
    PEACH = 15
