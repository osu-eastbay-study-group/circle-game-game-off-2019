from src.polarplaceable import PolarPlaceable


class Goal(PolarPlaceable):
    """
    Class representing the objects the player must collect to earn points.
    """
    def __init__(self, radius_list, radius_level, theta, color, points=1):
        """Creates a object of type Goal with a point value."""
        super().__init__(radius_list, radius_level, theta, color)
        self._points = points

    def get_points(self):
        return self._points
