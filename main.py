import numpy as np
import pygame
import time

WIDTH = 64
HEIGHT = 48
CELL_SIZE = 10
WINDOW_WIDTH = WIDTH * CELL_SIZE
WINDOW_HEIGHT = HEIGHT * CELL_SIZE

grid = np.random.choice([0, 1], size=(HEIGHT, WIDTH), p=[0.8, 0.2])

DEAD = 0
ALIVE = 1

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def count_neighbors(grid, row, col):
    neighbor_index = [
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
        (row, col - 1),                     (row, col + 1),
        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
    ]
    count = np.sum([grid[n_row % HEIGHT, n_col % WIDTH]
                   for n_row, n_col in neighbor_index])
    return count


def update_grid(grid):
    new_grid = grid.copy()
    for row in range(HEIGHT):
        for col in range(WIDTH):
            neighbors = count_neighbors(grid, row, col)
            if grid[row, col] == ALIVE:
                if neighbors < 2 or neighbors > 3:
                    new_grid[row, col] = DEAD
            else:
                if neighbors == 3:
                    new_grid[row, col] = ALIVE
    return new_grid


def display_grid(grid):
    window.fill(pygame.Color("black"))
    for row in range(HEIGHT):
        for col in range(WIDTH):
            cell = grid[row, col]
            cell_color = pygame.Color(
                "green") if cell == ALIVE else pygame.Color("black")
            cell_rect = pygame.Rect(
                col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(window, cell_color, cell_rect)
    pygame.display.update()


running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    if not paused:
        grid = update_grid(grid)
        display_grid(grid)
        time.sleep(0.1)

pygame.quit()
