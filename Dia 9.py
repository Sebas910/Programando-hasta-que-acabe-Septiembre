import random
import string
#Programa que genera una clave utilizando biblioteca random

print("Bienvenido al generador de clave mas genial del planeta")
cantidad = int(input("ingrese la cantidad de claves que desee generar"))

caracteres = list(string.ascii_letters + string.digits )

claves = []
i = 0
for veces in range(0,cantidad):
    
    clave = ""
    for caracter in range(0,13):
        
        caracter = caracteres[random.randint(0,61)]
        clave+=caracter

    claves.append(clave)
    i+=1
    
print("aqui tiene sus claves")

for cl in claves:
    print(cl)