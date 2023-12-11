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
    
    def sobe(self):
        cubo.subindo = True
    def desce(self):
        cubo.descendo = True
    def colisao(self):
        self.morre = True
        self.image = self.sprites[1]



    def update(self):
        if self.subindo :
            self.pos_y -= 6
            self.rect.topleft = self.pos_x, self.pos_y
            self.subindo = False
        if self.descendo:
            self.pos_y += 6
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
        

        self.image = pygame.transform.scale(self.image, (self.image.get_width()/ 1.5, self.image.get_height() / 1.5))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = (x, y)
        self.movement = 5


    def update_x(self):
        self.rect.x -= self.movement

        

# Fase 1
# Espinhos 
obstaculos1 = pygame.sprite.Group()

obstaculos1.add(Spike(x=600, y=0, tipo='a'))
obstaculos1.add(Spike(x=760, y=0, tipo='e'))
obstaculos1.add(Spike(x=880, y=600, tipo='k'))
obstaculos1.add(Spike(x=1300, y=533, tipo='f'))
obstaculos1.add(Spike(x=1635, y=667, tipo='b'))
obstaculos1.add(Spike(x=2000, y=40, tipo='j'))
obstaculos1.add(Spike(x=2800, y=40, tipo='j'))
obstaculos1.add(Spike(x=2400, y=600, tipo='k'))
obstaculos1.add(Spike(x=3200, y=600, tipo='k'))
obstaculos1.add(Spike(x=3080, y=0, tipo='e'))
obstaculos1.add(Spike(x=3600, y=40, tipo='j'))

# MOEDAS FASE 1 (940, "300") (2100, 60) (3100, 540)





# Fase 2
# Espinhos 
obstaculos2 = pygame.sprite.Group()

obstaculos2.add(Spike(x=600, y=754, tipo='l'))


# obstaculos2.add(Spike(x=600, y=754))
# obstaculos2.add(Spike(x=632, y=754))
# obstaculos2.add(Spike(x=664, y=754))
# obstaculos2.add(Spike(x=820, y=754))
# obstaculos2.add(Spike(x=852, y=754))
# obstaculos2.add(Spike(x=1160, y=754))
# obstaculos2.add(Spike(x=1576, y=754))
# obstaculos2.add(Spike(x=1673, y=754))
# obstaculos2.add(Spike(x=2073, y=754))
# obstaculos2.add(Spike(x=2106, y=754))
# obstaculos2.add(Spike(x=2139, y=754))
# obstaculos2.add(Spike(x=2273, y=754))
# obstaculos2.add(Spike(x=2306, y=754))
# obstaculos2.add(Spike(x=2339, y=754))
# obstaculos2.add(Spike(x=2700, y=754))
# obstaculos2.add(Spike(x=2748, y=754))
# obstaculos2.add(Spike(x=2796, y=754))
# obstaculos2.add(Spike(x=2844, y=754))
# obstaculos2.add(Spike(x=2892, y=754))
# obstaculos2.add(Spike(x=2943, y=754))


# # Fase 3
# # Espinhos 
# obstaculos3 = pygame.sprite.Group()
# obstaculos3.add(Spike(x=1243, y=570))
# obstaculos3.add(Spike(x=1313, y=690))
# obstaculos3.add(Spike(x=1345, y=690))
# obstaculos3.add(Spike(x=1439, y=690))

todas_sprites = pygame.sprite.Group()
cubo = Cubo()
todas_sprites.add(cubo)
