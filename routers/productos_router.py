from app import app
from controllers.productos_controller import ProductosController


@app.route('/productos/lista', methods=['GET'])
def productosListar():
    controller = ProductosController()
    return controller.listarProductos()
