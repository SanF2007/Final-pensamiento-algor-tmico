import pygame
import time

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 600, 400
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Parqueadero 🚗")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (100, 100, 100)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Definir posiciones del parqueadero
espacios = [(100, 100), (200, 100), (300, 100), (400, 100)]
entrada = (50, 300)
salida = (500, 300)

# Vehículo
vehiculo = pygame.Rect(entrada[0], entrada[1], 40, 40)
registrado = False
tiempo_inicio = None

# Bucle del juego
ejecutando = True
while ejecutando:
    PANTALLA.fill(BLANCO)

    # Dibujar espacios de parqueo
    for pos in espacios:
        pygame.draw.rect(PANTALLA, GRIS, (*pos, 40, 40))
    
    # Dibujar entrada y salida
    pygame.draw.rect(PANTALLA, VERDE, (*entrada, 40, 40))
    pygame.draw.rect(PANTALLA, ROJO, (*salida, 40, 40))

    # Dibujar vehículo
    pygame.draw.rect(PANTALLA, NEGRO, vehiculo)

    # Capturar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Capturar teclas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and vehiculo.x > 0:
        vehiculo.x -= 5
    if teclas[pygame.K_RIGHT] and vehiculo.x < ANCHO - 40:
        vehiculo.x += 5
    if teclas[pygame.K_UP] and vehiculo.y > 0:
        vehiculo.y -= 5
    if teclas[pygame.K_DOWN] and vehiculo.y < ALTO - 40:
        vehiculo.y += 5

    # Registro de ingreso
    if not registrado and any(vehiculo.colliderect(pygame.Rect(*pos, 40, 40)) for pos in espacios):
        registrado = True
        tiempo_inicio = time.time()
        print("Vehículo estacionado correctamente.")

    # Salida y cálculo de tarifa
    if registrado and vehiculo.colliderect(pygame.Rect(*salida, 40, 40)):
        tiempo_total = round(time.time() - tiempo_inicio, 2)
        costo = tiempo_total * 0.1  # Tarifa ficticia por segundo
        print(f"El vehículo ha salido. Tarifa: ${costo}")
        registrado = False

    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()
