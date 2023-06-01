import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Platformer Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define player properties
player_width = 50
player_height = 50
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height - 10
player_vel = 5

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of the keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_vel
    if keys[pygame.K_RIGHT]:
        player_x += player_vel

    # Update the game display
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (player_x, player_y, player_width, player_height))
    pygame.display.update()

# Quit the game
pygame.quit()
