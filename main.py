from flask import Flask, render_template, redirect
from crear_db import CargarDatos

productos = CargarDatos()


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', productos=productos)


@app.route('/producto/<int:pid>')
def producto(pid):
    for producto in productos:
        if pid == producto['id']:
            return render_template('producto.html', producto=producto)
    return redirect('/')


# Programa princiupal
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
