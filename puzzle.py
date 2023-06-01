import pygame
import random

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Puzzle Game")

# Define colors
background_color = (255, 255, 255)
block_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Define block size and gap
block_size = 50
block_gap = 10

# Create a grid of blocks
grid = []
for row in range(8):
    grid.append([])
    for column in range(8):
        color = random.choice(block_colors)
        block = pygame.Rect(column * (block_size + block_gap), row * (block_size + block_gap), block_size, block_size)
        grid[row].append((block, color))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill(background_color)

    # Draw the blocks
    for row in range(8):
        for column in range(8):
            block, color = grid[row][column]
            pygame.draw.rect(window, color, block)

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
