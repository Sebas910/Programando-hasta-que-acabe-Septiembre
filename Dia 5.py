import random
import subprocess

def generador_numeros(lista , numero):
    
    i = 0
    while(i<numero):
        
        lista.append(random.randrange(0,100))
        i+=1
        
    
def Detector_primos(lista):
    
    contador = 0
    
    for numero in lista:
        
        if(numero%2 == 1):
             
            contador+=1    
        
        
        
    return contador
        
    

subprocess.run("clear") 

print("\n Aqui somo unos cracks, podemos adivinar si una lista tiene primos o no")

listarda = []


generador_numeros(listarda, 10000)

print(listarda)
print("primos encontrados -->",Detector_primos(listarda))

