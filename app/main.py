from flask import Flask, request, render_template, session, url_for, redirect
from Servicios import autenticacion
import random

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/inicio', methods=['GET'])
def inicio():
    if 'user' in session:
        return redirect(url_for('juego'))
    return render_template('index.html')

@app.route("/juego")
def juego():
    if 'user' in session:
        user = autenticacion.login(session["user"][1])
        session['user'] = user[0]
        return render_template("juego.html", user = session["user"], dinero= session["user"][4])
    return redirect(url_for('inicio'))

@app.route("/login", methods=["POST"])
def login():
    user = request.form["user"]
    if autenticacion.login(user) == []:
        autenticacion.crear_usuario(user, user, "123")
        user = autenticacion.login(user)
        session['user'] = user[0]
    else:
        user = autenticacion.login(user)
        session['user'] = user[0]
    return redirect(url_for('juego'))

@app.route('/logout', methods=['GET', 'POST'])
def process_logout():
    session.pop('user', None)
    return redirect(url_for("inicio"))

@app.route('/quiz', methods=["GET", "POST"])
def crear_quiz():
    if request.method == "POST":
        correct = request.form["correct"]
        if request.form["cat"] == "Categoria 1":
            premio = 50
        elif request.form["cat"] == "Categoria 2":
            premio = 150
        elif request.form["cat"] == "Categoria 3":
            premio = 300
        else:
            premio = 500
        autenticacion.crear_pregunta(request.form["quiz"], request.form["resp1"], request.form["resp2"], request.form["resp3"], request.form["resp4"], request.form[correct], request.form["cat"], premio)
    return render_template("creacionpreg.html", user = session["user"])

@app.route('/categoria/<int:cat>')
def categoria(cat):
    if cat == 1:
        preguntas = autenticacion.devolver_pregunta("Categoria 1")
        monto  = 0
    elif cat == 2: 
        preguntas = autenticacion.devolver_pregunta("Categoria 2")
        monto  = 50
    elif cat == 3:
        preguntas = autenticacion.devolver_pregunta("Categoria 3")
        monto  = 150
    elif cat == 4:
        preguntas = autenticacion.devolver_pregunta("Categoria 4")
        monto  = 300
    else:
        preguntas = autenticacion.devolver_pregunta("Categoria 5")
        monto  = 500
    
    return render_template("cat.html", pregunta = preguntas[random.randint(0, 4)], cat=cat+1, monto= monto)

@app.route("/acreditar/<int:plata>", methods=["POST"])
def acreditar(plata):
    plata = plata + session["user"][4]
    autenticacion.modificar_usuario(session["user"][1], plata)
    return "ok"

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
