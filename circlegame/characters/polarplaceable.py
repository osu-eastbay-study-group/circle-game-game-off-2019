from circlegame.polarutilities.polarutilities import PolarUtilities as pol_util


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

    def is_colliding_with(self, that):
        """
        Checks if

        Parameters
        ----------
        that : PolarPlaceable

        Returns
        -------
        bool
            True if it collides with the argument, otherwise False.
        """
        r_this = self._radius_list[self._radius_index]
        r_that = self._radius_list[that._radius_index]
        dot_pixel_radius = 10
        return (pol_util.get_distance(r_this, self._theta,
                                      r_that, that.get_theta())
                < 2 * dot_pixel_radius)
