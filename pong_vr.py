import pygame
from pygame import vr

def main():
    pygame.init()

    vr.init()
    display = vr.create_vr_display()

    window_size = (800, 600)
    window = pygame.display.set_mode(window_size, pygame.OPENGL | pygame.DOUBLEBUF)

    paddle_width = 100
    paddle_height = 20
    paddle_x = window_size[0] // 2 - paddle_width // 2
    paddle_y = window_size[1] - 2 * paddle_height

    ball_radius = 10
    ball_x = window_size[0] // 2
    ball_y = window_size[1] // 2
    ball_dx = 2
    ball_dy = -2

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        _, _, _, _, yaw, _, _ = display.get_tracking_state()
        paddle_x = int((yaw + 90) * (window_size[0] - paddle_width) / 180)

        ball_x += ball_dx
        ball_y += ball_dy

        if ball_x <= ball_radius or ball_x >= window_size[0] - ball_radius:
            ball_dx *= -1
        if ball_y <= ball_radius or ball_y >= window_size[1] - ball_radius:
            ball_dy *= -1

        if paddle_x <= ball_x <= paddle_x + paddle_width and ball_y >= paddle_y - ball_radius:
            ball_dy *= -1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)
        glVertex2f(paddle_x, paddle_y)
        glVertex2f(paddle_x + paddle_width, paddle_y)
        glVertex2f(paddle_x + paddle_width, paddle_y + paddle_height)
        glVertex2f(paddle_x, paddle_y + paddle_height)
        glEnd()

        glColor3f(1, 1, 1)
        glBegin(GL_TRIANGLE_FAN)
        for angle in range(0, 360, 10):
            x = ball_x + ball_radius * cos(radians(angle))
            y = ball_y + ball_radius * sin(radians(angle))
            glVertex2f(x, y)
        glEnd()

        display.update()
        window.blit(display.get_left_eye_buffer(), (0, 0))
        pygame.display.flip()

    display.destroy()
    vr.quit()
    pygame.quit()

if __name__ == '__main__':
    main()
