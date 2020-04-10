import numpy as np
import pygame

from recordtype import recordtype
from collections import namedtuple
from pygame.locals import (
    MOUSEBUTTONUP,
    MOUSEBUTTONDOWN,
    MOUSEMOTION,
    QUIT,
)


Cell = recordtype("MatrixCell", ["figure", "is_wall", "distance_from_start"])


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def setup():
    NUMBER_OF_ROWS = WINDOW_HEIGHT // 10
    NUMBER_OF_COLUMNS = WINDOW_WIDTH // 10
    
    initialize_matrix(NUMBER_OF_ROWS, NUMBER_OF_COLUMNS)
    draw_grid(NUMBER_OF_ROWS, NUMBER_OF_COLUMNS)


def initialize_matrix(num_rows, num_cols):
    global matrix

    matrix = np.empty((num_rows, num_cols), dtype=Cell)


def draw_grid(num_rows, num_cols):
    MARGIN = 1
    DIMENSION = (WINDOW_WIDTH - MARGIN * num_cols) // num_cols

    for x in range(num_rows):
        for y in range(num_cols):
            rect = pygame.Rect((MARGIN + DIMENSION) * y + MARGIN, (MARGIN + DIMENSION) * x + MARGIN, DIMENSION, DIMENSION)
            pygame.draw.rect(screen, WHITE, rect)
            matrix[x][y] = Cell(rect.copy(), False, np.inf)
    
    pygame.display.update()


def fill_selected_squares():
    position = pygame.mouse.get_pos()
    col = position[0] // 10
    row = position[1] // 10

    matrix[row][col].is_wall = True
    rect = matrix[row][col].figure
    pygame.draw.rect(screen, BLACK, rect)

    pygame.display.update()


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
matrix = None

screen.fill(BLACK)

setup()

pygame.init()

running = True
dragging = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == MOUSEBUTTONDOWN:
            dragging = True
        
        if dragging and event.type == MOUSEMOTION:
            fill_selected_squares()
        
        if event.type == MOUSEBUTTONUP:
            dragging = False
       
pygame.quit()