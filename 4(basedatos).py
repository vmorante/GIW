import sqlite3
conn = sqlite3.connect('Universidad.sqlite3')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS universidades")
cur.execute("DROP TABLE IF EXISTS estudiantes")
cur.execute("DROP TABLE IF EXISTS solicitudes")
cur.execute("CREATE TABLE universidades(Nombre_Univ TEXT,Comunidad TEXT,Plazas INTEGER)")
cur.execute("CREATE TABLE estudiantes(ID INTEGER, Nombre_EST TEXT, Nota DOUBLE, Valor DOUBLE)")
cur.execute("CREATE TABLE solicitudes(ID INTEGER,Nombre_Univ TEXT,Carrera TEXT, Decision TEXT)")
cur.executemany('INSERT INTO universidades (Nombre_Univ, Comunidad, Plazas) VALUES (?, ?, ?)',
[('Universidad Complutense de Madrid', 'Madrid', 15000),
 ('Universidad de Barcelona', 'Barcelona',36000),('Universidad de Valencia','Valencia',10000),
 ('UPM','Madrid',21000)])
cur.executemany('INSERT INTO estudiantes(ID,Nombre_Est,Nota,Valor) VALUES (?,?,?,?)',
[(123,'Antonio',8.9,1000),(234,'Juan',8.6,1500),(345,'Isabel',8.5, 500),(456,'Doris',7.9,1000),
 (543,'Pedro',5.4,2000),(567,'Eduardo',6.9,2000),(654,'Alfonso',7.9,1000),(678,'Carmen',5.8,200),
 (765,'Javier',7.9,1500),(789,'Isidro',8.4,800),(876,'Irene',6.9,400),(987,'Elena',6.7,800)])
cur.executemany('INSERT INTO solicitudes(ID,Nombre_Univ,Carrera,Decision) VALUES (?,?,?,?)',
[(123,'Universidad Complutense de Madrid', 'Informatica', 'Si'),(123,'Universidad Complutense de Madrid','Economia','No'),
 (123,'Universidad de Barcelona','Informatica','Si'),(123, 'UPM','Economia','Si'),(234,'Universidad de Barcelona','Biologia','No'),
 (345, 'Universidad de Valencia','Bioingenieria','Si'),(345,'UPM','Bioingenieria','No'),(345, 'UPM','Informatica','Si'),(345,'UPM','Economia','No'),
 (678, 'Universidad Complutense de Madrid','Historia','Si'),(987,'Universidad Complutense de Madrid','Informatica','Si'),
 (987, 'Universidad de Barcelona','Informatica','Si'),(876,'Universidad Complutense de Madrid','Informatica','No'),
 (876, 'Universidad de Valencia','Biologia','Si'),(876,'Universidad de Valencia','Biologia Marina','No'),
 (765, 'Universidad Complutense de Madrid','Historia','Si'),(765,'UPM','Historia','No'),(765, 'UPM','Psicologia','Si'),
 (543,'Universidad de Valencia','Informatica','No')])
conn.commit()
cur.execute('SELECT Nombre_Est, Nota, Decision FROM estudiantes, solicitudes WHERE Nombre_Univ = "Universidad Complutense de Madrid" AND Carrera = "Informatica" AND estudiantes.ID = solicitudes.ID AND valor < 1000')
#for fila in cur.fetchall():
#    print fila
cur.execute('SELECT Nombre_Est FROM estudiantes WHERE abs((Nota*(Valor/1000))-Nota)>=1')
#for fila in cur.fetchall():
 #   print fila
cur.execute('SELECT Nombre_Est FROM estudiantes, solicitudes WHERE estudiantes.ID=solicitudes.ID')

#cur.execute('INSERT INTO solicitudes(ID,Nombre_Univ,Carrera,Decision) VALUES (?,?,?,?)',


cur.execute('SELECT ID FROM solicitudes')
idsolicitados=[]
for fila in cur.fetchall():
    numero=fila[0]
    repetido=False
    for codigo in idsolicitados:
        if numero==codigo:
            repetido=True
    if repetido==False:
        idsolicitados.append(numero)
cur.execute('SELECT ID FROM estudiantes')
ids=[]
for fila in cur.fetchall():
    numero=fila[0]
    ids.append(numero)
idsnosolicitados=[]
for numero in ids:
    repetido=False
    for codigo in idsolicitados:
        if numero==codigo:
            repetido=True
    if repetido==False:
        idsnosolicitados.append(numero)
univJaen=[]
for numero in idsnosolicitados:
    univJaen.append((numero,'Universidad de Jaen','Informatica','No'))
for dato in univJaen:
    cur.execute('INSERT INTO solicitudes (ID,Nombre_Univ,Carrera,Decision) VALUES (?,?,?,?)',dato)
conn.commit()


cur.execute('SELECT ID FROM solicitudes WHERE Carrera="Economia" AND Decision="No"')
idsNo=[]
for fila in cur.fetchall():
    numero=fila[0]
    repetido=False
    for codigo in idsNo:
        if numero==codigo:
            repetido=True
    if repetido==False:
        idsNo.append(numero)
cur.execute('SELECT ID FROM solicitudes WHERE Carrera="Economia" AND Decision="Si"')
for fila in cur.fetchall():
    numero=fila[0]
    repetido=False
    for codigo in idsNo:
        if numero==codigo:
            idsNo.remove(codigo)
univJaen=[]
for numero in idsNo:
    univJaen.append((numero,'Universidad de Jaen','Economia','Si'))
for dato in univJaen:
    cur.execute('INSERT INTO solicitudes (ID,Nombre_Univ,Carrera,Decision) VALUES (?,?,?,?)',dato)
conn.commit()




cur.execute('SELECT ID, Carrera FROM solicitudes')
ids=[]
for fila in cur.fetchall():
    repetido=False
    for codigo in ids:
        if fila==codigo:
            repetido=True
    if repetido==False:
        ids.append(fila)
ids.sort()
dato0=ids[0][0]
contador=0
idsBorrar=[]
for dato in ids:
    if dato[0]==dato0:
        contador=contador+1
    else:
        if contador>2:
            idsBorrar.append(dato0)
        contador=1
        dato0=dato[0]
for dato in idsBorrar:
    cur.execute('DELETE from solicitudes WHERE ID=?', [dato])
conn.commit()
cur.execute('SELECT * FROM solicitudes')
for linea in cur.fetchall():
    print linea
cur.close()







