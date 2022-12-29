import pygame as pyg
from pygame.locals import *
from cell import Cell
import random

WINWIDTH = 1200
WINDHEIGTH = 1200

cols = 20
rows = cols
w = WINWIDTH // cols
num_bees = (cols * rows) // 10


def make_2D_array(cols, rows):
    arr = [n for n in range(cols)]
    for i, _ in enumerate(arr):
        arr[i] = [n for n in range(rows)]
    return arr


def main():
    # Initialise screen
    pyg.init()
    screen = pyg.display.set_mode((WINWIDTH, WINDHEIGTH))
    pyg.display.set_caption('gridder')

    # Initialise clock
    clock = pyg.time.Clock()

    # Initialise grid
    grid = make_2D_array(cols, rows)
    for i in range(0, cols):
        for j in range(0, rows):
            grid[i][j] = Cell(i, j, w)

    # Make bees
    options = []
    for i in range(cols):
        for j in range(rows):
            options.append((i, j))
    
    for _ in range(num_bees):
        pick = random.choice(options)
        i = pick[0]
        j = pick[1]
        grid[i][j].bee = True
        options.remove(pick)

    # Count neighbours
    for i in range(cols):
        for j in range(rows):
            total = 0
            print('testing cell:', i, j)
            cell = grid[i][j]

            if cell.bee:
                print('found bee and skipping:', i, j)
                cell.neighbours = -1
                continue

            for xoff in range(i - 1, i + 2):
                for yoff in range(j - 1, j + 2):
                    if xoff >= 0 and xoff < cols and yoff >= 0 and yoff < rows:
                        if grid[xoff][yoff].bee:
                            total += 1
            
            cell.neighbours = total
    
    # Initialise sprites
    cells = pyg.sprite.Group()
    for i in range(cols):
        for j in range(rows):
            cells.add(grid[i][j])

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
                    cell.check_click(event.pos)

        cells.update()
        cells.draw(screen)
        pyg.display.update()

    
if __name__ == '__main__':
    main()


pyg.quit()
quit()
