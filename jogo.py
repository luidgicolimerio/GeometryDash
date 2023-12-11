import pygame
import math
from pygame.locals import *
from sys import exit
from cubo import todas_sprites, cubo, obstaculos1, obstaculos2, obstaculos3, coins1


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

    quad = pygame.image.load('Sprites/Morte/alien.png')
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

def game_over(screen):
    screen.fill((0,0,0))


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
        t = font.render("Nome: Luidgi Colimerio - Matrícula: 2320594", True, (255,255,255))
        screen.blit(t, (250,450))


        pygame.draw.rect(screen, (100, 100, 100), (900, 750, 300, 150))
        pygame.draw.rect(screen, (170, 170, 170), (920, 770, 260, 110))
        t = font.render("sair do jogo", True, (0,0,0))
        screen.blit(t, (950,810))

def update(dt):
    global px, cl1, clock, cl, scroll, fase, tiles, i, fade, fade_img, fade_alpha


    # MUDANÇA DE FASE
    while i <= 2:
        if cl1 <= -4130 and fase < 3:
            fase += 1
            cl1 = 0
        i += 1

    # espinho e retangulo da FASE 1, 2, 3
    if fase == 1:

        fundo = pygame.image.load('imagens/Frame1.PNG').convert()
        fundo_width = fundo.get_width()
        fundo_rect = fundo.get_rect()

        portal1 = pygame.image.load('imagens/PortalM1.PNG')
        portal1 = pygame.transform.scale(portal1, (portal1.get_width()/ 1, portal1.get_height() / 1))
        portal2 = pygame.image.load('imagens/PortalM2.PNG')
        portal2 = pygame.transform.scale(portal2, (portal2.get_width()/ 1, portal2.get_height() / 1))
        
        
        collision_sprites = check_collision(cubo, obstaculos1)
        collision_coins = check_collision_coin(cubo, coins1)
        if collision_sprites:
            cubo.colisao()
        if collision_coins:
            cubo.moeda()


        tiles = math.ceil(width  / fundo_width) + 1
        
        for i in range(0, tiles):
            screen.blit(fundo, (i * fundo_width + scroll, 0))
            fundo_rect.x = i * fundo_width + scroll
        #scroll background
            scroll = scroll - (0.15 * dt)
            cl1 = cl1 - (0.15 * dt)
            for espinho in obstaculos1:
                espinho.update_x()
            for coin in coins1:
                coin.update_x()
 

        #reset scroll
        if abs(scroll) > fundo_width:
            scroll = 0
        pygame.draw.rect(screen, (70, 70, 70), (0, 730, 5000, 4000))
        pygame.draw.rect(screen, (45, 45, 45), (0, 740, 5000, 4000))

        coins1.draw(screen)
        obstaculos1.draw(screen)

        screen.blit(portal1, (4275 + cl1, 150))
        

    if fase == 2:

        fundo = pygame.image.load('imagens/Frame2.PNG').convert()
        fundo_width = fundo.get_width()
        fundo_rect = fundo.get_rect()

        portal1 = pygame.image.load('imagens/PortalM3.PNG')
        portal1 = pygame.transform.scale(portal1, (portal1.get_width()/ 1, portal1.get_height() / 1))
        portal2 = pygame.image.load('imagens/PortalM4.PNG')
        portal2 = pygame.transform.scale(portal2, (portal2.get_width()/ 1, portal2.get_height() / 1))

        collision_sprites = check_collision(cubo, obstaculos2)
        if collision_sprites:
            cubo.colisao()
            print("Colisão detectada!")
        



        tiles = math.ceil(width  / fundo_width) + 1
        for i in range(0, tiles):
            screen.blit(fundo, (i * fundo_width + scroll, 0))
            fundo_rect.x = i * fundo_width + scroll


        #scroll background
            scroll = scroll - (0.15 * dt)
            cl1 = cl1 - (0.15 * dt)
            for espinho in obstaculos2:
                espinho.update_x()


        #reset scroll
        if abs(scroll) > fundo_width:
            scroll = 0
        pygame.draw.rect(screen, (70, 70, 70), (0, 730, 4000, 4000))
        pygame.draw.rect(screen, (45, 45, 45), (0, 740, 4000, 4000))

        obstaculos2.draw(screen)

        screen.blit(portal1, (4275 + cl1, 150))


    if fase == 3:

        fundo = pygame.image.load('imagens/Frame3.PNG').convert()
        fundo_width = fundo.get_width()
        fundo_rect = fundo.get_rect()


        portal1 = pygame.image.load('imagens/PortalM5.PNG')
        portal1 = pygame.transform.scale(portal1, (portal1.get_width()/ 1, portal1.get_height() / 1))
        portal2 = pygame.image.load('imagens/PortalM6.PNG')
        portal2 = pygame.transform.scale(portal2, (portal2.get_width()/ 1, portal2.get_height() / 1))

        collision_sprites = check_collision(cubo, obstaculos3)
        if collision_sprites:
            cubo.colisao()
            print("Colisão detectada!")
        



        tiles = math.ceil(width  / fundo_width) + 1
        for i in range(0, tiles):
            screen.blit(fundo, (i * fundo_width + scroll, 0))
            fundo_rect.x = i * fundo_width + scroll
            for espinho in obstaculos3:
                espinho.update_x()

        #scroll background
            scroll = scroll - (0.15 * dt)
            cl1 = cl1 - (0.15 * dt)

        #reset scroll
        if abs(scroll) > fundo_width:
            scroll = 0
        pygame.draw.rect(screen, (70, 70, 70), (0, 730, 5000, 4000))
        pygame.draw.rect(screen, (45, 45, 45), (0, 740, 5000, 4000))

        obstaculos3.draw(screen)

        screen.blit(portal1, (4275 + cl1, 150))


    pygame.draw.rect(screen, (105, 105, 105), (1120, 20, 60, 60))
    pygame.draw.rect(screen, (195, 195, 195), (1125, 25, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (1137, 30, 10, 40))
    pygame.draw.rect(screen, (0, 0, 0), (1152, 30, 10, 40))


    todas_sprites.draw(screen)
    if fase == 1:
        screen.blit(portal2, (4495 + cl1, 150))
    if fase == 2:
        screen.blit(portal2, (4495 + cl1, 150))
    if fase == 3:
        screen.blit(portal2, (4495 + cl1, 150))
    todas_sprites.update()
    pygame.display.flip()

def check_collision(player, obstacles):
    collision_sprites = pygame.sprite.spritecollide(player, obstacles, False, pygame.sprite.collide_mask)
    return collision_sprites
def check_collision_coin(player, coin):
    collision_sprites = pygame.sprite.spritecollide(player, coin, True, pygame.sprite.collide_mask)
    return collision_sprites


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

        if keys[pygame.K_UP]:
            cubo.sobe()
        if keys[pygame.K_DOWN]:
            cubo.desce()


        collision_sprites = check_collision(cubo, obstaculos1)
        if collision_sprites:
            cubo.colisao()

            print("Colisão detectada!")
        
        

        # Define FPS máximo
        clock.tick(60)
        # Calcula tempo transcorrido desde a última atualização 
        dt = clock.get_time()

        if cubo.perdeu:
            game_over(screen)

        if fase == 3 and cl1 <= -4130:
            sair = True
            play = True
            final(screen)

        else:
            if play == False:
                start(screen)
            if play == True:
                update(dt)

        # fade_alpha -= 1
        # fade_img.set_alpha(fade_alpha)
        # screen.blit(fade_img, fade)

        # Pygame atualiza o seu estado
        pygame.display.update()




pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sprites')
load()
main_loop(screen)
pygame.quit()