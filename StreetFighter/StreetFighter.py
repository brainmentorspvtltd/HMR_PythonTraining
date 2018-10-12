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
    standingFrames = []
    punchFrames = []
    kickFrames = []

    def __init__(self):
        super().__init__()
        spritesheet = Spritesheet(player_sprite)

        self.image = spritesheet.getImage(48, 247, 106, 239)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(264, 240, 113, 249)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(482, 248, 106, 237)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(687, 247, 112, 241)
        self.standingFrames.append(self.image)

        self.image = spritesheet.getImage(42, 247, 116, 243)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(44, 731, 118, 243)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(256, 731, 118, 243)
        self.walking_frames.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = (width / 2 - 250, height / 2 + 70)

        self.pos = 0

    def update(self):
        self.pos += 5

        frame = (self.pos // 30) % len(self.standingFrames)
        # print("Position",self.pos//30)
        # print("Frame",frame)
        self.image = self.standingFrames[frame]

player_sprite = pygame.image.load("images/ken_.png")

all_sprites = pygame.sprite.Group()
player = Player_1()

ken = pygame.sprite.Group()
ken.add(player)

all_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.blit(background,(0,0))

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()