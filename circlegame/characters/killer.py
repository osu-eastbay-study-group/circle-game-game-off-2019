from circlegame.characters.polarplaceable import PolarPlaceable
import random


class Killer(PolarPlaceable):
    """Represents the characters that can attack the player."""
    def __init__(self, radius_list, radius_index, angle):
        super().__init__(radius_list, radius_index, angle, "RED")
        self._moving_left = random.choice((True, False))

    def is_moving_left(self):
        return self._moving_left

    def move_left(self):
        self._moving_left = True

    def move_right(self):
        self._moving_left = False
