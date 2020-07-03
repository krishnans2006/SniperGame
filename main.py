import pygame

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
KILLS = 0


def shoot(x, y, persons):
    # for person in persons:
    #     if person.hitbox.collidepoint((x, y)):
    #         person.dead = True
    pygame.draw.circle(win, (255, 0, 0), (388, 445), 7)
    pygame.display.flip()

def redraw(win):
    win.blit(bg, bg_pos)
    win.blit(player_img, (300, H - player_img.get_height()))
    win.blit(person_img, (50, 50))
    win.blit(font.render(f"Kills: {KILLS}", 1, (255, 255, 255)), (10, 10))
    pygame.display.flip()


def main():
    global bg_pos
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            bg_pos[0] += move_speed
        if keys[pygame.K_RIGHT]:
            bg_pos[0] -= move_speed
        if keys[pygame.K_UP]:
            bg_pos[1] += move_speed
        if keys[pygame.K_DOWN]:
            bg_pos[1] -= move_speed
        if keys[pygame.K_SPACE]:
            shoot(500, 325, persons)

        redraw(win)
        clock.tick(30)


main()
