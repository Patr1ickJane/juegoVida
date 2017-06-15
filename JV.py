
import curses 
import random

#mas adelante hago que el usuario pida las dimensiones y bla bla bla, por ahora lo hago asi para probar primero que
#mi algoritmo funciona correctamente xD
#PARA QUE FUNCIONE DEBE TENER LA VENTANA DE COMANDOS TOTALMENTE ABIERTA, ESOS DETAALLES GAYS LOS ARREGLO AL FINAL
#PERO SI LO PROBAS Y TENES ERRORES ES POR ESO XD
#SI QUERES PROBAR OTRAS DIMENSIONES AHI LAS CAMBIAS EN LOS PARAMETROS, MAS ADELANTE HAGO EL USUARIO LO PIDA
#QUIERO PRIMERO ASEGURARME QUE LA PINGA FUNCIONA 
def main():
    parar = "s"
    #pantalla = curses.initscr()
    stdscr = curses.initscr()
    matriz = formarMatriz(24,80)#estas son las dimensiones
    matriz = dibujarEsquinas(matriz)
    matriz = lineasRectas(matriz)
    matriz = celulas_aleatorias(matriz,26,82,1000)#EJEMPLO DE CUANDO ES RANDOM PICHILLA el cuarto parametro son las cels vivas
                                             #las dimensiones aumentan en 2 en cada lado, porque les estoy metiendo
                                             #2 lineas mas para dibujar el cuadradito ese gay, por si eso te confunde
                                             #osea ahi en realidad la matriz de juego es 24 - 80 
    #caca = 0
    #letra = "a"
    while(True):
        #matriz = celulas_aleatorias(matriz,7,7,5)
        i = 0
        while i < len(matriz):
            j = 0
            while j < len(matriz[0]):
                stdscr.addstr(matriz[i][j])
            
                j += 1
            stdscr.addstr("\n")
            i += 1
        stdscr.refresh()
        #stdscr.getkey()
        curses.napms(700)
        stdscr.clear()
        matriz = sucesos(matriz,24,80)
        matriz = dibujarEsquinas(matriz)
        matriz = lineasRectas(matriz)
    
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

def dibujarEsquinas(matriz):
    matriz[0][0] = "@"
    matriz[0][len(matriz[0])-1] = "@"
    matriz[len(matriz)-1][0] = "@"
    matriz[len(matriz)-1][len(matriz[0])-1] = "@"
    return matriz
    
def lineasRectas(matriz):
    i = 1
    while(i < len(matriz)-1):
        matriz[i][0] = "|"
        matriz[i][len(matriz[0])-1] = "|"
        i += 1
    
    j = 1
    while(j < len(matriz[0])-1):
        matriz[0][j] = "-"
        matriz[len(matriz)-1][j] = "-"   
        j += 1
        
    return matriz
    

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


def sucesos(matriz,x,y):
    nueva_matriz = formarMatriz(x,y)
    i = 1
    while(i <= len(matriz)-2):
        j = 1
        nueva_matriz[i] 
        while(j <= len(matriz[0])-2):
            celulas_vivas = nacer_morir(i,j,matriz)
            
            if matriz[i][j] == "*" and (celulas_vivas-1 != 2 and celulas_vivas-1 != 3):
                nueva_matriz[i][j] = " "
            elif matriz[i][j] == "*" and (celulas_vivas-1 == 2 or celulas_vivas-1 == 3):
                nueva_matriz[i][j] = "*"
            
            elif matriz[i][j] == " " and celulas_vivas == 3:
                nueva_matriz[i][j] = "*"
            else:
                nueva_matriz[i][j] = " "
            j += 1
        i += 1
    return nueva_matriz


def nacer_morir(x,y,universo):
    
    celulas_vivas = 0
    j = y - 1
    while(j <= y+1):
        i = x - 1
        while(i <= x+1):
            
            if j != 0 and j != len(universo[0]) - 1 and i != 0 and i != len(universo)-1:# no sobrepasa ningun limite
                if universo[i][j] == "*":
                    celulas_vivas += 1
            
            elif j == 0:#sobre pasa sobre la primer columna
                if i == 0:#esquina sup derecha a esquina inf izq
                    if universo[len(universo)-2][len(universo[0]) - 2] == "*":
                        celulas_vivas += 1
                elif i == len(universo)-1:#esquina inf izq a esq sup der
                    if universo[1][len(universo[0])-2] == "*":
                        celulas_vivas += 1
                
                elif universo[i][len(universo[0])-2] == "*":
                    
                    celulas_vivas += 1
            
            elif i == 0:#sobre pasa sobre la primer fila
                if j == len(universo[0]) - 1:#esq sup izq a esq inf der
                    if universo[len(universo)-2][1] == "*":
                        celulas_vivas += 1
                elif universo[len(universo)-2][j] == "*":
                    celulas_vivas += 1 
            
            
            
            elif j == len(universo[0]) - 1:#sobre pasa en ultima columna
                if i == len(universo) - 1:#esq inf der a eqn sup izq
                    if universo[1][1] == "*":
                        celulas_vivas += 1
                else:
                    if universo[i][1] == "*":
                        celulas_vivas += 1
                        
            elif i == len(universo) - 1:#sobrepasa ultima fila, creo que hay que arreglar vamos a ver
               if universo[1][j] == "*":
                    celulas_vivas += 1
            i += 1
        j += 1
    
    return celulas_vivas
            
                
            




main()

















