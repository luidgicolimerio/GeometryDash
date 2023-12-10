import pygame
import math
from pygame.locals import *
from sys import exit
from cubo import todas_sprites, brilho, cubo


width = 1200
height = 900


def load():
    global sys_font, clock, x, cl1, cl, i, scroll, fase, play, quad, font, sair, inicio
    
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 80)
    font = pygame.font.Font(pygame.font.get_default_font(), 35)
    clock = pygame.time.Clock()
    x = 0
    cl1 = 0
    cl = 0
    fase = 1
    i = 0
    scroll = 0
    play = False
    sair = True

    quad = pygame.image.load('Sprites/Pulo/pulo_0.png')
    quad = pygame.transform.scale(quad, (quad.get_width()* 3, quad.get_height() * 3))
    inicio = pygame.image.load('imagens/inicio.PNG')





def draw_screen(screen):
    global cl1, cl2, cl3, cl, fundo, tri, ret
    screen.fill((100,160,255))
    
    t = sys_font.render(' ', False, (0,0,0))
    screen.blit(t, t.get_rect(top = 290, left = px))
    #screen.blit(fundo, (0,0))



def start(screen):
    global cl1, cl, fundo, tri, ret, quad, inicio
    screen.blit(inicio, (0, 0))

    screen.blit(quad, (144, 200))
    screen.blit(quad, (912, 200))

    t = sys_font.render("Geometry Dash", True, (255,255,255))
    screen.blit(t, (300,80))

    pygame.draw.rect(screen, (100, 100, 100), (412.8, 250, 374.4, 150))
    t = font.render("Está na Fase: %i" %(fase), True, (0,0,0))
    screen.blit(t, (470,305))

    pygame.draw.rect(screen, (100, 100, 100), (412.8, 450, 374.4, 150))
    pygame.draw.rect(screen, (170, 170, 170), (432.8, 470, 334.4, 110))

    if cl1 >= 0:
        t = font.render("Começar o jogo", True, (0,0,0))
    else:
        t = font.render("Retornar ao jogo", True, (0,0,0))
    
    screen.blit(t, (465,505))





    pygame.draw.rect(screen, (100, 100, 100), (412.8, 650, 374.4, 150))
    pygame.draw.rect(screen, (170, 170, 170), (432.8, 670, 334.4, 110))
    t = font.render("sair do jogo", True, (0,0,0))
    screen.blit(t, (495,705))


def final(screen):
    global cl1, cl, fundo, tri, ret, quad, fade_alpha, fade_img, fade, x
    screen.fill((0,0,0))
    while x < 1:
        fade_img = pygame.Surface((1200,900)).convert_alpha()
        fade = fade_img.get_rect()
        fade_img.fill('white')
        fade_alpha = 255
        x = 1
    if x == 1:
        fade_alpha -= 1
        fade_img.set_alpha(fade_alpha)
        screen.blit(fade_img, fade)
        if fade_alpha == 0:
            x = 2
    if x == 2:
        screen.blit(inicio, (0,0))
        t = sys_font.render("Creditos", True, (255,255,255))
        screen.blit(t, (430,80))
        t = sys_font.render("Trabalho de INF1034", True, (255,255,255))
        screen.blit(t, (200,200))
        t = font.render("Turma: 3WA", True, (255,255,255))
        screen.blit(t, (500,350))  
        t = font.render("Nome: José Carlos - Matrícula: 2320465", True, (255,255,255))
        screen.blit(t, (250,400))
        t = font.render("Nome: Luidgi Colimerio - Matrícula: *******", True, (255,255,255))
        screen.blit(t, (250,450))


        pygame.draw.rect(screen, (100, 100, 100), (900, 750, 300, 150))
        pygame.draw.rect(screen, (170, 170, 170), (920, 770, 260, 110))
        t = font.render("sair do jogo", True, (0,0,0))
        screen.blit(t, (950,810))


    






def update(dt):
    global px, cl1, clock, cl, scroll, fase, tiles, i, fade, fade_img, fade_alpha



<<<<<<< HEAD
    # MUDANÇA DE FASE
    while i <= 2:
        if cl1 <= -3000 and fase < 3:
            fase += 1
            cl1 = 0
        i += 1
=======
        if brilho.andando == True:
          #scroll background
            scroll = scroll - (0.1 * dt)
            cl1 = cl1 - (0.1 * dt)
>>>>>>> 782ea1b8e92f72237d2a08272398bdeaef98eaac






    # espinho e retangulo da FASE 1, 2, 3
    if fase == 1:


        tri = pygame.image.load('imagens/triangulo1.PNG')
        ret = pygame.image.load('imagens/retangulo1.PNG')

        tri = pygame.transform.scale(tri, (tri.get_width()/ 2.6, tri.get_height() / 2.6))
        ret = pygame.transform.scale(ret, (ret.get_width()/ 2.6, ret.get_height() / 2.6))
        tri_inv = pygame.transform.flip(tri, False, True)

        fundo = pygame.image.load('imagens/Frame1.PNG').convert()
        fundo_width = fundo.get_width()
        fundo_rect = fundo.get_rect()

        portal1 = pygame.image.load('imagens/PortalM1.PNG')
        portal1 = pygame.transform.scale(portal1, (portal1.get_width()/ 1.33, portal1.get_height() / 2))
        portal2 = pygame.image.load('imagens/PortalM2.PNG')
        portal2 = pygame.transform.scale(portal2, (portal2.get_width()/ 1.33, portal2.get_height() / 2))


        tiles = math.ceil(width  / fundo_width) + 1
        for i in range(0, tiles):
            screen.blit(fundo, (i * fundo_width + scroll, 0))
            fundo_rect.x = i * fundo_width + scroll

            if brilho.andando == True:
            #scroll background
                scroll = scroll - (0.1 * dt)
                cl1 = cl1 - (0.1 * dt)
        #reset scroll
        if abs(scroll) > fundo_width:
            scroll = 0
        pygame.draw.rect(screen, (70, 70, 70), (0, 790, 4000, 4000))
        pygame.draw.rect(screen, (45, 45, 45), (0, 800, 4000, 4000))



        screen.blit(tri, (600 + cl1, 754))
        screen.blit(tri, (800 + cl1, 754))
        screen.blit(tri, (1000 + cl1, 754))
        screen.blit(tri, (1200 + cl1, 754))
        screen.blit(ret, (1200 + cl1, 724))
        screen.blit(ret, (1350 + cl1, 694))
        screen.blit(ret, (1500 + cl1, 664))
        screen.blit(ret, (1600 + cl1, 724))
        screen.blit(tri, (1603 + cl1, 580))
        screen.blit(ret, (1600 + cl1, 614))
        screen.blit(ret, (1750 + cl1, 724))
        screen.blit(ret, (1795 + cl1, 724))
        screen.blit(ret, (1840 + cl1, 724))
        screen.blit(tri, (1753 + cl1, 754))
        screen.blit(tri, (1798 + cl1, 754))
        screen.blit(tri, (1843 + cl1, 754))
        screen.blit(ret, (2000 + cl1, 664))
        screen.blit(ret, (2150 + cl1, 724))
        screen.blit(ret, (2230 + cl1, 744))
        screen.blit(ret, (2300 + cl1, 670))
        screen.blit(tri, (2348 + cl1, 636))
        screen.blit(ret, (2345 + cl1, 670))
        screen.blit(tri_inv, (2348 + cl1, 586))

        screen.blit(portal1, (3145 + cl1, 565))
        

    if fase == 2:

        tri = pygame.image.load('imagens/triangulo2.PNG')
        ret = pygame.image.load('imagens/retangulo2.PNG')

        tri = pygame.transform.scale(tri, (tri.get_width()/ 2.6, tri.get_height() / 2.6))
        ret = pygame.transform.scale(ret, (ret.get_width()/ 2.6, ret.get_height() / 2.6))
        tri_inv = pygame.transform.flip(tri, False, True)

        fundo = pygame.image.load('imagens/Frame2.PNG').convert()
        fundo_width = fundo.get_width()
        fundo_rect = fundo.get_rect()

        portal1 = pygame.image.load('imagens/PortalM3.PNG')
        portal1 = pygame.transform.scale(portal1, (portal1.get_width()/ 1.33, portal1.get_height() / 2))
        portal2 = pygame.image.load('imagens/PortalM4.PNG')
        portal2 = pygame.transform.scale(portal2, (portal2.get_width()/ 1.33, portal2.get_height() / 2))

        tiles = math.ceil(width  / fundo_width) + 1
        for i in range(0, tiles):
            screen.blit(fundo, (i * fundo_width + scroll, 0))
            fundo_rect.x = i * fundo_width + scroll

            if brilho.andando == True:
            #scroll background
                scroll = scroll - (0.1 * dt)
                cl1 = cl1 - (0.1 * dt)
        #reset scroll
        if abs(scroll) > fundo_width:
            scroll = 0
        pygame.draw.rect(screen, (70, 70, 70), (0, 790, 4000, 4000))
        pygame.draw.rect(screen, (45, 45, 45), (0, 800, 4000, 4000))


        
        screen.blit(tri, (600 + cl1, 754))
        screen.blit(tri, (632 + cl1, 754))
        screen.blit(tri, (664 + cl1, 754))
        screen.blit(tri, (820 + cl1, 754))
        screen.blit(tri, (852 + cl1, 754))
        screen.blit(ret, (1100 + cl1, 704))
        screen.blit(tri_inv, (1100 + cl1, 565))
        screen.blit(tri, (1160 + cl1, 754))
        screen.blit(ret, (1400 + cl1, 700))
        screen.blit(ret, (1550 + cl1, 670))
        screen.blit(ret, (1630 + cl1, 720))
        screen.blit(ret, (1670 + cl1, 620))
        screen.blit(tri, (1576 + cl1, 754))
        screen.blit(tri, (1673 + cl1, 586))
        screen.blit(ret, (2000 + cl1, 720))
        screen.blit(ret, (2200 + cl1, 720))
        screen.blit(ret, (2400 + cl1, 720))
        screen.blit(tri, (2073 + cl1, 754))
        screen.blit(tri, (2106 + cl1, 754))
        screen.blit(tri, (2139 + cl1, 754))
        screen.blit(tri, (2273 + cl1, 754))
        screen.blit(tri, (2306 + cl1, 754))
        screen.blit(tri, (2339 + cl1, 754))
        screen.blit(ret, (2550 + cl1, 690))
        screen.blit(ret, (2700 + cl1, 660))
        screen.blit(ret, (2680 + cl1, 734))
        screen.blit(tri, (2700 + cl1, 754))
        screen.blit(tri, (2748 + cl1, 754))
        screen.blit(tri, (2796 + cl1, 754))
        screen.blit(tri, (2844 + cl1, 754))
        screen.blit(tri, (2892 + cl1, 754))
        screen.blit(ret, (2850 + cl1, 630))
        screen.blit(ret, (2895 + cl1, 630))
        screen.blit(ret, (2940 + cl1, 630))
        screen.blit(tri, (2943 + cl1, 596))

        screen.blit(portal1, (3145 + cl1, 565))


    if fase == 3:

        tri = pygame.image.load('imagens/triangulo3.PNG')
        ret = pygame.image.load('imagens/retangulo3.PNG')

        tri = pygame.transform.scale(tri, (tri.get_width()/ 2.6, tri.get_height() / 2.6))
        ret = pygame.transform.scale(ret, (ret.get_width()/ 2.6, ret.get_height() / 2.6))

        fundo = pygame.image.load('imagens/Frame3.PNG').convert()
        fundo_width = fundo.get_width()
        fundo_rect = fundo.get_rect()


        portal1 = pygame.image.load('imagens/PortalM5.PNG')
        portal1 = pygame.transform.scale(portal1, (portal1.get_width()/ 1.33, portal1.get_height() / 2))
        portal2 = pygame.image.load('imagens/PortalM6.PNG')
        portal2 = pygame.transform.scale(portal2, (portal2.get_width()/ 1.33, portal2.get_height() / 2))

        tiles = math.ceil(width  / fundo_width) + 1
        for i in range(0, tiles):
            screen.blit(fundo, (i * fundo_width + scroll, 0))
            fundo_rect.x = i * fundo_width + scroll

            if brilho.andando == True:
            #scroll background
                scroll = scroll - (0.1 * dt)
                cl1 = cl1 - (0.1 * dt)

        #reset scroll
        if abs(scroll) > fundo_width:
            scroll = 0
        pygame.draw.rect(screen, (70, 70, 70), (0, 790, 4000, 4000))
        pygame.draw.rect(screen, (45, 45, 45), (0, 800, 4000, 4000))



        cl = 0
        while cl < 2070:
            screen.blit(tri, (555 + cl + cl1, 754))
            cl += 45
        screen.blit(ret, (600 + cl1, 724))
        screen.blit(ret, (750 + cl1, 694))
        screen.blit(ret, (820 + cl1, 724))
        screen.blit(ret, (970 + cl1, 694))
        screen.blit(ret, (1115 + cl1, 664))
        screen.blit(ret, (1240 + cl1, 604))
        screen.blit(tri, (1243 + cl1, 570))
        screen.blit(tri, (1313 + cl1, 690))
        screen.blit(tri, (1345 + cl1, 690))
        screen.blit(tri, (1439 + cl1, 690))
        screen.blit(ret, (1235 + cl1, 724))
        screen.blit(ret, (1284 + cl1, 724))
        screen.blit(ret, (1333 + cl1, 724))
        screen.blit(ret, (1382 + cl1, 724))
        screen.blit(ret, (1431 + cl1, 724))
        screen.blit(ret, (1480 + cl1, 724))
        screen.blit(ret, (1630 + cl1, 700))
        screen.blit(ret, (1800 + cl1, 700))
        screen.blit(ret, (1950 + cl1, 670))
        screen.blit(ret, (2040 + cl1, 724))
        screen.blit(ret, (2190 + cl1, 690))
        screen.blit(ret, (2340 + cl1, 650))
        screen.blit(ret, (2389 + cl1, 650))

        screen.blit(portal1, (3145 + cl1, 565))


    pygame.draw.rect(screen, (105, 105, 105), (1120, 20, 60, 60))
    pygame.draw.rect(screen, (195, 195, 195), (1125, 25, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (1137, 30, 10, 40))
    pygame.draw.rect(screen, (0, 0, 0), (1152, 30, 10, 40))


    todas_sprites.draw(screen)
    if fase == 1:
        screen.blit(portal2, (3275 + cl1, 565))
    if fase == 2:
        screen.blit(portal2, (3275 + cl1, 565))
    if fase == 3:
        screen.blit(portal2, (3275 + cl1, 565))
    todas_sprites.update()
    pygame.display.flip()






def check_click(x1,y1,w1,h1,x2,y2):
    return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1
def mouse_click_up(px_mouse, py_mouse, mouse_buttons):
    pass    
def keyboard_keyup(keys):
    pass
def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
    global play, sair
    if mouse_buttons[0]: # left
        if check_click(432.8, 470, 334.4, 110, px_mouse, py_mouse):
            play = True
        if check_click(1120, 20, 60, 60, px_mouse, py_mouse):
            sair = True
            play = False
        if check_click(432.8, 670, 334.4, 110, px_mouse, py_mouse):
            sair = False
        if check_click(900, 750, 300, 150, px_mouse, py_mouse):
            if x == 2:
                play = False
                sair = False
        

    elif mouse_buttons[2]: # right
        if check_click(432.8, 470, 334.4, 110, px_mouse, py_mouse):
            play = True
        if check_click(1120, 20, 60, 60, px_mouse, py_mouse):
            sair = True
            play = False
        if check_click(432.8, 670, 334.4, 110, px_mouse, py_mouse):
            sair = False
        if check_click(900, 750, 300, 150, px_mouse, py_mouse):
            if x == 2:
                play = False
                sair = False


def main_loop(screen):  
    global clock, width, scroll, fundo, fase, play, sair, fade_alpha, fade_img, fade
    running = True

    
    fade_img = pygame.Surface((1200,900)).convert_alpha()
    fade = fade_img.get_rect()
    fade_img.fill('black')
    fade_alpha = 255

    while running:
    

        for e in pygame.event.get(): 
            if e.type == pygame.QUIT or (sair == False and play == False):
                running = False
                break
            
            elif e.type == pygame.MOUSEBUTTONDOWN: #detecta o inicio do clique do mouse
                mouse_buttons = pygame.mouse.get_pressed()
                px_mouse, py_mouse = pygame.mouse.get_pos()
                mouse_click_down(px_mouse, py_mouse, mouse_buttons)
            elif e.type == pygame.MOUSEBUTTONUP: #detecta o fim do clique do mouse
                mouse_buttons = pygame.mouse.get_pressed()
                px_mouse, py_mouse = pygame.mouse.get_pos()
                mouse_click_up(px_mouse, py_mouse, mouse_buttons)






            
        keys = pygame.key.get_pressed()
<<<<<<< HEAD
=======

        if keys[pygame.K_UP]:
            brilho.pula()
>>>>>>> 782ea1b8e92f72237d2a08272398bdeaef98eaac
        if keys[pygame.K_RIGHT]:
            brilho.andar()
        else:
            brilho.parado()
        
<<<<<<< HEAD
        if keys[pygame.K_UP]:
            brilho.pula()
            cubo.pula()
            
=======
        if keys[pygame.K_SPACE]:
            brilho.pula()
            cubo.pula()
            
    
>>>>>>> 782ea1b8e92f72237d2a08272398bdeaef98eaac

        # Define FPS máximo
        clock.tick(60)
        # Calcula tempo transcorrido desde a última atualização 
        dt = clock.get_time()

        if fase == 3 and cl1 <= -3000:
            sair = True
            play = True
            final(screen)

        else:
            if play == False:
                start(screen)
            if play == True:
                update(dt)


        fade_alpha -= 1
        fade_img.set_alpha(fade_alpha)
        screen.blit(fade_img, fade)

        # Pygame atualiza o seu estado
        pygame.display.update()




pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sprites')
load()
main_loop(screen)
pygame.quit()