# Final-pensamiento-algoritmico
Repositorio con los códigos de los 2 juegos
Parqueadero Python
En esta carpeta se encuentran dos tipos de juegos en formato .py de parqueadero.

Parqueadero Ver.1
Este proyecto implementa un sistema básico de gestión de parqueadero en Python, simulando la entrada y salida de vehículos, el cálculo de tarifas y la representación visual del estado del parqueadero.
Características
El sistema de gestión de parqueadero ofrece las siguientes funcionalidades:
•	Representación Visual del Parqueadero: El parqueadero se visualiza como una matriz de caracteres en la consola. Cada carácter representa un elemento específico del mapa:
o	E: Entrada
o	S: Salida
o	█: Pared
o	·: Carretera
o	L: Espacio Libre
o	O: Espacio Ocupado
o	: Espacio Vacío (usado para inicialización)
•	Registro de Entrada de Vehículos:
o	Permite ingresar la placa de un vehículo para registrar su entrada.
o	Asigna automáticamente el primer espacio libre y accesible encontrado en el mapa.
o	Registra la hora exacta de entrada del vehículo.
o	Maneja el caso de que el vehículo ya esté estacionado o que no haya espacios disponibles.
•	Registro de Salida de Vehículos y Cálculo de Tarifa:
o	Solicita la placa del vehículo para registrar su salida.
o	Calcula el tiempo total que el vehículo estuvo estacionado.
o	Calcula la tarifa total a pagar basándose en el tiempo estacionado y la tarifa por hora.
o	Libera el espacio que ocupaba el vehículo en el mapa.
o	Genera un recibo detallado con el tiempo estacionado y el costo.
•	Control de Disponibilidad:
o	El mapa se actualiza dinámicamente para reflejar los espacios ocupados y libres.
o	El sistema lleva un conteo de los espacios libres y ocupados, mostrando la disponibilidad actual en todo momento.
•	Listado de Vehículos Estacionados: Permite visualizar una lista de todos los vehículos actualmente estacionados, incluyendo su placa, la ubicación del espacio que ocupan y la hora de entrada.
•	Accesibilidad de Espacios: Incluye una lógica básica para determinar si un espacio de parqueo es "accesible" (es decir, si está adyacente a una carretera), lo que es fundamental para una simulación más realista.
•	Simulación de Rutas: Aunque simplificado, el sistema indica una "ruta simulada" desde la entrada hasta el espacio asignado y desde el espacio de salida hasta la salida, utilizando los caracteres de carretera.

Parqueadero Ver.2
El juego ofrece las siguientes funcionalidades:

Interfaz Gráfica Sencilla: Utiliza la librería Pygame para crear una ventana de juego con elementos gráficos básicos.
Representación Visual:
Espacios de Parqueo: Cuadrados grises que representan los lugares donde se puede estacionar.
Entrada: Un cuadrado verde que indica el punto de ingreso al parqueadero.
Salida: Un cuadrado rojo que señala el punto de egreso.
Vehículo: Un cuadrado negro que el jugador controla.
Movimiento del Vehículo: El jugador puede mover el vehículo usando las teclas de flecha (arriba, abajo, izquierda, derecha) dentro de los límites de la pantalla.
Registro de Estacionamiento: Cuando el vehículo colisiona con un espacio de parqueo, se considera "estacionado" y se registra el tiempo de inicio.
Cálculo de Tarifa: Al mover el vehículo hacia la zona de salida (cuadrado rojo) después de haberse estacionado, el juego calcula una tarifa basada en el tiempo que el vehículo estuvo estacionado. La tarifa se calcula a 0.1 unidades monetarias por segundo.
Mensajes en Consola: El juego proporciona mensajes en la consola para indicar cuando el vehículo ha sido estacionado correctamente y el costo total al salir.
CONDICIONES IMPORTANTES PARA PODER JUGARLO
Se requiere tener Pygame instalado, para instalarlo solo es necesario escribir en el CMD el siguiente comando: pip install pygame y si se esta usando Python 3 y se tiene problemas con pip entonces utiliza el siguiente: pip3 install pygame


Pokemon

Este juego presenta un pokememon con un sistema simple, en el cual al igual que en el original se puede pover por el mapa y enfrentarse a un rival.

En el juego el usuario empezara desde un punto en el mapa, en el que tendra que moverse por medio de las flechas hasta donde se encuentra el enemigo, al chocar de frente con el enemigo se iniciara el combate automaticamente, el sistema del mapa funciona de la siguiente manera:

• # Como las paredes u obstaculos

•'@' como el jugador (Editado por medio de una libreria propia)

•'$' como el enemigo (Editado por medio de una libreria propia)

Mientras que la batalla se da por medio de un menu de batalla, el cual permite desplazar libremente al usuario por medio de las flechas y elegir cual opcion va a utilizar, en el menu de batalla se da a seleccionar seleccionar:

•"huir" finalizara la batalla 

•"Cambio" Cambiara el pokemon

•"Objeto" No funcionara al no tener objetos

•"Atacar" dirigira al usuario a un menu de batalla donde se podra escojer entre 2 ataques

al finalizar el combate saldra el mensaje de victoria o derrota, dependiendo del resultado del combate.

Integrantes del grupo:

• Juan David Triana

• Santiago Forero
