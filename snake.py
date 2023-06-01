import pygame
import random

pygame.init()

width = 640
height = 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

snake_size = 20
food_size = 20

snake_x = width // 2
snake_y = height // 2
snake_dx = 0
snake_dy = 0

food_x = random.randint(0, width - food_size) // 20 * 20
food_y = random.randint(0, height - food_size) // 20 * 20

clock = pygame.time.Clock()

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dy != 20:
                snake_dx = 0
                snake_dy = -20
            elif event.key == pygame.K_DOWN and snake_dy != -20:
                snake_dx = 0
                snake_dy = 20
            elif event.key == pygame.K_LEFT and snake_dx != 20:
                snake_dx = -20
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx != -20:
                snake_dx = 20
                snake_dy = 0

    snake_x += snake_dx
    snake_y += snake_dy

    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, width - food_size) // 20 * 20
        food_y = random.randint(0, height - food_size) // 20 * 20

    window.fill(BLACK)

    pygame.draw.rect(window, GREEN, (snake_x, snake_y, snake_size, snake_size))
    pygame.draw.rect(window, RED, (food_x, food_y, food_size, food_size))

    pygame.display.update()

    clock.tick(10)

pygame.quit()
