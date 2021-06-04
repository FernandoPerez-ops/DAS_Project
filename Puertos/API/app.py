import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from Nucleo.Clases.libros import libros
from Puertos.baseDatos.DB import BibliotecarioEx
from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://root:root@mongo:27017/project"
mongo = PyMongo(app)

@app.route('/libros', methods=['POST'])
def create_libro():
    titulo = request.json['Titulo']
    autor = request.json['Autor']
    anoLanzamiento = request.json['Año Lanzamiento']
    categoria = request.json['Categoria']
    editorial = request.json['Editorial']
    idioma = request.json['Idioma']
    numPaginas = request.json['Numero de Paginas']
    descripcion = request.json['Descripcion']
    x = libros(titulo,autor,anoLanzamiento,categoria,editorial,idioma,numPaginas,descripcion)

    if mongo.db.libros.count_documents({"Titulo":titulo}, limit=1):
        return {'Fallo':'Libro ya existe'}
    else:
        mongo.db.libros.insert({
            "Titulo" : titulo,
            "Autor" : autor,
            "Año Lanzamiento" : anoLanzamiento,
            "Categoria" : categoria,
            "Editorial" : editorial,
            "Idioma" : idioma,
            "Nummero de Paginas" : numPaginas,
            "Descripcion" : descripcion
        })
        return {'Exito':'Libro guardado'}
    
    

if __name__ == '__main__':
    app.run(debug=True)