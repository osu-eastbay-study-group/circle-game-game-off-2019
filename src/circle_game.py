import pygame
from coordinateconverter import CoordinateConverter

BLACK, WHITE, RED, GREEN, BLUE = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)

class CircleGame:
    def __init__(self):

        self.display_width = 800
        self.display_height = 600
        self.title = 'Circle Game'

        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode((self.display_width, self.display_height))
        self.screen.fill(WHITE)

    def display_dot(self, x_pixel, y_pixel):
        self.x_pixel = x_pixel
        self.y_pixel = y_pixel
        self.dot_img = pygame.image.load('../img/red_dot.png')
        self.screen.blit(self.dot_img, (self.x_pixel, self.y_pixel))

    def convert_dot(self, pygame, clock):
        self.pygame, self.clock = pygame, clock
        self.r, self.theta, self.r_change, self.theta_change = 0, 0, 0, 0
        self.converter = CoordinateConverter(self.display_width, self.display_height)
        self.crashed = False

        while not self.crashed:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.crashed = True

                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_LEFT:
                        self.theta_change = -5  # move clockwise
                        print("←")
                        self.display_dot(self.dot_x, self.dot_y)
                    if event.key == self.pygame.K_RIGHT:
                        self.theta_change = 5  # move counterclockwise
                        print("→")
                        self.display_dot(self.dot_x, self.dot_y)
                    if event.key == self.pygame.K_DOWN:
                        self.r_change = -5  # move towards origin
                        print("↓")
                        self.display_dot(self.dot_x, self.dot_y)
                    if event.key == self.pygame.K_UP:
                        self.r_change = 5  # move away from origin
                        print("↑")

                        self.display_dot(self.dot_x, self.dot_y)

                if event.type == self.pygame.KEYUP:
                    if event.key in (self.pygame.K_LEFT, self.pygame.K_RIGHT):
                        self.theta_change = 0
                    if event.key in (self.pygame.K_DOWN, self.pygame.K_UP):
                        self.r_change = 0
            self.r += self.r_change
            self.theta += self.theta_change
            self.dot_x, self.dot_y = self.converter.cartesian_to_pixel(self.converter.polar_to_cartesian((self.r,
                                                                                                             self.theta)))

            self.display_dot(self.dot_x, self.dot_y)

            self.pygame.display.update()
            self.clock.tick(30)

        return self.pygame, self.clock