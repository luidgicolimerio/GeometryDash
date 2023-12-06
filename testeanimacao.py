import pygame
from pygame.locals import *
from sys import exit

from cubo import todas_sprites, cubo

pygame.init()

largura = 640
altura = 480

PRETO = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('Sprites')

clock = pygame.time.Clock()

while True:
    tela.fill(PRETO)
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        cubo.andar()
    else:
        cubo.parado()

    

    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()