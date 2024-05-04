from flask import Flask, render_template, redirect, g
from crear_db import CargarDatos

productos = CargarDatos()

# Crear un diccionario para agrupar los productos por categoría
productos_por_categoria = {}

# Agrupar los productos por categoría
for producto in productos:
    categoria = producto['categoria']
    if categoria not in productos_por_categoria:
        productos_por_categoria[categoria] = []
    productos_por_categoria[categoria].append(producto)


app = Flask(__name__)


@app.before_request
def before_request():
    g.categorias = list(productos_por_categoria.keys())


@app.route('/')
def index():
    return render_template('index.html', productos=productos)


@app.route('/producto/<int:pid>')
def producto(pid):
    for producto in productos:
        if pid == producto['id']:
            return render_template('producto.html', producto=producto)
    return redirect('/')


@app.route('/categoria/<string:categoria>')
def categoria(categoria):
    if categoria in productos_por_categoria:
        return render_template('categoria.html', categoria=categoria, productos=productos_por_categoria[categoria])
    else:
        return redirect('/')


# Programa princiupal
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
