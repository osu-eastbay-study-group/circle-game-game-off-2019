import math


class PolarUtilities:
    @staticmethod
    def normalize_angle(angle, start=0, end=360):
        """
        Normalize a value to a given periodic range, assuming the range wraps
        around (like 360 degrees back to zero degrees)

        Parameters
        ----------
        angle : float or int
        start : float or int
            Beginning of the periodic range.
        end : float or int
            Last value of the period range. Assumes start and end are the same
            value if the range wraps around (e.g. 0 and 360 degrees)

        Returns
        -------
        float
            The given value normalized back to fall within the original range.
        """
        width = end - start
        offset_value = angle - start
        return (offset_value - (math.floor(offset_value / width) * width)) + start

    @staticmethod
    def get_distance(radius_1, angle_1, radius_2, angle_2):
        """
        Compute the distance between two points.
        Parameters
        ----------
        radius_1 : float
        angle_1 : float
        radius_2 : float
        angle_2 : float

        Returns
        -------
        float
            Distance between the two points.
        """
        return math.sqrt(radius_1 ** 2 + radius_2 ** 2
                         - (2 * radius_1 * radius_2 * math.cos((angle_1 - angle_2)
                                                               * math.pi / 180)))
