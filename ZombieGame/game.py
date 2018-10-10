import pygame
import random

pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))

bg_img = pygame.image.load("images/background.png")

zombieList = []

for i in range(4):
    zombie = pygame.image.load("images/zombie_{}.png".format(i+1))
    zombieList.append(zombie)

zombieImage = random.choice(zombieList)
zombieHeight = zombieImage.get_height()
zombieWidth = zombieImage.get_width()

random_x = random.randrange(0, width - zombieWidth)
random_y = random.randrange(0, height - zombieHeight)

game = True
gun_aim = pygame.image.load("images/aim_pointer.png")

gun_image = pygame.image.load("images/gun_1.png")
gun_y = height - 200
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_1.colliderect(rect_2):
                print("Collision")
                zombieImage = random.choice(zombieList)
                random_x = random.randrange(0, width - zombieWidth)
                random_y = random.randrange(0, height - zombieHeight)

    pos_x, pos_y = pygame.mouse.get_pos()
    screen.blit(bg_img, (0,0))
    screen.blit(zombieImage, (random_x, random_y))
    screen.blit(gun_aim, (pos_x - gun_aim.get_width() / 2, pos_y - gun_aim.get_height() / 2))
    screen.blit(gun_image, (pos_x, gun_y))

    rect_1 = pygame.Rect(pos_x, pos_y, gun_aim.get_width(), gun_aim.get_height())
    rect_2 = pygame.Rect(random_x, random_y, zombieImage.get_width(), zombieImage.get_height())

    pygame.display.update()