
import pyray as pr
import sys
sys.path.append('..')
from faller.gem import Gem
from faller.rock import Rock
from player.player import Player


class ScreenService:

    def __init__(self, width, height, fallers):
        self._width = width
        self._height = height+1
        self._cell_size = 20
        self._fallers = fallers

    def close_window(self):
        pr.close_window()

    def clear_buffer(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
    
    def draw_faller(self, faller, x):
        text = faller.getSymbol()
        y = faller.getHeight()
        pr.draw_text(text,x,y,self._cell_size,pr.WHITE)

    def draw_fallers(self, fallers):
        for x in range(0,self._width):
            self.draw_faller(fallers[x],x)

    def draw_player(self, player):
        pr.draw_text(player.getSymbol(),player.getX(),self._height,self._cell_size,pr.YELLOW)

    def flush_buffer(self):
        pr.end_drawing()

    def get_cell_size(self):
        return self._cell_size

    def get_height(self):
        return self._height

    def is_window_open(self):
        return not pr.window_should_close()

    def open_window(self):
        pr.init_window(self._width, self._height, 'Hello')
        pr.set_target_fps(30)
