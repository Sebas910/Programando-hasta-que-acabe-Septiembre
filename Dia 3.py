def Ordenar_Numeros (Lista):
    
    n = len(Lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if Lista[j] > Lista[j + 1]:
                Lista[j], Lista[j + 1] = Lista[j + 1], Lista[j]


Lista_numeros = [100,20,5,1,8,3,1,7,3,5]


i = 0

while(len(Lista_numeros) > i):
    
   
    print(Lista_numeros[i])
    i+=1
    
    
tupla_Words = ("turururututuututrurururu", "tururutu", "turutu")

for word in tupla_Words:
    
    print(word)
    
    

Ordenar_Numeros(Lista_numeros)

print (Lista_numeros) 


Lista_numeros[1] = 900

print(Lista_numeros[1])

print (Lista_numeros)