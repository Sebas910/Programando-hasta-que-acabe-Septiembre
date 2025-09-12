texto = input("Ingrese un texto cualquier mi pana: ")

lista_palabras = texto.split()

diccionario_palabras = {}

for palabras in lista_palabras: #Increible que en python esto sea suficiente para verificar si hay algo dentro de una ED 
    
    if palabras in diccionario_palabras:
        
        diccionario_palabras[palabras] += 1
    else:
        diccionario_palabras[palabras] = 1

print("Palabras Encontradas...")
for clave, valor in diccionario_palabras.items():
    
    print(clave,":", valor)
    
   
    