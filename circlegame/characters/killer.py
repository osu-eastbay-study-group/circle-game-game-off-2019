from circlegame.characters.polarplaceable import PolarPlaceable


class Killer(PolarPlaceable):
    """Represents the characters that can attack the player."""
    def __init__(self, radius_list, radius_level, theta):
        super().__init__(radius_list, radius_level, theta, "RED")

