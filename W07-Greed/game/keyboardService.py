
import pyray

class KeyboardService:

    def get_direction(self):
        # Movement
        dx = 0
        x = pyray.get_key_pressed()

        if (x > 0):

            if (x == pyray.KEY_LEFT):
                dx = -1
            
            if (x ==pyray.KEY_RIGHT):
                dx = 1
        
        return dx

