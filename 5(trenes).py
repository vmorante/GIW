

import urllib
from BeautifulSoup import *
import os, sys
def fotos():
    html = urllib.urlopen('http://trenesytiempos.blogspot.com.es/').read()
    sopa = BeautifulSoup(html)
    etiquetas=sopa('a',{"class":"post-count-link"})
    datos=[]
    for etiqueta in etiquetas:
        n=etiqueta[u'href'].find("2015")
        if n != (-1):
            datos.append(etiqueta[u'href'])
            
    num=0
    del datos[0]
    datos.pop()
    directorioActual=os.getcwd()
    for dato in datos:
        html = urllib.urlopen(dato).read()
        sopa = BeautifulSoup(html)
        os.chdir(directorioActual)
        os.makedirs( "directorio"+str(num), 0777 );
        os.chdir(directorioActual+"\directorio"+str(num))
        num=num+1
        etiquetas=sopa('a',{"imageanchor":"1"})
        j=0
        for etiqueta in etiquetas:
            archivo=open("foto"+str(j)+".jpg", "wb")
            imagen=urllib.urlopen(etiqueta.get('href', None))
            while True:
                info=imagen.read(100000)
                if len(info) < 1 : break
                archivo.write(info)
            archivo.close()
            j=j+1

def buscar():     
    palabras = raw_input('Introduce las palabras a buscar: ')
    palabras = palabras.split()
    html = urllib.urlopen('http://trenesytiempos.blogspot.com.es/').read()
    sopa = BeautifulSoup(html)
    etiquetas=sopa('a',{"class":"post-count-link"})
    links=[]
    encontrado=False
    for etiqueta in etiquetas:
        links.append(etiqueta[u'href'])
    for link in links:
        encontrado=False
        html = urllib.urlopen(link).read()
        sopa = BeautifulSoup(html)
        aux=palabras[:]
        contador=0
        textos=sopa('span')
        for texto in textos:
            contenidos =str(texto.contents)
            for palabra in aux:
                if contenidos.find(" "+ palabra +" ")!= -1 or contenidos.find(" "+ palabra +",")!= -1 or contenidos.find(" "+ palabra +".")!= -1:
                    contador=contador+1
                    ubicacion = aux.index(palabra)
                    del aux[ubicacion]
            if contador==len(palabras) :
                print link
                break
