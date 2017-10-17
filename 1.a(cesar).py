def busqueda(car, desplazamiento):
    diccionario = {1 :'a',2 :'b',3 :'c',4 :'d',5 :'e',6 :'f',7 :'g',8 :'h',9 :'i',
                   10 :'j',11 :'k',12 :'l',13 :'m',14 :'n',15 :'ñ',16 :'o',17 :'p',18 :'q',
                   19 :'r',20 :'s',21 :'t',22 :'u',23 :'v',24 :'w',25 :'x',26 :'y',27 :'z'}
    numero=0
    i=1
    encontrado = False
    while True:
        if car!=diccionario[i]:
            if i>=27:
                break
            i=i+1
            continue
        numero=i;
        encontrado=True
        break
    numero = numero + desplazamiento
    if numero > 27:
        numero = numero - 27
    if encontrado:
        caracter = diccionario[numero]
    else:
        caracter = car
    return caracter

def cesar(cadena, desplazamiento):
    cadenaNueva = ""
    for car in cadena:
        cadenaNueva = cadenaNueva + busqueda(car, desplazamiento)
    print cadenaNueva


