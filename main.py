import pygame
import time
pygame.init()
pygame.font.init()
pygame.mixer.init()
time.sleep()

W = 800
H = 600
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Scarlett Inferno")
clock = pygame.time.Clock()

bg = pygame.image.load("sniper_bg.jpg")
# person_img = pygame.image.load() # will be filled in

KILLS = 0


def redraw(win):
    win.blit(bg, (0, 0))
    pygame.display.flip()


def main():
    music = pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.set_volume(40)
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        redraw(win)
        clock.tick(30)


main()