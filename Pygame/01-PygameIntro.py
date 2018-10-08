import pygame

pygame.init()

width = 800
height = 500

red = 255,0,0
black = 0,0,0

# will display the screen
screen = pygame.display.set_mode((width, height))

# to hold the screen
while True:

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # fill the color on screen
    screen.fill(red)

    # surface, color, [x,y,w,h]
    pygame.draw.rect(screen, black, [0,0,100,100])

    # surface, color, [x,y], radius
    pygame.draw.circle(screen, black, [200,200], 80)

    # update the screen
    pygame.display.update()







    
