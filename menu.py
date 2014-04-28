__author__ = 'Matt Geiger'

import pygame as pg
import pong

class Menu:
    def __init__(self, screen, screen_rect, done=False, highlighted="START"):
        self.screen = screen
        self.screen_rect = screen_rect
        self.done = done
        self.highlighted = highlighted
        self.start_color = (255, 0, 255)
        self.quit_color = (255, 255, 255)
        self.next = "GAME"

    def get_event(self, event, keys):
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN and self.highlighted == "START":
                self.highlighted = "QUIT"
            if event.key == pg.K_UP and self.highlighted == "QUIT":
                self.highlighted = "START"
            if event.key == pg.K_RETURN:
                if self.highlighted == "START":
                    self.done = True
                if self.highlighted == "QUIT":
                    pg.quit()

    def start_button(self, color):
        start_text = "START"
        start_obj = pg.font.Font(None, 48)
        start_surface = start_obj.render(start_text, False, color)
        start_surface_rect = start_surface.get_rect()
        start_surface_rect.topleft = (350, 250)
        return start_surface, start_surface_rect

    def quit_button(self, color):
        quit_text = "QUIT"
        quit_obj = pg.font.Font(None, 48)
        quit_surface = quit_obj.render(quit_text, False, color)
        quit_surface_rect = quit_surface.get_rect()
        quit_surface_rect.topleft = (350, 300)
        return quit_surface, quit_surface_rect

    def render(self):
        start_surface, start_surface_rect = self.start_button(self.start_color)
        quit_surface, quit_surface_rect = self.quit_button(self.quit_color)
        self.screen.blit(start_surface, start_surface_rect)
        self.screen.blit(quit_surface, quit_surface_rect)

    def update(self):
        if self.highlighted == "QUIT":
            self.quit_color = (255, 0, 255)
            self.start_color = (255, 255, 255)
        if self.highlighted == "START":
            self.start_color = (255, 0, 255)
            self.quit_color = (255, 255, 255)

    def cleanup(self):
        pass






