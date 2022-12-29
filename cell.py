import pygame as pyg
 
class Cell(pyg.sprite.Sprite):

    def __init__(self, i, j, w):
        super().__init__()
        self.i = i
        self.j = j
        self.x = i * w
        self.y = j * w
        self.w = w
        self.bee = False
        self.revealed = True
        self.font = pyg.font.SysFont('comicsans', self.w // 2)

        self.image = pyg.Surface((w, w))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.neighbours = 0

    def reveal(self):
        self.revealed = True

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            self.reveal()

    def update(self):
        pyg.draw.rect(self.image, 'black', pyg.Rect(0, 0, self.w, self.w))

        if not self.revealed:
            pyg.draw.rect(self.image, 'gray70', pyg.Rect(1, 1, self.w - 2, self.w - 2))

        if self.revealed:
            pyg.draw.rect(self.image, 'gray90', pyg.Rect(1, 1, self.w - 2, self.w - 2))

            if self.bee:
                pyg.draw.circle(self.image, 'black', (self.w * 0.5, self.w * 0.5), self.w * 0.3)
            else:
                if self.neighbours > 0:
                    text = self.font.render(str(self.neighbours), True, 'black')
                    text_rect = text.get_rect(center=(self.w / 2, self.w / 2))
                    self.image.blit(text, text_rect)
