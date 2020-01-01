from flask import Flask, render_template,  session, redirect, url_for, escape, request
from flask import request
from pickleshare import *
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
db = client.SampleCollections        # Elegimos la base de datos de ejemplo

app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

def addHistorial(pagina):
    historial = session['historial']
    if len(historial) < 3:
        historial.append(pagina)          
        print(len(historial))
    else:
        historial.pop(0)
        historial.append(pagina)
        print(str(len(historial)) + "primera")

    session['historial'] = historial

@app.route('/')
def index():
    if 'username' in session and 'password' in session:
        return render_template('base.html', username=session['username'])
    return render_template('base.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        passwd = request.form['password']
        db = PickleShareDB('miBD')

        if db[user] and passwd == db[user]["pass"]:
            session['username'] = user
            session['historial'] = []
            return render_template('base.html', username = user)
        else:
             return render_template('base.html')
    else:
        if 'username' in session:
            user = session['username']
            return render_template('base.html', username = user)
        else: 
            return redirect(url_for('index'))

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    session.pop('historial', None)
    return redirect(url_for('index'))


@app.route('/registrar', methods=['GET','POST'])
def registrar():
    if request.method == 'POST':
        user = request.form['username']
        passwd = request.form['password'] 

        db = PickleShareDB('miBD')
        db[user] = {'pass': passwd}

        return render_template('registrar.html', username = user)
    else:
        if 'username' in session:
            user = session['username']
            addHistorial("registrar.html")
            return render_template('registrar.html', username = user, historial = session['historial'])
        else:
            return render_template('registrar.html')

@app.route('/datos', methods=['GET','POST'])
def datos():
    datos = []
    if request.method == 'POST':
        user = request.form['username']
        passwd = request.form['password']
        db = PickleShareDB('miBD')
        db[user] = {'pass': passwd}
        datos.append(user)
        datos.append(db[user]["pass"])

        return render_template('datos.html', username = user, datos = datos)
    else:   
        if 'username' in session:
            user = session['username']
            db = PickleShareDB('miBD')
            datos.append(user)
            datos.append(db[user]["pass"])
            addHistorial("datos.html")
            return render_template('datos.html', username = user, datos = datos, historial = session['historial'])
        else: 
            return render_template('datos.html')

@app.errorhandler(404)
def page_not_found(error):
    if 'username' in session:
        user = session['username']
        addHistorial("error.html")
        return render_template('error.html', username = user, historial = session['historial'])
    else: 
        return render_template('error.html')

@app.route('/mongo')
def mongo():
    val = db.samples_friends.find()
    return val[24]['name']

@app.route('/busqueda', methods=['GET','POST'])
def busqueda():
    if request.method == 'POST':
        client = MongoClient("mongo", 27017)
        db = client.SampleCollections

        clave = request.form['palabra']
        temp = request.form['temporada']

        if temp == "0":
            bqd = db.samples_friends.find({ "$or": [{"name": {"$regex": clave}}, {"summary": {"$regex": clave}}]})    
        else:
            bqd = db.samples_friends.find({"$and":[{"season": float(temp)}, {"name": {"$regex": clave}}]})

        if 'username' in session:
            user = session['username']
            addHistorial("busqueda.html")
            return render_template('busqueda.html', username = user, historial = session['historial'], busqueda = bqd)
        else:
            return render_template('busqueda.html', busqueda = bqd)
    else: 
        if 'username' in session:
            user = session['username']
            addHistorial("busqueda.html")
            return render_template('busqueda.html', username = user, historial = session['historial'])
        else:
            return render_template('busqueda.html')
        

@app.route('/modificar', methods=['GET','POST'])
def modificar():
    if 'username' in session:
        user = session['username']
        addHistorial("modificar.html")

        if request.method == 'POST':
            client = MongoClient("mongo", 27017)
            db = client.SampleCollections

            numero = request.form['numero']
            nombre = request.form['nombre']

            if db.samples_pokemon.update({"name" : nombre}, {"$set" : {"num" : numero}}):
                nota = "Editado con exito"
                return render_template('modificar.html', username = user, historial = session['historial'], nota = nota)
            else:
                nota = "No se ha realizado con exito"
                return render_template('modificar.html', username = user, historial = session['historial'], nota = nota)
        else:
            return render_template('modificar.html', username = user, historial = session['historial'])
    else:
        nota = "No eres usuario, no puedes acceder aqui"
        return render_template('modificar.html', nota = nota)
        
        

@app.route('/eliminar', methods=['GET','POST'])
def eliminar():
    if 'username' in session:
        user = session['username']
        addHistorial("eliminar.html")
        historial = []
        historial = session['historial']

        if request.method == 'POST':
            client = MongoClient("mongo", 27017)
            db = client.SampleCollections

            numero = request.form['numero']

            if db.samples_pokemon.remove({"num" : numero}):
                nota = "Eliminado con exito"
                return render_template('eliminar.html', username = user, historial = session['historial'], nota = nota)
            else:
                nota = "No se ha realizado con exito"
                return render_template('eliminar.html', username = user, historial = session['historial'], nota = nota)
        else:
            return render_template('eliminar.html', username = user, historial = session['historial'])
    else:
        nota = "No eres usuario, no puedes acceder aqui"
        return render_template('eliminar.html', nota = nota)
    
        