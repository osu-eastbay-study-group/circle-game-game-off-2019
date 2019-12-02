from circlegame.characters.polarplaceable import PolarPlaceable


class Player(PolarPlaceable):
    """Class to represent the object that the player controls. Collects points during game."""
    def __init__(self, radius_list, radius_index, angle):
        """Create a player object with a YELLOW color."""
        super().__init__(radius_list, radius_index, angle, "YELLOW")
        self._points_collected = 0
        self._moving_left = True
        self._alive = True

    def pick_up_goal(self, goal):
        """
        Adds the parameter's points to the players total points.

        Parameters
        ----------
        goal : Goal
            Object of class Goal.

        Returns
        -------
        None
        """
        self._points_collected += goal.get_points()

    def get_points_collected(self):
        """
        Getter method.
        Returns
        -------
        int
        """
        return self._points_collected

    def is_alive(self):
        """
        Predicate indicating whether the player is alive or not.

        Getter method for _alive member.

        Returns
        -------
        bool
        """
        return self._alive

    def die(self):
        """
        Causes the player today and negates a single point from their score.

        Returns
        -------
        None
        """
        self._alive = False
        if self._points_collected > 0:
            self._points_collected -= 1

    def resurrect(self):
        """
        Changes player alive status back to True.

        Returns
        -------
        None
        """
        self._alive = True

    def renew_point(self):
        self._points_collected = 0

    def is_moving_left(self):
        """
        Predicate indicating whether playing is moving left or right.

        If True then left, otherwise right.

        Returns
        -------
        bool
        """
        return self._moving_left

    def move_left(self):
        """
        Sets _moving_left to True.

        Returns
        -------
        None
        """
        self._moving_left = True

    def move_right(self):
        """
        Sets _moving_left to False.

        Returns
        -------
        None
        """
        self._moving_left = False
