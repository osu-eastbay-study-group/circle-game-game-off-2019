#!/usr/bin/env python
import pygame
import circlegame.game

if __name__ == "__main__":
    # Initialization
    display_width = 1080
    display_height = 1080
    title = 'Circle Game'
    wallpaper_path = '../img/space_img.jpg'

    # PyGame Setup
    pygame.display.set_caption(title)
    pygame.init()
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()
    game = circlegame.game.Game(screen, clock, wallpaper_path)

    # Start the game
    print("START GAME")
    game.start()
    pygame.quit()
    print("GAME OVER")
