from flask import request
from flask_restful import Resource
from db import editoriales
from models import Editorial

class EditorialResource(Resource):
    def get(self, id):
        editorial = editoriales.get(id)
        if editorial:
            return editorial.__dict__, 200
        return {'message': 'Editorial no encontrada'}, 404

    def post(self):
        data = request.get_json()
        id = int(max(editoriales.keys() or [0])) + 1
        editorial = Editorial(id=id, nombre=data['nombre'])
        editoriales[id] = editorial
        return editorial.__dict__, 201

    def put(self, id):
        data = request.get_json()
        editorial = editoriales.get(id)
        if editorial:
            editorial.nombre = data['nombre']
            return editorial.__dict__, 200
        return {'message': 'Editorial no encontrada'}, 404

    def delete(self, id):
        if id in editoriales:
            del editoriales[id]
            return '', 204
        return {'message': 'Editorial no encontrada'}, 404
