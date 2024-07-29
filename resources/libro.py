from flask import request
from flask_restful import Resource
from db import libros
from models import Libro

class LibroResource(Resource):
    def get(self, id):
        libro = libros.get(id)
        if libro:
            return libro.__dict__, 200
        return {'message': 'Libro no encontrado'}, 404

    def post(self):
        data = request.get_json()
        id = int(max(libros.keys() or [0])) + 1
        libro = Libro(
            id=id,
            titulo=data['titulo'],
            fecha=data['fecha'],
            autor_id=data['autor_id'],
            categoria_id=data['categoria_id'],
            editorial_id=data['editorial_id'],
            idioma=data['idioma'],
            paginas=data['paginas'],
        )
        libros[id] = libro
        return libro.__dict__, 201

    def put(self, id):
        data = request.get_json()
        libro = libros.get(id)
        if libro:
            libro.titulo = data['titulo']
            libro.fecha = data['fecha']
            libro.autor_id = data['autor_id']
            libro.category=ia_id = data['categoria_id']
            libro.editorial_id = data['editorial_id']
            libro.idioma=data['idioma']
            libro.paginas=data['paginas']
            return libro.__dict__, 200
        return {'message': 'Libro no encontrado'}, 404

    def delete(self, id):
        if id in libro:
            del libro[id]
            return '', 204
        return {'message': 'Libro no encontrado'}, 404
