import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Memory Game")

# Define colors
background_color = (255, 255, 255)
card_color = (200, 200, 200)
text_color = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 36)

# Define game variables
grid_size = 4
card_width = window_width // grid_size
card_height = window_height // grid_size
cards = [i // 2 for i in range(grid_size**2)]
random.shuffle(cards)
flipped = [False] * (grid_size**2)
selected = []
matched = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // card_height
            col = x // card_width
            index = row * grid_size + col
            if not flipped[index] and len(selected) < 2:
                flipped[index] = True
                selected.append(index)

    window.fill(background_color)

    for i in range(grid_size):
        for j in range(grid_size):
            index = i * grid_size + j
            x = j * card_width
            y = i * card_height

            if flipped[index]:
                pygame.draw.rect(window, card_color, (x, y, card_width, card_height))
                text = font.render(str(cards[index]), True, text_color)
                text_rect = text.get_rect(center=(x + card_width/2, y + card_height/2))
                window.blit(text, text_rect)
            else:
                pygame.draw.rect(window, card_color, (x, y, card_width, card_height))

            pygame.draw.rect(window, text_color, (x, y, card_width, card_height), 3)

    if len(selected) == 2:
        index1, index2 = selected
        if cards[index1] == cards[index2]:
            matched += 2
            if matched == grid_size**2:
                pygame.time.wait(1000)
                running = False
        else:
            pygame.time.wait(1000)
            flipped[index1] = False
            flipped[index2] = False
        selected = []

    pygame.display.flip()
pygame.quit()
