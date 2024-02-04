import pygame
import sys


# Llamar a la pantalla de carga antes de entrar al bucle principal


# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (Ancho_Pantalla - 250) // 2.3 < event.pos[0] < ((ancho_pantalla - 250) // 2.3) + 250 and alto_pantalla - 380 < event.pos[1] < alto_pantalla - 300:
                abrir_ventana("Selección de nivel")
            elif (ancho_pantalla - 300) // 2.3 < event.pos[0] < ((ancho_pantalla - 300) // 2.3) + 300 and alto_pantalla - 180 < event.pos[1] < alto_pantalla - 100:
                pygame.quit()
                sys.exit()

    Ventana_Principal.blit(imagen_fondo_principal, (0, 0))

    # Agregar un título centra
    # do en la parte superior de la ventana principal
    fuente_titulo = pygame.font.Font(None, 80)
    titulo_texto = fuente_titulo.render("¡HUMAN JUMP!", True, blanco)
    Ventana_Principal.blit(titulo_texto, ((ancho_pantalla - titulo_texto.get_width()) // 2.3, alto_pantalla * 0.10))#desplaza hacia abajo el titutlo

    # Crear botón "Jugar" centrado en la parte inferior de la ventana principal
    boton_jugar = pygame.Rect((ancho_pantalla - 300) // 2.3, alto_pantalla - 380, 300, 100)
    pygame.draw.rect(Ventana_Principal, blanco, boton_jugar)
    pygame.draw.rect(Ventana_Principal, (0, 0, 0), boton_jugar, 5)  # Borde del botón "Jugar"

    fuente_boton = pygame.font.Font(None, 30)
    texto_boton = fuente_boton.render("JUGAR", True, (0, 0, 0))
    Ventana_Principal.blit(texto_boton, (boton_jugar.x + (boton_jugar.width - texto_boton.get_width()) // 2,
                                         boton_jugar.y + (boton_jugar.height - texto_boton.get_height()) // 2))

    # Crear botón "Salir" centrado en la parte inferior de la ventana principal
    boton_salir_principal = pygame.Rect((ancho_pantalla - 300) // 2.3, alto_pantalla - 180, 300, 100)
    pygame.draw.rect(Ventana_Principal, blanco, boton_salir_principal)
    pygame.draw.rect(Ventana_Principal, (0, 0, 0), boton_salir_principal, 5)  # Borde del botón "Salir"

    fuente_boton_salir_principal = pygame.font.Font(None, 30)
    texto_boton_salir_principal = fuente_boton_salir_principal.render("Salir", True, (0, 0, 0))
    Ventana_Principal.blit(texto_boton_salir_principal, (boton_salir_principal.x + (boton_salir_principal.width - texto_boton_salir_principal.get_width()) // 2,
                                                          boton_salir_principal.y + (boton_salir_principal.height - texto_boton_salir_principal.get_height()) // 2))

    pygame.display.flip()
    reloj.tick(60)


 #Crear botón "Salir" centrado en la parte inferior de la ventana secundaria
        #boton_salir_nueva = pygame.Rect((ancho_pantalla - 300) // 2, alto_pantalla - 150, 300, 100)
        #pygame.draw.rect(ventana_nueva, blanco, boton_salir_nueva)
        #pygame.draw.rect(ventana_nueva, (0, 0, 0), boton_salir_nueva, 5)  # Borde del botón "Salir"

        #fuente_boton_salir = pygame.font.Font(None, 20)
        #texto_boton_salir = fuente_boton_salir.render("Salir", True, (0, 0, 0))
        #ventana_nueva.blit(texto_boton_salir, (boton_salir_nueva.x + (boton_salir_nueva.width - texto_boton_salir.get_width()) // 2,
                                               #boton_salir_nueva.y + (boton_salir_nueva.height - texto_boton_salir.get_height()) // 2))
