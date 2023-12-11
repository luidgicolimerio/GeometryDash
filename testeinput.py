import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da janela
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Campo de entrada de texto')

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
border_color = (50, 50, 50)
font_color = (10, 10, 10)

# Fonte e texto
font = pygame.font.Font(None, 36)
input_text = ''

text_area = pygame.Rect(50, 50, 300, 40)  # Área do texto
color_active = pygame.Color('lightskyblue3')
color_inactive = pygame.Color('dodgerblue2')
color = color_inactive
active = False

clock = pygame.time.Clock()

running = True
while running:
    window.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if text_area.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print("Texto digitado:", input_text)  # Aqui você pode usar o texto digitado
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode  # Adiciona caracteres ao texto digitado

    # Desenha a área do texto
    width = max(300, font.size(input_text)[0] + 10)
    text_area.w = width
    pygame.draw.rect(window, black, text_area, border_radius=5)  # Borda arredondada
    pygame.draw.rect(window, color, (text_area.x + 2, text_area.y + 2, text_area.w - 4, text_area.h - 4),
                     border_radius=4)  # Área do texto
    text_surface = font.render(input_text, True, font_color)
    window.blit(text_surface, (text_area.x + 5, text_area.y + 5))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
