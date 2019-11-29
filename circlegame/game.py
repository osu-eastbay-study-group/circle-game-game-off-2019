import pygame
from circlegame.polarutilities.coordinateconverter import CoordinateConverter
import random
import circlegame.characters.goal
import circlegame.characters.killer
import circlegame.characters.player


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
        self.goals = self.setup_goals()
        self.killers = self.setup_killers()
        self.player = self.setup_player()

    def setup_orbits(self):
        smaller_dimension = min(self.screen.get_width(), self.screen.get_height())
        orbit_spacing = 50  # number of pixels
        orbit_count = (smaller_dimension // 2) // orbit_spacing
        return [orbit_spacing * i for i in range(1, orbit_count)]

    def setup_goals(self):
        goal_count = len(self.radius_list)  # 1 goal per orbit
        # TODO: Set up points to be proportional to difficulty of orbit
        return [circlegame.characters.goal.Goal(self.radius_list,
                                                i,
                                                random.randint(0, 359)) for i in range(goal_count)]

    def setup_killers(self):
        killer_count = len(self.radius_list)  # 1 goal per orbit
        return [circlegame.characters.killer.Killer(self.radius_list,
                                                    i,
                                                    random.randint(0, 359)) for i in range(killer_count)]

    def setup_player(self):
        """
        Must be called after setup_killers() not before.
        """
        radius_index = len(self.radius_list) - 1

        # Place on opposite side of killer as not to get killed immediately when spawned.
        theta = self.killers[radius_index].get_theta() - 180

        return circlegame.characters.player.Player(self.radius_list, radius_index, theta)

    def start(self):
        while not self.game_over:
            self.listen_for_events()

            self.move_killers()


            self.screen_set()      # make sure to be the first thing to display
            self.display_orbits()  # draw the orbits over the screens
            self.display_characters()
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


    def move_killers(self):
        for killer in self.killers:
            killer.change_theta(5)

    def screen_set(self):
        self.screen.blit(self.wallpaper_img, self.wallpaper_img.get_rect())

    def display_orbits(self):
        for r in self.radius_list:
            for theta in range(360):
                pygame.draw.circle(self.screen, WHITE, self.converter.polar_to_pixel((r, theta)), 1)

    def display_characters(self):
        for character in self.goals + self.killers + [self.player]:
            radius_index, theta, color_key = character.get_draw_data()
            print(radius_index, theta, color_key)
            r = self.radius_list[radius_index]
            pygame.draw.circle(self.screen, colors[color_key],
                               self.converter.polar_to_pixel((r, theta)), 10)
