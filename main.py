import pygame as pyg
from pygame.locals import *
from cell import Cell
import random
import settings


def main():
    settings.init()

    # Initialise screen
    pyg.init()
    screen = pyg.display.set_mode((settings.window_size, settings.window_size))
    pyg.display.set_caption('gridder')

    # Initialise clock
    clock = pyg.time.Clock()

    # Initialise grid
    for i in range(0, settings.cols):
        for j in range(0, settings.rows):
            settings.grid[i][j] = Cell(i, j)

    # Make bees
    options = []
    for i in range(settings.cols):
        for j in range(settings.rows):
            options.append((i, j))
    
    for _ in range(settings.num_bees):
        pick = random.choice(options)
        i = pick[0]
        j = pick[1]
        settings.grid[i][j].bee = True
        options.remove(pick)

    # Count neighbours
    for i in range(settings.cols):
        for j in range(settings.rows):
            settings.grid[i][j].count_bees()
    
    # Initialise sprites
    cells = pyg.sprite.Group()
    for i in range(settings.cols):
        for j in range(settings.rows):
            cells.add(settings.grid[i][j])

    while True:
        clock.tick(60)

        for event in pyg.event.get():
            if event.type == QUIT:
                return
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

            if event.type == MOUSEBUTTONDOWN:
                for cell in cells:
                    if cell.check_click(event.pos):
                        cell.reveal()

        cells.update()
        cells.draw(screen)
        pyg.display.update()

    
if __name__ == '__main__':
    main()


pyg.quit()
quit()
