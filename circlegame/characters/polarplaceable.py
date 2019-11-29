from circlegame.polarutilities.polarutilities import PolarUtilities as pol_util


class PolarPlaceable():
    """
    Class to represent objects in the PyGame window with position given
    with a radius index and a angle.
    """
    def __init__(self, radius_list, radius_index, angle, color):
        """

        Parameters
        ----------
        radius_list : list of float or int
            List of permissible orbit radii for the object to be located at.
            Represents the concentric circles of the map.
        radius_index : int
            Index of the current radius the object is located at.
        angle : float or int
            Angle value in the polar coordinate (radius, angle).
        color : str
            Color of the circle to draw.
        """
        self._radius_list = radius_list
        self._radius_index = radius_index
        self._angle = angle
        self._color = color

    def get_draw_data(self):
        """
        Provides relevant data for PyGame to draw the object.

        Returns
        -------
        Tuple of (int, float or int, str)
            Index of the radius list, current angle, and color string.
        """
        return (self._radius_index, self._angle, self._color)

    def get_radius_index(self):
        return self._radius_index

    def get_angle(self):
        return self._angle

    def get_color(self):
        return self._color

    def increment_radius_index(self):
        """
        Increases radius index but not past the max index.

        Returns
        -------
        bool
            True if successfully increments. Otherwise False.
        """
        if self._radius_index < len(self._radius_list) - 1:
            self._radius_index += 1
            return True
        return False

    def decrement_radius_index(self):
        """
        Decreases radius index but not past the max index.

        Returns
        -------
        bool
            True if successfully decrements. Otherwise False.
+        """
        if self._radius_index > 0:
            self._radius_index -= 1
            return True
        return False

    def change_angle(self, angle_change):
        """
        Adds a value to the angle and then normalizes afterwards.

        Parameters
        ----------
        angle_change : float or int
            Amount to change the current angle by.

        Returns
        -------
        None
        """
        self._angle += angle_change
        pol_util.normalize_angle(self._angle)

    def is_colliding_with(self, that):
        """
        Checks if the calling placeable occupies the same space as the
        placeable in the parameter.

        Parameters
        ----------
        that : PolarPlaceable

        Returns
        -------
        bool
            True if it collides with the argument, otherwise False.
        """
        radius_this = self._radius_list[self._radius_index]
        radius_that = self._radius_list[that._radius_index]
        dot_pixel_radius = 10
        return (pol_util.get_distance(radius_this, self._angle,
                                      radius_that, that.get_angle())
                < 2 * dot_pixel_radius)

    def __repr__(self):
        return f"{self._radius_index}, {self._angle}, {self._color}"
