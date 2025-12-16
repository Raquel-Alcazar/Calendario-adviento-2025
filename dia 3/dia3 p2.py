
####PARTE 2####

fichero = open('dia 3\\archivo3.txt')
lineas = fichero.readlines()

contador = 0
numero_digitos = 12

for i in lineas:
    bateria = i.strip()
    cadena = bateria
    numero_eliminar = len(bateria) - numero_digitos
    
    resultado = []  
    pos_actual = 0  
    eliminar_restantes = numero_eliminar  
    
    print("Línea: ", bateria)
    print("Eliminar total: ", numero_eliminar)
    
    while len(resultado) < 12:
        ventana = eliminar_restantes + 1
        comprobar = bateria [:ventana]
        maximo = max(comprobar)
        resultado.append(maximo)
        print("este es el resultado", resultado)
        if bateria.index(maximo) > 0:
            aux = bateria.index(maximo) 
            eliminar_restantes = eliminar_restantes - (bateria.index(maximo))
            bateria = bateria[bateria.index(maximo)+1:]
        else:
            bateria = bateria[1:]
        
        
        if eliminar_restantes == 0:
            for num in bateria:
                resultado.append(num)
        
    print(resultado)
    contador = contador + int(''.join(map(str,resultado)))
        
print("la suma total es: ", contador)







        

