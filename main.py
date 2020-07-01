import pygame
pygame.init()
pygame.font.init()

W = 800
H = 600
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Scarlett Inferno")
clock = pygame.time.Clock()

bg = pygame.image.load("sniper_bg.jpg")
playerImg = pygame.image.load("player.png")
person_img = pygame.image.load() # will be filled in

KILLS = 0


def redraw(win):
    win.blit(bg, (0, 0))
    pygame.display.flip()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        redraw(win)
        clock.tick(30)


main()