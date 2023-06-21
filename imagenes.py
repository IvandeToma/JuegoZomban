import pygame

esta_der = [pygame.transform.scale(pygame.image.load("imagenes\_statico_der\_terrorist_1_Idle_000.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\_statico_der\_terrorist_1_Idle_001.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\_statico_der\_terrorist_1_Idle_002.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\_statico_der\_terrorist_1_Idle_003.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\_statico_der\_terrorist_1_Idle_004.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\_statico_der\_terrorist_1_Idle_005.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\_statico_der\_terrorist_1_Idle_006.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\_statico_der\_terrorist_1_Idle_007.png"),(180,280))]

camina_der = [ pygame.transform.scale(pygame.image.load("imagenes\walk_der\_terrorist_1_Walk_000.png"), (180,280)),
                                pygame.transform.scale(pygame.image.load("imagenes\walk_der\_terrorist_1_Walk_001.png"), (180,280)),
                                pygame.transform.scale(pygame.image.load("imagenes\walk_der\_terrorist_1_Walk_002.png"), (180,280)),
                                pygame.transform.scale(pygame.image.load("imagenes\walk_der\_terrorist_1_Walk_003.png"), (180,280)),
                                pygame.transform.scale(pygame.image.load("imagenes\walk_der\_terrorist_1_Walk_004.png"), (180,280)),
                                pygame.transform.scale(pygame.image.load("imagenes\walk_der\_terrorist_1_Walk_005.png"), (180,280)),
                                pygame.transform.scale(pygame.image.load("imagenes\walk_der\_terrorist_1_Walk_006.png"), (180,280)),
                                pygame.transform.scale(pygame.image.load("imagenes\walk_der\_terrorist_1_Walk_007.png"), (180,280))]

camina_izq = [pygame.transform.scale(pygame.image.load("imagenes\walk_izq\image_0.png"), (180,280)),
                                pygame.transform.scale(pygame.image.load("imagenes\walk_izq\image_1.png"), (180,280)),
                                pygame.transform.scale(pygame.image.load("imagenes\walk_izq\image_2.png"), (180,280)),
                                pygame.transform.scale(pygame.image.load("imagenes\walk_izq\image_3.png"), (180,280)),
                                pygame.transform.scale(pygame.image.load("imagenes\walk_izq\image_4.png"), (180,280)),
                                pygame.transform.scale(pygame.image.load("imagenes\walk_izq\image_5.png"), (180,280)),
                                pygame.transform.scale(pygame.image.load("imagenes\walk_izq\image_6.png"), (180,280)),
                                pygame.transform.scale(pygame.image.load("imagenes\walk_izq\image_7.png"), (180,280))]

esta_izq = [pygame.transform.scale(pygame.image.load("imagenes\_statico_izq\image_0.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\_statico_izq\image_1.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\_statico_izq\image_2.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\_statico_izq\image_3.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\_statico_izq\image_4.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\_statico_izq\image_5.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\_statico_izq\image_6.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\_statico_izq\image_7.png"),(180,280))]

muert = [pygame.transform.scale(pygame.image.load("imagenes\muerto_perso_der\_terrorist_1_Hurt_0.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\muerto_perso_der\_terrorist_1_Hurt_1.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\muerto_perso_der\_terrorist_1_Hurt_2.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\muerto_perso_der\_terrorist_1_Hurt_3.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\muerto_perso_der\_terrorist_1_Hurt_5.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\muerto_perso_der\_terrorist_1_Hurt_6.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\muerto_perso_der\_terrorist_1_Hurt_7.png"),(180,280)),
                            pygame.transform.scale(pygame.image.load("imagenes\muerto_perso_der\_terrorist_1_Hurt_8.png"),(180,280))]

dispara_der = [pygame.transform.scale(pygame.image.load("imagenes\perso_dispara_der\_terrorist_1_Attack1_000.png"), (270,280)),
                                        pygame.transform.scale(pygame.image.load("imagenes\perso_dispara_der\_terrorist_1_Attack1_001.png"), (270,280)),
                                        pygame.transform.scale(pygame.image.load("imagenes\perso_dispara_der\_terrorist_1_Attack1_002.png"), (270,280)),
                                        pygame.transform.scale(pygame.image.load("imagenes\perso_dispara_der\_terrorist_1_Attack1_003.png"), (270,280)),
                                        pygame.transform.scale(pygame.image.load("imagenes\perso_dispara_der\_terrorist_1_Attack1_004.png"), (270,280)),
                                        pygame.transform.scale(pygame.image.load("imagenes\perso_dispara_der\_terrorist_1_Attack1_005.png"), (270,280))]

sangre = pygame.transform.scale(pygame.image.load("imagenes\sangre\sangre_derramada.png"), (100,100))


zombie_izq = [pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_0.png"), (200,280)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_1.png"), (200,280)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_2.png"), (200,280)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_3.png"), (200,280)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_4.png"), (200,280)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_5.png"), (200,280)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_6.png"), (200,280)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_7.png"), (200,280)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_8.png"), (200,280)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_9.png"), (200,280))]

zombie_dos = [pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_0.png"), (300,350)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_1.png"), (300,350)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_2.png"), (300,350)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_3.png"), (300,350)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_4.png"), (300,350)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_5.png"), (300,350)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_6.png"), (300,350)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_7.png"), (300,350)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_8.png"), (300,350)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_3_izq\image_9.png"), (300,350))]

zombie_tres = [pygame.transform.scale(pygame.image.load("imagenes\walk_zom_mujer\image_0.png"), (400,550)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_mujer\image_1.png"), (400,550)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_mujer\image_2.png"), (400,550)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_mujer\image_3.png"), (400,550)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_mujer\image_4.png"), (400,550)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_mujer\image_5.png"), (400,550)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_mujer\image_6.png"), (400,550)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_mujer\image_7.png"), (400,550)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_mujer\image_8.png"), (400,550)),
              pygame.transform.scale(pygame.image.load("imagenes\walk_zom_mujer\image_9.png"), (400,550))]