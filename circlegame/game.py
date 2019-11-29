import pygame
from circlegame.polarutilities.coordinateconverter import CoordinateConverter

BLACK, WHITE, RED, \
GREEN, BLUE, HOTPINK = (0, 0, 0), (255, 255, 255), (255, 0, 0), \
                       (0, 255, 0), (0, 0, 255), (255, 105, 180)


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.converter = CoordinateConverter(screen.get_width,
                                             screen.get_height)
        self.game_over = False

    def screen_set(self):
        space_img = pygame.image.load('../img/space_img.jpg')
        self.screen.blit(space_img, space_img.get_rect())

    def start(self):
        while not self.game_over:
            self.listen_for_events()
            pygame.display.flip()
            self.screen_set()
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
