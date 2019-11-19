class CoordinateConverter:
    """
    Class to do coordinate conversions for a given PyGame window.
    """

    def __init__(self, max_x_pixel, max_y_pixel, min_x_pixel=0, min_y_pixel=0):
        """
        Create a CoordinateConverter object for a region of a window given
        specific dimensions.

        Parameters
        ----------
        max_x_pixel : int
            The maximum pixel in the x direction. If min_x_pixel is 0 then this
            is just the length of the window. Must be a positive integer.
        max_y_pixel : int
            The maximum pixel in the y direction. If min_y_pixel is 0 then this
            is just the height of the window. Must be a positive integer.
        min_x_pixel : int
            The minimum pixel in the x direction. If representing the entire
            window this should be 0.
        min_y_pixel : int
            The minimum pixel in the y direction. If representing the entire
            window this should be 0.
        """
        self._window_x_max = max_x_pixel
        self._window_y_max = max_y_pixel
        self._window_x_min = min_x_pixel
        self._window_y_min = min_y_pixel