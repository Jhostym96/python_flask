from models.productos_model import ProductosModel


class ProductosController:

    def __init__(self) -> None:
        self.model = ProductosModel

    def crearProducto(self):
        return {
            'message': 'Soy el metodo crear producto'
        }

    def listarProductos(self):
        productos = ProductosModel.query.all()
        return {
            'message': 'Lista de productos'
        }
