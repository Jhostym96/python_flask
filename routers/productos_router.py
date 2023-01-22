from app import app
from controllers.productos_controller import ProductosController


@app.route('/productos/listar', methods=['GET'])
def productosListar():
    controller = ProductosController()
    return controller.listarProductos()
