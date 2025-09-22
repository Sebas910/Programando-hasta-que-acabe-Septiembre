#conversor de dolar a peso

import requests

def obtencion_tasa_clp():
    
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()
        return data['rates']['CLP']
    except Exception as e:
        print(f"Error al obtener la tasa: {e}")
        return None
    
def obtener_tasa(pesos_chilenos):
    
    tasa = obtencion_tasa_clp()
    
    if tasa:
        
        dolares = pesos_chilenos / tasa
        return dolares
    
    return None
 
def convertir_usd_a_clp(dolares):
    
    """Convierte dólares a pesos chilenos"""
    tasa = obtencion_tasa_clp()
    if tasa:
        pesos = dolares * tasa
        return pesos
    return None

print()
print("Bienvenido al mejor lugar para saber la tasa del dolar")

dolar = int(input("ingrese la cantidad de pesos que quiere ver en dolares"))

print("equivalen a: ", obtener_tasa(dolar),"$")

