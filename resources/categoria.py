from flask import request
from flask_restful import Resource
from db import categorias
from models import Categoria

class CategoriaResource(Resource):
    def get(self, id):
        categoria = categorias.get(id)
        if categoria:
            return categoria.__dict__, 200
        return {'message': 'Categoria no encontrada'}, 404

    def post(self):
        data = request.get_json()
        id = int(max(categorias.keys() or [0])) + 1
        categoria = categoria(id=id, nombre=data['nombre'])
        categorias[id] = categoria
        return categoria.__dict__, 201

    def put(self, id):
        data = request.get_json()
        categoria = categorias.get(id)
        if categoria:
            categoria.nombre = data['nombre']
            return categoria.__dict__, 200
        return {'message': 'categoria no encontrada'}, 404

    def delete(self, id):
        if id in categorias:
            del categorias[id]
            return '', 204
        return {'message': 'categoria no encontrada'}, 404
