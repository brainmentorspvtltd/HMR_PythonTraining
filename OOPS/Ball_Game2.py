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
        self.moveX = random.randint(1,3)
        self.moveY = random.randint(1,3)

    def moveBall(self):
        self.x += self.moveX
        self.y += self.moveY

    def checkBoundary(self):

        if self.x > width - self.radius:
            self.moveX = -(random.randint(1,3))
        elif self.y > height - self.radius:
            self.moveY = -(random.randint(1,3))
        elif self.x < self.radius:
            self.moveX = random.randint(1, 5)
        elif self.y < self.radius:
            self.moveY = random.randint(1, 5)

# no = input("Enter number of balls : ")

ballList = []

for i in range(100):
    ball = Ball()
    ballList.append(ball)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    for i in range(len(ballList)):
        pygame.draw.circle(screen,red,[ballList[i].x,ballList[i].y],ballList[i].radius)
        ballList[i].moveBall()
        ballList[i].checkBoundary()

    pygame.display.update()