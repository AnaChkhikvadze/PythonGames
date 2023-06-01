import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Invaders")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the player
player_size = 50
player_x = window_width // 2 - player_size // 2
player_y = window_height - player_size * 2
player_speed = 5

# Set up the enemy
enemy_size = 50
enemy_x = random.randint(0, window_width - enemy_size)
enemy_y = random.randint(50, 150)
enemy_speed = 3

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_width - player_size:
        player_x += player_speed

    # Update enemy position
    enemy_y += enemy_speed
    if enemy_y > window_height:
        enemy_x = random.randint(0, window_width - enemy_size)
        enemy_y = random.randint(50, 150)

    # Check for collision
    if (player_x < enemy_x + enemy_size and player_x + player_size > enemy_x and
            player_y < enemy_y + enemy_size and player_y + player_size > enemy_y):
        print("Game Over")
        running = False

    # Refresh the window
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(window, WHITE, (enemy_x, enemy_y, enemy_size, enemy_size))
    pygame.display.update()

# Quit the game
pygame.quit()
