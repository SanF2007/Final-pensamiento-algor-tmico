#ifndef GRAFICOS_H
#define GRAFICOS_H

#include <string>
using namespace std;

string obtenerSimbolo(char simbolo) {
    switch (simbolo) {
        case '@': return "í";      
        case '$': return "._.";      
        case '#': return "\xDB";   
        case 'H': return "H";      
        case 'E': return "E";      
        default:  return " ";
    }
}

#endif
