import _sqlite3
import pygame
from _funcion_mostrar_text import *
from colores import *
"""
with _sqlite3.connect("bd_rank.db") as conexion:
    try:
        sentencia = ''' create table ranking
                        (
                            nombre text,
                            kills real

                        )
                    '''
        conexion.execute(sentencia)
        print('se creo la tabla de rankins')
    except _sqlite3.OperationalError:
        print('ya existe')
"""


"""
with _sqlite3.connect("bd_rank.db") as conexion:
    try:
            conexion.execute("insert into ranking(nombre,kills) values (?,?)", ("Jose", "4"))
            conexion.execute("insert into ranking(nombre,kills) values (?,?)", ("Manuel", "8"))
            conexion.commit()
    except:
        print("error")
"""

def actualizar_ranking(puntaje):
    with _sqlite3.connect("bd_rank.db") as conexion:
        try:
                conexion.execute("insert into ranking(nombre,kills) values (?,?)", ("Jugador_1", f"{puntaje}"))
                conexion.commit()
        except:
            print("error")

def mostrar_lista_ranking():
    indice = 0
    lista_ranking = []
    with _sqlite3.connect("bd_rank.db") as conexion:
        sentencia = "SELECT * FROM ranking  ORDER BY kills DESC"
        cursor=conexion.execute(sentencia)
        for fila in cursor:
            if indice < 4:
                lista_ranking.append(fila)
                indice += 1
    
    return lista_ranking

#mostrar_lista()

def pantalla_ranking():
    pygame.init()
    
    #Inicializacion sobre la pantalla
    ANCHO_VENTANA = 1200
    ALTO_VENTANA = 800
    pantalla = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA])
    pygame.display.set_caption("ZOMBAN")
    fondo = pygame.transform.scale(pygame.image.load("imagenes\_background_inicial.py\_background.jpg"),(1200,800))
    icono = pygame.image.load("imagenes\walk_zom_3_izq\image_2.png")
    pygame.display.set_icon(icono)
    
    #sonido ambiente
    ambiente = pygame.mixer.Sound("sonidos\sonido_ambiente_principal.mp3")
    ambiente.set_volume(0.5)
    ambiente.play()

    retorno = ''
    running_flag = True
    while running_flag:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_flag = False
                retorno = "salio"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running_flag = False
                    retorno = "salio"
                if event.key == pygame.K_RETURN:
                    running_flag = False
                    retorno = "continuo"
        
        pantalla.blit(fondo, (0,0))

        ranking = mostrar_lista_ranking()
        y_muestra_texto = 100
        for tupla in ranking:
            muestra_texto(pantalla,"Odachi", f"{tupla[0]}: {int(tupla[1])}",ROJO_TRES, 50, ANCHO_VENTANA//2,ALTO_VENTANA//2 + y_muestra_texto)
            y_muestra_texto += 50

        muestra_texto(pantalla,"Odachi", "ranking de kills",VIDA_COLOR, 150, ANCHO_VENTANA//2,ALTO_VENTANA//3)
        muestra_texto(pantalla,"Odachi", "tu usuario: usuario_1",ROJO, 30, ANCHO_VENTANA//2,ALTO_VENTANA//3 + 100)
        muestra_texto(pantalla,"Odachi", "ESC",ROJO, 30, 50,30)
        muestra_texto(pantalla,"Odachi", "para salir",ROJO, 15, 100,30)
        muestra_texto(pantalla,"Odachi", "enter",ROJO, 30, 1050,30)
        muestra_texto(pantalla,"Odachi", "para continuar",ROJO, 15, 1130,30)
        pygame.display.flip()

    pygame.quit()
    return retorno

