import pygame

def muestra_texto(pantalla,fuente,texto,color,dimension,x,y):
    tipo_letra = pygame.font.SysFont(fuente,dimension)
    superficie = tipo_letra.render(texto,True,color)
    rect_punt = superficie.get_rect()
    rect_punt.center = (x,y)
    pantalla.blit(superficie,rect_punt)