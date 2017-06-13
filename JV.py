
import curses 
import random
#mas adelante hago que el usuario pida las dimensiones y bla bla bla, por ahora lo hago asi para probar primero que
#mi algoritmo funciona correctamente xD

def main():
    
    stdscr = curses.initscr()
    matriz = formarMatriz(24,80)#estas son las dimensiones
    matriz = dibujarEsquinas(matriz)
    matriz = lineasVerticales(matriz)
    matriz = celulas_aleatorias(matriz,26,82,95)#EJEMPLO DE CUANDO ES RANDOM PICHILLA el cuarto parametro son las cels vivas
    #stdscr.clear()
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            stdscr.addstr(matriz[i][j])
            j += 1
        stdscr.addstr("\n")
        i += 1
    
    
    stdscr.getkey()
    curses.endwin()

    

def formarMatriz(x,y):
    matriz = []
    i = 0
    x += 2
    y += 2
    while(i < x):
        j = 0
        matriz += [[]]
        while(j < y):
            
            matriz[i] += [" "]
            j += 1
        i += 1
    return matriz

def dibujarEsquinas(ventana):
    ventana[0][0] = "@"
    ventana[0][len(ventana[0])-1] = "@"
    ventana[len(ventana)-1][0] = "@"
    ventana[len(ventana)-1][len(ventana[0])-1] = "@"
    return ventana
    
def lineasVerticales(ventana):
    i = 1
    while(i < len(ventana)-1):
        ventana[i][0] = "|"
        ventana[i][len(ventana[0])-1] = "|"
        i += 1
    
    j = 1
    while(j < len(ventana[0])-1):
        ventana[0][j] = "-"
        ventana[len(ventana)-1][j] = "-"   
        j += 1
        
    return ventana
    

def celulas_aleatorias(matriz,filas,columnas,cantidad):
    coordenadas = crear_coordenadas(filas,columnas)

    while(cantidad > 0):
        posicion = random.randint(0,len(coordenadas)-1)
        matriz[coordenadas[posicion][0]][coordenadas[posicion][1]] = "*"
        coordenadas = coordenadas[:posicion] + coordenadas[posicion+1:]
        cantidad -= 1
        
    return matriz
    
    

def crear_coordenadas(filas,columnas):
    coordenadas = []
    i = 1
    while(i < filas-1):
        j = 1
        while(j < columnas-1):
            coordenadas += [[i,j]]
            j += 1
        i += 1
    
    return coordenadas

    
    
main()

















