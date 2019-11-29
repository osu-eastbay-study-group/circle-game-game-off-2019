import pygame
import coordinateconverter
from circle_game import CircleGame

if __name__ == "__main__":
    pygame.init()
    circle_game = CircleGame()
    clock = pygame.time.Clock()
    pygame, clock = circle_game.convert_dot(pygame, clock)
    pygame.quit()
