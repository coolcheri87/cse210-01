

import pyray

class KeyboardService:

    def __init__(self):
        self._cell_size = 1

    def get_direction(self):
        # Movement
        dx = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
        
        return dx