__author__ = 'Matt Geiger'

import pygame as pg
import game, menu


class Pong:

    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([800, 600])
        self.screen_rect = self.screen.get_rect()
        self.keys = pg.key.get_pressed()
        self.state_dict = {
            "GAME": game.Game(self.screen, self.screen_rect),
            "MENU": menu.Menu(self.screen, self.screen_rect)
        }
        self.state_name = "MENU"
        self.state = self.state_dict[self.state_name]

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type in (pg.KEYDOWN, pg.KEYUP):
                self.keys = pg.key.get_pressed()
            self.state.get_event(event, self.keys)

    def change_state(self):
        if self.state.done:
            self.state.cleanup()
            self.state_name = self.state.next
            self.state.done = False
            self.screen.fill(0)
            self.state = self.state_dict[self.state_name]

    def run(self):
        while True:
            self.event_loop()
            self.change_state()
            self.state.update()
            self.state.render()
            pg.display.update()
            self.clock.tick(30)