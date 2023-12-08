from typing import Any
import pygame
from pygame.locals import *
from pygame.sprite import Group

class Cubo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_pulo = []
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_0.png'))
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_1.png'))
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_2.png'))
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_3.png'))
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_4.png'))
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_5.png'))
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_6.png'))
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_7.png'))

        self.sprites_anda = []
        self.sprites_anda.append(pygame.image.load('Sprites/Andar/sprite_0.png'))
        self.sprites_anda.append(pygame.image.load('Sprites/Andar/sprite_1.png'))
        self.sprites_anda.append(pygame.image.load('Sprites/Andar/sprite_2.png'))
        self.sprites_anda.append(pygame.image.load('Sprites/Andar/sprite_3.png'))
        self.sprites_anda.append(pygame.image.load('Sprites/Andar/sprite_4.png'))
        self.atual = 0
        self.image = self.sprites_anda[self.atual]

        self.pos_x = 300
        self.pos_y = 742

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos_x, self.pos_y

        self.andando = False
        self.pulando = False

        self.gravity = 0.6
        self.heigth = 12
        self.velocity = self.heigth

    def andar(self):
        self.andando = True

    def parado(self):
        self.andando = False
        self.atual = 0
        self.image = self.sprites_pulo[self.atual]
    
    def pula(self):
        self.pulando = True

    def update(self):
        if self.andando:
            if self.atual >= 4:
                self.atual = 1
                self.andando = False
            self.atual += 0.05
            self.image = self.sprites_anda[int(self.atual)]

        if self.pulando:
            self.pos_y -= self.velocity
            self.velocity -= self.gravity
            self.rect.topleft = self.pos_x, self.pos_y
            if self.velocity < -self.heigth:
                self.pulando = False
                self.gravity = 0.6
                self.heigth = 12
                self.velocity = self.heigth
                self.pos_y = 742
                self.rect.topleft = self.pos_x, self.pos_y

class Spike(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('triangulo.png')
        self.rect = self.image.get_rect()
        



colisao_sprites = pygame.sprite.Group()
todas_sprites = pygame.sprite.Group()
cubo = Cubo()
spike = Spike()
todas_sprites.add(cubo)
todas_sprites.add(spike)
