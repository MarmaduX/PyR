from ..Datos.Modelos import user as modelo_usuario, preguntas as modelo_preguntas

def crear_usuario(nombre, usuario, clave):
    modelo_usuario.crear_usuario(nombre, usuario, clave)

def modificar_usuario(nombre, money):
    modelo_usuario.modificar_usuario(nombre, money)

def login(idusuario):
    return modelo_usuario.login(idusuario)

def crear_pregunta(pregunta, respuesta1, respuesta2, respuesta3, respuesta4, correcta, categoria, premio):
    modelo_preguntas.crear_pregunta(pregunta, respuesta1, respuesta2, respuesta3, respuesta4, correcta, categoria, premio)

def devolver_pregunta(categoria):
    return modelo_preguntas.devolver_pregunta(categoria)
