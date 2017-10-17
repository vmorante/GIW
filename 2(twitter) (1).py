import json

def frecuencia(archivo):
    texto=open(archivo+".txt")
    datos = []
    for line in texto:
        datos.append(json.loads(line))
    for dato in datos:
       if dato.has_key(u'text'):
         print dato[u'text'][0]
         
def hashtags(archivo):
    texto=open(archivo+".txt")
    datos = []
    for line in texto:
        datos.append(json.loads(line))
    for dato in datos:
       if dato.has_key(u'entities'):
           if dato[u'entities'].has_key(u'hashtags'):
               if dato[u'entities'][u'hashtags'] 
                data = dato[u'entities']
                print data[u'hashtags'][u'indices']
