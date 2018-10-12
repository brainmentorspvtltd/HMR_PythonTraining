import pygame
pygame.init()
width = 1200
height = 600
screen = pygame.display.set_mode((width,height))
background = pygame.image.load("images/background.png")

black = 0,0,0
class Spritesheet():
    def __init__(self, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet = file_name
    def getImage(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.spriteSheet, (0,0), (x, y, width, height))
        image.set_colorkey(black)

        return image

class Player_1(pygame.sprite.Sprite):
    walking_frames = []
    def __init__(self):
        super().__init__()
        spritesheet = Spritesheet(player_sprite)
        self.image = spritesheet.getImage(42, 247, 116, 243)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(44, 731, 118, 243)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(256, 731, 118, 243)
        self.walking_frames.append(self.image)

player_sprite = pygame.image.load("images/ken_.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.blit(background,(0,0))
    pygame.display.update()