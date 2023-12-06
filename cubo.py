from typing import Any
import pygame
from pygame.locals import *
from pygame.sprite import Group

class Cubo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_pulo = []
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_1.png'))
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_2.png'))
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_3.png'))
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_4.png'))
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_5.png'))
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_6.png'))
        self.sprites_pulo.append(pygame.image.load('Sprites/Pulo/pulo_7.png'))

        self.sprites_anda = []
        self.sprites_anda.append(pygame.image.load('Sprites/Pulo/pulo_1.png'))
        self.sprites_anda.append(pygame.image.load('Sprites/Andar/sprite_0.png'))
        self.sprites_anda.append(pygame.image.load('Sprites/Andar/sprite_1.png'))
        self.sprites_anda.append(pygame.image.load('Sprites/Andar/sprite_2.png'))
        self.sprites_anda.append(pygame.image.load('Sprites/Andar/sprite_3.png'))
        self.sprites_anda.append(pygame.image.load('Sprites/Andar/sprite_4.png'))
        self.atual = 0
        self.image = self.sprites_anda[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        self.andando = False
        self.pulando = False

    def andar(self):
        self.andando = True

    def parado(self):
        self.andando = False
        self.atual = 0
    
    def pula(self):
        self.pulando = True



    def update(self):
        if self.andando:
            if self.atual >= 5:
                self.atual = 1
                self.andando = False
            self.atual += 0.05
            self.image = self.sprites_anda[int(self.atual)]

        if self.pulando:
            if self.atual >= 6:
                self.atual = 0
                self.pulando = False
            self.atual += 0.1
            self.image = self.sprites_pulo[int(self.atual)]



todas_sprites = pygame.sprite.Group()
cubo = Cubo()
todas_sprites.add(cubo)
