import random

import pygame
from pygame.locals import *

from classes import Person

pygame.init()
pygame.font.init()

W = 800
H = 600
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Scarlett Inferno")
clock = pygame.time.Clock()
font = pygame.font.SysFont("timesnewroman", 30, True)

bg = pygame.image.load("sniper_bg.jpg")
bg_pos = [0, 0]
move_speed = 8

player_img = pygame.image.load("player.png")
person_img = pygame.image.load("person.png")
persons = []
kills = 0
pygame.time.set_timer(USEREVENT + 1, 8000)


def shoot(x, y, persons):
    global kills
    for person in persons:
        if not person.dead and person.hitbox.collidepoint((x, y)):
            person.dead = True
            print(f"Killed person at {person.x}, {person.y} by aiming at {x}, {y}")
            kills += 1
    pygame.draw.circle(win, (255, 0, 0), (388, 445), 7)
    pygame.display.flip()


def move(dirn):
    global bg_pos, persons
    if dirn == "left":
        if bg_pos[0] < 0:
            bg_pos[0] += move_speed
    elif dirn == "right":
        if bg_pos[0] > (bg.get_width() - W) * -1:
            bg_pos[0] -= move_speed
    elif dirn == "up":
        if bg_pos[1] < 0:
            bg_pos[1] += move_speed
    elif dirn == "down":
        if bg_pos[1] > (bg.get_height() - H) * -1:
            bg_pos[1] -= move_speed


def redraw(win, persons):
    win.blit(bg, bg_pos)
    for person in persons:
        person.draw(win, bg_pos)
    win.blit(player_img, (300, H - player_img.get_height()))
    win.blit(font.render(f"Kills: {kills}", 1, (255, 255, 255)), (10, 10))
    loc = font.render(f"Location: {abs(bg_pos[0]) + 388}, {abs(bg_pos[1]) + 445}", 1, (255, 255, 255))
    win.blit(loc, (W - loc.get_width() - 10, 10))
    pygame.display.flip()


def main():
    global bg_pos
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == USEREVENT + 1:
                x = random.randint(388, 1636)
                y = random.randint(445, 677)
                persons.append(Person(x, y, person_img))
                print(f"New person added at {x}, {y}")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            move("left")
        if keys[pygame.K_RIGHT]:
            move("right")
        if keys[pygame.K_UP]:
            move("up")
        if keys[pygame.K_DOWN]:
            move("down")
        if keys[pygame.K_SPACE]:
            shoot(abs(bg_pos[0]) + 388, abs(bg_pos[1]) + 445, persons)
        redraw(win, persons)
        clock.tick(30)


main()
