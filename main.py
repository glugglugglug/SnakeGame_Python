import pyxel


#class for apple that handles drawing and moving it
#also checks if anything is on apple (snake eating it)
class Apple:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 0, self.w, self.h)
class App:
    #constructor of the class
    def __init__(self):
        scale = 4
        pyxel.init(192, 128, display_scale=scale, capture_scale=scale, title="Snake Game :P", fps=60)
        pyxel.load("assets/resources.pyxres")
        self.apple = Apple(64,32)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        self.apple.draw()


#kickstarting the program
App()