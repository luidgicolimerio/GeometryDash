from typing import Any
import pygame
from pygame.locals import *
from pygame.sprite import Group
import ranking

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
        self.movement = 5


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
        self.movement = 5

    def update_x(self):
        self.rect.x -= self.movement   

# Fase 1
# Espinhos 
def fase1():

    obstaculos1 = None
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

    return obstaculos1, coins1

# Fase 2
# Espinhos 
def fase2():

    obstaculos2 = None
    obstaculos2 = pygame.sprite.Group()
    coins2 = pygame.sprite.Group()


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
    obstaculos2.add(Spike(x=3500, y=415, tipo='n'))
    obstaculos2.add(Spike(x=3500, y=550, tipo='n'))
    obstaculos2.add(Spike(x=3500, y=700, tipo='n'))
    obstaculos2.add(Spike(x=4200, y=40, tipo='n'))
    obstaculos2.add(Spike(x=4200, y=165, tipo='n'))
    obstaculos2.add(Spike(x=4200, y=290, tipo='n'))
    obstaculos2.add(Spike(x=4200, y=500, tipo='n'))
    obstaculos2.add(Spike(x=4200, y=625, tipo='n'))

    coins2.add(Coin(x=1370, y=110))
    coins2.add(Coin(x=2800, y=200))
    coins2.add(Coin(x=3750, y=395))

    return obstaculos2, coins2


# Fase 3
# Espinhos
def fase3():
 

    obstaculos3 = None
    obstaculos3 = pygame.sprite.Group()
    coins3 = pygame.sprite.Group()

    obstaculos3.add(Spike(x=800, y=580, tipo='h'))
    obstaculos3.add(Spike(x=800, y=20, tipo='h'))
    obstaculos3.add(Spike(x=800, y=638, tipo='g'))
    obstaculos3.add(Spike(x=800, y=80, tipo='g'))
    obstaculos3.add(Spike(x=950, y=310, tipo='i'))
    obstaculos3.add(Spike(x=1300, y=160, tipo='i'))
    obstaculos3.add(Spike(x=1300, y=460, tipo='i'))
    obstaculos3.add(Spike(x=1670, y=150, tipo='i'))
    obstaculos3.add(Spike(x=1750, y=240, tipo='i'))
    obstaculos3.add(Spike(x=1810, y=340, tipo='i'))
    obstaculos3.add(Spike(x=2070, y=150, tipo='i'))
    obstaculos3.add(Spike(x=2070, y=480, tipo='i'))
    obstaculos3.add(Spike(x=2520, y=200, tipo='i'))
    obstaculos3.add(Spike(x=2520, y=500, tipo='i'))
    obstaculos3.add(Spike(x=2820, y=150, tipo='i'))
    obstaculos3.add(Spike(x=2820, y=400, tipo='i'))
    obstaculos3.add(Spike(x=2820, y=500, tipo='i'))
    obstaculos3.add(Spike(x=2970, y=250, tipo='i'))
    obstaculos3.add(Spike(x=3320, y=200, tipo='i'))
    obstaculos3.add(Spike(x=3420, y=400, tipo='i'))
    obstaculos3.add(Spike(x=3620, y=300, tipo='i'))

    coins3.add(Coin(x=1455, y=180))
    coins3.add(Coin(x=2270, y=500))
    coins3.add(Coin(x=2670, y=220))
    coins3.add(Coin(x=3750, y=300))

    return obstaculos3, coins3


todas_sprites = pygame.sprite.Group()
cubo = Cubo()
todas_sprites.add(cubo)
