import sqlite3

sql_tabla_usuario = '''CREATE TABLE User (
        idUser INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre varchar(50) NOT NULL,
        usuario varchar(50) NOT NULL,
        contraseña varchar(50) NOT NULL,
        dinero INTEGER
    );'''

sql_tabla_preg = '''CREATE TABLE PregyResp (
        idPreg INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta varchar(200) NOT NULL,
        respuesta1 varchar(200) NOT NULL,
        respuesta2 varchar(200) NOT NULL,
        respuesta3 varchar(200) NOT NULL,
        respuesta4 varchar(200) NOT NULL,
        correcta varchar(200) NOT NULL,
        categoria INTEGER NOT NULL,
        premio INTEGER NOT NULL
    );'''

if __name__ == '__main__':
    try:
        print('Creando Base de Datos...')
        conexion = sqlite3.connect('..\PyRHeroku\pregyresp.db')

        print('Creando Tablas...')
        conexion.executescript(sql_tabla_usuario)
        conexion.executescript(sql_tabla_preg)

        conexion.close()
        print('Creacion finalizada.')
    except Exception as e:
        print(f'Error creando base de datos:{e}', e)