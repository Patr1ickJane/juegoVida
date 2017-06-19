import curses
import Modos



def main():
    '''
    Entradas: Ninguna
    Salidas: Ninguna
    Restricciones: la pantalla debe estar en pantalla completa
                   debe escojer unicamente las opciones del menu
                   cuando se pide una cantidad deben ser numeros y enteros
    Funcion: aqui es donde estan todas las interacciones con la terminal
    
    '''
    stdscr = curses.initscr()
    error = True
    while(error == True):
        lonx,lony = stdscr.getmaxyx()
        stdscr.clear()
        stdscr.refresh()
        if int(lonx) < 30 or int(lony) < 87:
            
            stdscr.addstr("ponga pantalla completa\n")
            stdscr.getstr()
        else:
            error = False
    error = True
    
    stdscr.addstr("no tuve tiempo de investigar como predefinir dimensiones\ntenia que salvar FOC lo siento :( xD\nVuelva a darle enter para que ya ahora si entre al juego xD")
    stdscr.getstr()
    stdscr.clear()
    stdscr.refresh()
    juego = curses.newwin(30,87)
    
    while(error == True):#Menu de opciones
        #subwin = stdscr.subwin(stdscr_y-3, stdscr_x, 0, 0)
        juego.addstr("Juego de Conway")
        juego.addstr("\n(1) Modo Aleatorio")
        juego.addstr("\n(2) Modo Oscilador")
        juego.addstr("\n(3) Modo Configurado")
        juego.addstr("\n(4) Salir")
        juego.addstr("\nOpcion escogida: ")
        eleccion = juego.getstr()
        eleccion = eleccion.decode(encoding = "utf-8")
        if eleccion.isdigit() == False or int(eleccion) < 1 or int(eleccion) > 4:
            juego.addstr("digito una opcion incorrecta se devolvera al menu principal\nPresione cualquier tecla")
            juego.getch()
        else:
            error = False
    
    if eleccion == "1":#por si escoje aleatorio
        juego.clear()
        juego.refresh()
        juego.addstr("ha escogido modo aleatorio")
        juego.addstr("\nel modo aleatorio tiene una dimension 24X80 y modalidad 23/3 escoja la cantidad de celulas vivas que se pondran en el universo")
        juego.addstr("\ncantidad(solo se aceptan numeros): ")
        cantidad = juego.getstr()
        cantidad = cantidad.decode(encoding = "utf-8")
        cantidad = int(cantidad)
        matriz,vivir,nacer = Modos.aleatorio(cantidad)
    
    elif eleccion == "2":# oscilador
        matriz,vivir,nacer = Modos.oscilador()
    
    
    elif eleccion == "3":#configurado
        
        juego.clear()
        juego.refresh()
        juego.addstr("a continuacion se le pedira que escoja las condiciones para que una celula siga viva(debe ser digito)\nPresione una tecla para continuar")
        juego.getstr()
        vivir = ""
        salir = False
        while(salir == False):#aqui escoje las condiciones para que una celula siga viviendo
            juego.addstr("numero: ")
            condicion = juego.getstr()
            condicion = condicion.decode(encoding = "utf-8")
            if condicion.isdigit() == False:
                juego.addstr("\nescoja un digito")
                juego.getstr()
            else:
                vivir += condicion
                error = True
                while(error == True):
                    juego.addstr("\nQuiere escojer un numero mas? S/N")
                    condicion = juego.getstr()
                    condicion = condicion.decode(encoding = "utf-8")
                    if condicion == "N" or condicion == "n":
                        salir = True
                        error = False
                    elif condicion == "S" or condicion == "s":
                        error = False
                        
        juego.clear()
        juego.refresh()
        juego.addstr("a continuacion se le pedira que escoja las condiciones para que una celula nazca(debe ser digito)\nPresione una tecla para continuar")
        juego.getstr()
        nacer = ""
        salir = False
        while(salir == False):#aqui escoje las condiciones para que una celula nazca
            juego.addstr("numero: ")
            condicion = juego.getstr()
            condicion = condicion.decode(encoding = "utf-8")
            if condicion.isdigit() == False:
                juego.addstr("\nescoja un digito")
                juego.getstr()
            else:
                nacer += condicion
                error = True
                while(error == True):
                    juego.addstr("\nQuiere escojer un numero mas? S/N")
                    condicion = juego.getstr()
                    condicion = condicion.decode(encoding = "utf-8")
                    if condicion == "N" or condicion == "n":
                        salir = True
                        error = False
                    elif condicion == "S" or condicion == "s":
                        error = False
        
        error = False
        while(error == False):#escoje las filas
            juego.clear()
            juego.refresh()
            juego.addstr("cuantas columnas quiere que tenga el tablero?\ncolumnas:")
            x = juego.getstr()
            x = x.decode(encoding = "utf-8")
            if x.isdigit() == False or int(x) < 5 or int(x) > 24:
                juego.addstr("el numero no es un digito o no esta entre las dimensiones permitidas(5...24)")
            else:
                x = int(x)
                error = True
        
        
        
        error = False
        while(error == False):
            juego.clear()
            juego.refresh()
            juego.addstr("cuantas filas quiere que tenga el tablero?\nfilas:")
            y = juego.getstr()
            y = y.decode(encoding = "utf-8")
            if y.isdigit() == False or int(y) < 5 or int(y) > 80:
                juego.addstr("el numero no es un digito o no esta entre las dimensiones permitidas(5...24)")
            else:
                y = int(y)
                error = True
                
        
        maximo = str(x*y)
        error = True
        while(error == True):
            juego.clear()
            juego.refresh()
            juego.addstr("cuantas celulas quiere que tenga el universo? max("+maximo+")")
            celulas = juego.getstr()
            celulas = celulas.decode(encoding = "utf-8")
            if celulas.isdigit() == False or int(celulas) > int(maximo) or int(celulas) < 0:
                juego.addstr("no digitaste un numero o escojiste un numero mayor a "+maximo)
            else:
                error = False
        
        matriz,vivir,nacer = Modos.configurado(x,y,vivir,nacer,int(celulas))
        
        
        
    else:
        juego.addstr("vuelva pronto")
        curses.endwin()
    
    x = len(matriz)
    y = len(matriz[0])

    juego.clear()
    pausa = -1
    while(True):#muestra el universo
        
        i = 0
        while i < len(matriz):
            j = 0
            while j < len(matriz[0]):
                juego.addstr(matriz[i][j])
            
                j += 1
            juego.addstr("\n")
            i += 1
        juego.addstr("para pausar el juego aprete cualquier tecla(para terminar el juego presiona (s)")
        juego.refresh()
        juego.nodelay(1)
        pausa = juego.getch()
        curses.napms(100)
        matriz = juego_iniciado(matriz,x-2,y-2,vivir,nacer)
        
        if pausa != -1:
            if chr(pausa) != "s" and chr(pausa) != "S": 
                juego.addstr("\nSe ha pausado el juego presiona cualquier tecla para continuar el juego o (s) para salir")
                juego.nodelay(0)
                pausa = juego.getch()
            if chr(pausa) == "s" or chr(pausa) == "S":
                juego.clear()
                juego.refresh()
                juego.addstr("has salido del juego")
                juego.getstr()
                curses.endwin()
                break
            
        juego.clear()


def juego_iniciado(matriz,x,y,vivir,nacer):
    '''
    Entradas: matriz = el universo
              x = cantidad de filas
              y = cantidad de columnas
              vivir = condiciones para que una celula viva
              nacer = condiciones para que una celula nazca
    Salidas la matriz actualizada
    Funcion: llama una funcion donde revisara cual celulas merecen morir o vivir esa funcion devuelve el universo actualizado
    esta funcion solo pinta de nuevo el cuadro y devuelve el universo d
    '''
    matriz = Modos.sucesos(matriz,x,y,vivir,nacer)
    matriz = Modos.dibujarEsquinas(matriz)
    matriz = Modos.lineasRectas(matriz)
    return matriz


main()
