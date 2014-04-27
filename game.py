__author__ = 'Matt Geiger'

import paddle as _paddle
import ball as _ball
import pygame as pg


class Game:
    def __init__(self, screen, screen_rect, pause=True):
        self.pause = pause
        self.screen_rect = screen_rect
        self.screen = screen
        self.ball = _ball.Ball(self.screen_rect)
        self.player = _paddle.Paddle(screen_rect, 750, 275)
        self.computer = _paddle.Paddle(screen_rect, 50, 275)
        self.done = False
        self.ball.set_ball()

    def render(self):
        self.screen.fill(0)
        self.ball.render(self.screen)
        self.player.render(self.screen)
        self.computer.render(self.screen)

    def get_event(self, event, keys):
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.done = True
            if event.key == pg.K_UP:
                self.player.move(-25)
            if event.key == pg.K_DOWN:
                self.player.move(25)

    def update(self):
        self.ball.update(self.computer.rect, self.player.rect)
        self.computer.move_computer(self.ball.rect.y)





