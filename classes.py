import pygame


class Person:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.shooting = False

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
