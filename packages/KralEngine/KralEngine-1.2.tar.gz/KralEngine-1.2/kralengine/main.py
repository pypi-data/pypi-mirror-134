import pygame
import os
from typing import Iterable

import __main__



class KralEngine:
    def __init__(self, title: str = "KralEngine",
                 color: Iterable[int] = (0, 0, 0), fps: int = 60,
                 size: Iterable[int] = (500, 300), debug=False):
        self.title = title
        self.color = color
        self.fps = fps
        self.size = size
        self.width = self.size[0]
        self.height = self.size[1]
        self.debug = debug

        self.light = False
        self.light_surf = pygame.Surface(self.size)
        self.light_surf.fill("White")

        self.objects = []

        self.running = True

        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

        self.splashsurface = pygame.Surface(self.size)
        self.splashsurface.fill((0, 0, 0))
        self.splashsurface.convert_alpha()
        self.splashscreendone = False
        self.splashfont = pygame.font.Font(None, 100)
        self.poweredfont = pygame.font.Font(None, 50)
        self.splashtext = self.splashfont.render("KralEngine", True, (255, 255, 255))
        self.poweredtext = self.poweredfont.render("Powered by Pygame", True, (255, 255, 255))

        self.fadein = pygame.Surface(self.size).convert_alpha()


    def run(self):
        while self.running:
            pygame.display.flip()
            self.clock.tick(self.fps)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            if not self.splashscreendone:
                for i in range(85):
                    pygame.display.flip()
                    self.clock.tick(self.fps)
                    pygame.display.update()
                    if self.debug:
                        pygame.display.set_caption(self.title + " " + str(int(self.clock.get_fps())))
                    self.window.blit(self.splashsurface, (0, 0))
                    self.splashsurface.fill((0, 0, 0))
                    self.splashsurface.blit(self.splashtext, ((self.splashsurface.get_width() // 2) -
                                                              self.splashtext.get_width() // 2,
                                                              (self.splashsurface.get_height() // 2)))
                    self.splashsurface.blit(self.poweredtext, ((self.splashsurface.get_width() // 2) -
                                                               self.poweredtext.get_width() // 2,
                                                               (self.splashsurface.get_height() -
                                                                self.poweredtext.get_height())))
                    self.splashsurface.blit(self.fadein, (0, 0))
                    if self.fadein.get_alpha() != 1:
                        self.fadein.set_alpha(255 - i * 3)
                    else:
                        break
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                            pygame.quit()
                            quit()
                for i in reversed(range(85)):
                    pygame.display.flip()
                    self.clock.tick(self.fps)
                    pygame.display.update()
                    if self.debug:
                        pygame.display.set_caption(self.title + " " + str(int(self.clock.get_fps())))
                    self.window.blit(self.splashsurface, (0, 0))
                    self.splashsurface.fill((0, 0, 0))
                    self.splashsurface.blit(self.splashtext, ((self.splashsurface.get_width() // 2) -
                                                              self.splashtext.get_width() // 2,
                                                              (self.splashsurface.get_height() // 2)))
                    self.splashsurface.blit(self.poweredtext, ((self.splashsurface.get_width() // 2) -
                                                               self.poweredtext.get_width() // 2,
                                                               (self.splashsurface.get_height() -
                                                                self.poweredtext.get_height())))
                    self.splashsurface.blit(self.fadein, (0, 0))
                    if self.fadein.get_alpha() != 255:
                        self.fadein.set_alpha(255 - i * 3)
                    else:
                        break
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                            pygame.quit()
                            quit()
                self.splashscreendone = True

            else:
                self.window.fill(self.color)
                if hasattr(__main__, "update") and __main__.update:
                    __main__.update()
                for i in self.objects:
                    i.update()
                if self.light:
                    self.window.blit(self.light_surf, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
                    self.light_surf.fill("White")
            if self.debug:
                pygame.display.set_caption(self.title + " " + str(int(self.clock.get_fps())))
        pygame.quit()
        quit()

    def light_init(self):
        self.light = True
