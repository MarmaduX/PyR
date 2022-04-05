from Datos.basededatos import BaseDeDatos

def crear_pregunta(pregunta, respuesta1, respuesta2, respuesta3, respuesta4, correcta, categoria, premio):
    crear_usuario_sql = f"""
        INSERT INTO PregyResp(pregunta, respuesta1, respuesta2, respuesta3, respuesta4, correcta, categoria, premio)
        VALUES ('{pregunta}', '{respuesta1}', '{respuesta2}', '{respuesta3}', '{respuesta4}', '{correcta}', '{categoria}', '{premio}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)

def devolver_pregunta(categoria):
    ingresar_sql = f"""
        SELECT * FROM PregyResp WHERE categoria = '{categoria}'
    """
    bd = BaseDeDatos()
    existe = []
    existe = bd.ejecutar_sql(ingresar_sql)
    return existe

