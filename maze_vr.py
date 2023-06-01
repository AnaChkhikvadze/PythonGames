import pygame
from pygame import vr

def main():
    pygame.init()
    vr.init()
    display = vr.create_vr_display()
    window_size = (800, 600)
    window = pygame.display.set_mode(window_size)
    maze = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    maze_width = len(maze[0])
    maze_height = len(maze)
    cell_size = window_size[0] // maze_width
    player_x = 1
    player_y = 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        _, _, _, _, yaw, _, _ = display.get_tracking_state()
        if yaw < -45:
            player_x = max(0, player_x - 1)
        elif yaw > 45:
            player_x = min(maze_width - 1, player_x + 1)
        if yaw > 135:
            player_y = max(0, player_y - 1)
        elif yaw < -135:
            player_y = min(maze_height - 1, player_y + 1)
        for y in range(maze_height):
            for x in range(maze_width):
                if maze[y][x] == 1:
                    pygame.draw.rect(window, (255, 255, 255), (x * cell_size, y * cell_size, cell_size, cell_size))
                else:
                    pygame.draw.rect(window, (0, 0, 0), (x * cell_size, y * cell_size, cell_size, cell_size))
        pygame.draw.rect(window, (255, 0, 0), (player_x * cell_size, player_y * cell_size, cell_size, cell_size))
        display.update()
        window.blit(display.get_left_eye_buffer(), (0, 0))
        pygame.display.flip()
    display.destroy()
    vr.quit()
    pygame.quit()

if __name__ == '__main__':
    main()
