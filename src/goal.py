from src.polarplaceable import PolarPlaceable


class Goal(PolarPlaceable):
    def __init__(self, radius_list, radius_level, theta, color, points=1):
        super().__init__(radius_list, radius_level, theta, color)
        self._points = points

    def get_points(self):
        return self._points
