# -*- coding: utf-8 -*-
"""
Autores: Jesús Menéndez, Verónica Morante, Miguel Pomboza
Grupo 09

Este código es fruto ÚNICAMENTE del trabajo de sus miembros. Declaramos no haber
colaborado de ninguna manera con otros grupos, haber compartido el ćodigo con
otros ni haberlo obtenido de una fuente externa.
"""


from bottle import get, run, request,template
# Resto de importaciones
from pymongo import MongoClient
import json


@get('/find_user_id')
def find_user_id():
    # http://localhost:8080/find_user_id?_id=user_1
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    collection = db.users
    
    ID = request.forms.get('_id')
	
    cursor = collection.find_one({"_id":ID})
 
    mongoClient.close()

    if cursor <> None:
        return template("mostrar_usu.tpl",c=cursor)
    else
        return "<p>No existe en la base de datos</p>"
    


@get('/find_users')
def find_users():
    # http://localhost:8080/find_users?gender=Male
    # http://localhost:8080/find_users?gender=Male&year=2009
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    collection = db.users
    
    _id = request.forms.get('_id')
    email = request.forms.get('email')
    gender = request.forms.get('gender')
    year = request.forms.get('year')
    
    dic = dict()
    if _id <> "":
        dic["_id"] = _id
    if email <> "":
        dic["email"] = email
    if gender <> "":
        dic["gender"] = gender
    if year <> "":
        dic["year"] = int(year)
        
    atributos = json.dumps(dic)
    
    cursor = collection.find(atributos)
	
    mongoClient.close()

    if cursor <> None:
        return template("mostrar.tpl",c=cursor,n=cursor.count())
    else
        return "<p>No existe en la base de datos</p>"


@get('/find_users_or')
def find_users_or():
    # http://localhost:8080/find_users_or?gender=Male&year=2000
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    collection = db.users
    
    _id = request.forms.get('_id')
    email = request.forms.get('email')
    gender = request.forms.get('gender')
    year = request.forms.get('year')
    
    atributos = []
    
    if _id <> "":
        atributo = {"_id":_id}
        atributo = json.dumps(atributo)
        atributos.append(atributo)
    if email <> "":
        atributo = {"email":email}
        atributo = json.dumps(atributo)
        atributos.append(atributo)
    if gender <> "":
       atributo = {"gender":gender}
       atributo = json.dumps(atributo)
       atributos.append(atributo)
    if year <> "":
        atributo = {"year":year}
        atributo = json.dumps(atributo)
        atributos.append(atributo)
        
    
    cursor = collection.find({$or: atributos[]})
	
    mongoClient.close()

    if cursor <> None:
        return template("mostrar.tpl",c=cursor,n=cursor.count())
    else
        return "<p>No existe en la base de datos</p>"

       
@get('/find_like')
def find_like():
    # http://localhost:8080/find_like?like=football
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    collection = db.users
    
    like = request.forms.get('like')
    
    cursor = collection.find({"likes":like})
    
    mongoClient.close()

    if cursor <> None:
        return template("mostrar.tpl",c=cursor,n=cursor.count())
    else
        return "<p>No existe en la base de datos</p>"    


@get('/find_country')
def find_country():
    # http://localhost:8080/find_country?country=Spain
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    collection = db.users
    
    country = request.GET.get('country')
    
    cursor = collection.find({"address.country":country})
    if :
        return template("mostrar.tpl",c=cursor,n=cursor.count())
    else :
        return "<p>No existe en la base de datos</p>"   
	
    mongoClient.close()
    


@get('/find_email_year')
def email_year():
    # http://localhost:8080/find_email_year?year=1992
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    collection = db.users
    
    year = request.forms.get('year')
    
    cursor = collection.find({"year":year}, {"_id":1, "address":0, "email":1, "gender":0, "likes":0, "password":0, "year":0})
	
    mongoClient.close()

    if cursor <> None:
        return template("mostrar_año.tpl",c=cursor,n=cursor.count())
    else:
        return "<p>No existe en la base de datos</p>"   


@get('/find_country_limit_sorted')
def find_country_limit_sorted():
   # http://localhost:8080/find_country_limit_sorted?country=Spain&limit=20&ord=asc
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    collection = db.users
    
    country = request.GET.get('country')
    limit = request.GET.get('limit')
    ord1 = request.GET.get('ord')
    error = False    
    
    if ord1 == 'asc':
        ordN = 1
    elif ord1 == 'desc':
        ordN = -1
    elif limit < 0:
        error=False
    else:
        error=True
        
    if (not error):
        cursor= collection.find({"address.country":country}).sort([("year",ordN)]).limit(int(limit))
        if cursor <> None:
            return template("mostrar.tpl",c=cursor,n=cursor.count())
        else :
            return "<p>No existe en la base de datos</p>"   
         
    else:
        return "<p>Ha introducido datos erroneos</p>"
    mongoClient.close()
    


###############################################################################
################# Funciones auxiliares a partir de este punto #################
###############################################################################




###############################################################################
###############################################################################

if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)
