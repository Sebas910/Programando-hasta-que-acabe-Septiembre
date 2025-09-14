#Calculadora de Gastos Semanales

def suma_facturas (lista_facturas):


    total = 0
    
    for montos in lista_facturas:
        total +=montos
    
    return total

def gastos_fijos (lista_fijos):
    
    
    total = 0
    for fijos in lista_fijos:
        
        total+=fijos
    
    return total


# Codigo_Main

print("")
n_facturas = int(input("Ingrese el numero de facturas que tiene: "))

lista_facturas = []
lista_fijos = []


for facturas in range(0,n_facturas):
    
    try: 
     lista_facturas.append(float(input("ingrese el monto de su factura: ")))
    
    except ValueError:
        print("ingrese solamente numeros ")
        lista_facturas.append(float(input("ingrese el monto de su factura: ")))
    
print("Ahora ingrese los gastos fijos que posee por semana (suscripciones)")

n_fijos = int(input("Ingrese el numero de suscripciones que tiene"))

for hijos in range(0,n_fijos):
    
    try:
        lista_fijos.append(float(input("ingrese el monto de su factura: ")))

    except ValueError:
        
        print("Ingrese solamente numeros")
        lista_fijos.append(float(input("ingrese el monto de su factura: ")))

total = suma_facturas(lista_facturas) + gastos_fijos(lista_fijos)

print("el total que usted gasta por semana es el siguente: ",total)