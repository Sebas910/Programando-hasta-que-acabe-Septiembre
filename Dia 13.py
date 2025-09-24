#Conversor de Unidades

def Mts_A_Cm(medida):
    
    resultado = medida * 100
    
    return resultado

def cel_A_kelvin(temp):
    
    resultado = temp + 273.15
    return resultado
    
    
print()
print("bienvenido al mejor converso de Unidades del mundo")

i = int(input("Ingrese que unidad quiere convertir (1 = Mts a Cm ; 2 = Celcius a Kelvin): "))


match i:
    
    case 1:
        
        unidad = float(input(("Ingrese la cantidad que quiere convertir: ")))
        print("El resultado es: ", Mts_A_Cm(unidad))
        
    case 2:
        
        unidad = float(input(("Ingrese la cantidad que quiere convertir: ")))
        print("El resultado es: ", cel_A_kelvin(unidad))
        

    
    