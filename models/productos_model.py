from app import db
from sqlalchemy import Column, Integer, String, Float, Text, Boolean
from sqlalchemy.orm import relationship


class ProductosModel(db.Model):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(45), nullable=False)
    precio = Column(Float, nullable=False)
    imagen = Column(Text, nullable=False)
    estado = Column(Boolean, default=True)

    categorias_productos = relationship('CategoriasProductosModel')

    def __init__(self, nombre, precio, imagen, estado=None) -> None:
        self.nombre = nombre
        self.precio = precio
        self.imagen = imagen
        self.estado = estado

    def convertirJson(self):
        categorias_productos = []
        for categoria_producto in self.categorias_productos:
            categorias_productos.append(categoria_producto.categoria.convertirJson())

        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen': self.imagen,
            'estado': self.estado,
            'categorias': categorias_productos
        }