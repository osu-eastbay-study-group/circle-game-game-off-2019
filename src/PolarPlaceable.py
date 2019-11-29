class PolarPlaceable():
    """
    Class to represent objects in the PyGame window with position given
    with a radius index and a angle (theta).
    """
    def __init__(self, radius_list, radius_level, theta, color):
        """

        Parameters
        ----------
        radius_list : list of float or int
            List of permissible radius levels for the object to be located at.
            Represents the concentric circles of the map.
        radius_level : int
            Index of the current radius the object is located at.
        theta : float or int
            Angle value in the polar coordinate (r, theta).
        color : str
            Color of the circle to draw.
        """
        self._radius_list = radius_list
        self._radius_index = radius_level
        self._theta = theta
        self._color = color

    def get_draw_data(self):
        """
        Provides relevant data for PyGame to draw the object.

        Returns
        -------
        Tuple of (int, float or int, str)
            Index of the radius list, current theta value, and color string.
        """
        return (self._radius_index, self._theta, self._color)

    def get_radius_index(self):
        return self._radius_index

    def get_theta(self):
        return self._theta

    def get_color(self):
        return self._color

    def increment_radius_index(self):
        """
        Increases radius index but not past the max index.

        Returns
        -------
        None
        """
        if self._radius_index < len(self._radius_list) - 1:
            self._radius_index += 1

    def decrement_radius_index(self):
        """
        Decreases radius index but not past the max index.

        Returns
        -------
        None
        """
        if self._radius_index > 0:
            self._radius_index -= 1


if __name__ == "__main__":
    radius_list = [50, 100, 150, 200, 250]
    placeable = PolarPlaceable(radius_list, 1, 45, "HOTPINK")
    print(placeable.get_draw_data())
    print(placeable.get_radius_index(), placeable.get_theta(), placeable.get_color())