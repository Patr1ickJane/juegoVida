#from curses import wrapper
import curses 

def main():
    
    stdscr = curses.initscr()
    matriz = formarMatriz(25,81)
    matriz = dibujarEsquinas(matriz)
    matriz = lineasVerticales(matriz)
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
    ventana = []
    i = 0
    while(i < x):
        j = 0
        ventana += [[]]
        while(j < y):
            
            ventana[i] += [" "]
            j += 1
        i += 1
    return ventana

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
    

    
    
    
    
main()

















