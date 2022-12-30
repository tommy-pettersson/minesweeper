import pygame as pyg
import settings
 
class Cell(pyg.sprite.Sprite):

    def __init__(self, i, j):
        super().__init__()
        self.i = i
        self.j = j
        self.x = i * settings.w
        self.y = j * settings.w
        self.mine = False
        self.revealed = False
        self.font = pyg.font.SysFont('comicsans', settings.w // 2)

        self.image = pyg.Surface((settings.w, settings.w))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.neighbours = 0

    def count_mines(self):
        if self.mine:
            self.neighbours = -1
            return

        total = 0
        for xoff in range(-1, 2):
            for yoff in range(-1, 2):
                i = self.i + xoff
                j = self.j + yoff

                if i >= 0 and i < settings.cols and j >= 0 and j < settings.rows:
                    if settings.grid[i][j].mine:
                        total += 1
        self.neighbours = total

    def floodFill(self):
        for xoff in range(-1, 2):
            for yoff in range(-1, 2):
                i = self.i + xoff
                j = self.j + yoff

                if i >= 0 and i < len(settings.grid) and j >= 0 and j < len(settings.grid[0]):
                    if not settings.grid[i][j].mine and not settings.grid[i][j].revealed:
                        settings.grid[i][j].reveal()

    def reveal(self):
        self.revealed = True
        if self.neighbours == 0:
            self.floodFill()

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            return True
        else:
            return False

    def update(self):
        pyg.draw.rect(self.image, 'black', pyg.Rect(0, 0, settings.w, settings.w))

        if not self.revealed:
            pyg.draw.rect(self.image, 'gray70', pyg.Rect(1, 1, settings.w - 2, settings.w - 2))

        if self.revealed:
            pyg.draw.rect(self.image, 'gray90', pyg.Rect(1, 1, settings.w - 2, settings.w - 2))

            if self.mine:
                pyg.draw.circle(self.image, 'black', (settings.w * 0.5, settings.w * 0.5), settings.w * 0.3)
            else:
                if self.neighbours > 0:
                    text = self.font.render(str(self.neighbours), True, 'black')
                    text_rect = text.get_rect(center=(settings.w / 2, settings.w / 2))
                    self.image.blit(text, text_rect)
