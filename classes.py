import pygame


class Person:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.hitbox = pygame.Rect(self.x, self.y, 83, 200)
        self.dead = False

    def draw(self, win, bg_pos):
        if not self.dead:
            win.blit(self.img, (self.x + bg_pos[0], self.y + bg_pos[1]))

