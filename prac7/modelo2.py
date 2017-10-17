# -*- coding: utf-8 -*-
"""
Autores: Jesús Menéndez, Veronica Morante, Miguel Pomboza
Grupo 09

Este código es fruto ÚNICAMENTE del trabajo de sus miembros. Declaramos no haber
colaborado de ninguna manera con otros grupos, haber compartido el ćodigo con
otros ni haberlo obtenido de una fuente externa.
"""

from bottle import run,request,post
# Resto de importaciones...
from pymongo import MongoClient


# ¡MUY IMPORTANTE!
# Todas las inserciones se deben realizar en la colección 'users' dentro de la
# base de datos 'giw'.


@post('/add_user')
def add_user_post():
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    #cambiar a collection users
    collection = db.user
  
    _id = request.forms.get('_id')
    country = request.forms.get('country')
    zip1 = request.forms.get('zip')
    email = request.forms.get('email')
    gender = request.forms.get('gender')
    gustos = request.forms.get('likes')
    likes = gustos.split(",")
    password = request.forms.get('password')
    year = request.forms.get('year')
    
    result = collection.insert_one({"_id":_id,"address":{"country":country,"zip":zip1},"email":email,"gender":gender,"likes":json_encode(likes),"password":password,"year":year})
    if result.inserted_id == _id:
        return "<p>La insercion ha sido un exito</p>"
    else :
        return "<p>El usuario ya existe</p>"
    mongoClient.close()
    

@post('/change_email')
def change_email():
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
      #cambiar a collection users
    collection = db.user
    
    ID = request.forms.get('_id')
    email = request.forms.get('email')
   
    result = collection.update_one({"_id":ID}, {"$set":{"email":email}})
    if result.modified_count == 1:
        return "<p>Se ha modificado un elemento</p>"
    else :
         return "<p>Se ha modificado 0 elementos</p>"
    mongoClient.close()
    


@post('/insert_or_update')
def insert_or_update():
   
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    #cambiar a collection users
    collection = db.user
  
    _id = request.forms.get('_id')
    country = request.forms.get('country')
    zip1 = request.forms.get('zip')
    email = request.forms.get('email')
    gender = request.forms.get('gender')
    gustos = request.forms.get('likes')
    likes = gustos.split(",")
    password = request.forms.get('password')
    year = request.forms.get('year')
    result = collection.update_one({"_id":_id}, {{"_id":_id},"address":{"country":country,"zip":zip1},"email":email,"gender":gender,"likes":jason_encode(likes)[],"password":password,"year":year}, upsert=True)
    if result.modified_count == 0:
        return "<p>Se ha producido una inserccion</p>"
    else:
        return "<p>Se ha producido una modificacion</p>"
       
    mongoClient.close()


@post('/delete')
def delete_id():
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    #cambiar a collection users
    collection = db.user
    
    ID = request.forms.get('_id')
    result = collection.delete_one({"_id":ID})
    if result.deleted_count == 1:
        return "<p>Se ha borrado un elemento</p>"
    else:
        return "<p>Se ha borrado 0 elementos</p>"
        
    
    mongoClient.close()
    


@post('/delete_year')
def delete_year():
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    collection = db.user
    year = request.forms.get('year')

    collection.delete_many({"year":year})
    return "<p>Se ha borrado "+str(result.deleted_count)+" elementos</p>"
    
    mongoClient.close()



run(host='localhost', port=8080)

