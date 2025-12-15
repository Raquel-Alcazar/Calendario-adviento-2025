numero = 50
contador = 0

fichero = open('dia 1\\archivo1.txt')
lineas = fichero.readlines()
#for linea in lineas:
#    print(linea.strip())

def sacarNumero (linea) :
    numero=""
    for caracter in linea:
        if caracter.isdigit() == True:
            numero += caracter
    return int(numero)

def comprobar (numero):
    global contador
    if numero == 0:
        contador += 1
        return 0


print("El dial comienza en 50")
for linea in lineas:
    if linea[0].strip() == "L":
        #print("hola")
        numerolinea = sacarNumero(linea)
        #print(numerolinea)
        numero -= numerolinea
        if numero < 0 :
            numero = numero % 100
        #print(numero)
        print("Hemos restado ", numerolinea, "El total es ", numero)
        comprobar(numero)
    if linea[0].strip() == "R":
        numerolinea = sacarNumero(linea)
        numero += numerolinea
        if numero > 99 :
            numero = numero%100
        print("Hemos sumado ", numerolinea, "El total es ", numero)
        comprobar(numero)




print("El contador suma ", contador)


        







