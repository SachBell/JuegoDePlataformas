import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla principal en modo pantalla completa


# Cargar la imagen de fondo y redimensionar

# Crear un reloj para controlar la velocidad de la aplicación


# Definir colores


# Función para abrir una nueva ventana
def abrir_ventana(titulo):
    ventana_nueva = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption(titulo)

    # Cargar la imagen de fondo y redimensionar
    
    # Crear una lista de nombres para las ventanas
    ventanas = ["Ventana 1", "Ventana 2", "Ventana 3", "Ventana 4"]

    # Calcular el espacio total necesario para los botones
    espacio_total = len(ventanas) * 120  # Espacio entre los botones y el espacio adicional

    # Calcular la posición y inicial para centrar los botones
    pos_y_inicial = (alto_pantalla - espacio_total) // 2

    while True:  # Bucle para la nueva ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        ventana_nueva.blit(imagen_fondo_nueva, (0, 0))

        # Loop para crear y mostrar los botones para las ventanas
        for i, nombre_ventana in enumerate(ventanas):
            # Crear botón para la ventana
            boton_ventana = pygame.Rect((ancho_pantalla - 300) // 2.3, pos_y_inicial + i * 120, 300, 100)
            pygame.draw.rect(ventana_nueva, blanco, boton_ventana)
            pygame.draw.rect(ventana_nueva, (0, 0, 0), boton_ventana, 5)  # Borde del botón de ventana

            # Crear texto del botón de ventana
            fuente_boton_ventana = pygame.font.Font(None, 30)
            texto_boton_ventana = fuente_boton_ventana.render(nombre_ventana, True, (0, 0, 0))
            ventana_nueva.blit(texto_boton_ventana, (boton_ventana.x + (boton_ventana.width - texto_boton_ventana.get_width()) // 2,
                                                     boton_ventana.y + (boton_ventana.height - texto_boton_ventana.get_height()) // 2))

        pygame.display.flip()
        reloj.tick(60)

# Función para la pantalla de carga
# Función para la pantalla de carga
def pantalla_carga():
    # Configuración de la barra de carga
    barra_carga_ancho = 600
    barra_carga_alto = 50
    barra_carga_color_lleno = (50, 150, 50)
    barra_carga_color_vacio = (150, 150, 150)
    barra_carga_x = (ancho_pantalla - barra_carga_ancho) // 2.3
    barra_carga_y = (alto_pantalla - barra_carga_alto) // 2.3  
    
    # Simulando una carga de 2 segundos
    tiempo_carga = 2000
    tiempo_inicial = pygame.time.get_ticks()    

    while pygame.time.get_ticks() - tiempo_inicial < tiempo_carga:
        progreso = (pygame.time.get_ticks() - tiempo_inicial) / tiempo_carga
        pygame.draw.rect(Ventana_Principal, barra_carga_color_lleno, (barra_carga_x, barra_carga_y, int(barra_carga_ancho * progreso), barra_carga_alto))
        pygame.draw.rect(Ventana_Principal, barra_carga_color_vacio, (barra_carga_x + int(barra_carga_ancho * progreso), barra_carga_y, int(barra_carga_ancho * (1 - progreso)), barra_carga_alto))
        pygame.display.update()

    # Puedes agregar aquí la carga de otros recursos como imágenes, sonidos, etc.

    # Aquí puedes cargar todos los recursos necesarios
    # Mientras se cargan, puedes mostrar una pantalla de carga
    # Puedes mostrar un mensaje o una animación de carga

    # Simulando una carga con un simple mensaje
    font = pygame.font.Font(None, 46)
    texto_carga = font.render("Cargando...", True, blanco)
    Ventana_Principal.blit(texto_carga, ((ancho_pantalla - texto_carga.get_width()) // 2.3, (alto_pantalla - texto_carga.get_height()) // 2.3))
    pygame.display.flip()

    # Puedes agregar aquí la carga de otros recursos como imágenes, sonidos, etc.
    pygame.time.wait(2000)  # Simulando una carga de 2 segundos

# Llamar a la pantalla de carga antes de entrar al bucle principal
pantalla_carga()

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
            if (ancho_pantalla - 250) // 2.3 < event.pos[0] < ((ancho_pantalla - 250) // 2.3) + 250 and alto_pantalla - 380 < event.pos[1] < alto_pantalla - 300:
                abrir_ventana("Selección de nivel")
            elif (ancho_pantalla - 300) // 2.3 < event.pos[0] < ((ancho_pantalla - 300) // 2.3) + 300 and alto_pantalla - 180 < event.pos[1] < alto_pantalla - 100:
                pygame.quit()
                sys.exit()

    Ventana_Principal.blit(imagen_fondo_principal, (0, 0))

    # Agregar un título centrado en la parte superior de la ventana principal
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
