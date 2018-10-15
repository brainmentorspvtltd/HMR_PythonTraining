import pygame
from pygame.locals import *

pygame.init()
width = 1200
height = 600
screen = pygame.display.set_mode((width,height))
background = pygame.image.load("images/background.png")

black = 0,0,0
blue = 0,0,255
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
    superKickFrame = []

    isAttack = False
    health = 450

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

        self.image = spritesheet.getImage(42, 490, 118, 240)
        self.punchFrames.append(self.image)
        self.image = spritesheet.getImage(260, 489, 166, 240)
        self.punchFrames.append(self.image)
        self.image = spritesheet.getImage(472, 487, 122, 245)
        self.punchFrames.append(self.image)

        self.image = spritesheet.getImage(250, 1451, 118, 250)
        self.kickFrames.append(self.image)
        self.image = spritesheet.getImage(428, 1457, 208, 248)
        self.kickFrames.append(self.image)
        self.image = spritesheet.getImage(676, 1461, 120, 244)
        self.kickFrames.append(self.image)

        self.image = spritesheet.getImage(18, 1701, 116, 248)
        self.superKickFrame.append(self.image)
        self.image = spritesheet.getImage(212, 1705, 172, 240)
        self.superKickFrame.append(self.image)
        self.image = spritesheet.getImage(426, 1707, 216, 238)
        self.superKickFrame.append(self.image)
        self.image = spritesheet.getImage(658, 1737, 188, 210)
        self.superKickFrame.append(self.image)
        self.image = spritesheet.getImage(898, 1727, 118, 218)
        self.superKickFrame.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = (width / 2 - 250, height / 2 + 70)

        self.pos = 0

        self.stand = True
        self.walk = False
        self.kick = False
        self.punch = False
        self.superKick = False

    def update(self):
        self.pos += 2

        self.moveX = 0

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_d]:
            self.walk = True
            self.moveX = 3
        elif keypressed[pygame.K_a]:
            self.walk = True
            self.moveX = -3
        elif keypressed[pygame.K_w]:
            self.punch = True
        elif keypressed[pygame.K_s]:
            self.kick = True
        elif keypressed[pygame.K_f]:
            self.superKick = True
        else:
            self.walk = False
            self.punch = False
            self.kick = False
            self.superKick = False
            self.moveX = 0

        self.rect.x += self.moveX

        frame = (self.pos // 30) % len(self.standingFrames)
        # print("Position",self.pos//30)
        # print("Frame",frame)
        self.image = self.standingFrames[frame]

        self.hit = pygame.sprite.groupcollide(ken, ryu, False, False)

        if self.walk:
            frame = (self.pos // 30) % len(self.walking_frames)
            self.image = self.walking_frames[frame]
        elif self.punch:
            frame = (self.pos // 30) % len(self.punchFrames)
            self.image = self.punchFrames[frame]

            if self.hit:
                self.isAttack = True
                punchSound.play()
                player_2.health -= 1

        elif self.kick:
            frame = (self.pos // 30) % len(self.kickFrames)
            self.image = self.kickFrames[frame]

            if self.hit:
                self.isAttack = True
                punchSound.play()
                player_2.health -= 3

        elif self.superKick:
            frame = (self.pos // 30) % len(self.superKickFrame)
            self.image = self.superKickFrame[frame]

            if self.hit:
                self.isAttack = True
                punchSound.play()
                player_2.health -= 5

class Player_2(pygame.sprite.Sprite):

    standingFrames = []
    walking_frames = []
    punch_frames = []
    kick_frames = []
    super_kick_frames = []
    hit_frames = []

    health = 450
    isAttack = False

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        spritesheet = Spritesheet(player_sprite_2)

        self.image = spritesheet.getImage(2959, 41, 105, 228)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(2751, 38, 99, 230)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(2557, 34, 104, 236)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(2358, 40, 108, 228)
        self.standingFrames.append(self.image)

        self.image = spritesheet.getImage(2750,41,102,226)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(2756,317,110,224)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(2394,315,94,226)
        self.walking_frames.append(self.image)

        self.image = spritesheet.getImage(2737,1219,130,238)
        self.punch_frames.append(self.image)
        self.image = spritesheet.getImage(2492,1213,184,240)
        self.punch_frames.append(self.image)
        self.image = spritesheet.getImage(2492,1213,184,240)
        self.punch_frames.append(self.image)
        self.image = spritesheet.getImage(2300,1219,130,236)
        self.punch_frames.append(self.image)
        self.image = spritesheet.getImage(2108,1225,112,232)
        self.punch_frames.append(self.image)

        self.image = spritesheet.getImage(1012,905,94,228)
        self.kick_frames.append(self.image)
        self.image = spritesheet.getImage(811,878,135,252)
        self.kick_frames.append(self.image)

        self.image = spritesheet.getImage(58,217,96,267)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(216,260,136,219)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(394,332,212,118)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(646,282,92,200)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(806,365,180,111)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(1026,300,98,258)
        self.super_kick_frames.append(self.image)

        self.image = spritesheet.getImage(1174,1571,144,242)
        self.hit_frames.append(self.image)
        self.image = spritesheet.getImage(1375,1583,123,226)
        self.hit_frames.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = (width/2+250, height/2+90)

        self.punchActive = 0
        self.kickActive = 0
        self.superKickActive = 0

        self.pos = 0

    def update(self):
        self.pos += 2
        self.speedx = 0

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_j]:
            self.speedx = -3
            self.walk = True
        elif keypressed[pygame.K_l]:
            self.speedx = 3
            self.walk = True
        elif keypressed[pygame.K_k]:
            self.punch = True
        elif keypressed[pygame.K_i]:
            self.kick = True
        elif keypressed[pygame.K_h]:
            self.superKick = True
        else:
            self.superKick = False
            self.punch = False
            self.kick = False
            self.walk = False

        self.rect.x += self.speedx
        frame = (self.pos // 30) % len(self.standingFrames)
        self.image = self.standingFrames[frame]

        self.hit = pygame.sprite.groupcollide(ryu, ken, False, False)

        if self.walk:
            frame = (self.pos // 30) % len(self.walking_frames)
            self.image = self.walking_frames[frame]

        if self.punch:
            frame = (self.pos // 30) % len(self.punch_frames)
            self.image = self.punch_frames[frame]

            if self.hit:
                self.isAttack = True
                punchSound.play()
                player.health -= 1

        if self.kick:
            frame = (self.pos // 30) % len(self.kick_frames)
            self.image = self.kick_frames[frame]

            if self.hit:
                self.isAttack = True
                punchSound.play()
                player.health -= 3

        if self.superKick:
            frame = (self.pos // 30) % len(self.super_kick_frames)
            self.image = self.super_kick_frames[frame]

            if self.hit:
                self.isAttack = True
                punchSound.play()
                player.health -= 5

pygame.time.set_timer(USEREVENT,1000)

def timer(seconds):
    red = 255,0,0
    font = pygame.font.Font('Digital_tech.otf', 50)
    text = font.render("{}".format(str(seconds)), True, red)
    screen.blit(text, (520,10))

clock = pygame.time.Clock()
FPS = 90

player_sprite = pygame.image.load("images/ken_.png")
player_sprite_2 = pygame.image.load("images/ryu_.png")

punchSound = pygame.mixer.Sound("sounds/punch2.wav")
backgroundSound = pygame.mixer.Sound("sounds/StreetFighter.ogg")
backgroundSound.play(-1)

all_sprites = pygame.sprite.Group()
player = Player_1()
player_2 = Player_2()

ken = pygame.sprite.Group()
ken.add(player)

ryu = pygame.sprite.Group()
ryu.add(player_2)

all_sprites.add(player)
all_sprites.add(player_2)

def kenHealth():
    pygame.draw.rect(screen, blue, [10,10,player.health,40])

def ryuHealth():
    pygame.draw.rect(screen, blue, [width - 490,10,player_2.health,40])


def homeScreen():
    image_1 = pygame.image.load("images/image_1.jpg")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()

        screen.blit(image_1, (0,0))
        pygame.display.update()

def main():
    seconds = 30
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == USEREVENT:
                seconds -= 1

        screen.blit(background,(0,0))

        all_sprites.update()
        all_sprites.draw(screen)

        kenHealth()
        ryuHealth()

        timer(seconds)

        pygame.display.update()
        clock.tick(FPS)

homeScreen()