from models.categorias_model import CategoriasModel
from app import db


class CategoriasController:
    def __init__(self) -> None:
        self.model = CategoriasModel

    def crearCategoria(self, data):
      try:
        categoria = self.model(data['nombre'])
        db.session.add(categoria)
        db.session.commit()
        return {
          'data': categoria.convertirJson()
        }
      except Exception as e:
        return {
          'message': 'Internal server error',
          'error': str(e)
        }

