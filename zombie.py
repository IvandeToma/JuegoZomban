import pygame
from imagenes import *

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.zx = 1250
        self.zy = 510
        self.velocidad_zom = 5
        self.contador = 0
        self.image_zom = pygame.surface.Surface((130,250))
        self.rect = self.image_zom.get_rect()
        self.rect.center = (1350,670)
        self.sonido_mordida = pygame.mixer.Sound("sonidos\mordida_zombie.mp3")
        self.sonido_mordida.set_volume(0.5)

    
    def zombie_mov(self,pantalla):
        if self.contador + 1 >= 10:
            self.contador = 0
        if self.zx < -250:
            self.zx = 1250
            self.rect.center = (1350,670)
        pantalla.blit(zombie_izq[self.contador // 1], (int(self.zx),int(self.zy)))
        self.contador += 1
        
        self.zx -= self.velocidad_zom
        self.rect.x -= self.velocidad_zom

class ZombieDos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.zx = 1300
        self.zy = 460
        self.velocidad_zom = 9
        self.contador = 0
        self.image_zom = pygame.surface.Surface((180,280))
        self.rect = self.image_zom.get_rect()
        self.rect.center = (1450,650)
        self.sonido_mordida = pygame.mixer.Sound("sonidos\mordida_zombie.mp3")
        self.sonido_mordida.set_volume(0.5)

    
    def zombie_mov(self,pantalla):
        if self.contador + 1 >= 10:
            self.contador = 0
        if self.zx < -250:
            self.zx = 1300
            self.rect.center(1450,650)
        pantalla.blit(zombie_dos[self.contador // 1], (int(self.zx),int(self.zy)))
        self.contador += 1
        
        self.zx -= self.velocidad_zom
        self.rect.x -= self.velocidad_zom

class ZombieTres(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.zx = 1300
        self.zy = 250
        self.velocidad_zom = 8
        self.contador = 0
        self.image_zom = pygame.surface.Surface((200,550))
        self.rect = self.image_zom.get_rect()
        self.rect.center = (1500,600)
        self.sonido_mordida = pygame.mixer.Sound("sonidos\mordida_zombie.mp3")
        self.sonido_mordida.set_volume(0.5)

    
    def zombie_mov(self,pantalla):
        if self.contador + 1 >= 10:
            self.contador = 0
        if self.zx < -250:
            self.zx = 1300
            self.rect.center = (1450,650)
        pantalla.blit(zombie_tres[self.contador // 1], (int(self.zx),int(self.zy)))
        self.contador += 1
        
        self.zx -= self.velocidad_zom
        self.rect.x -= self.velocidad_zom
