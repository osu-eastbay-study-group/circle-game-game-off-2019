from circlegame.characters.polarplaceable import PolarPlaceable


class Player(PolarPlaceable):
    """Class to represent the object that the player controls. Collects points during game."""
    def __init__(self, radius_list, radius_index, angle):
        """Create a player object with a HOTPINK color."""
        super().__init__(radius_list, radius_index, angle, "YELLOW")
        self._points_collected = 0
        self._moving_left = True
        self._alive = True

    def pick_up_goal(self, goal):
        self._points_collected += goal.get_points()

    def get_points_collected(self):
        return self._points_collected

    def is_alive(self):
        return self._alive

    def die(self):
        self._alive = False
        if self._points_collected > 0:
            self._points_collected -= 1

    def resurrect(self):
        self._alive = True

    def renew_point(self):
        self._points_collected = 0

    def is_moving_left(self):
        return self._moving_left

    def move_left(self):
        self._moving_left = True

    def move_right(self):
        self._moving_left = False
