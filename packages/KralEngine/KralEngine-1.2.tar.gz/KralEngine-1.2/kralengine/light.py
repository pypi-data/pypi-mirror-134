import math
from typing import Union

import pygame
import pygame.gfxdraw

import __main__

from pygame import Surface
from pygame.surface import Surface, SurfaceType

import kralengine.utils
from reportlab.lib import colors


class PointLight:
    polygon_surface: Surface
    angle: float
    polygon_surface_rotated: Union[Surface, SurfaceType]

    def __init__(self, window: kralengine.KralEngine, width, height, pos, color=(255, 255, 255)):
        self.window = window
        self.width = width
        self.height = height
        self.pos = list(pos)
        self.drawed = False
        self.color = color
        self.real_color = []
        self.points = []
        self.angle = 0
        self.rect = pygame.Rect(*self.pos, self.width, self.height)
        self.rect.midtop = self.pos
        for i in color:
            self.real_color.append(255 - i)
        if hasattr(self.window, "objects"):
            self.window.objects.append(self)

        self.polygon_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        # self.polygon_surface.fill("Grey")
        self.polygon_surface_rotated = self.polygon_surface

        self.points.append((self.polygon_surface.get_width() // 2, 0))
        self.points.append((self.polygon_surface.get_width(), self.height))
        self.points.append((0, self.height))

        self.pivot = list(self.rect.center)
        self.offset = pygame.math.Vector2(0, self.height // 2)

        self.light_texture = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.light_txtr = kralengine.utils.colorRanger(colors.Color(*self.real_color, 255),
                                                  colors.Color(*self.real_color, 0), self.height)
        for i in range(self.height):
            pygame.gfxdraw.line(self.light_texture, 0, i, self.width, i, self.light_txtr[i])
        pygame.gfxdraw.textured_polygon(self.polygon_surface, self.points, self.light_texture, 0, -1)
        self.drawed = True
        self.polygon_surface_rotated = self.polygon_surface

    def draw(self):
        self.light_txtr = kralengine.utils.colorRanger(colors.Color(*self.real_color, 255),
                                                       colors.Color(*self.real_color, 0), self.height)
        self.polygon_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.points.append((self.polygon_surface.get_width() // 2, 0))
        self.points.append((self.polygon_surface.get_width(), self.height))
        self.points.append((0, self.height))
        self.light_texture = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        for i in range(self.height):
            pygame.gfxdraw.line(self.light_texture, 0, i, self.width, i, self.light_txtr[i])
        pygame.gfxdraw.textured_polygon(self.polygon_surface, self.points, self.light_texture, 0, -1)
        self.points.clear()
        mouse_pos = pygame.mouse.get_pos()
        self.polygon_surface_rotated, self.rect = self.rotate(self.polygon_surface, self.angle, self.pivot, self.offset)
        self.window.light_surf.blit(self.polygon_surface_rotated, (self.rect[0], self.rect[1]))

        pygame.draw.line(self.window.light_surf, (0, 0, 0), (mouse_pos[0], mouse_pos[1]), self.pivot)

        self.drawed = True

    def rotate(self, surface, angle, pivot, offset):
        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
        rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
        # Add the offset vector to the center/pivot point to shift the rect.
        rect = rotated_image.get_rect(center=pivot + rotated_offset)
        return rotated_image, rect  # Return the rotated image and shifted rect.

    def update(self):
        self.width = abs(self.width)
        self.height = abs(self.height)
        if self.drawed:
            self.draw()

