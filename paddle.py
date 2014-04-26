__author__ = 'Matt Geiger'

import pygame as pg


class Paddle:
    def __init__(self, screen_rect, x, y, width=15, height=50, color=(255, 255, 255)):
        self.screen_rect = screen_rect
        self.surface = pg.Surface([width, height])
        self.rect = self.surface.get_rect()
        self.x = x
        self.y = y
        self.color = color

    def move(self, y):
        self.y += y

    def render(self, screen):
        self.surface.fill(self.color)
        screen.blit(self.surface, [self.x, self.y])
