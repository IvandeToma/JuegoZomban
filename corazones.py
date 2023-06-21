import pygame
import random
from colores import *
#corazon_img = [pygame.transform.scale(pygame.image.load("Juego3\heart pixel art\heart pixel art 64x64.png"), (270,280))]

class Corazon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("imagenes\heart pixel art\heart pixel art 64x64.png")
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.sonido_corazon = pygame.mixer.Sound("sonidos\_vida_sonido.mp3")
        self.sonido_corazon.set_volume(0.5)
        self.rect.x  = random.randrange(0 + 64,1200 - 64)

    def update(self):
        self.rect.y += 2
        if self.rect.y > 700:
            self.rect.y = 700