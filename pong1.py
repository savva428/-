from pygame import *
from random import randint
from time import time as timer
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, w, h, player_x, player_y, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x>5:
            self.rect.x-=self.speed 
        if key_pressed[K_RIGHT] and self.rect.x<715:
            self.rect.x+=self.speed 

#Игровая сцена:
finish= False
game = True
window = display.set_mode((1000, 600))
display.set_caption("Bestes Spiel")
window.fill((randint(0,255),randint(0,255),randint(0,255)))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not(finish):
        window.blit
        display.update()
    