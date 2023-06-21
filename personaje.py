import pygame
from colores import *
from imagenes import *
from corazones import *
from zombie import *
class Personaje(pygame.sprite.Sprite):
    def __init__(self,lista_imagenes):
        super().__init__()
        self.image = pygame.surface.Surface((150,250))
        self.rect = self.image.get_rect()
        self.rect.center = (75, 660)
        self.px = 0
        self.py = 533
        self.ancho = 100
        self.velocidad = 7
        self.derecha = False
        self.izquierda = False
        self.esta_der = True
        self.esta_izq = False
        self.cuenta_pasos = 0
        
        #kills
        self.contador_kills = 0
        self.contador_tiros_acertados = 0

        #puntuacion
        self.puntuacion = 0

        #disparos
        self.cadencia = 750
        self.ultimo_disparo = pygame.time.get_ticks()
        self.dispara = False
        self.contador_dispara = 0
        self.disparo_sonido = pygame.mixer.Sound("sonidos\disparo_sound.mp3")
        self.lista_imagenes = lista_imagenes
        
        #vida
        self.hp = 100
    
    def detecto_precionado(self):
        precionada = pygame.key.get_pressed()

        if precionada[pygame.K_d] :
            self.px += self.velocidad
            self.rect.x += self.velocidad
            self.derecha = True
            self.izquierda = False
            self.esta_izq = False
            self.esta_der = True
            self.dispara = False
            if self.px > 1100:
                self.px = 1100
                self.rect.x = 1100
        elif precionada[pygame.K_a]:
            self.px -= self.velocidad
            self.rect.x -= self.velocidad
            self.izquierda = True
            self.derecha = False
            self.esta_izq = True
            self.esta_der = False
            self.dispara = False
            if self.px < 0:
                self.px = 0
                self.rect.x = 0
        elif self.esta_izq:
            self.derecha = False
            self.izquierda = False
            self.esta_der = False
            self.esta_izq = True
            self.dispara = False
        elif self.esta_der:
            self.esta_der = True
            self.derecha = False
            self.izquierda = False
            self.esta_der = False
            self.esta_izq = False
        
        if precionada[pygame.K_SPACE]:
            self.dispara = True
        elif not precionada[pygame.K_SPACE]:
            self.dispara = False
            self.esta_der = True

    def movimiento(self,pantalla):       
        if self.contador_dispara >5:
            self.contador_dispara = 0 
        if self.cuenta_pasos + 1 >= 9:
            self.cuenta_pasos = 0
        if self.derecha:
            pantalla.blit(camina_der[self.cuenta_pasos // 1], (int(self.px), int(self.py)))
            self.cuenta_pasos += 1
        elif self.izquierda:
            pantalla.blit(camina_izq[self.cuenta_pasos // 1], (int(self.px), int(self.py)))
            self.cuenta_pasos += 1
        elif self.esta_izq:
            pantalla.blit(esta_izq[self.cuenta_pasos // 1], (int(self.px), int(self.py)))
            self.cuenta_pasos += 1

        elif  self.esta_der and self.cuenta_pasos < 8: 
            pantalla.blit(esta_der[self.cuenta_pasos // 1], (int(self.px), int(self.py)))
            self.cuenta_pasos += 1

        elif self.dispara and self.contador_dispara <= 5:
            ahora = pygame.time.get_ticks()
            if ahora - self.ultimo_disparo > self.cadencia:
                pantalla.blit(dispara_der[self.contador_dispara // 1], (int(self.px), int(self.py)))
                self.contador_dispara += 1
                self.fun_disparo()
                self.ultimo_disparo = ahora
            elif ahora - self.ultimo_disparo < self.cadencia:
                pantalla.blit(esta_der[1], (int(self.px), int(self.py)))
                
    def fun_disparo(self):
        bala = Disparo(self.rect.right + 40, self.rect.top + 100)
        self.lista_imagenes.add(bala)
        self.disparo_sonido.play()

    def kills(self,cantidad_acertados):
        self.contador_tiros_acertados += 1
        if self.contador_tiros_acertados == cantidad_acertados:
            self.puntuacion += 1
            self.contador_kills += 1
            self.contador_tiros_acertados = 0

    def barra_hp(self,pantalla,x,y,hp):
        self.largo = 200
        self.ancho = 20
        calculo_barra = int((hp / 100) * self.largo)
        borde = pygame.Rect(x,y,self.largo,self.ancho)
        rectangulo = pygame.Rect(x,y,calculo_barra,self.ancho)
        pygame.draw.rect(pantalla,VIDA_COLOR,rectangulo)
        pygame.draw.rect(pantalla,VIDA_COLOR,borde, 2)
        pantalla.blit(pygame.transform.scale(esta_der[1], (20,25)), (480,15))
        if hp <0:
            hp = 0

class Disparo(pygame.sprite.Sprite):
    def __init__(self,x,y) -> None:
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("imagenes\disparo\_disparo.png"), (30,10))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def mostrar_disparo(self,pantalla):
        pantalla.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(pantalla, ROJO, self.rect)
        pantalla.blit(self.image,self.rect)

    def update(self):
        self.rect.x += 70
        if self.rect.x > 1200:
            self.kill()


