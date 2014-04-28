__author__ = 'Matt Geiger'

import pygame as pg
import random


class Ball:
    def __init__(self, screen_rect, x=400, y=300, width=7, height=7, speed=7, color=(255, 255, 255)):
        self.surface = pg.Surface([width, height])
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen_rect = screen_rect
        self.velocity = [0, 0]
        self.color = color
        self.speed = speed

    def get_random_float(self):
        while True:
            num = random.uniform(-1.0, 1.0)
            if num > -.5 and num < .5:
                continue
            else:
                return num

    def set_ball(self):
        x = self.get_random_float()
        y = self.get_random_float()
        self.rect.x = 400
        self.rect.y = 300
        self.velocity = [x*self.speed, y*self.speed]

    def move(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def render(self, screen):
        self.surface.fill(self.color)
        screen.blit(self.surface, [self.rect.x, self.rect.y])

    def collide_walls(self):
        if self.rect.x < 0:
            return -1
        if self.rect.x > self.screen_rect.width:
            return 1
        if self.rect.y < 0 or self.rect.y > self.screen_rect.height:
            self.velocity[1] *= -1
        return 0

    def collide_paddle(self, paddle_left_rect, paddle_right_rect):
        if self.rect.colliderect(paddle_left_rect):
            self.velocity[0] *= -1
            self.rect.x += 5
        if self.rect.colliderect(paddle_right_rect):
            self.velocity[0] *= -1
            self.rect.x -= 5

    def update(self, paddle_left_rect, paddle_right_rect):
        hit_wall = self.collide_walls()
        if hit_wall:
            return hit_wall
        self.collide_paddle(paddle_left_rect, paddle_right_rect)
        self.move()
