from flask import Flask

app = Flask(__name__)

# Datos de ejemplo de productos (solo para demostración)
productos = [
    {"nombre": "Producto 1", "precio": 10.99, "cantidad": 5},
    {"nombre": "Producto 2", "precio": 20.49, "cantidad": 10},
    {"nombre": "Producto 3", "precio": 15.75, "cantidad": 3}
]

@app.route('/')
def listar_productos():
    head = '<h1>Listado de Productos</h1>'
    lista_productos = '<ul>'
    for producto in productos:
        lista_productos += '<li>Nombre: {} - Precio: {} - Cantidad: {}</li>'.format(producto["nombre"], producto["precio"], producto["cantidad"])
    lista_productos += '</ul>'
    return head + lista_productos

if __name__ == '__main__':
    app.run(debug=True)
