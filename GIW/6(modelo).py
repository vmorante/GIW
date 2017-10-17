import sqlite3

def init():
    conn = sqlite3.connect('videoclub.sqlite3')
    db = conn.cursor()
    db.execute("DROP TABLE IF EXISTS peliculas")
    db.execute("DROP TABLE IF EXISTS usuarios")
    
    db.execute("CREATE TABLE peliculas (item CHAR(100) PRIMARY KEY , cantidad INTEGER NOT NULL, genero CHAR(100))")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('El corredor del laberinto', 4, 'Accion')")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('The martian', 2, 'Ciencia-ficcion')")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('Los becarios', 4, 'Comedia')")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('La mujer de negro', 1, 'Terror')")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('Los padres de ella', 4, 'Comedia')")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('Los padres de el', 4, 'Comedia')")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('Soy leyenda', 2, 'Accion')")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('El exorcista', 4, 'Terror')")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('Los juegos del hambre', 1, 'Ciencia-ficcion')")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('StarWars', 4, 'Ciencia-ficcion')")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('El rey leon', 4, 'Animacion')")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('Aladdin', 2, 'Animacion')")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('Origen', 4, 'Ciencia-ficcion')")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('Fast and furious', 1, 'Accion')")
    db.execute("INSERT INTO peliculas (item,cantidad,genero) VALUES ('La jungla de cristal', 4, 'Accion')")
    conn.commit()

    db.execute("CREATE TABLE usuarios (alias CHAR(100) PRIMARY KEY, nombre CHAR(100) NOT NULL, apellido CHAR(100) NOT NULL, password CHAR(100))")
    db.execute("INSERT INTO usuarios (alias,nombre,apellido,password) VALUES ('JChus7', 'Jesus', 'Menendez', 'zas')")
    db.execute("INSERT INTO usuarios (alias,nombre,apellido,password) VALUES ('vero1', 'Veronica', 'Morante', '1234')")
    db.execute("INSERT INTO usuarios (alias,nombre,apellido,password) VALUES ('miguel94', 'Miguel', 'Pomboza', 'pio')")
    db.execute("INSERT INTO usuarios (alias,nombre,apellido,password) VALUES ('paco123', 'Francisco', 'Fernandez', 'das')")
    conn.commit()
 

