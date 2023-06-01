import pygame
import random

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pygame Racing Game")
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the player's car
car_width = 50
car_height = 100
car_x = (window_width - car_width) // 2
car_y = window_height - car_height - 20
car_speed = 5

# Set up the AI cars
ai_car_width = 50
ai_car_height = 100
ai_car_x = random.randint(0, window_width - ai_car_width)
ai_car_y = -ai_car_height
ai_car_speed = 5

clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    window.fill(white)
    pygame.draw.rect(window, black, (car_x, car_y, car_width, car_height))
    pygame.draw.rect(window, red, (ai_car_x, ai_car_y, ai_car_width, ai_car_height))

    ai_car_y += ai_car_speed
    if ai_car_y > window_height:
        ai_car_x = random.randint(0, window_width - ai_car_width)
        ai_car_y = -ai_car_height

    if car_x < 0 or car_x > window_width - car_width:
        game_over = True

    if car_y < ai_car_y + ai_car_height and car_y + car_height > ai_car_y:
        if car_x < ai_car_x + ai_car_width and car_x + car_width > ai_car_x:
            game_over = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
