#include <iostream>
#include <windows.h>
#include <conio.h>
#include "graficos.h"
using namespace std;

void moverCursor(int x, int y);
void encontrarJugador(int &x, int &y);
void mostrarBarraVida(string nombre, int vida, int vidaMax);
void dibujarSpritePersonaje(int x, int y);
void dibujarSpriteEnemigo(int x, int y);
int elegirAtaque(struct Personaje &p);
int mostrarMenuBatalla();
int siguienteVivo(struct Personaje arr[], int total, int actual);
void batalla(struct Personaje jugador[], struct Personaje enemigo[]);


char map[10][21] = {
    "##################",
    "#                #",
    "####             #",
    "#  #             #",
    "# @#    $        #",
    "#  # #############",
    "#  #             #",
    "#                #",
    "#                #",
    "##################"
};

void moverCursor(int x, int y) {
    COORD coord = { (SHORT)x, (SHORT)y };
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

void encontrarJugador(int &x, int &y) {
    for (int i = 0; i < 10; i++)
        for (int j = 0; j < 20; j++)
            if (map[i][j] == '@') {
                y = i;
                x = j;
                return;
            }
}

struct Ataque {
    string nombre;
    int danio;
};

struct Personaje {
    string nombre;
    int vida;
    int vidaMax;
    Ataque ataques[2];
};

void mostrarBarraVida(string nombre, int vida, int vidaMax) {
    cout << nombre << " ";
    int largoBarra = 20;
    int vidaVisible = (vida * largoBarra) / vidaMax;
    cout << "[";
    for (int i = 0; i < largoBarra; i++) {
        if (i < vidaVisible)
            cout << "#";
        else
            cout << " ";
    }
    cout << "] " << vida << "/" << vidaMax << endl;
}

void dibujarSpritePersonaje(int x, int y) {
    moverCursor(x, y);     cout << "  O  ";
    moverCursor(x, y + 1); cout << " /|\\ ";
    moverCursor(x, y + 2); cout << " / \\ ";
}

void dibujarSpriteEnemigo(int x, int y) {
    moverCursor(x, y);     cout << "  ^  ";
    moverCursor(x, y + 1); cout << " /#\\ ";
    moverCursor(x, y + 2); cout << " / \\ ";
}

int elegirAtaque(Personaje &p) {
    int seleccion = 0;
    while (true) {
        system("cls");
        cout << "Selecciona un ataque:\n\n";
        for (int i = 0; i < 2; i++) {
            if (i == seleccion)
                cout << "> ";
            else
                cout << "  ";
            cout << p.ataques[i].nombre << "\t";
        }
        cout << endl;

        char tecla = _getch();
        if (tecla == -32) {
            tecla = _getch();
            if (tecla == 75 && seleccion > 0) seleccion--;
            else if (tecla == 77 && seleccion < 1) seleccion++;
        } else if (tecla == 13) {
            return seleccion;
        }
    }
}

int mostrarMenuBatalla() {
    int seleccion = 0;
    string opciones[4] = { "Atacar", "Objeto", "Cambio", "Huir" };

    while (true) {
        system("cls");
        cout << "----- MENU DE BATALLA -----\n\n";

        for (int i = 0; i < 4; i++) {
            if (i == seleccion)
                cout << "> ";
            else
                cout << "  ";
            cout << opciones[i] << (i % 2 == 0 ? "\t" : "\n");
        }

        char tecla = _getch();
        if (tecla == -32) {
            tecla = _getch();
            if (tecla == 72 && seleccion >= 2) seleccion -= 2;
            else if (tecla == 80 && seleccion <= 1) seleccion += 2;
            else if (tecla == 75 && seleccion % 2 == 1) seleccion--;
            else if (tecla == 77 && seleccion % 2 == 0) seleccion++;
        } else if (tecla == 13) {
            return seleccion;
        }
    }
}

int siguienteVivo(Personaje arr[], int total, int actual) {
    for (int i = 0; i < total; i++) {
        if (i != actual && arr[i].vida > 0)
            return i;
    }
    return -1;
}

void batalla(Personaje jugador[], Personaje enemigo[]) {
    int activoJugador = 0, activoEnemigo = 0;
    bool enBatalla = true;

    while (enBatalla) {
        if (jugador[activoJugador].vida <= 0) {
            activoJugador = siguienteVivo(jugador, 2, activoJugador);
            if (activoJugador == -1) {
                cout << "Todos tus pokemon han sido derrotados.\n";
                break;
            }
        }
        if (enemigo[activoEnemigo].vida <= 0) {
            activoEnemigo = siguienteVivo(enemigo, 2, activoEnemigo);
            if (activoEnemigo == -1) {
                cout << "¡Ganaste la batalla!\n";
                break;
            }
        }

        system("cls");
        cout << "------ BATALLA ------\n\n";

        mostrarBarraVida(jugador[activoJugador].nombre, jugador[activoJugador].vida, jugador[activoJugador].vidaMax);
        mostrarBarraVida(enemigo[activoEnemigo].nombre, enemigo[activoEnemigo].vida, enemigo[activoEnemigo].vidaMax);

        dibujarSpritePersonaje(5, 8);
        dibujarSpriteEnemigo(30, 8);

        int opcion = mostrarMenuBatalla();

        switch (opcion) {
            case 0: {
                int ataqueIdx = elegirAtaque(jugador[activoJugador]);
                enemigo[activoEnemigo].vida -= jugador[activoJugador].ataques[ataqueIdx].danio;
                cout << jugador[activoJugador].nombre << " usó " << jugador[activoJugador].ataques[ataqueIdx].nombre << "!\n";
                Sleep(1000);
                break;
            }
            case 1:
                cout << "No tienes objetos...\n";
                Sleep(1000);
                continue;
            case 2: {
                int otro = siguienteVivo(jugador, 2, activoJugador);
                if (otro != -1) {
                    activoJugador = otro;
                    cout << "Cambiando a " << jugador[activoJugador].nombre << "\n";
                } else {
                    cout << "Pokemons derrotados.\n";
                }
                Sleep(1000);
                continue;
            }
            case 3:
                cout << "¡Escapaste de la batalla!\n";
                Sleep(1000);
                enBatalla = false;
                continue;
        }

        if (enemigo[activoEnemigo].vida > 0) {
            int ataqueEnemigo = rand() % 2;
            jugador[activoJugador].vida -= enemigo[activoEnemigo].ataques[ataqueEnemigo].danio;
            cout << enemigo[activoEnemigo].nombre << " usó " << enemigo[activoEnemigo].ataques[ataqueEnemigo].nombre << "!\n";
            Sleep(1000);
        }
    }
}

int main() {
    const int velocidad = 100;
    int nivel = 1;
    bool Parar = false;

    Personaje jugador[2] = {
        { "Raichu", 60, 90, { {"Bola electrica", 40}, {"Trueno", 60} } },
        { "Charizard", 78, 84, { {"Garra dragon", 50}, {"Llamarada", 70} } }
    };
    Personaje enemigo[2] = {
        { "Snorlax", 160, 110, { {"Derribo", 30}, {"Hiper rayo", 60} } },
        { "Blastoise", 79, 83, { {"Surf", 50}, {"Hidro bomba", 70} } }
    };

    while (!Parar && nivel == 1) {
        moverCursor(0, 0);

        for (int y = 0; y < 10; y++) {
            for (int x = 0; x < 20; x++)
                cout << obtenerSimbolo(map[y][x]);
            cout << endl;
        }

        int x, y;
        encontrarJugador(x, y);

        if (GetAsyncKeyState(VK_UP) & 0x8000 && map[y - 1][x] == ' ') {
            map[y][x] = ' ';
            map[y - 1][x] = '@';
        } else if (GetAsyncKeyState(VK_DOWN) & 0x8000 && map[y + 1][x] == ' ') {
            map[y][x] = ' ';
            map[y + 1][x] = '@';
        } else if (GetAsyncKeyState(VK_LEFT) & 0x8000 && map[y][x - 1] == ' ') {
            map[y][x] = ' ';
            map[y][x - 1] = '@';
        } else if (GetAsyncKeyState(VK_RIGHT) & 0x8000) {
            if (map[y][x + 1] == '$') {
                batalla(jugador, enemigo);
                map[y][x + 1] = ' ';
            } else if (map[y][x + 1] == ' ') {
                map[y][x] = ' ';
                map[y][x + 1] = '@';
            }
        }

        Sleep(velocidad);
    }

    return 0;
}
