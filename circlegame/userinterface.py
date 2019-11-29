import pygame
from circlegame.circle_game import CircleGame

if __name__ == "__main__":
    pygame.init()
    circle_game = CircleGame()
    clock = pygame.time.Clock()
    pygame, clock = circle_game.dots_move(pygame, clock)
    pygame.quit()
