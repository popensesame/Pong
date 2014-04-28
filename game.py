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
        self.score = [0, 0]
        self.score_text = str(self.score[0]) + ":" + str(self.score[1])
        self.score_obj = pg.font.Font(None, 48)
        self.score_surface = self.score_obj.render(self.score_text, False, (255, 255, 255))
        self.score_surface_rect = self.score_surface.get_rect()
        self.score_surface_rect.topleft = (360, 20)
        self.next = "MENU"

    def render(self):
        self.screen.fill(0)
        self.ball.render(self.screen)
        self.player.render(self.screen)
        self.computer.render(self.screen)
        self.render_score()

    def render_score(self):
        self.score_text = str(self.score[0]) + ":" + str(self.score[1])
        self.score_surface = self.score_obj.render(self.score_text, False, (255, 255, 255))
        self.screen.blit(self.score_surface, self.score_surface_rect)

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

    def adjust_score(self, hit_wall):
        if hit_wall == -1:
            self.score[1] += 1
        if hit_wall == 1:
            self.score[0] += 1

    def update(self):
        hit_wall = self.ball.update(self.computer.rect, self.player.rect)
        if hit_wall:
            self.adjust_score(hit_wall)
            self.ball.set_ball()
        self.computer.move_computer(self.ball.rect.y, self.ball.moving_away_from_ai)

    def cleanup(self):
        self.score = [0, 0]





