from flask import Flask, render_template, url_for #Importamos las librerias a ser usadas
import requests

app = Flask(__name__)  #Creabamos el objetoi app


@app.route("/")     #Llamabamos al metodo route y le pasamos el argumento slug o url
def inicio(): #Creamos la funcion inicio
    return render_template('inicio.html')
                #Retornamos la renderizacion de un documento

@app.route("/trabajana")
def trabajana():
    return render_template('trabajana.html')

@app.route("/contratana")
def contratana():
    return render_template('contratana.html')

@app.route("/aprendena")
def aprendena():
    return render_template('aprendena.html')

@app.route("/ensenana")
def ensenana():
    return render_template('ensenana.html')

@app.route("/ingresana")
def ingresana():
    return render_template('ingresana.html')

@app.route("/registratena")
def registratena():
    return render_template('registratena.html')

@app.route("/informatena")
def informatena():
    return render_template('informatena.html')

@app.route("/contratana_menu")
def contratana_menu():
    return render_template('contratana_menu.html')

@app.route("/contactana")
def contactana():
    return render_template('contactana.html')

@app.route("/publicana")
def publicana():
    return render_template('publicana.html')

@app.route("/profile_card2")
def profile_card2():
    return render_template('profile_card2.html')

@app.route("/buscana")
def buscana():
    return render_template('buscana.html')

if __name__ == "__main__":
    app.run(debug=True)