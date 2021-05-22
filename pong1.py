from pygame import *
from random import randint
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, w, h, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.speed_x = self.speed
        self.speed_y = self.speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y>0:
            self.rect.y-=self.speed 
        if key_pressed[K_DOWN] and self.rect.y<500:
            self.rect.y+=self.speed 
class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y>0:
            self.rect.y-=self.speed 
        if key_pressed[K_s] and self.rect.y<500:
            self.rect.y+=self.speed
class Ball(GameSprite):
    def update(self):
        global b
        global c
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y <1 or self.rect.y >549:
            self.speed_y*=-1
        if sprite.collide_rect(ball_1,palka1) or sprite.collide_rect(ball_1,palka2):
            kkk = randint(1,3)
            if kkk == 1:
                udar_1.play()
            if kkk == 2:
                udar_2.play()
            if kkk == 3:
                udar_3.play()
            self.speed_x*=-1
        if self.rect.x > 949:
            c += 1
            self.rect.x = 500
            self.rect.y = 300
            self.speed_x*=-1
            gol.play()
        if self.rect.x < 1:
            b += 1
            self.rect.x = 500
            self.rect.y = 300
            self.speed_x*=-1   
            gol.play()

palka1 =Player('rocket.png',15,100,930,300,3)
palka2 =Player2('rocket.png',15,100,40,300,3)
ball_1 = Ball('ball.png',50,50,500,300,1)


a = (0, 0, 205)
collar = (255,255,255)
collar2 = (0,0,0)
c = 0
b = 0
speed_y = 2
speed_x = 2

mixer.init()
udar_1 = mixer.Sound('udar1.ogg')
udar_2 = mixer.Sound('udar2.ogg')
udar_3 = mixer.Sound('udar3.ogg')
gol = mixer.Sound('gol.ogg')
clock = time.Clock()
finish= False
game = True
font.init()

text = font.SysFont('Arial',100).render(str(c), 1, (collar))
text2 = font.SysFont('Arial',100).render(str(b), 1, (collar))
text3 = font.SysFont('Arial',50).render('!левый победил!', 1, (collar2))
text4 = font.SysFont('Arial',50).render('!правый победил!', 1, (collar2))
window = display.set_mode((1000, 600))
display.set_caption("Bestes Spiel")

window.fill(a)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(a)
    window.blit(text,(150,150))
    window.blit(text2,(700,150))
    if c == 10:
        finish = True
        window.blit(text3,(300,50))
    if b == 10:
        finish = True
        window.blit(text4,(300,50))
    if not(finish):
        ball_1.reset()
        ball_1.update()
        palka1.reset()
        palka1.update()
        palka2.reset()
        palka2.update()
        window.blit
        text = font.SysFont('Arial',300).render(str(c), 1, (collar))
        text2 = font.SysFont('Arial',300).render(str(b), 1, (collar))
    display.update()
    clock.tick(380)