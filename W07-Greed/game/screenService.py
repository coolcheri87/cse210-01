
import pyray
from faller.gem import Gem
from faller.rock import Rock
from player.player import Player


class ScreenService:

    def __init__(self, width, height, fallers):
        self._width = width
        self._height = height+1
        self._sell_size = 20
        self._fallers = fallers

    def close_window(self):
        pyray.close_window()

    def clear_buffer(self):
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
    
    def draw_faller(self, faller, x):
        text = faller.getSymbol()
        y = faller.getHeight()
        pyray.draw_text(text,x,y,12,Color.WHITE)

    def draw_fallers(self, fallers):
        for x in range(0,self.width):
            self.draw_faller(fallers[x],x)

    def flush_buffer(self):
        pyray.end_drawing()

    def get_cell_size(self):
        return self._cell_size

    def get_height(self):
        return self._height

    def is_window_open(self):
        return not pyray.window_should_close()

    def open_window(self):
        pyray.init_window(self._width, self._height, 'Hello')
        pyray.set_target_fps(30)
