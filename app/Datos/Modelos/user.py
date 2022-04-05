from ..basededatos import BaseDeDatos


def crear_usuario(nombreCompleto, nombreUsuario, contraseña):
    crear_usuario_sql = f"""
        INSERT INTO User(nombre, usuario, contraseña, dinero)
        VALUES ('{nombreCompleto}', '{nombreUsuario}', '{contraseña}', 0)
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)


def modificar_usuario(nombre, money):
    modificar_usuario_sql = f"""
        UPDATE User SET dinero = '{money}'
        WHERE nombre = '{nombre}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_usuario_sql)


def eliminar_usuario(idUsuario):
    eliminar_usuario_sql = f"""
        DELETE FROM user WHERE idUsuario = '{idUsuario}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_usuario_sql)


def login(nombreUsuario):
    ingresar_sql = f"""
        SELECT * FROM User WHERE nombre = '{nombreUsuario}'
    """
    bd = BaseDeDatos()
    existe = []
    existe = bd.ejecutar_sql(ingresar_sql)
    return existe
