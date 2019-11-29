from circlegame.characters.polarplaceable import PolarPlaceable


class Player(PolarPlaceable):
    """Class to represent the object that the player controls. Collects points during game."""
    def __init__(self, radius_list, radius_level, theta):
        """Create a player object with a HOTPINK color."""
        super().__init__(radius_list, radius_level, theta, "HOTPINK")
        self._points_collected = 0

    def get_points_collected(self):
        return self._points_collected
