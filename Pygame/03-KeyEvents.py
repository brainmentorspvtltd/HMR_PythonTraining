import pygame
import random

pygame.init()

width = 800
height = 500

red = 255,0,0
black = 0,0,0

screen = pygame.display.set_mode((width, height))

frog = pygame.image.load("frog.png")

x = 0
y = 0

moveX = 0
moveY = 0

random_x = random.randrange(0, width - 50)
random_y = random.randrange(0, height - 50)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0
    
    screen.fill(red)
    
    rect_1 = pygame.draw.rect(screen, black, [x,y,50,50])
    #rect_2 = pygame.draw.rect(screen, black, [random_x,random_y,50,50])
    rect_2 = pygame.Rect(random_x,random_y,50,50)

    screen.blit(frog, (random_x,random_y))

    x += moveX
    y += moveY

    if rect_1.colliderect(rect_2):
        #print("Collision detection")
        random_x = random.randrange(0, width - 50)
        random_y = random.randrange(0, height - 50)

    if x > width:
        moveX = -1
    elif y > height:
        moveY = -1
    elif x < 0:
        moveX = 1
    elif y < 0:
        moveY = 1
    
    pygame.display.update()







    
