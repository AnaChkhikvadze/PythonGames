import pygame
import random

pygame.init()

window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ping Pong")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

paddle_width = 10
paddle_height = 60
ball_radius = 10
paddle_speed = 5
ball_speed_x = 3
ball_speed_y = 3
score_player = 0
score_opponent = 0

player_paddle = pygame.Rect(50, window_height // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent_paddle = pygame.Rect(window_width - 50 - paddle_width, window_height // 2 - paddle_height // 2, paddle_width, paddle_height)

ball = pygame.Rect(window_width // 2 - ball_radius // 2, window_height // 2 - ball_radius // 2, ball_radius, ball_radius)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.y > 0:
        player_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and player_paddle.y < window_height - paddle_height:
        player_paddle.y += paddle_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x *= -1

    if ball.y <= 0 or ball.y >= window_height - ball_radius:
        ball_speed_y *= -1

    if opponent_paddle.y + paddle_height // 2 < ball.y and opponent_paddle.y < window_height - paddle_height:
        opponent_paddle.y += paddle_speed
    elif opponent_paddle.y + paddle_height // 2 > ball.y and opponent_paddle.y > 0:
        opponent_paddle.y -= paddle_speed

    if ball.x <= 0:
        score_opponent += 1
        ball.x = window_width // 2 - ball_radius // 2
        ball.y = window_height // 2 - ball_radius // 2
    elif ball.x >= window_width - ball_radius:
        score_player += 1
        ball.x = window_width // 2 - ball_radius // 2
        ball.y = window_height // 2 - ball_radius // 2

    window.fill(BLACK)

    pygame.draw.rect(window, WHITE, player_paddle)
    pygame.draw.rect(window, WHITE, opponent_paddle)
    pygame.draw.ellipse(window, WHITE, ball)
    font = pygame.font.Font(None, 36)
    player_score_text = font.render("Player: " + str(score_player), True, WHITE)
    opponent_score_text = font.render("Opponent: " + str(score_opponent), True, WHITE)
    window.blit(player_score_text, (50, 50))
    window.blit(opponent_score_text, (window_width - opponent_score_text.get_width() - 50, 50))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
