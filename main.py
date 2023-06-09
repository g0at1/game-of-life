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

def countNeighbors(grid, row, col):
    neighborIndex = [
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
        (row, col - 1),                     (row, col + 1),
        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
    ]
    count = np.sum([grid[n_row % HEIGHT, n_col % WIDTH] for n_row, n_col in neighborIndex])
    return count

def updateGrid(grid):
    newGrid = grid.copy()
    for row in range(HEIGHT):
        for col in range(WIDTH):
            neighbors = countNeighbors(grid, row, col)
            if grid[row, col] == ALIVE:
                if neighbors < 2 or neighbors > 3:
                    newGrid[row, col] = DEAD
            else:
                if neighbors == 3:
                    newGrid[row, col] = ALIVE
    return newGrid

def displayGrid(grid):
    window.fill(pygame.Color("black"))
    for row in range(HEIGHT):
        for col in range(WIDTH):
            cell = grid[row, col]
            cellColor = pygame.Color("green") if cell == ALIVE else pygame.Color("black")
            cellRect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(window, cellColor, cellRect)
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
        grid = updateGrid(grid)
        displayGrid(grid)
        time.sleep(0.1)

pygame.quit()

