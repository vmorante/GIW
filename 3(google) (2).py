import urllib
import xml.sax

class manejador(xml.sax.ContentHandler):
    def __init__(self):
        self.Datos=""
        self.tmp1=""
        self.tmp2=""
        self.nombre=""
        self.pais=""
        self.nombreCorto=""
        self.entidad=""
        self.direccion=""
        self.latitud=""
        self.longitud=""
        self.terminado= False

    def startElement(self, etiqueta, atributos):
        self.Datos=etiqueta
        
    
    def endElement(self, etiqueta):
        if self.terminado:
            print "Informacion: "
            print "Nombre: ", self.nombre
            print "Pais: ", self.pais
            print "Nombre corto de pais: ", self.nombreCorto
            print "Entidad de nivel 1: ", self.entidad
            print "Direccion formateada: ", self.direccion
            print "Latitud: ", self.latitud
            print "Longitud: ", self.longitud
        self.Datos=""
        self.terminado=False

    def characters(self, contenido):
        if self.Datos=="long_name":
            self.tmp1=contenido
        elif self.Datos=="short_name":
            self.tmp2=contenido
        elif self.Datos=="type":
            if contenido=="administrative_area_level_1":
                self.entidad=self.tmp2
            elif contenido=="country":
                self.pais=self.tmp1
                self.nombreCorto=self.tmp2
            elif contenido=="locality":
                self.nombre=self.tmp1
        elif self.Datos=="formatted_address":
            self.direccion=contenido
        elif self.Datos=="lat":
            if self.latitud=="":
                self.latitud=contenido
        elif self.Datos=="lng":
            if self.longitud=="":
                self.longitud=contenido
                self.terminado=True



serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Entrar ciudad: ')
    if address == "stop" :
        break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    uh = urllib.urlopen(url)
    data = uh.read()
    parser=xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces,0)
    Handler=manejador()
    parser.setContentHandler(Handler)
    parser.parse(url)
    
   
    




    
