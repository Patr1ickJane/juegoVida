#from Principal import mostrar_tablero
import random

def configurado(x,y,vivir,nacer,cantidad_celulas):
    '''
    Entradas: x = cantidad de filas
              y = cantidad de columnas
              vivir = condiciones para que una celula viva
              nacer = condiciones para que una celula nazca
              cantidad_celulas = cantidad de celulas en el universo
    salidas: el universo,vivir,nacer
    Funcion: recibe las caracteristicas del juego y crea un universo que actue conforme a esas caracteristicas
    '''
    matriz = formarMatriz(x,y)
    matriz = dibujarEsquinas(matriz)
    matriz = lineasRectas(matriz)
    matriz = celulas_aleatorias(matriz,x+2,y+2,cantidad_celulas)
    return matriz,vivir,nacer

def aleatorio(cantidad_celulas):
    '''
    Entradas: cantidad_celulas = celulas que habran en el universo
    Salidas: el universo, condiciones para que una celula vva, condiciones para que una celula nazca
    Funcion: forma un universo con celulas random y con la modalidad 23/3 
    '''
    matriz = formarMatriz(24,80)
    matriz = dibujarEsquinas(matriz)
    matriz = lineasRectas(matriz)
    matriz = celulas_aleatorias(matriz,26,82,cantidad_celulas)
    
    return matriz,"23","3"
    

def celulas_aleatorias(matriz,filas,columnas,cantidad):
    '''
    Entradas: matriz = universo
              filas = cantidad de filas
              columnas = cantddad de columnas
              cantidad = cantidad de celulas rando en el universo
    Salidas: matriz
    Funcion: coloca celulas aleatorias en el universo, llama una funcion que crea coordenadas y de ahi escoje random las coordenadas y coloca las celulas
    '''
    coordenadas = crear_coordenadas(filas,columnas)

    while(cantidad > 0):
        posicion = random.randint(0,len(coordenadas)-1)
        matriz[coordenadas[posicion][0]][coordenadas[posicion][1]] = "*"
        coordenadas = coordenadas[:posicion] + coordenadas[posicion+1:]
        cantidad -= 1
        
    return matriz
    
    

def crear_coordenadas(filas,columnas):
    '''
    Entradas: filas = numero de filas
              columnas = numero de columnas
    Salidas: una lista con cada coordenada que hay en la matriz
    Funcion: crea coordenadas de cada posicion de la matriz lo guarda en una lista y la devuelve
    '''
    coordenadas = []
    i = 1
    while(i < filas-1):
        j = 1
        while(j < columnas-1):
            coordenadas += [[i,j]]
            j += 1
        i += 1
    
    return coordenadas

def oscilador():
    '''
    Entradas: ninguna
    Salidas: el universo, condiciones para que una celula vva, condiciones para que una celula nazca
    Funcion: crea un universo oscilador con la modalidad 23/3
    '''
    matriz = formarMatriz(24,82)
    matriz = dibujarEsquinas(matriz)
    matriz = lineasRectas(matriz)
    matriz = pajaritos(matriz)
    return matriz,"23","3"
    
def pajaritos(matriz):
    '''
    Entradas: matriz = tablero de juego
    Salidas: el tablero ya dibujado
    Funcion: predefine las celulas vivas en el tablero de manera que queden pajaritos lindos volando a la hora
             de iniciar el juego
    '''
    pajaritos_dibujados = 0
    i = 1
    while(pajaritos_dibujados < 3):
        matriz[i][3] = "*"
        matriz[i][4] = "*"
        matriz[i+1][1] = "*"
        matriz[i+1][6] = "*"
        matriz[i+2][7] = "*"
        matriz[i+3][1] = "*"
        matriz[i+3][7] = "*"
        j = 2
        while(j <= 7):
            matriz[i+4][j] = "*"
            j += 1
        pajaritos_dibujados += 1
        i += 8
    return matriz





def formarMatriz(x,y):
    '''
    Entradas: x = cantidad de columnas que tendra la matriz
              y = cantidad de filas que tendra la matriz
    Salidas: una matriz que sera el tablero
    Funcion: forma la matriz que sera el tablero 
    '''
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
    '''
    Entradas: el tablero
    Salidas: el tablero con las lineas dibujadas
    Funcion: dibuja las esquinas a la par del tablero
    '''
    matriz[0][0] = "@"
    matriz[0][len(matriz[0])-1] = "@"
    matriz[len(matriz)-1][0] = "@"
    matriz[len(matriz)-1][len(matriz[0])-1] = "@"
    return matriz
    
def lineasRectas(matriz):
    '''
    Entradas: el tablero
    Salidas: el tablero con las lineas dibujadas
    Funcion: dibuja lineas rectas a la par del tablero
    '''
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




def sucesos(matriz,x,y,vivir,nacer):
    '''
    Entradas: x = cantidad de filas
              y = cantidad de columnas
              vivir = condiciones para que una celula viva
              nacer = condiciones para que una celula nazca
              
    salidas: el universo actualizado
    Funcion: esta funcion recorre la matriz y llama una funcion para ver sus vecinas
    y devuelve la cantidad de veinas que estan vivas, y dependiendo del modo de juego
    mata, nace, o deja vivir las celulas correspondientes las guarda cada una en otra matriz
    y la devuelve
    '''
    nueva_matriz = formarMatriz(x,y)
    i = 1
    while(i <= len(matriz)-2):
        j = 1
        nueva_matriz[i] 
        while(j <= len(matriz[0])-2):
            celulas_vivas = nacer_morir(i,j,matriz)
            
            if matriz[i][j] == "*" and celulas_vivas not in vivir:
                nueva_matriz[i][j] = " "
            elif matriz[i][j] == "*" and celulas_vivas in vivir:
                nueva_matriz[i][j] = "*"
            
            elif matriz[i][j] == " " and celulas_vivas in nacer:
                nueva_matriz[i][j] = "*"
            else:
                nueva_matriz[i][j] = " "
            j += 1
        i += 1
    return nueva_matriz


def nacer_morir(x,y,universo):
    '''
    Entradas: x = posicion de columna de la celula que se esta revisando
              y = posicion de fila de la celula que se esta revisando
              universo = el tablero de juego
    Salidas: cantidad de celulas vivas alrededor de la celula que se esta revisando
    funcion: revisa las celulas vecinas de la celula actual y cuenta la cantidad que estan vivas
    y lo devuelve
    '''
    
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
    if universo[x][y] == "*":
        celulas_vivas -= 1
    return str(celulas_vivas)

























