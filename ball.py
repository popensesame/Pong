__author__ = 'Matt Geiger'

import pygame as pg

class Ball:
    def __init__(self, screen_rect, x=400, y=300, width=5, height=5, color=(0, 0, 0)):
        self.surface = pg.Surface([width, height])
        self.rect = self.surface.get_rect()
        self.screen_rect = screen_rect
        self.velocity = [0, 0]
        self.color = color
        self.x = x
        self.y = y

    def move(self, x, y):
        self.velocity[0] += x
        self.velocity[1] += y

    def render(self, screen):
        self.surface.fill(self.color)
        screen.blit(self.surface, [self.x, self.y])

    def collide_walls(self):
        if self.x < 0:
            return -1
        if self.x > self.screen_rect.x:
            return 1
        if self.y < 0 or self.y > self.screen_rect.y:
            self.velocity[1] *= -1
        return 0

    def update(self):
