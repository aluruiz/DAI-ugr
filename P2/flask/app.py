from flask import Flask
from flask import request
import mandelbort as mb
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<usuario>')
def hola(usuario):
    return 'Bienvenido ' + usuario + '!'

@app.route('/')
def html():
    return """
        <html>
        <head>
        <title>Titulo de la pagina</title>
        </head>

        <body>
            <img src="./static/saludo.jpg" height="100">
            <h1>Titulo de la pagina</h1>
            <h2>Subtitulo</h2>
            <p>Esto es una <b>pagina de prueba</b> para la asignatura de DAI</p>
        </body>
        </html>
    """

@app.route('/mandel',methods=['GET'])
def mandelbort():
        x1=int(request.args.get('x1'))
        y1=int(request.args.get('y1'))
        x2=int(request.args.get('x2'))
        y2=int(request.args.get('y2'))
        fichero=request.args.get('fichero')
        mb.pintaMandelbrot(x1,y1,x2,y2,400,255,fichero + ".png")
        return '<html><img src="/static/'-+fichero+'.png"></html>'


@app.errorhandler(404)
def error(error):
    return 'Error. Sitio no encontrado.'
