import pygame as pyg
from pygame.locals import *
from cell import Cell
import random
import settings
import time


def gameOver():
    for i in range(settings.cols):
        for j in range(settings.rows):
            settings.grid[i][j].revealed = True


def main():
    pyg.init()

    settings.init()
    settings.font = pyg.font.SysFont('comicsans', settings.w // 2)

    screen = pyg.display.set_mode((settings.window_size, settings.window_size))
    pyg.display.set_caption('MineSweeper')

    # Initialise clock
    clock = pyg.time.Clock()

    # Initialise grid
    for i in range(0, settings.cols):
        for j in range(0, settings.rows):
            settings.grid[i][j] = Cell(i, j)

    # Make mines
    options = []
    for i in range(settings.cols):
        for j in range(settings.rows):
            options.append((i, j))
    
    for _ in range(settings.num_mines):
        pick = random.choice(options)
        i = pick[0]
        j = pick[1]
        settings.grid[i][j].mine = True
        options.remove(pick)

    # Count neighbours
    for i in range(settings.cols):
        for j in range(settings.rows):
            settings.grid[i][j].count_mines()
    
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
                        if event.button == 1:
                            if cell.mine:
                                gameOver()
                            cell.reveal()

                        if event.button == 3:
                            cell.mark()

        cells.update()
        cells.draw(screen)
        pyg.display.update()

    
if __name__ == '__main__':
    main()


pyg.quit()
quit()
