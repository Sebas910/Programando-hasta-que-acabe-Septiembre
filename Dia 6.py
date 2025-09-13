import random

def creador_num(lista):
    
    i = 0
    while (i<100):
    
        lista.append(random.randrange(1,100))
        i+=1
        
    numero_ganador = lista[random.randrange(0,99)]    
    
    print("shhh no le digas a nadie pero este es el numero ganador: ->", numero_ganador)
    
    return numero_ganador

def begin_game(lista):
    
    print("Bienvenido al mejor juego de todos, donde todos ganan o todos pierden")
    print("el juego consiste en lo siguiente, tienes que adivinar un juego del 1 al 100")
    print("si eres inteligente lo adivinas, si no lo eres, lo adivinas, es justo no?")
    
    choise = int(input("ingrese el numero que estima ganador: "))
    
    if choise == creador_num(lista):
        
        print("EXCELENTE, USTED HA GANADO")
        
    else:
        
        print("Excelente, usted a perdido con ganas")
        
#Comienzo Juego

lista = []

begin_game(lista)