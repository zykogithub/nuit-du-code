import pyxel as py

class App :
    def __init__(self) -> None:
        py.init(500,500,title="apprentissage",quit_key=py.KEY_BACKSPACE)
        py.run(self.update,self.draw)
    def update():
        pass
    def draw():
        pass


