from bottle import Bottle,route,run,request,template,default_app, template, run, static_file, error
import sqlite3
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')
@route('/')
def inicio():
    return template("temp1.tpl",name="",max=0,min=0)

@route('/login') 
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="usuario" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>'''

def passwd(usuario):
    conn = sqlite3.connect('videoclub.sqlite3')
    db = conn.cursor()
    db.execute('SELECT alias FROM usuarios')
    existe=False
    for dato in db.fetchall():
        if str(dato[0])==usuario:
            existe=True
            break
    if existe:
        db.execute('SELECT password FROM usuarios WHERE alias=?',[usuario])
        passwd=db.fetchone()
        passwd=str(passwd[0])
    else:
        passwd=""
    return passwd

@route('/login',method='POST') 
def do_login():
    username = request.forms.get('usuario')
    password = request.forms.get('password')
    pas = ""
    pas = passwd(username)
    if password==pas and pas>0:
        #return "<p>Login correcto</p>"
        
        return template("temp.tpl",name=username,max=3,min=2)
    else:
        return "<p>Login incorrecto.</p>"

@route('/registre') 
def registre():
    return '''
        <form action="/registre" method="post">
            Alias: <input name="alias" type="text" />
            Nombre: <input name="nombre" type="text" />
            Apellido: <input name="apellido" type="text" />
            Password: <input name="password" type="password" />
            <input value="Registrar" type="submit" />
        </form>'''

@route('/registre',method='POST') 
def do_registre():
    conn = sqlite3.connect('videoclub.sqlite3')
    db = conn.cursor()
    alias = request.forms.get('alias')
    nombre = request.forms.get('nombre')
    apellido = request.forms.get('apellido')
    password = request.forms.get('password')
    db.execute('SELECT alias FROM usuarios')
    existe=False
    for dato in db.fetchall():
        if str(dato[0])==alias:
            existe=True
    if password>0 and alias>0 and apellido>0 and nombre>0 and not(existe):
        db.execute('INSERT INTO usuarios (alias,nombre,apellido,password) VALUES (?,?,?,?)', (alias,nombre,apellido,password))
        conn.commit()
       # return "<p>Registro correcto.</p>"
        return template("temp.tpl",name="",max=3,min=2)
    else:
        return "<p>Registro incorrecto.</p>"

@route('/borrarUsuario') 
def borrarUsuario():
    return '''
        <form action="/borrarUsuario" method="post">
            Nombre: <input name="alias" type="text" />
            <input value="Eliminar" type="submit" />
        </form>'''

@route('/borrarUsuario',method='POST') 
def do_borrarUsuario():
    conn = sqlite3.connect('videoclub.sqlite3')
    db = conn.cursor()
    nombre = request.forms.get('alias')
    existe=False
    db.execute('SELECT alias FROM usuarios')
    for dato in db.fetchall():
        if str(dato[0])==nombre:
            existe=True
    if nombre>0 and existe:
        db.execute('DELETE FROM usuarios WHERE alias=?', [nombre])
        conn.commit()
        return "<p>Eliminado con exito.</p>"
    else:
        return "<p>Fallo al eliminar.</p>"


@route('/modificarUsuario') 
def modificarUsuario():
    return '''
        <form action="/modificarUsuario" method="post">
            Alias: <input name="alias" type="text" />
            Password: <input name="password" type="password" />
            NuevoAlias: <input name="nuevoAlias" type="text" />
            NuevoNombre: <input name="nuevoNombre" type="text" />
            NuevoApellido: <input name="nuevoApellido" type="text" />
            NuevaPassword: <input name="nuevaPassword" type="passwordt" />
            <input value="Modificar" type="submit" />
        </form>'''

@route('/modificarUsuario',method='POST') 
def do_modificarUsuario():
    conn = sqlite3.connect('videoclub.sqlite3')
    db = conn.cursor()
    alias = request.forms.get('alias')
    password = request.forms.get('password')
    nuevoAlias = request.forms.get('nuevoAlias')
    nuevoNombre = request.forms.get('nuevoNombre')
    nuevoApellido = request.forms.get('nuevoApellido')
    nuevaPassword = request.forms.get('nuevaPassword')
    db.execute('SELECT alias FROM usuarios')
    existe=False
    for dato in db.fetchall():
        if str(dato[0])==alias:
            existe=True
        elif str(dato[0])==nuevoAlias:
            existe=False
            break
    if existe:
        pas = ""
        pas = passwd(alias)
        print pas
        print password
        if nuevaPassword>0 and nuevoAlias>0 and nuevoApellido>0 and nuevoNombre>0 and pas==password:
            db.execute('UPDATE usuarios set alias=?, nombre=?, apellido=?, password=? WHERE alias=?', [nuevoAlias,nuevoNombre,nuevoApellido,nuevaPassword, alias])
            conn.commit()
            return "<p>Registro correcto.</p>"
        else:
            return "<p>Registro incorrecto.</p>"
    else:
        return "<p>Registro incorrecto.</p>"

@route('/incluir') 
def incluir():
    return '''
        <form action="/incluir" method="post">
            Nombre: <input name="nombre" type="text" />
            Genero: <input name="genero" type="text" />
            <input value="Incluir" type="submit" />
        </form>'''

@route('/incluir',method='POST') 
def do_incluir():
    conn = sqlite3.connect('videoclub.sqlite3')
    db = conn.cursor()
    nombre = request.forms.get('nombre')
    genero = request.forms.get('genero')
    cantidad = 1
    existe=False
    db.execute('SELECT item FROM peliculas')
    for dato in db.fetchall():
        if str(dato[0])==nombre:
            existe=True
    if nombre>0 and genero>0 and not(existe):
        db.execute('INSERT INTO peliculas (item,cantidad,genero) VALUES (?,?,?)', (nombre,cantidad,genero))
        conn.commit()
        return "<p>Insercion correcta.</p>"
    else:
        return "<p>Insercion incorrecta.</p>"

@route('/borrarPeli') 
def borrarPeli():
    return '''
        <form action="/borrarPeli" method="post">
            Nombre: <input name="nombre" type="text" />
            <input value="Eliminar" type="submit" />
        </form>'''

@route('/borrarPeli',method='POST') 
def do_borrarPeli():
    conn = sqlite3.connect('videoclub.sqlite3')
    db = conn.cursor()
    nombre = request.forms.get('nombre')
    existe=False
    db.execute('SELECT item FROM peliculas')
    for dato in db.fetchall():
        if str(dato[0])==nombre:
            existe=True
    if nombre>0 and existe:
        db.execute('DELETE FROM peliculas WHERE item=?', [nombre])
        conn.commit()
        return "<p>Eliminado con exito.</p>"
    else:
        return "<p>Fallo al eliminar.</p>"

@route('/modificarPeli') 
def incluir():
    return '''
        <form action="/modificarPeli" method="post">
            Nombre: <input name="nombre" type="text" />
            NuevaCantidad: <input name="cantidad" type="text" />
            <input value="Modificar" type="submit" />
        </form>'''

@route('/modificarPeli',method='POST') 
def do_modificarPeli():
    conn = sqlite3.connect('videoclub.sqlite3')
    db = conn.cursor()
    nombre = request.forms.get('nombre')
    cantidad = request.forms.get('cantidad')
    cantidad=int(cantidad)
    existe=False
    db.execute('SELECT item FROM peliculas')
    for dato in db.fetchall():
        if str(dato[0])==nombre:
            existe=True
            break
    if nombre>0 and cantidad>=0 and existe:
        db.execute('UPDATE peliculas set cantidad=? WHERE item=?', [cantidad, nombre])
        conn.commit()
        return "<p>Insercion correcta.</p>"
    else:
        return "<p>Insercion incorrecta.</p>"



run(host='localhost', port=8080)
