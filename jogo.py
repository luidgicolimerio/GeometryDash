import pygame
import math
from pygame.locals import *
from sys import exit
from cubo import todas_sprites, cubo




width = 1200
height = 900


def load():
    global sys_font, clock, px, cl1, cl2, cl3, cl, fundo,tiles, fundo_width,scroll, fundo_rect
    
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    clock = pygame.time.Clock()
    px = 0
    cl1 = 100
    cl2 = 150
    cl3 = 250
    cl = 0


    fundo = pygame.image.load('Frame1.PNG').convert()
    fundo_width = fundo.get_width()
    fundo_rect = fundo.get_rect()

    
    scroll = 0
    tiles = math.ceil(width  / fundo_width) + 1
    


def draw_screen(screen):
    global cl1, cl2, cl3, cl, fundo
    screen.fill((100,160,255))
    
    t = sys_font.render(' ', False, (0,0,0))
    screen.blit(t, t.get_rect(top = 290, left = px))

    screen.blit(fundo, (0,0))


    




def update(dt):
    global px, cl1, cl2, cl3, clock, cl, scroll

    for i in range(0, tiles):
        screen.blit(fundo, (i * fundo_width + scroll, 0))
        fundo_rect.x = i * fundo_width + scroll
        pygame.draw.rect(screen, (255, 0, 0), fundo_rect, 1)

          #scroll background
        scroll = scroll - 1.33

          #reset scroll
        if abs(scroll) > fundo_width:
            scroll = 0


    pygame.draw.rect(screen, (255, 130, 130), (0, 790, 2000, 2000))
    pygame.draw.rect(screen, (255, 100, 100), (0, 800, 2000, 2000))

    
    todas_sprites.draw(screen)
    todas_sprites.update()
    pygame.display.flip()






def main_loop(screen):  
    global clock, width, scroll, fundo
    running = True
    while running:
    

        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                running = False
                break

            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            cubo.andar()
        else:
            cubo.parado()





        # Define FPS máximo
        clock.tick(60)        
        # Calcula tempo transcorrido desde a última atualização 
        dt = clock.get_time()
        # Desenha objetos na tela 
        draw_screen(screen)
        # Atualiza posição dos objetos da tela
        update(dt)
        # Pygame atualiza o seu estado
        pygame.display.update()





pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sprites')
load()
main_loop(screen)
pygame.quit()
