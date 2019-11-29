from circlegame.characters.polarplaceable import PolarPlaceable


class Player(PolarPlaceable):
    """Class to represent the object that the player controls."""
    def __init__(self, radius_list, radius_level, theta):
        """Create a player object with a HOTPINK color."""
        super().__init__(radius_list, radius_level, theta, "HOTPINK")
