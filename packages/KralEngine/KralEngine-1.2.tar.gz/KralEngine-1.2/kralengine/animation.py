import os

import pygame
import kralengine as ke
from collections.abc import Iterable
from reportlab.lib import colors


class SpriteAnimation:
    def __init__(self, name, frames, time):
        self.name = name
        self.frames = frames
        self.time = time
        self.type = "sprite"
        temp = []
        if isinstance(self.frames, list):
            for frame in self.frames:
                temp.append(ke.ResourceLocation(frame).getFullPath())
            self.frames = temp
        elif isinstance(self.frames, str):
            for frame in os.listdir(ke.ResourceLocation(self.frames).getFullPath()):
                temp.append(ke.ResourceLocation(os.path.join(self.frames, frame)).getFullPath())
            temp = sorted(temp)
            self.frames = temp


class ColorAnimation:
    def __init__(self, from_color, to_color, time):
        self.from_color = from_color
        self.to_color = to_color
        self.length = 256
        self.color_list = []
        self.time = time
        self.type = "color"
        for i in self.colorRanger():
            self.color_list.append(list(map(int, list(i.rgb()))))


    def get_list(self):
        return self.color_list

    def colorRanger(self):
        temp = []
        if self.length == 1: return [self.from_color]

        if self.length > 1:
            lim = self.length - 1
            for i in range(self.length):
                temp.append(colors.linearlyInterpolatedColor(colors.Color(*self.from_color),
                                                             colors.Color(*self.to_color), 0, lim, i))
        return temp