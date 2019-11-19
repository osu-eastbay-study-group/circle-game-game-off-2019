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
        self._max_x_pixel = max_x_pixel
        self._max_y_pixel = max_y_pixel
        self._min_x_pixel = min_x_pixel
        self._min_y_pixel = min_y_pixel

    def cartesian_to_pixel(self, cartesian_pair):
        """
        Converts a given Cartesian ordered pair to corresponding pixel
        coordinates for the window.

        Note that for a window of with even number of pixels for width and
        height the extra pixel will be given to the axis closest to the upper
        left hand corner.

        In particular for a window 2*n pixels wide, allocate
          - n pixels on the negative x-axis
          - 1 pixel for the origin
          - (n - 1) pixels for the positive x-axis

        Similarly for a window 2*m pixels tall, allocate
          - m pixels on the positive y-axis
          - 1 pixel for the origin
          - (m - 1) pixels for negative y-axis.

        Parameters
        ----------
        cartesian_pair : list
            Size 2 list where the first element represents the x coordinate
            and the second element represents the y coordinate. Assumes x and
            y coordinates between

        Returns
        -------
        list
            Size 2 list of the pixel coordinates.
        """
        return [int(cartesian_pair[0]
                    + (self._max_x_pixel + self._min_x_pixel) / 2),
                int(-cartesian_pair[1]
                    + (self._max_y_pixel + self._min_y_pixel) / 2)]


if __name__ == '__main__':
    cc = CoordinateConverter(800, 600)
    cartesian_points = (
        (0, 0),     # Origin
        (-400, 0),  # Most negative x value
        (399, 0),   # Most positive x value
        (0, 300),   # Most positive y value
        (0, -299)   # Most negative y value
    )
    for cartesian_point in cartesian_points:
        print(cc.cartesian_to_pixel(cartesian_point))
