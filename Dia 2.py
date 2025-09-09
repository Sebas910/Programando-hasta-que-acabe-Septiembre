def factorial(n):
    
    if n == 0 or n == 1:
        return 1
        
    else:
        return n * factorial(n-1)  


def Bucle_Suma(n):
    
    for numero in range(1,10):
         
         print(numero)
         n+=numero

    return n

def String_Printer(texto):
    
    for numero in range(5,10):
        
        print(texto, numero)

opcion = int(input("Ingrese una opcion")) 


match opcion:
    
    case 1:
        print("CALCULADORA FACTORIAL PAPA")
        Entrada = int(input("Ingrese un numero "))

        resultado = factorial(Entrada)
        
        print("el numero que tu necesita es este: ", resultado)

    case 2:
        
        print("CALCULADORA DE SUMAS PROGRESIVAS")
        Entrada = int(input("Ingrese un numero "))

        resultado = Bucle_Suma(Entrada)
        
        print("el numero que tu necesita es este: ", resultado)

        
String_Printer("mmgvazo digo glu glu")

n=0

while(n!= 6):
    
    n+=1 
    
    if n == 1:
    
        print("ELIJA UNA OPCION O SI NO NO SALDREMOS DEL BUCLE TEMPORAL!!!")
        input("presione enter para continuar...")
    
    if n == 2:
        
        print("EL DIABLO PERO A TI TE GUSTAN LOS BUCLES PARECE, ESTAMOS EN EL 2 Ya")
        input("presione enter para continuar...")
        
    if n == 3:
        
        print("YA VAMOS POR EL TRES Y TU SIGUE DANDOLE Y DANDOLE")
        input("presione enter para continuar...")
        
    if n == 4:
        print("PERO TU TA CONSCIENTE QUE ESTO ES INFINITO???")
        input("presione enter para continuar...")
   
    if n == 5:
        
        opcion = int(input("Mete aqui cualquier numero, pero distinto de cero si, pa que salgamo de esta vaina"))
        
        if opcion != 0:
            break
        
    if n == 6:
        
        print("TU DE VELDA ERES TERCO COMO UNA PIEDRA MI LOCO")
        
            
            
        
            