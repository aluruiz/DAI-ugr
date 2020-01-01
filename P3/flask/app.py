from flask import Flask, render_template,  session, redirect, url_for, escape, request
from flask import request
from pickleshare import *

app = Flask(__name__)

app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

nPaginas = 0
historial = []

def addHistorial(pagina):
    global nPaginas
    global historial
    
    if nPaginas < 3:
        historial.append(pagina)
        nPaginas = nPaginas + 1
    else:
        del historial[0]
        historial.append(pagina)
    
    return historial

@app.route('/')
def index():
    return render_template("base.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        passwd = request.form['password']
        db = PickleShareDB('miBD')
        if db[user] and passwd == db[user]["pass"]:
            session['username'] = user
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
    global nPaginas
    nPaginas = 0
    global historial 
    historial.clear()
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
            historial = addHistorial("registrar.html")
            return render_template("registrar.html", username = user, historial = historial)
        else:
            return render_template("registrar.html")

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
            historial = addHistorial("datos.html")
            return render_template('datos.html', username = user, datos = datos, historial = historial)
        else: 
            return render_template('datos.html')

@app.errorhandler(404)
def page_not_found(error):
    if 'username' in session:
        user = session['username']
        historial = addHistorial("error.html")
        return render_template('error.html', username = user, historial = historial)
    else: 
        return render_template('error.html')
    

