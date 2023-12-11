from typing import Any
import pygame
from pygame.locals import *
from pygame.sprite import Group

class Cubo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        self.sprites.append(pygame.image.load('Sprites/Morte/morte1.png'))
        self.sprites.append(pygame.image.load('Sprites/Morte/morte2.png'))
        self.sprites.append(pygame.image.load('Sprites/Morte/morte3.png'))
        self.atual = 0
        self.personagem = pygame.image.load('Sprites/Morte/alien.png')
        self.personagem = pygame.transform.scale(self.personagem, (self.personagem.get_width()/ 2, self.personagem.get_height() / 2))
        self.image = self.personagem
        self.pos_x = 300
        self.pos_y = 300

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos_x, self.pos_y

        self.pulando = False
        self.on_plataforma = False

        self.gravity = 0.5
        self.heigth = 8
        self.velocity = self.heigth
        self.subindo = False
        self.descendo = False
        self.morre = False
        self.perdeu = False
        self.pontos = 0
        self.tentativas = 1
    
    def sobe(self):
        cubo.subindo = True
    def desce(self):
        cubo.descendo = True
    def colisao(self):
        self.morre = True
        self.tentativas += 1
        self.image = self.sprites[1]
    def moeda(self):
        self.pontos += 1
        



    def update(self):
        if self.subindo :
            self.pos_y -= 7
            self.rect.topleft = self.pos_x, self.pos_y
            self.subindo = False
        if self.descendo:
            self.pos_y += 7
            self.rect.topleft = self.pos_x, self.pos_y
            self.descendo = False

        if self.morre:
            self.atual += 0.2
            try:
                self.image = self.sprites[int(self.atual)]
            except:
                self.perdeu = True
                self.morre = False
                self.image = self.personagem

    
        # if self.pulando:
        #     self.gravity = 0.5
        #     self.pos_y -= self.velocity
        #     self.velocity -= self.gravity
        #     self.rect.topleft = self.pos_x, self.pos_y
        #     if self.velocity < -self.heigth:
        #         self.pulando = False
        #         self.gravity = 0.5
        #         self.heigth = 8
        #         self.velocity = self.heigth
        #         self.rect.topleft = self.pos_x, self.pos_y
        # if self.on_plataforma == False:
        #     self.pos_y = 742

class Brilho(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprites_anda = []
        self.atual = 0
        self.image = self.sprites_anda[self.atual]

        self.pos_x = 252
        self.pos_y = 742

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos_x, self.pos_y

        self.andando = False
        self.pulando = False

        self.gravity = 0.4
        self.heigth = 12
        self.velocity = self.heigth

    def andar(self):
        self.andando = True

    def parado(self):
        self.andando = False
        self.atual = 0
        self.image = self.sprites_anda[self.atual]
    
    def pula(self):
        self.pulando = True

    def update(self):

        if self.andando:
            if self.pos_y >= 742:
                if self.atual >= 4:
                    self.atual = 1
                    self.andando = False
                self.atual += 0.2
                self.image = self.sprites_anda[int(self.atual)]
            else:
                self.image = self.sprites_anda[0]

        if self.pulando:
            self.pos_y -= self.velocity
            self.velocity -= self.gravity
            self.rect.topleft = self.pos_x, self.pos_y
            if self.velocity < -self.heigth:
                self.pulando = False
                self.gravity = 0.7
                self.heigth = 12
                self.velocity = self.heigth
                self.pos_y = 742
                self.rect.topleft = self.pos_x, self.pos_y

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y, tipo):
        pygame.sprite.Sprite.__init__(self)
        if tipo == 'a':
            self.image = pygame.image.load('imagens/2triB.png')
        elif tipo == 'b':
            self.image = pygame.image.load('imagens/2triC.png')
        elif tipo == 'c':
            self.image = pygame.image.load('imagens/6triB.png')
        elif tipo == 'd':
            self.image = pygame.image.load('imagens/6triC.png')
        elif tipo == 'e':
            self.image = pygame.image.load('imagens/ConstrucaoB.png')
        elif tipo == 'f':
            self.image = pygame.image.load('imagens/ConstrucaoC.png')
        elif tipo == 'g':
            self.image = pygame.image.load('imagens/CorrenteB.png')
        elif tipo == 'h':
            self.image = pygame.image.load('imagens/CorrenteC.png')
        elif tipo == 'i':
            self.image = pygame.image.load('imagens/EspinhoHE.png')
        elif tipo == 'j':
            self.image = pygame.image.load('imagens/EspinhoVB.png')
        elif tipo == 'k':
            self.image = pygame.image.load('imagens/EspinhoVC.png')
        elif tipo == 'l':
            self.image = pygame.image.load('imagens/MuroC.png')
        elif tipo == 'm':
            self.image = pygame.image.load('imagens/MuroB.png')
        elif tipo == 'n':
            self.image = pygame.image.load('imagens/EspinhoHC.png')        

        self.image = pygame.transform.scale(self.image, (self.image.get_width()/ 1.5, self.image.get_height() / 1.5))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = (x, y)
        self.movement = 10


    def update_x(self):
        self.rect.x -= self.movement

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagens/coin.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/ 1.5, self.image.get_height() / 1.5))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = (x, y)
        self.movement = 10

    def update_x(self):
        self.rect.x -= self.movement


        

# Fase 1
# Espinhos 
obstaculos1 = pygame.sprite.Group()
coins1 = pygame.sprite.Group()

obstaculos1.add(Spike(x=600, y=0, tipo='a'))
obstaculos1.add(Spike(x=760, y=0, tipo='e'))
obstaculos1.add(Spike(x=880, y=450, tipo='k'))
obstaculos1.add(Spike(x=1300, y=533, tipo='f'))
obstaculos1.add(Spike(x=1635, y=667, tipo='b'))
obstaculos1.add(Spike(x=2000, y=250, tipo='j'))
obstaculos1.add(Spike(x=2800, y=250, tipo='j'))
obstaculos1.add(Spike(x=2400, y=450, tipo='k'))
obstaculos1.add(Spike(x=3200, y=450, tipo='k'))
obstaculos1.add(Spike(x=3080, y=0, tipo='e'))
obstaculos1.add(Spike(x=3600, y=250, tipo='j'))

coins1.add(Coin(x=900, y=200))
coins1.add(Coin(x=2100, y=60))
coins1.add(Coin(x=3400, y=540))
# MOEDAS FASE 1 (940, "300") (2100, 60) (3100, 540)



# Fase 2
# Espinhos 
obstaculos2 = pygame.sprite.Group()


obstaculos2.add(Spike(x=750, y=130, tipo='c'))
obstaculos2.add(Spike(x=750, y=530, tipo='d'))
obstaculos2.add(Spike(x=1600, y=450, tipo='l'))
obstaculos2.add(Spike(x=2000, y=450, tipo='l'))
obstaculos2.add(Spike(x=2400, y=450, tipo='l'))
obstaculos2.add(Spike(x=2800, y=450, tipo='l'))
obstaculos2.add(Spike(x=2000, y=25, tipo='n'))
obstaculos2.add(Spike(x=1800, y=100, tipo='m'))
obstaculos2.add(Spike(x=2400, y=25, tipo='n'))
obstaculos2.add(Spike(x=2200, y=100, tipo='m'))
obstaculos2.add(Spike(x=2800, y=25, tipo='n'))
obstaculos2.add(Spike(x=2600, y=100, tipo='m'))
obstaculos2.add(Spike(x=3000, y=100, tipo='m'))
obstaculos2.add(Spike(x=3500, y=25, tipo='n'))
obstaculos2.add(Spike(x=3500, y=225, tipo='n'))
obstaculos2.add(Spike(x=3500, y=400, tipo='n'))
obstaculos2.add(Spike(x=3500, y=550, tipo='n'))
obstaculos2.add(Spike(x=3500, y=700, tipo='n'))
obstaculos2.add(Spike(x=4200, y=40, tipo='n'))
obstaculos2.add(Spike(x=4200, y=165, tipo='n'))
obstaculos2.add(Spike(x=4200, y=290, tipo='n'))
obstaculos2.add(Spike(x=4200, y=500, tipo='n'))
obstaculos2.add(Spike(x=4200, y=625, tipo='n'))




# Fase 3
# Espinhos 
obstaculos3 = pygame.sprite.Group()

obstaculos3.add(Spike(x=800, y=580, tipo='h'))
obstaculos3.add(Spike(x=800, y=20, tipo='h'))
obstaculos3.add(Spike(x=800, y=638, tipo='g'))
obstaculos3.add(Spike(x=800, y=80, tipo='g'))
obstaculos3.add(Spike(x=950, y=310, tipo='i'))
obstaculos3.add(Spike(x=1300, y=160, tipo='i'))
obstaculos3.add(Spike(x=1300, y=460, tipo='i'))
# moeda (1455, 180)
obstaculos3.add(Spike(x=1670, y=150, tipo='i'))
obstaculos3.add(Spike(x=1750, y=240, tipo='i'))
obstaculos3.add(Spike(x=1810, y=340, tipo='i'))
obstaculos3.add(Spike(x=2070, y=150, tipo='i'))
obstaculos3.add(Spike(x=2070, y=480, tipo='i'))
#moeda (2270, 500)
obstaculos3.add(Spike(x=2520, y=200, tipo='i'))
obstaculos3.add(Spike(x=2520, y=500, tipo='i'))
# moeda (2670, 220)
obstaculos3.add(Spike(x=2820, y=150, tipo='i'))
obstaculos3.add(Spike(x=2820, y=400, tipo='i'))
obstaculos3.add(Spike(x=2820, y=500, tipo='i'))
obstaculos3.add(Spike(x=2970, y=250, tipo='i'))
obstaculos3.add(Spike(x=3320, y=200, tipo='i'))
obstaculos3.add(Spike(x=3420, y=400, tipo='i'))
obstaculos3.add(Spike(x=3620, y=300, tipo='i'))
# moeda ( 3750, 300)


todas_sprites = pygame.sprite.Group()
cubo = Cubo()
todas_sprites.add(cubo)
