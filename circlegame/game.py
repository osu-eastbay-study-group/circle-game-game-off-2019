import pygame
from circlegame.polarutilities.coordinateconverter import CoordinateConverter

BLACK, WHITE, RED, \
GREEN, BLUE, HOTPINK = (0, 0, 0), (255, 255, 255), (255, 0, 0), \
                       (0, 255, 0), (0, 0, 255), (255, 105, 180)

colors = {"BLACK": (0, 0, 0),
          "WHITE": (255, 255, 255),
          "RED": (255, 0, 0),
          "GREEN": (0, 255, 0),
          "BLUE": (0, 0, 255),
          "HOTPINK": (255, 105, 180)}


class Game:
    def __init__(self, screen, clock, wallpaper_path):
        self.screen = screen
        self.clock = clock
        self.converter = CoordinateConverter(screen.get_width(), screen.get_height())
        self.game_over = False
        self.wallpaper_img = pygame.image.load(wallpaper_path)

        self.radius_list = self.setup_orbits()
        print(self.radius_list)
        # self.player = circlegame.characters.player.Player()

    def setup_orbits(self):
        smaller_dimension = min(self.screen.get_width(), self.screen.get_height())
        orbit_spacing = 50  # number of pixels
        orbit_count = (smaller_dimension // 2) // orbit_spacing
        return [orbit_spacing * i for i in range(1, orbit_count)]

    def start(self):
        while not self.game_over:
            self.listen_for_events()

            self.screen_set()      # make sure to be the first thing to display
            self.display_orbits()  # draw the orbits over the screens
            # TODO: draw the circles over the orbits
            pygame.display.flip()
            self.clock.tick(30)

    def listen_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_UP:
                    pass

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    pass
                if event.key in (pygame.K_DOWN, pygame.K_UP):
                    pass

    def screen_set(self):
        self.screen.blit(self.wallpaper_img, self.wallpaper_img.get_rect())

    def display_orbits(self):
        for r in self.radius_list:
            for theta in range(360):
                pygame.draw.circle(self.screen, WHITE, self.converter.polar_to_pixel((r, theta)), 1)