import pygame
import random

NEGRO = (10, 8, 12)
COLOR_PISTA2 = (50, 58, 52)
BLANCO = (255, 255, 255)
VERDE = (90, 232, 64)
ROJO = (255, 20, 20)
AZUL = (10, 222, 255)
COLOR_FUENTE = (255, 122, 88)


def dibujar_texto(screen, texto, pos):
    fuente = pygame.font.SysFont('Barber Street_PersonalUseOnly', 50)
    text = fuente.render(texto, 1, COLOR_FUENTE)
    screen.blit(text, pos)


def dibujar_pista(x_pista, ancho, color_pista):
    pygame.draw.rect(pantalla, color_pista, [x_pista, 0, ancho, dimensiones[1]])
    for i in range(10, dimensiones[1], 20):
        pygame.draw.rect(pantalla, BLANCO, [234, i, 6, 8])


pygame.init()

dimensiones = [480, 600]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Animaciones")

auto = [185, 540, 40, 54]
velocidad_auto = 0

inicio_pista = 160
ancho_pista = 160

game_over = False
reloj = pygame.time.Clock()

pos = 1199

while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
    pantalla.fill(VERDE)
    dibujar_pista(inicio_pista, ancho_pista, NEGRO)
    pygame.draw.rect(pantalla, AZUL, auto)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()