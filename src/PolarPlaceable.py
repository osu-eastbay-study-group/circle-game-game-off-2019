class PolarPlaceable():
    def __init__(self, radius_list, radius_level, theta, color):
        self._radius_list = radius_list
        self._radius_index = radius_level
        self._theta = theta
        self._color = color

    def get_draw_data(self):
        return (self._radius_index, self._theta, self._color)

    def get_radius_index(self):
        return self._radius_index

    def get_theta(self):
        return self._theta

    def get_color(self):
        return self._color


if __name__ == "__main__":
    radius_list = [50, 100, 150, 200, 250]
    placeable = PolarPlaceable(radius_list, 1, 45, "HOTPINK")
    print(placeable.get_draw_data())
    print(placeable.get_radius_index(), placeable.get_theta(), placeable.get_color())