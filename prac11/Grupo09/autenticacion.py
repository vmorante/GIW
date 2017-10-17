# -*- coding: utf-8 -*-
"""
Autores: Verónica Morante, Jesús Menéndez, Miguel Pomboza
Grupo 09

Este código es fruto ÚNICAMENTE del trabajo de sus miembros. Declaramos no 
haber colaborado de ninguna manera con otros grupos, haber compartido el ćodigo 
con otros ni haberlo obtenido de una fuente externa.
"""

from bottle import run, request, post
# Resto de importaciones
from pymongo import MongoClient
import hashlib, binascii
import os
import random
import string

##############
# APARTADO A #
##############


@post('/signup')
def signup():
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    
    collection = db.users
  
    _id = request.forms.get('nickname')
    name = request.forms.get('name')
    country = request.forms.get('country')
    email = request.forms.get('email')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')
    
    if password == password2 :
        salt = os.urandom(16)
        salt = binascii.hexlify(salt)
        dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
        passCod = binascii.hexlify(dk)
        try:
            collection.insert_one({"_id":_id,"name":name,"country":country,"email":email,"password":passCod,"salt":salt})
            return "<p>Bienvenido usuario " + name + ".</p>"
        except:
             return "<p>El alias de usuario ya existe.</p>"
    else :
        return "<p>Las contraseñas no coinciden.</p>"
        
    mongoClient.close()
    
    

@post('/change_password')
def change_password():
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    
    collection = db.users
  
    _id = request.forms.get('nickname')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')
    
    cursor = collection.find_one({"_id":_id})

    if cursor <> None:
        salt = cursor["salt"]
        dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
        passCod = binascii.hexlify(dk)
        if cursor["password"] == passCod :
            salt = os.urandom(16)
            salt = binascii.hexlify(salt)
            dk = hashlib.pbkdf2_hmac('sha256', password2, salt, 100000)
            passCod = binascii.hexlify(dk)
            cursor = collection.update_one({"_id":_id}, {"$set":{"password":passCod, "salt":salt}})
            return "<p>La contraseña de " + _id + " ha sido modificada.</p>"
        else:
            return "<p>Usuario o contraseña incorrectos.</p>"
    else:
        return "<p>Usuario o contraseña incorrectos.</p>"
    
    mongoClient.close()
            

@post('/login')
def login():
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    
    collection = db.users
  
    _id = request.forms.get('nickname')
    password = request.forms.get('password')
    
    cursor = collection.find_one({"_id":_id})

    if cursor <> None:
        salt = cursor["salt"]
        dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
        passCod = binascii.hexlify(dk)
        if cursor["password"] == passCod :
            return "<p>Bienvenido " + cursor["name"] + ".</p>"
        else:
            return "<p>Usuario o contraseña incorrectos.</p>"
    else:
        return "<p>Usuario o contraseña incorrectos.</p>"
        
    mongoClient.close()
    


##############
# APARTADO B #
##############


def gen_secret():
    # Genera una cadena aleatoria de 16 caracteres a escoger entre las 26 
    # letras mayúsculas del inglés y los dígitos 2, 3, 4, 5, 6 y 7. 
    #
    # Ejemplo:
    # >>> gen_secret()
    # '7ZVVBSKR22ATNU26'
    chars = string.ascii_uppercase + "234567"
    return ''.join(random.SystemRandom().choice(chars) for _ in range(16))
    
    
    
def gen_gauth_url(app_name, username, secret):
    # Genera la URL para insertar una cuenta en Google Authenticator
    #
    # Ejemplo:
    # >>> gen_gauth_url( 'GIW_grupoX', 'pepe_lopez', 'JBSWY3DPEHPK3PXP')
    # 'otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX
    #    
    # Formato de la URL:
    # otpauth://totp/<ETIQUETA>?secret=<SECRETO>&issuer=<NOMBRE_APLICACION_WEB>
    #
    # Más información en: 
    #   https://github.com/google/google-authenticator/wiki/Key-Uri-Format
    return "otpauth://totp/" + username + "?secret=" + secret + "&issuer=" + app_name
        

def gen_qrcode_url(gauth_url):
    # Genera la URL para generar el código QR que representa 'gauth_url'
    # Información de la API: http://goqr.me/api/doc/create-qr-code/
    #
    # Ejemplo:
    # >>> gen_qrcode_url('otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX')
    # 'http://api.qrserver.com/v1/create-qr-code/?data=otpauth%3A%2F%2Ftotp%2Fpepe_lopez%3Fsecret%3DJBSWY3DPEHPK3PXP%26issuer%3DGIW_grupoX'
    return "http://api.qrserver.com/v1/create-qr-code/?data=" + gauth_url
    


@post('/signup_totp')
def signup_totp():
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    
    collection = db.users
  
    _id = request.forms.get('nickname')
    name = request.forms.get('name')
    country = request.forms.get('country')
    email = request.forms.get('email')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')
        
    if password == password2 :
        salt = os.urandom(16)
        salt = binascii.hexlify(salt)
        dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
        passCod = binascii.hexlify(dk)
        try:
            seed = gen_secret()
            url = gen_gauth_url("GIW_09", _id, seed)
            qrcode = gen_qrcode_url(url)
            collection.insert_one({"_id":_id,"name":name,"country":country,"email":email,"password":passCod,"salt":salt, "seed": seed})
            return "<a href=" + qrcode + ">Continuar</a>"
        except:
             return "<p>El alias de usuario ya existe.</p>"
    else :
        return "<p>Las contraseñas no coinciden.</p>"
        
    mongoClient.close()
        
@post('/login_totp')        
def login_totp():
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.giw
    
    collection = db.users
  
    _id = request.forms.get('nickname')
    password = request.forms.get('password')
    topt = request.forms.get('topt')
    
    
    cursor = collection.find_one({"_id":_id})

    if cursor <> None:
        salt = cursor["salt"]
        dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
        passCod = binascii.hexlify(dk)
        seed = cursor["seed"]
        get_topt(seed, as_string=True)
        if cursor["password"] == passCod :
            return "<p>Bienvenido " + cursor["name"] + ".</p>"
        else:
            return "<p>Usuario o contraseña incorrectos.</p>"
    else:
        return "<p>Usuario o contraseña incorrectos.</p>"
        
    mongoClient.close()
    

    
if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)
