import pygame
import random

pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0

class Ball():

    def __init__(self):
        self.radius = 50
        self.x = 0
        self.y = 0
        self.moveX = random.randint(1,5)
        self.moveY = random.randint(1,5)

    def moveBall(self):
        self.x += self.moveX
        self.y += self.moveY

    def checkBoundary(self):

        if self.x > width - self.radius:
            self.moveX = -(random.randint(1,5))
        elif self.y > height - self.radius:
            self.moveY = -(random.randint(1,5))
        elif self.x < self.radius:
            self.moveX = random.randint(1, 5)
        elif self.y < self.radius:
            self.moveY = random.randint(1, 5)

ball_1 = Ball()
ball_2 = Ball()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    pygame.draw.circle(screen,red,[ball_1.x,ball_1.y],ball_1.radius)
    ball_1.moveBall()
    ball_1.checkBoundary()

    pygame.draw.circle(screen, red, [ball_2.x, ball_2.y], ball_2.radius)
    ball_2.moveBall()
    ball_2.checkBoundary()

    pygame.display.update()