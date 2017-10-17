import csv,os

def eliminarCabeceras(csvFilename):
    # Leer el archivo cvs y saltarse la primera línea
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # Saltar primera línea
        csvRows.append(row)
    csvFileObj.close()

    # Escribir la salida al archivo csv
    csvFileObj = open( csvFilename, 'w')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

def acumAnios(texto):
    eliminarCabeceras(texto+".csv")
    archivo=open(texto+".csv")
    lector=csv.reader(archivo)
    datos=list(lector)
    archivoSalida=open("AcumAnnos.csv", "w")
    escritor=csv.writer(archivoSalida)
    contador=0
    c=0
    anio=datos[0][1]
    for linea in datos:
        if anio == datos[c][1]:
            contador=contador+1
        else:
            escritor.writerow([anio, contador])
            contador=1
            anio=datos[c][1]
        c=c+1
    archivo.close()
    archivoSalida.close()

def ordenar(datos):
    contador=0
    lista=[]
    c=0
    for linea in datos:
        n=0;
        insertado=False
        while n<len(lista) :
            
            if linea[0] >lista[n][0] :
                n=n+1
                
            else:
                lista.insert(n,linea)
                insertado=True
                break
        if insertado==False:
            lista.insert(n,linea)
    return lista

    
def ordenado(texto):
    archivo=open(texto + ".csv")
    lector=csv.reader(archivo)
    datos=list(lector)
    archivoSalida=open("Ordenado.csv", "w")
    escritor=csv.writer(archivoSalida)
    contador=0
    lista=ordenar(datos)
    for linea in lista :
        escritor.writerow(linea)
    
    archivo.close()
    archivoSalida.close()

def acumJugadores(texto):
    archivo=open(texto+".csv")
    lector=csv.reader(archivo)
    lista=list(lector)
    datos=ordenar(lista)
    archivoSalida=open("AcumJugadores.csv", "w")
    escritor=csv.writer(archivoSalida)
    contador=0
    c=0
    nombre=datos[0][0]
    
    for linea in datos:
        if nombre == datos[c][0]:
            contador=contador+1
        else:
            escritor.writerow([nombre, contador])
            contador=1
            nombre=datos[c][0]
        c=c+1
    archivo.close()
    archivoSalida.close()
