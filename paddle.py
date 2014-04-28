__author__ = 'Matt Geiger'

import pygame as pg


class Paddle:
    def __init__(self, screen_rect, x, y, width=10, height=100, color=(255, 255, 255)):
        self.screen_rect = screen_rect
        self.surface = pg.Surface([width, height])
        self.rect = self.surface.get_rect()
        self.reset_x = x
        self.reset_y = y
        self.rect.x = x
        self.rect.y = y
        self.color = color

    def reset(self):
        self.rect.x, self.rect.y = self.reset_x, self.reset_y

    def move(self, y):
        self.rect.y += y
        self.rect.clamp_ip(self.screen_rect)

    def render(self, screen):
        self.surface.fill(self.color)
        screen.blit(self.surface, [self.rect.x, self.rect.y])

    def move_computer(self, ball_y, moving_away_from_ai):
        if not moving_away_from_ai:
            if ball_y > self.rect.centery+10:
                self.move(4)
            elif ball_y < self.rect.centery-10:
                self.move(-4)