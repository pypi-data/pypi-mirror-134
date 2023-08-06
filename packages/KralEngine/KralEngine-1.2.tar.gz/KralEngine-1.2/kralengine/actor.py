import traceback
from pprint import pprint

import pygame

import kralengine
import kralengine as ke
import logging
import os

import __main__


class Actor:
    def __init__(self, window: ke.KralEngine, atype, shape, pos, size, color=(0, 0, 0)):
        self.logger = logging.getLogger(str(id(self)) + " " + os.path.basename(__main__.__file__))
        # Logger
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler('file.log')
        c_handler.setLevel(logging.WARNING)
        f_handler.setLevel(logging.ERROR)
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)
        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)

        self.drawed = False
        self.animate = False
        self.animations = {}
        self.atype = atype
        self.shape = shape
        self.pos = list(pos)
        self.size = size
        self.window = window
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.color = color
        self.image = None
        self.colliders = []
        self.collider_rects = []
        if hasattr(self.window, "objects"):
            self.window.objects.append(self)

    def draw(self):
        if type(self.atype()) == ke.IMAGE:
            try:
                if self.window.splashscreendone:
                    if not self.animate and not type(self.shape) == str:
                        self.shape = self.shape.getFullPath()
                    elif self.animate:
                        # pprint(self.animations)
                        self.shape = self.animations[self.animate]["frames"][
                            int(self.animations[self.animate]["index"])]
                        if not int(self.animations[self.animate]["index"]) >= len(
                                self.animations[self.animate]["frames"]) - 1:
                            self.animations[self.animate]["index"] += self.animations[self.animate]["time"]
                        else:
                            self.animations[self.animate]["index"] = 0
                    self.image = pygame.image.load(self.shape)
                    if type(self.size) == ke.SIZE:
                        self.image = pygame.transform.scale(self.image, self.size.get_size())
                    if self.animate and self.animations[self.animate]["mirror_x"]:
                        self.image = pygame.transform.flip(self.image, True, False)
                    if self.animate and self.animations[self.animate]["mirror_y"]:
                        self.image = pygame.transform.flip(self.image, False, True)
                    self.window.window.blit(self.image, self.pos)
                self.drawed = True
            except Exception as e:
                self.logger.error("Image can't load!")
                self.drawed = False
                print(e)
        elif type(self.atype()) == ke.OBJECT:
            try:
                if self.window.splashscreendone:
                    if self.animate and self.animations[self.animate]["type"] == "color":
                        if not ((int(self.animations[self.animate]["index"]) >=
                                 len(self.animations[self.animate]["colors"]) - 1) or
                                (int(self.animations[self.animate]["index"]) < 0)):
                            self.color = self.animations[self.animate]["colors"][self.animations[self.animate]["index"]]
                            if self.animations[self.animate]["iter-dir"] == "-":
                                self.animations[self.animate]["index"] -= self.animations[self.animate]["time"]
                            else:
                                self.animations[self.animate]["index"] += self.animations[self.animate]["time"]
                        else:
                            if self.animations[self.animate]["iteration"] == "infinite-reverse":
                                if self.animations[self.animate]["iter-dir"] == "+":
                                    self.animations[self.animate]["index"] -= 1
                                    self.animations[self.animate]["iter-dir"] = "-"
                                elif self.animations[self.animate]["iter-dir"] == "-":
                                    self.animations[self.animate]["index"] += 1
                                    self.animations[self.animate]["iter-dir"] = "+"
                            else:
                                self.animations[self.animate]["index"] = 0

                    if type(self.shape()) == ke.RECT:
                        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size.get_width(), self.size.get_height())
                        pygame.draw.rect(self.window.window, self.color, self.rect)
                    elif type(self.shape()) == ke.ELLIPSE:
                        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size.get_width(), self.size.get_height())
                        pygame.draw.ellipse(self.window.window, self.color, self.rect)
                self.drawed = True
            except Exception as e:
                self.logger.error("Object can't draw!")
                self.drawed = False
                print(e)

    def update(self):
        if self.drawed:
            self.draw()
        self.updateColliders()

    def addSpriteAnimation(self, name, animation, mirror_x=False, mirror_y=False, iteration="infinite-reverse"):
        self.animations[name] = {
            "name": name,
            "frames": animation.frames,
            "time": animation.time,
            "index": 0,
            "type": animation.type,
            "mirror_x": mirror_x,
            "mirror_y": mirror_y,
            "iteration": iteration
        }

    def addColorAnimation(self, name, animation, iteration="infinite-reverse"):
        self.animations[name] = {
            "name": name,
            "colors": animation.color_list,
            "time": animation.time,
            "index": 0,
            "type": animation.type,
            "iteration": iteration,
            "iter-dir": "+"
        }

    def playAnimation(self, name):
        # self.stopAnimation()
        self.animate = name

    def stopAnimation(self):
        for k in self.animations.keys():
            self.animations[k]["index"] = 0
        self.animate = False

    def addCollider(self, collider):
        self.colliders.append(collider)
        rect = pygame.Rect(self.pos[0] + collider.offset[0], self.pos[1] + collider.offset[1],
                           collider.width, collider.height)
        self.collider_rects.append(rect)
        del rect

    def updateColliders(self):
        temp = []
        temp2 = []
        for cr in self.colliders:
            temp.append(pygame.Rect(self.pos[0] + cr.offset[0], self.pos[1] + cr.offset[1],
                                    cr.width, cr.height))
        for cr in self.colliders:
            temp2.append(kralengine.BoxCollider(cr.width, cr.height, cr.offset))
        self.collider_rects = temp
        self.colliders = temp2
        del temp
        del temp2

    def isCollide(self, obj):
        temp = None
        for cr in self.collider_rects:
            temp = (cr.collidelist(obj.collider_rects))
        if temp == -1:
            return False
        else:
            return True
