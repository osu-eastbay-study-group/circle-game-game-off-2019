import pygame
import coordinateconverter
from circle_game import CircleGame

if __name__ == "__main__":
    pygame.init()
    cgame = CircleGame()
    clock = pygame.time.Clock()
    pygame, clock = cgame.convert_dot(pygame, clock)
    pygame.quit()
