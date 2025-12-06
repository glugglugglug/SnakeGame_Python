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


#colour labels
class Colour:
    BLACK = 0
    YELLOW = 10