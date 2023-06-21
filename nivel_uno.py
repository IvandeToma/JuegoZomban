import pygame
from colores import *
from personaje import *
from zombie import *
from ranking import *
from imagenes import *
from _funcion_mostrar_text import *

def lvl_1():
    pygame.init()

    #Inicializacion sobre la pantalla
    ANCHO_VENTANA = 1200
    ALTO_VENTANA = 800
    pantalla = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA])
    pygame.display.set_caption("ZOMBAN")
    fondo = pygame.transform.scale(pygame.image.load("imagenes\_1_game_background\_1_game_background.png"),(1200,800))
    x_para_fondo = 0
    FPS = 25
    RELOJ = pygame.time.Clock()
    icono = pygame.image.load("imagenes\walk_zom_3_izq\image_2.png")
    pygame.display.set_icon(icono)

    #sonido ambiente
    ambiente = pygame.mixer.Sound("sonidos\sonido_ambiente_zombie.mp3")
    ambiente.set_volume(0.5)
    ambiente.play()

    #texto kills
    fuente = pygame.font.SysFont("HoMicIDE EFfeCt", 55)
    texto = fuente.render("Kills", True, (255,0,0))

    #requerido para utilizar al personaje,zombie,corazon,disparo
    lista_personaje = pygame.sprite.Group()
    lista_disparos = pygame.sprite.Group()
    lista_zombies = pygame.sprite.Group()
    lista_corazones = pygame.sprite.Group()
    personaje = Personaje(lista_disparos)
    zombie = Zombie()
    corazones = Corazon()
    lista_zombies.add(zombie)
    lista_corazones.add(corazones)
    lista_personaje.add(personaje)

    #posicion de la sangre
    sangre_posicion_personaje = (-100,-100)
    sangre_posicion_zombie = (-100,-100)

    retorno = ''
    running_flag = True
    while running_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_flag = False
                retorno = "salio"
        #fondo
        x_relativa_para_fondo = x_para_fondo % fondo.get_rect().width
        pantalla.blit(fondo, (x_relativa_para_fondo - fondo.get_rect().width, 0))
        if x_relativa_para_fondo < ANCHO_VENTANA:
            pantalla.blit(fondo,(x_relativa_para_fondo,0)) 
        x_para_fondo -= 1
        pantalla.blit(texto, (50,50))

        #updates necesarios para ver las diferentes cosas
        lista_corazones.update()
        lista_disparos.update()
        lista_zombies.update()
        
        #funciones de movimiento
        personaje.detecto_precionado()
        personaje.movimiento(pantalla)
        corazones.update()

        #dibujo en pantalla corazones y diparos
        lista_corazones.draw(pantalla)
        lista_disparos.draw(pantalla) 

        #coliciones entre personaje y zombie
        if personaje.rect.colliderect(zombie.rect):
            zombie.sonido_mordida.play()
            sangre_posicion_personaje = (personaje.px+20,personaje.py+200)
            personaje.hp -= 20
            zombie.kill()
            zombie = Zombie()
            lista_zombies.add(zombie)

        #si se que sin vida
        if personaje.hp <= 0:
            running_flag = False
            retorno =  "perdio"
            actualizar_ranking(personaje.puntuacion)
        
        #zombie movimiento
        zombie.zombie_mov(pantalla)

        #zombie colicion con disparos
        colicion_disparo_zom = pygame.sprite.groupcollide(lista_zombies,lista_disparos,False,True)
        if colicion_disparo_zom:
            personaje.kills(2)

        #muestro la sangre
        pantalla.blit(sangre, (sangre_posicion_personaje))
        pantalla.blit(sangre, (sangre_posicion_zombie))
        
        #puntuacion
        muestra_texto(pantalla,"HoMicIDE EFfeCt",str(personaje.puntuacion),ROJO, 50, 220,75)

        #vida del personaje
        personaje.barra_hp(pantalla,500,15,personaje.hp)
        muestra_texto(pantalla,"HoMicIDE EFfeCt",str(personaje.hp),ROJO, 20, 520,25)
        colicion_perso_corazon = pygame.sprite.groupcollide(lista_personaje,lista_corazones,False,True)
        if colicion_perso_corazon:
            personaje.hp += 20
            corazones.sonido_corazon.play()
        
        #personaje mato al zombie
        if personaje.contador_kills ==  1:
            sangre_posicion_zombie = (zombie.zx+40, zombie.zy+220)
            zombie.kill()
            zombie = Zombie()
            lista_zombies.add(zombie)
            personaje.contador_kills = 0
        
        #timer
        RELOJ.tick(FPS)

        pygame.display.flip()

        #paso de nivel
        if personaje.puntuacion == 4:
            running_flag = False
            retorno = "gano"
    pygame.quit()
    return retorno