import pygame
import circlegame.game

if __name__ == "__main__":
    display_width = 800
    display_height = 600
    title = 'Circle Game'
    pygame.display.set_caption(title)

    pygame.init()
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    circle_game = circlegame.game.Game(screen, clock)
    print("START GAME")
    circle_game.start()
    pygame.quit()
    print("GAME OVER")
