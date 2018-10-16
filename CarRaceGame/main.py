import pygame
import random
from pygame.locals import *
import time

pygame.init()

size = width,height = 820,600

white = 255,255,255
red = 255,0,0
blue = 0,0,255

screen = pygame.display.set_mode(size)

backgroundImage = pygame.image.load('assets/bg_1.jpg')
backgroundImage2 = pygame.image.load('assets/bg_2.jpg')

myCar = pygame.image.load("assets/car_1.png")
myCarRect = myCar.get_rect()
oppCar_1 = pygame.image.load("assets/car_2.png")
oppCar_1Rect = oppCar_1.get_rect()
oppCar_2 = pygame.image.load("assets/car_3.png")
oppCar_2Rect = oppCar_2.get_rect()

mainBg = pygame.image.load("assets/mainBg.jpg")
startGame = pygame.image.load("assets/startGame.png")

finish_line = pygame.image.load("assets/finish_line.jpg")

theme = pygame.mixer.Sound('assets/bh_main.wav')
theme.play(-1)

clock = pygame.time.Clock()
FPS = 30

def homeScreen():
    while True:
        screen.fill(white)
        posX,posY = pygame.mouse.get_pos()
        startGameRect = pygame.Rect(590, 200, startGame.get_width(), startGame.get_height())
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if posX > startGameRect.left and posX < startGameRect.right and posY < startGameRect.bottom and posY > startGameRect.top:
                    mainGame()

        screen.blit(mainBg, (0,0))
        screen.blit(startGame, (590, 200))

        pygame.display.update()



def speedText(speed):
    font = pygame.font.Font(None, 40)
    text = font.render("Speed : "+str(speed), True, red)
    screen.blit(text, (width - 190, 20))

def timer(seconds):
    font = pygame.font.Font('zerovelo.ttf', 20)
    seconds_display = font.render("Time Left: " + str(seconds), 1, blue)
    screen.blit(seconds_display, (width-210, 60))

def mainGame():
    backgroundY = 0
    backgroundY2 = -height

    moveBackground = 2
    carX = width/2 - 10
    carY = height - 140

    moveCarPos = 0

    oppCar_1X = width/2 - 85
    oppCar_1Y = height - 140

    oppCar_2X = width/2 + 65
    oppCar_2Y = height - 140

    moveCar1 = random.randint(-2,-1)
    moveCar2 = random.randint(-2,-1)
    
    finish_y = -100

    speed = 10

    seconds = 20
    pygame.time.set_timer(USEREVENT + 1, 1000)

    game = True
    race = True

    while game:

        screen.fill(white)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT + 1:
                seconds -= 1

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP:
            #         moveBackground += 5
            #         moveCarPos += 5
            #         moveCar1 = random.randint(-6,-1)
            #         moveCar2 = random.randint(-6,-1)
            #     elif event.key == pygame.K_DOWN:
            #         moveBackground -= 5
            # if event.type == pygame.KEYUP:
            #     moveCarPos = 0
            if event.type == pygame.KEYUP:
                speed = moveBackground + 10

        keystate = pygame.key.get_pressed()
        if race:

            if keystate[pygame.K_UP]:
                moveBackground += 0.3
                moveCarPos += 0.2
                speed += 1
                # moveCar1 = random.randint(-2,-1)
                # moveCar2 = random.randint(-2,-1)
            elif keystate[pygame.K_DOWN]:
                moveBackground -= 1
                moveCarPos = 0

        if seconds == -1:
            seconds = 0
            race = False
            print("Game Over")
            moveBackground -= 10
            moveCarPos = 0
            moveCar1 = 0
            moveCar2 = 0
            speed -= 20
            print(moveBackground)

        # print(moveBackground)

        screen.blit(backgroundImage, (0,0))
        screen.blit(backgroundImage, (0,backgroundY))
        screen.blit(backgroundImage2, (0,backgroundY2))

        if seconds <= 2:
            finish_y += 10
            
        screen.blit(finish_line, (300,finish_y))

        carY -= moveCarPos

        oppCar_1Y += moveCar1
        oppCar_2Y += moveCar2

        screen.blit(myCar, (carX, carY))
        screen.blit(oppCar_1, (oppCar_1X, oppCar_1Y))
        screen.blit(oppCar_2, (oppCar_2X, oppCar_2Y))

        speedText(speed)
        timer(seconds)

        if carY > height - 140 or carY < height/2 - 100:
            moveCarPos = 0

        if moveBackground >= 50:
            moveBackground = 50
        elif moveBackground <= 0:
            moveBackground = 0

        if speed <= 0:
            speed = 0

        if oppCar_1Y  < -100:
            moveCar1 = random.randint(1,3)
        elif oppCar_1Y > height:
            moveCar1 = random.randint(-3,-1)

        if oppCar_2Y < -100:
            moveCar2 = random.randint(2,4)
        elif oppCar_2Y > height:
            moveCar2 = random.randint(-4,-2)

        if speed >= 300:
            speed = 300

        backgroundY += moveBackground
        backgroundY2 += moveBackground

        if backgroundY > height:
            backgroundY = -height + 10
        elif backgroundY2 > height:
            backgroundY2 = -height + 10

        pygame.display.update()
        clock.tick(FPS)

homeScreen()
# mainGame()
