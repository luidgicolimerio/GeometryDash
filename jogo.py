import pygame
import math
from pygame.locals import *
from sys import exit
from cubo import todas_sprites, cubo, fase1, fase2, fase3


width = 1200
height = 900


def load():
    global sys_font, rankk, ranking, Tfinal, py, color_active, color_inactive, color, active, text_area, obstaculos1, coins1,obstaculos2, obstaculos3, voltar, clock, x, cl1, cl, i, scroll, fase, play, quad, over, font, sair, inicio, p,  white, black, border_color, font_color, input_text

    
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 80)
    font = pygame.font.Font(pygame.font.get_default_font(), 35)
    clock = pygame.time.Clock()
    py = 0
    x = 0
    cl1 = 0
    cl = 0
    fase = 3
    i = 0
    scroll = 0
    p = 0
    play = False
    sair = True
    voltar = False
    rankk = False
    l1 = fase1()
    obstaculos1, coins1 = l1
    l2 = fase2()
    obstaculos2 = l2
    l3 =fase3()
    obstaculos3 = l3

    ranking = [['josé', 25, 10], ['luidgi', 24, 10], ['pedro', 23, 9], ['pedro', 23, 9], ['pedro', 23, 9], ['pedro', 23, 9]
               , ['pedro', 23, 9], ['pedro', 23, 9], ['pedro', 23, 9]
               , ['pedro', 23, 9], ['pedro', 23, 9], ['pedro', 23, 9]
               , ['pedro', 23, 9], ['pedro', 23, 9], ['pedro', 23, 9]]


    # Campo de Entrada de Texto
    # Cores
    white = (255, 255, 255)
    black = (0, 0, 0)
    border_color = (50, 50, 50)
    font_color = (10, 10, 10)

    # Fonte e texto
    font = pygame.font.Font(None, 60)
    input_text = ''

    text_area = pygame.Rect(395, 670, 400, 70)  # Área do texto
    tamanho = max(400, font.size(input_text)[0] + 10)
    text_area.w = tamanho
    color_active = pygame.Color('lightskyblue3')
    color_inactive = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False






    quad = pygame.image.load('Sprites/Morte/alien.png')
    quad = pygame.transform.scale(quad, (quad.get_width()* 3, quad.get_height() * 3))
    inicio = pygame.image.load('imagens/Inicial.PNG')
    Tfinal = pygame.image.load('imagens/Final.PNG')
    over = pygame.image.load('imagens/GameOver.PNG')

def rank(screen):
    global cl1, cl, tela, py
 
    
    tela = pygame.image.load('imagens/rank.PNG')
    text = pygame.font.Font(pygame.font.get_default_font(), 28)

    
    
    if py == 0:
        screen.blit(tela, (0,0))
        for (i, el) in enumerate(ranking):
            t = text.render('%i: - %s %s tentativas %s/10' %(i + 1, el[0], el[1], el[2]), False, (219,225,0))
            screen.blit(t,(395,400 + py))
            py = py + 50
            print(py)
            if i >= 9:
                break



    fonte = pygame.font.Font(pygame.font.get_default_font(), 40)
    t = fonte.render("Retornar", True, (219, 225, 0))
    screen.blit(t, (45,205))




def start(screen):
    global cl1, cl, fundo, tri, ret, quad, inicio, white, black, border_color, font_color, input_text, color, color_active, color_inactive, text_area, active
    screen.blit(inicio, (0, 0))

    fonte = pygame.font.Font(pygame.font.get_default_font(), 65)
    t = fonte.render("%i" %(fase), True, (219, 225, 0))
    screen.blit(t, (225,478))

    fonte = pygame.font.Font(pygame.font.get_default_font(), 40)
    if cl1 >= 0:
        t = fonte.render("Começar", True, (219, 225, 0))
    else:
        t = fonte.render("Retornar", True, (219, 225, 0))
    
    screen.blit(t, (515,595))


    t = fonte.render("Sair", True, (219, 225, 0))
    screen.blit(t, (1065,795))

    # Desenha a área do texto
    pygame.draw.rect(screen, black, text_area, border_radius=5)  # Borda arredondada
    pygame.draw.rect(screen, color, (text_area.x + 2, text_area.y + 2, text_area.w - 4, text_area.h - 4),
                     border_radius=4)  # Área do texto
    text_surface = font.render(input_text, True, font_color)
    screen.blit(text_surface, (text_area.x + 5, text_area.y + 5))


    #pygame.draw.rect(screen, (0,0,0), (884, 425, 150, 150))
    










def game_over(screen):
    global cl1, cl, fundo, tri, ret, quad, fade_alpha, fade_img, fade, p, obstaculos1, obstaculos2, obstaculos3, coins1
    screen.fill((0,0,0))
    while p < 1:
        fade_img = pygame.Surface((1200,900)).convert_alpha()
        fade = fade_img.get_rect()
        fade_img.fill('white')
        fade_alpha = 255
        p = 1
    if p == 1:
        fade_alpha -= 5
        fade_img.set_alpha(fade_alpha)
        screen.blit(fade_img, fade)
        if fade_alpha <= 0: 
            p = 2
        
    if p == 2:

        screen.blit(over, (0, 0))
        l1 = fase1()
        obstaculos1, coins1 = l1
        l2 = fase2()
        obstaculos2 = l2
        l3 =fase3()
        obstaculos3 = l3
        









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
        if fade_alpha <= 0:
            x = 2
    if x == 2:
        screen.blit(Tfinal, (0,0))


def update(dt):
    global px, cl1, clock, cl, scroll, fase, tiles, i, fade, fade_img, fade_alpha, perdeu

    # MUDANÇA DE FASE
    while i <= 2:
        if cl1 <= -4230 and fase < 3:
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

        screen.blit(portal1, (4375 + cl1, 150))
        

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

        screen.blit(portal1, (4375 + cl1, 150))


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

        screen.blit(portal1, (4375 + cl1, 150))


    pygame.draw.rect(screen, (105, 105, 105), (1120, 20, 60, 60))
    pygame.draw.rect(screen, (195, 195, 195), (1125, 25, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (1137, 30, 10, 40))
    pygame.draw.rect(screen, (0, 0, 0), (1152, 30, 10, 40))


    todas_sprites.draw(screen)
    if fase == 1:
        screen.blit(portal2, (4615 + cl1, 150))
    if fase == 2:
        screen.blit(portal2, (4615 + cl1, 150))
    if fase == 3:
        screen.blit(portal2, (4615 + cl1, 150))
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
    global play, sair, voltar, cl1, active, rankk, py
    if mouse_buttons[0]: # left
        if check_click(525, 425, 150, 150, px_mouse, py_mouse):
            play = True
        if check_click(1120, 20, 60, 60, px_mouse, py_mouse):
            sair = True
            play = False
        if check_click(1028, 740, 150, 150, px_mouse, py_mouse):
            sair = False
        if check_click(900, 750, 300, 150, px_mouse, py_mouse):
            if x == 2:
                play = False
                sair = False
        if check_click(518, 603, 150, 150, px_mouse, py_mouse):
            voltar = True
            cl1 = 0
            cubo.perdeu = False

        if check_click(395, 670, 400, 70, px_mouse, py_mouse):
            active = True
            print(active)
        else:
            active = False
        if check_click(50, 33, 150, 150, px_mouse, py_mouse):
                rankk = False
                print('a')
        if check_click(884, 425, 150, 150, px_mouse, py_mouse):
            if play == False or (play == True and sair == True):
                rankk = True
                py = 0
            


def main_loop(screen):  
    global clock, voltar,rankk, width, scroll, fundo, fase, play, sair, fade_alpha, fade_img, fade, cl1, text_area, color, color_active, color_inactive, active, input_text
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
                if text_area.collidepoint(e.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
                mouse_buttons = pygame.mouse.get_pressed()
                px_mouse, py_mouse = pygame.mouse.get_pos()
                mouse_click_down(px_mouse, py_mouse, mouse_buttons)
            elif e.type == pygame.KEYDOWN:
                if active == True:
                    if e.key == pygame.K_RETURN:
                        print("Texto digitado:", input_text)  # Aqui você pode usar o texto digitado
                        input_text = ''
                    elif e.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += e.unicode
            elif e.type == pygame.MOUSEBUTTONUP: #detecta o fim do clique do mouse
                mouse_buttons = pygame.mouse.get_pressed()
                px_mouse, py_mouse = pygame.mouse.get_pos()
                mouse_click_up(px_mouse, py_mouse, mouse_buttons)



        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            cubo.sobe()
        if keys[pygame.K_DOWN]:
            cubo.desce()




        # Define FPS máximo
        clock.tick(60)
        # Calcula tempo transcorrido desde a última atualização 
        dt = clock.get_time()


        if cubo.perdeu == False:
            voltar = False
            if rankk == True:
                rank(screen)

            elif fase == 3 and cl1 <= -4230:
                sair = True
                play = True
                final(screen)



            else:
                if play == False:
                    start(screen)
                if play == True:
                    update(dt)
        else:

            cubo.pos_y -= 0
            cl1 = 0
            cubo.pos_y = 300
            scroll = 0
            for espinho in obstaculos2:
                espinho.movement = 0
            game_over(screen)
                        
            




        # fade_alpha -= 5
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