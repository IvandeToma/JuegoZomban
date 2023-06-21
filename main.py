from _pantalla_principal import *
import pygame
from personaje import *
from  nivel_uno import *
from nivel_dos import *
from nivel_tres import *
from game_over import *
from win_final import *
from ranking import *

def ejecucion_perdio(en_juego:False):
    retorno = juego_game_over()
    if retorno == "continuo":
        en_juego = True
    if retorno == "ranking":
        retorno = pantalla_ranking()
        if retorno == "continuo":
            en_juego = True
    return en_juego

pygame.init()
en_juego = True 
while en_juego:
    en_juego = False
    retorno = ejecucion_princi()
    if retorno == "paso":
        lvl_uno = True
    while lvl_uno:  
        lvl_dos = False
        lvl_uno = False
        retorno = lvl_1()
        if retorno == "gano":
            lvl_dos = True
        elif retorno == "perdio":
            retorno = ejecucion_perdio(en_juego)
            en_juego = retorno
        while lvl_dos:
            lvl_dos = False
            lvl_3_while = False
            retorno = lvl_dos_ejecu()
            if retorno == "gano":
                lvl_3_while = True
            elif retorno == "perdio":
                retorno = ejecucion_perdio(en_juego)
                en_juego = retorno
            while lvl_3_while:
                lvl_3_while = False
                retorno = lvl_tres()
                if retorno == "perdio":
                    retorno = ejecucion_perdio(en_juego)
                    en_juego = retorno
                if retorno == "gano":
                    retorno = w_ejecu()
                    if retorno == "continuo":
                        en_juego = True
                    if retorno == "ranking":
                        retorno = pantalla_ranking()
                        if retorno == "continuo":
                            en_juego = True                  
pygame.quit()
