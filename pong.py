__author__ = 'Matt Geiger'

import pygame as pg
import game as _game
import ball as _ball
import paddle as _paddle

pg.init()
clock = pg.time.Clock()
screen_rect = [800, 600]
screen = pg.display.set_mode(screen_rect)
game = _game.Game

ball = _ball.Ball(screen_rect)
player = _paddle.Paddle(screen_rect, 785, 275)
computer = _paddle.Paddle(screen_rect, 0, 275)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    screen.fill((0, 0, 0))
    ball.update(computer.rect, player.rect)
    ball.render(screen)
    player.render(screen)
    computer.render(screen)
    pg.display.update()
    clock.tick(30)

