import pygame
import coordinateconverter

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

dot_img = pygame.image.load('../img/red_dot.png')  # Image that user moves

# Position related
converter = coordinateconverter.CoordinateConverter(display_width,
                                                    display_height)
r = 0
theta = 0
r_change = 0
theta_change = 0


# Display the image
def dot(x_pixel, y_pixel):
    game_display.blit(dot_img, (x_pixel, y_pixel))


crashed = False  # When to quit

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                theta_change = -5  # move clockwise
                print("←")
            if event.key == pygame.K_RIGHT:
                theta_change = 5  # move counterclockwise
                print("→")
            if event.key == pygame.K_DOWN:
                r_change = -5  # move towards origin
                print("↓")
            if event.key == pygame.K_UP:
                r_change = 5   # move away from origin
                print("↑")

    # Update the pixel coordinates of the image
    r += r_change
    theta += theta_change
    x_pixel, y_pixel = converter.cartesian_to_pixel(converter.polar_to_cartesian((r, theta)))

    game_display.fill(colors['white'])
    dot(x_pixel, y_pixel)  # show in middle of window
    pygame.display.update()
    clock.tick(30)

pygame.quit()
