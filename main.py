import pygame

pygame.init()
pygame.font.init()

W = 800
H = 600
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Scarlett Inferno")
clock = pygame.time.Clock()

music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

bg = pygame.image.load("sniper_bg.jpg")
person_img = pygame.image.load() # will be filled in

KILLS = 0


def redraw(win):
    win.blit(bg, (0, 0))
    pygame.display.flip()


def main():
    while True:
        redraw(win)
        clock.tick(30)

main()