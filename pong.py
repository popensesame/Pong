__author__ = 'Matt Geiger'

import pygame as pg
import game


class Pong:

    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([800, 600])
        self.screen_rect = self.screen.get_rect()
        self.keys = pg.key.get_pressed()
        self.state_dict = {
            "GAME": game.Game(self.screen, self.screen_rect)
        }
        self.state = self.state_dict["GAME"]

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type in (pg.KEYDOWN, pg.KEYUP):
                self.keys = pg.key.get_pressed()
            self.state.get_event(event, self.keys)

    def run(self):
        while not self.state.done:
            self.event_loop()
            self.state.update()
            self.state.render()
            pg.display.update()
            self.clock.tick(30)