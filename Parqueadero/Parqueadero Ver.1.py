import datetime
import time # Para simular el paso del tiempo si es necesario

# --- Constantes del Mapa ---
VACIO = " "
CARRETERA = "·"
ENTRADA = "E"
SALIDA = "S"
PARED = "█"
ESPACIO_LIBRE = "L"
ESPACIO_OCUPADO = "O"

# --- Configuración del Parqueadero ---
FILAS_MAPA = 10
COLUMNAS_MAPA = 15
TARIFA_POR_HORA = 2.5  # Ejemplo: 2.5 unidades monetarias por hora

# --- Estructuras de Datos ---
# El mapa se representará como una lista de listas (matriz)
mapa_parqueadero = []
vehiculos_estacionados = {}  # Diccionario para guardar info: { "placa": {"fila": f, "col": c, "hora_entrada": datetime_obj}}

def inicializar_mapa():
    """Crea el diseño inicial del parqueadero."""
    global mapa_parqueadero
    mapa_parqueadero = [[VACIO for _ in range(COLUMNAS_MAPA)] for _ in range(FILAS_MAPA)]

    # Definir paredes exteriores
    for r in range(FILAS_MAPA):
        mapa_parqueadero[r][0] = PARED
        mapa_parqueadero[r][COLUMNAS_MAPA - 1] = PARED
    for c in range(COLUMNAS_MAPA):
        mapa_parqueadero[0][c] = PARED
        mapa_parqueadero[FILAS_MAPA - 1][c] = PARED

    # Definir Entrada y Salida
    mapa_parqueadero[1][1] = ENTRADA
    mapa_parqueadero[FILAS_MAPA - 2][COLUMNAS_MAPA - 2] = SALIDA

    # Definir Carreteras Principales (Ejemplo)
    # Carretera de entrada
    for c in range(1, 7):
        mapa_parqueadero[1][c] = CARRETERA
    for r in range(1, FILAS_MAPA -1):
        mapa_parqueadero[r][6] = CARRETERA # Carretera vertical central
    
    # Carretera hacia la salida
    for c in range(6, COLUMNAS_MAPA - 1):
        mapa_parqueadero[FILAS_MAPA - 2][c] = CARRETERA
    
    # Conexión adicional para acceso
    for r in range(1, FILAS_MAPA -1):
        mapa_parqueadero[r][COLUMNAS_MAPA - 7] = CARRETERA # Otra carretera vertical

    # Definir Espacios de Parqueo (Ejemplo)
    # Bloque 1
    for r in range(2, 5):
        for c in range(2, 5):
            if mapa_parqueadero[r][c] == VACIO: # Solo si no es carretera
                 mapa_parqueadero[r][c] = ESPACIO_LIBRE
    # Bloque 2
    for r in range(6, FILAS_MAPA - 2):
        for c in range(2, 5):
            if mapa_parqueadero[r][c] == VACIO:
                mapa_parqueadero[r][c] = ESPACIO_LIBRE
    
    # Bloque 3
    for r in range(2, 5):
        for c in range(COLUMNAS_MAPA - 5, COLUMNAS_MAPA - 2):
             if mapa_parqueadero[r][c] == VACIO:
                mapa_parqueadero[r][c] = ESPACIO_LIBRE
    # Bloque 4
    for r in range(6, FILAS_MAPA - 2):
        for c in range(COLUMNAS_MAPA - 5, COLUMNAS_MAPA - 2):
            if mapa_parqueadero[r][c] == VACIO:
                mapa_parqueadero[r][c] = ESPACIO_LIBRE

    # Asegurar accesibilidad (simplificado)
    # Esto es un ejemplo, una lógica más compleja podría verificar caminos.
    # Por ahora, nos aseguramos que los espacios estén junto a carreteras.
    # (La lógica anterior ya intenta hacer esto)

def mostrar_mapa():
    """Imprime el mapa del parqueadero en la consola."""
    print("\n--- Mapa del Parqueadero ---")
    for fila in mapa_parqueadero:
        print(" ".join(fila))
    print("--------------------------")
    print(f"{ENTRADA}: Entrada, {SALIDA}: Salida, {CARRETERA}: Carretera")
    print(f"{ESPACIO_LIBRE}: Libre, {ESPACIO_OCUPADO}: Ocupado, {PARED}: Pared")
    mostrar_disponibilidad()

def mostrar_disponibilidad():
    """Muestra la cantidad de espacios libres y ocupados."""
    libres = 0
    ocupados = 0
    for r in range(FILAS_MAPA):
        for c in range(COLUMNAS_MAPA):
            if mapa_parqueadero[r][c] == ESPACIO_LIBRE:
                libres += 1
            elif mapa_parqueadero[r][c] == ESPACIO_OCUPADO:
                ocupados += 1
    print(f"Espacios Libres: {libres}")
    print(f"Espacios Ocupados: {ocupados}")
    print("--------------------------")


def es_accesible(fila, col):
    """
    Verifica si un espacio de parqueo es accesible desde una carretera.
    Simplificado: verifica si hay una carretera adyacente (no diagonal).
    """
    adyacentes = [
        (fila - 1, col), (fila + 1, col),
        (fila, col - 1), (fila, col + 1)
    ]
    for r_ady, c_ady in adyacentes:
        if 0 <= r_ady < FILAS_MAPA and 0 <= c_ady < COLUMNAS_MAPA:
            if mapa_parqueadero[r_ady][c_ady] in [CARRETERA, ENTRADA, SALIDA]:
                return True
    return False

def encontrar_espacio_libre():
    """Encuentra la primera coordenada (fila, col) de un espacio libre y accesible."""
    for r in range(FILAS_MAPA):
        for c in range(COLUMNAS_MAPA):
            if mapa_parqueadero[r][c] == ESPACIO_LIBRE and es_accesible(r,c):
                # Simular ruta (muy básico)
                # En un juego más complejo, esto usaría un algoritmo de pathfinding
                print(f"Ruta simulada: Desde {ENTRADA} por {CARRETERA} hasta ({r},{c})")
                return r, c
    return None, None

def registrar_entrada_vehiculo():
    """Registra la entrada de un vehículo."""
    placa = input("Ingrese la placa del vehículo: ").upper()
    if placa in vehiculos_estacionados:
        print("Error: Un vehículo con esta placa ya se encuentra en el parqueadero.")
        return

    fila_libre, col_libre = encontrar_espacio_libre()

    if fila_libre is not None:
        mapa_parqueadero[fila_libre][col_libre] = ESPACIO_OCUPADO
        hora_entrada = datetime.datetime.now()
        vehiculos_estacionados[placa] = {
            "fila": fila_libre,
            "col": col_libre,
            "hora_entrada": hora_entrada
        }
        print(f"Vehículo {placa} estacionado en ({fila_libre}, {col_libre}) a las {hora_entrada.strftime('%H:%M:%S')}.")
    else:
        print("Lo sentimos, el parqueadero está lleno o no hay espacios accesibles.")

def calcular_tarifa(placa):
    """Calcula la tarifa a pagar por un vehículo."""
    if placa not in vehiculos_estacionados:
        print("Error: Vehículo no encontrado.")
        return None, None

    info_vehiculo = vehiculos_estacionados[placa]
    hora_entrada = info_vehiculo["hora_entrada"]
    hora_salida = datetime.datetime.now()

    tiempo_estacionado = hora_salida - hora_entrada
    horas_estacionado = tiempo_estacionado.total_seconds() / 3600.0

    # Redondear hacia arriba a la próxima hora o fracción para el cobro
    if horas_estacionado < 1:
        horas_a_cobrar = 1
    else:
        horas_a_cobrar = round(horas_estacionado + 0.49) # Redondeo simple hacia arriba

    costo = horas_a_cobrar * TARIFA_POR_HORA
    return costo, tiempo_estacionado

def registrar_salida_vehiculo():
    """Registra la salida de un vehículo y calcula la tarifa."""
    placa = input("Ingrese la placa del vehículo a retirar: ").upper()

    if placa not in vehiculos_estacionados:
        print("Error: Vehículo con placa {} no encontrado en el parqueadero.".format(placa))
        return

    costo, tiempo_total = calcular_tarifa(placa)

    if costo is not None:
        info_vehiculo = vehiculos_estacionados[placa]
        mapa_parqueadero[info_vehiculo["fila"]][info_vehiculo["col"]] = ESPACIO_LIBRE
        del vehiculos_estacionados[placa]

        print(f"\n--- Recibo de Salida ---")
        print(f"Vehículo: {placa}")
        print(f"Tiempo estacionado: {str(tiempo_total).split('.')[0]} (HH:MM:SS)") # Muestra solo horas, min, seg
        print(f"Costo total: ${costo:.2f}")
        print(f"Vehículo {placa} ha salido del parqueadero.")
        print(f"Ruta simulada: Desde ({info_vehiculo['fila']},{info_vehiculo['col']}) por {CARRETERA} hasta {SALIDA}")

def main():
    """Función principal del juego."""
    inicializar_mapa()

    while True:
        mostrar_mapa()
        print("\nOpciones del Parqueadero:")
        print("1. Registrar entrada de vehículo")
        print("2. Registrar salida de vehículo")
        print("3. Ver vehículos estacionados")
        print("4. Salir del sistema")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_entrada_vehiculo()
        elif opcion == "2":
            registrar_salida_vehiculo()
        elif opcion == "3":
            if not vehiculos_estacionados:
                print("\nNo hay vehículos estacionados actualmente.")
            else:
                print("\n--- Vehículos Estacionados ---")
                for placa, datos in vehiculos_estacionados.items():
                    print(f"Placa: {placa}, Espacio: ({datos['fila']},{datos['col']}), Entrada: {datos['hora_entrada'].strftime('%Y-%m-%d %H:%M:%S')}")
                print("-----------------------------")
        elif opcion == "4":
            print("Saliendo del sistema de parqueadero. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        
        input("\nPresione Enter para continuar...") # Pausa para que el usuario pueda leer

if __name__ == "__main__":
    main()
