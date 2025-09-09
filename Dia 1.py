import ctypes

String = input("Ingrese un texto")
opcion = int(input("Ingrese que desea hacer con el texto: "))

match opcion:
   
   case 1: 
    print("Seleccion 1 ")
    
    input1 = input("ingrese que quiere cambiar")
    input2 = input("ingrese ahora lo que quiere colocar")
    
    String = String.replace(input1, input2)
    
    print("Texto cambiado:")
    print(String)    
   case 2:
        print("seleccion 2")
        
        print("Ahora le vamo a bajar al asunto") 
        String = String.lower()        
        print(String)
        
        
   case 4:
        print("Seleccion sorpresa wuajajaj")
        
        numero = 4
        if numero == 4:
            print("Tu computador va explotar en:")
            ctypes.windll.user32.MessageBoxW(0, "TU COMPUTADOR HA SIDO INFECTADO, CON BELLEZA BB", "Alerta", 0x10)
            
            