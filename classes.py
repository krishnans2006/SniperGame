import pygame


class Person:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.shooting = False
        self.isJump = False
        self.left = False
        self.right = False
        self.width = 100
        self.height = 300
        self.vel = 5
        keys = pygame.key.get_pressed()

    def draw(self, win):
        keys = pygame.key.get_pressed()
        player = pygame.image.load("player.png")
        win.blit(self.img, (self.x, self.y))
        if keys[pygame.K_LEFT] and player.x > player.vel:
            player.x -= player.vel
            player.left = True
            player.right = False
            player.standing = False
        elif keys[pygame.K_RIGHT] and player.x < 500 - player.width - player.vel:
            player.x += player.vel
            player.right = True
            player.left = False
            player.standing = False
        else:
            player.standing = True
            player.walkCount = 0

        if not player.isJump:
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                player.isJump = True
                player.right = False
                player.left = False
        else:
            if player.jumpCount >= -10:
                neg = 1
                if player.jumpCount < 0:
                    neg = -1
                player.y -= (player.jumpCount ** 2) * 0.5 * neg
                player.jumpCount -= 1
            else:
                player.isJump = False
                player.jumpCount = 10