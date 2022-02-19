

import pyray

class KeyboardService:

    def get_direction(self):
        # Movement
        dx = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
        
        return dx