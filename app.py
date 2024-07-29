from flask import Flask
from flask_restful import Api
from resources.autor import AuthorResource
from resources.libro import BookResource
from resources.categoria import CategoryResource
from resources.editorial import PublisherResource

app = Flask(__name__)
api = Api(app)

api.add_resource(AutorResource, '/autores', '/autores/<int:id>')
api.add_resource(LibroResource, '/libros', '/libros/<int:id>')
api.add_resource(CategoriaResource, '/categorias', '/categorias/<int:id>')
api.add_resource(EditorialResource, '/editoriales', '/editoriales/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
