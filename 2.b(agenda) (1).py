def crear(lista):
    print"Nombre: "
    nombre=raw_input()
    print"Primer apellido: "
    apellido1=raw_input()
    print "Segundo Apellido"
    apellido2=raw_input()
    print"Telefono: "
    telefono=raw_input()
    lista.append(nombre)
    lista.append(apellido1)
    lista.append(apellido2 )
    lista.append(telefono )
    
def buscarNombre(lista):
    print" Introduce nombre: "
    nombre=raw_input()
    contador=0
    encontrado=False
    for linea in lista:
        if(linea.find(nombre)==-1):
            contador=contador+1
            continue
        encontrado=True
        break
    if(encontrado==False):
        contador=-1
    return contador
    
def buscarApellido(lista):
    print"Introduce apellido: "
    apellido=raw_input()             
    contador=0
    encontrado=False
    for linea in lista:
         
        if(linea.find(apellido)==-1):
            contador=contador+1
            continue
        encontrado=True
        break
    if(encontrado==False):
        contador=-1
    return contador

def buscarTelefono(lista):
    print"Introduce telefono: "
    telefono=raw_input()
    encontrado=False
    contador=0
    for linea in lista:
        if(linea.find(telefono)==-1) :
            contador=contador+1
            continue
        encontrado=True
        break
    if(encontrado==False):
        contador=-1
    return contador

def borrar(lista):
    indice=buscarTelefono(lista)
    del lista[indice-3:indice+1]
    
def buscar(lista):
    while True:
        print "Elige opcion\n"
        print "1-Buscar nombre\n"
        print "2-Buscar Apellido\n"
        print "3-Buscar telefono\n"
        print "4-Salir\n"
        opcion = raw_input()
        if opcion=='1':
            contador=buscarNombre(lista)
            if contador==-1 :
                print "Nombre no encontrado"
            else:
                n=0
                while n<4 :
                    print lista[contador+n]
                    n=n+1
                break    
        elif opcion=='2':
            contador=buscarApellido(lista)
            if contador==-1 :
                print "Apellido no encontrado"
            else:
                if (contador%2)==0:
                    n=2
                    while n>=0 :
                        print lista[contador-n]
                        n=n-1 
                    print lista[contador+1]
                    break
                else:
                    print lista[contador-1]
                    n=0
                    while n<3 :
                        print lista[contador+n]
                        n=n+1
                    break   
        elif opcion=='3':
            contador=buscarTelefono(lista)
            if contador==-1 :
                print "Telefono no encontrado"
            else:
                n=3
                while n>=0 :
                    print lista[contador-n]
                    n=n-1
                break
        elif opcion=='4':
            break
        else :
            print "Opcion invalida\n"  

def guardarArchivo(lista,nombreArch):
    archivo=open(nombreArch,"w")
    for linea in lista :
        archivo.write(linea+"\n")
    archivo.close()
    
def cargar(lista,nombreArch):
    guardarArchivo(lista,nombreArch)
    print "Nombre del archivo a cargar:"
    nombre=raw_input()
    nombre=nombre+".txt"
    return nombre

def agenda():
    nombreArchivo=open("agenda.txt")
    nombreArch="agenda.txt"
    lista=[]
    for linea in nombreArchivo:      
        linea=linea.rstrip()
        lista.append(linea)
    nombreArchivo.close()
    while True:
        print "Elige opcion:\n"
        print "1-Crear entrada\n"
        print "2-Borrar entrada\n"
        print "3-Buscar entrada por nombre, apellido o telefono\n"
        print "4-Cargar entrada\n"
        print "5-Salir\n"
        opcion = raw_input()
        if opcion=='1':
            crear(lista)
        elif opcion=='2':
            borrar(lista)
        elif opcion=='3':
            buscar(lista)
        elif opcion=='4':
            nombreArch = cargar(lista, nombreArch)
            nombreArchivo=open(nombreArch)
            lista=[]
            for linea in nombreArchivo:      
                linea=linea.rstrip()
                lista.append(linea)
            nombreArchivo.close()
        else :
            guardarArchivo(lista,nombreArch)
            break     
