from circlegame.characters.polarplaceable import PolarPlaceable


class Player(PolarPlaceable):
    """Class to represent the object that the player controls. Collects points during game."""
    def __init__(self, radius_list, radius_level, theta):
        """Create a player object with a HOTPINK color."""
        super().__init__(radius_list, radius_level, theta, "HOTPINK")
        self._points_collected = 0
        self.moving_left = False

    def get_points_collected(self):
        return self._points_collected

    def is_moving_left(self):
        return self.moving_left

    def move_left(self):
        self.moving_left = True

    def move_right(self):
        self.moving_left = False