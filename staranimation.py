import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1500, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gold Star Animation")

# Colors
white = (255, 255, 255)
gold = (255, 215, 0)

# Star vertices
star_vertices = [(400, 100), (440, 220), (560, 220), (460, 300), (500, 420),
                 (400, 350), (300, 420), (340, 300), (240, 220), (360, 220)]

# Increased spacing between stars
star_spacing = 300

# Animation parameters
fill_rate = 5
filled_points = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(white)

    # Draw three filled stars with increased spacing
    for i in range(1):
        offset_x = i * (len(star_vertices) * fill_rate + star_spacing)
        filled_star = [(x + offset_x, y) for x, y in star_vertices[:filled_points]]
        if len(filled_star) >= 3:
            pygame.draw.polygon(screen, gold, filled_star, 0)

    # Incrementally fill the stars
    if filled_points < len(star_vertices):
        filled_points += fill_rate

    pygame.display.flip()
    pygame.time.delay(300)  # Delay to control animation speed
