import pygame


class Person:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
