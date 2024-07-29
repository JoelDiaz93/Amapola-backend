from flask import request
from flask_restful import Resource
from db import autores
from models import Autor

class AutorResource(Resource):
    def get(self, id):
        autor = autores.get(id)
        if autor:
            return autor.__dict__, 200
        return {'message': 'Autor no encontrado'}, 404

    def post(self):
        data = request.get_json()
        id = int(max(autores.keys() or [0])) + 1
        autor = Autor(id=id, nombre=data['nombre'])
        autores[id] = autor
        return autor.__dict__, 201

    def put(self, id):
        data = request.get_json()
        autor = autores.get(id)
        if autor:
            autor.nombre = data['nombre']
            return autor.__dict__, 200
        return {'message': 'Autor no encontrado'}, 404

    def delete(self, id):
        if id in autores:
            del autores[id]
            return '', 204
        return {'message': 'Autor no encontrado'}, 404
