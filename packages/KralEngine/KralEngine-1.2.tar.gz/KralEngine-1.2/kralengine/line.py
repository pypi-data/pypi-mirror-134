import pygame


class Line:
    def __init__(self, window, color, start, end):
        self.window = window
        self.color = color
        self.start = list(start)
        self.end = list(end)
        self.drawed = False

        self.window.objects.append(self)

    def draw(self):
        self.drawed = True
        pygame.draw.aaline(self.window.window, self.color, self.start, self.end)

    def update(self):
        if self.drawed:
            self.draw()