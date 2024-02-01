#Menu
from Configuración import *
from src.importMethod import *
import sys

def abrir_ventana(titulo):

    ventana_nueva = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption(titulo)

    # Cargar la imagen de fondo y redimensionar
    imagen_fondo_nueva = pygame.transform.scale(imagen_fondo_nueva, (Ancho_Pantalla, Alto_Pantalla))

    # Crear una lista de nombres para las ventanas
    ventanas = ["Ventana 1", "Ventana 2", "Ventana 3", "Ventana 4"]

    # Calcular el espacio total necesario para los botones
    espacio_total = len(ventanas) * 120  # Espacio entre los botones y el espacio adicional

    # Calcular la posición y inicial para centrar los botones
    pos_y_inicial = (Alto_Pantalla - espacio_total) // 2

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
            boton_ventana = pygame.Rect((Ancho_Pantalla - 300) // 2.3, pos_y_inicial + i * 120, 300, 100)
            pygame.draw.rect(ventana_nueva, blanco, boton_ventana)
            pygame.draw.rect(ventana_nueva, (0, 0, 0), boton_ventana, 5)  # Borde del botón de ventana

            # Crear texto del botón de ventana
            fuente_boton_ventana = pygame.font.Font(None, 30)
            texto_boton_ventana = fuente_boton_ventana.render(nombre_ventana, True, (0, 0, 0))
            ventana_nueva.blit(texto_boton_ventana, (boton_ventana.x + (boton_ventana.width - texto_boton_ventana.get_width()) // 2,
                                                     boton_ventana.y + (boton_ventana.height - texto_boton_ventana.get_height()) // 2))

        pygame.display.flip()
        reloj.tick(60)

def pantalla_carga():
    # Configuración de la barra de carga
    barra_carga_ancho = 600
    barra_carga_alto = 50
    barra_carga_color_lleno = (50, 150, 50)
    barra_carga_color_vacio = (150, 150, 150)
    barra_carga_x = (Ancho_Pantalla - barra_carga_ancho) // 2.3
    barra_carga_y = (Alto_Pantalla - barra_carga_alto) // 2.3  
  
    # Simulando una carga de 2 segundos
    tiempo_carga = 1000
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
    Ventana_Principal.blit(texto_carga, ((Ancho_Pantalla - texto_carga.get_width()) // 2.3, (Alto_Pantalla - texto_carga.get_height()) // 2.3))
    pygame.display.flip()

    # Puedes agregar aquí la carga de otros recursos como imágenes, sonidos, etc.
    pygame.time.wait(200)  # Simulando una carga de 2 segundos


