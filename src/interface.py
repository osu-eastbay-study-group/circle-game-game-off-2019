import pygame

# Avoid hard coding resolution
display_width = 800
display_height = 600

# Initialize PyGame
pygame.init()

# PyGame Settings
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Circle Game')
clock = pygame.time.Clock()

# RGB Colors
# RGB colors
colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)}

crashed = False  # When to quit

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    game_display.fill(colors['white'])
    pygame.display.update()
    clock.tick(30)

pygame.quit()
