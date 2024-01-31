import pygame
import sys
from grid import Grid

pygame.init()
# dark_blue = (44, 44, 127)
dark_blue = (143, 188, 219)

screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Python Tetris")

game_grid = Grid()
game_grid.print_grid()

# Duration
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(dark_blue)
    game_grid.draw(screen)
    pygame.display.update()
