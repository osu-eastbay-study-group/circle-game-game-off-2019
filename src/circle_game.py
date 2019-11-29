import pygame
from coordinateconverter import CoordinateConverter

BLACK, WHITE, RED, GREEN, BLUE = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)

class CircleGame:
    def __init__(self):

        self.display_width = 800
        self.display_height = 600
        self.title = 'Circle Game'
        pygame.display.set_caption(self.title)

    def screen_set(self):
        self.screen = pygame.display.set_mode((self.display_width, self.display_height))
        self.space_img = pygame.image.load('../img/space_img.jpg')
        self.screen.blit(self.space_img, self.space_img.get_rect())

    def display_player(self, x_pixel, y_pixel):
        self.x_pixel = x_pixel
        self.y_pixel = y_pixel
        self.player = pygame.draw.circle(self.screen, BLUE, (self.x_pixel, self.y_pixel), 10)

    def convert_dot(self, pygame, clock):
        self.pygame, self.clock = pygame, clock
        self.r, self.theta, self.r_change, self.theta_change = 0, 0, 0, 0
        self.converter = CoordinateConverter(self.display_width, self.display_height)
        self.exit = False

        while not self.exit:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.exit = True

                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_LEFT:
                        self.theta_change = -10  # move clockwise
                        print("←")

                    if event.key == self.pygame.K_RIGHT:
                        self.theta_change = 10  # move counterclockwise
                        print("→")

                    if event.key == self.pygame.K_DOWN:
                        self.r_change = -20  # move towards origin
                        print("↓")

                    if event.key == self.pygame.K_UP:
                        self.r_change = 20  # move away from origin
                        print("↑")

                if event.type == self.pygame.KEYUP:
                    if event.key in (self.pygame.K_LEFT, self.pygame.K_RIGHT):
                        self.theta_change = 0
                    if event.key in (self.pygame.K_DOWN, self.pygame.K_UP):
                        self.r_change = 0

            self.r += self.r_change
            self.theta += self.theta_change
            self.player_x, self.player_y = self.converter.cartesian_to_pixel(self.converter.polar_to_cartesian((self.r,
                                                                                                             self.theta)))
            self.screen_set()
            self.display_player(self.player_x, self.player_y)

            self.pygame.display.flip()
            self.clock.tick(30)

        return self.pygame, self.clock