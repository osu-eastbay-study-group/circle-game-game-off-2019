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

# RGB colors
colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)}

# Image that user moves
dot_img = pygame.image.load('../img/red_dot.png')

# Display the image
def dot(x_pixel, y_pixel):
    game_display.blit(dot_img, (x_pixel, y_pixel))

crashed = False  # When to quit

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    game_display.fill(colors['white'])
    dot(display_width // 2, display_height // 2)  # show in middle of window
    pygame.display.update()
    clock.tick(30)

pygame.quit()
