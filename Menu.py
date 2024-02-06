#Menu
from Configuración import *
from Importaciones import *
import sys
import random

class Menus:
    
    def __init__(self) -> None:
        self.tiempo_carga = 1000
        self.tiempo_inicial = pygame.time.get_ticks()
        self.ventana_nueva = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.imagen_fondo_nueva = pygame.transform.scale(imagen_fondo_nueva, (Ancho_Pantalla, Alto_Pantalla))


    def abrir_ventana(self, titulo):

        
        pygame.display.set_caption(titulo)

        # Cargar la imagen de fondo y redimensionar
        

        # Crear una lista de nombres para las ventanas
        self.ventanas = ["Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4"]

        # Calcular el espacio total necesario para los botones
        self.espacio_total = len(self.ventanas) * 120  # Espacio entre los botones y el espacio adicional

        # Calcular la posición y inicial para centrar los botones
        self.pos_y_inicial = (Alto_Pantalla - self.espacio_total) // 2

        while True:  # Bucle para la nueva ventana
            

            self.ventana_nueva.blit(imagen_fondo_nueva, (0, 0))

            # Loop para crear y mostrar los botones para las ventanas
            for i, nombre_ventana in enumerate(self.ventanas):
                # Crear botón para la ventana
                self.boton_ventana = pygame.Rect((Ancho_Pantalla - 300) // 2.3, self.pos_y_inicial + i * 120, 300, 100)
                pygame.draw.rect(self.ventana_nueva, blanco, self.boton_ventana)
                pygame.draw.rect(self.ventana_nueva, (0, 0, 0), self.boton_ventana, 5)  # Borde del botón de ventana

                # Crear texto del botón de ventana
                self.fuente_boton_ventana = pygame.font.Font(None, 30)
                self.texto_boton_ventana = self.fuente_boton_ventana.render(nombre_ventana, True, (0, 0, 0))
                self.ventana_nueva.blit(self.texto_boton_ventana, (self.boton_ventana.x + (self.boton_ventana.width - self.texto_boton_ventana.get_width()) // 2,
                                                        self.boton_ventana.y + (self.boton_ventana.height - self.texto_boton_ventana.get_height()) // 2))

            pygame.display.flip()
            reloj.tick(60)

    def pantalla_carga(self):
        
        self.barra_carga_ancho = 600
        self.barra_carga_alto = 50
        self.barra_carga_color_lleno = (50, 150, 50)
        self.barra_carga_color_vacio = (150, 150, 150)
        self.barra_carga_x = (Ancho_Pantalla - self.barra_carga_ancho) // 2.3
        self.barra_carga_y = (Alto_Pantalla - self.barra_carga_alto) // 2.3
        
        num_particulas = 30
        particulas = [{'x': random.randint(0, Ancho_Pantalla),
                    'y': random.randint(0, Alto_Pantalla),
                    'dx': random.uniform(-2, 2),
                    'dy': random.uniform(-2, 2),
                    'radio': random.randint(5, 15),
                    'color': celeste} for _ in range(num_particulas)]

        while pygame.time.get_ticks() - self.tiempo_inicial < self.tiempo_carga:
            Ventana_Principal.fill((0, 0, 0))  # Limpiar la pantalla

            # Dibujar las partículas
            for particula in particulas:
                pygame.draw.circle(Ventana_Principal, particula['color'], (int(particula['x']), int(particula['y'])), particula['radio'])

                # Actualizar posición de la partícula
                particula['x'] += particula['dx']
                particula['y'] += particula['dy']

                # Rebotar en los bordes de la pantalla
                if particula['x'] <= 0 or particula['x'] >= Ancho_Pantalla:
                    particula['dx'] *= -1
                if particula['y'] <= 0 or particula['y'] >= Alto_Pantalla:
                    particula['dy'] *= -1  
                pygame.time.delay(100)

                progreso = (pygame.time.get_ticks() - self.tiempo_inicial) / self.tiempo_carga
                pygame.draw.rect(Ventana_Principal, self.barra_carga_color_lleno, (self.barra_carga_x, self.barra_carga_y, int(self.barra_carga_ancho * progreso), self.barra_carga_alto))
                pygame.draw.rect(Ventana_Principal, self.barra_carga_color_vacio, (self.barra_carga_x + int(self.barra_carga_ancho * progreso), self.barra_carga_y, int(self.barra_carga_ancho * (1 - progreso)), self.barra_carga_alto))
                pygame.display.update()
                pygame.display.flip()
    
        # Simulando una carga de 2 segundos
        pygame.time.delay(1000)
        
        
            

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
        
    def MenuPrincipal(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (Ancho_Pantalla - 250) // 2.3 < event.pos[0] < ((Ancho_Pantalla - 250) // 2.3) + 250 and Alto_Pantalla - 380 < event.pos[1] < Alto_Pantalla - 300:
                        self.abrir_ventana("Selección de nivel")
                    elif (Ancho_Pantalla - 300) // 2.3 < event.pos[0] < ((Ancho_Pantalla - 300) // 2.3) + 300 and Alto_Pantalla - 180 < event.pos[1] < Alto_Pantalla - 100:
                        pygame.quit()
                        sys.exit()


    
    


