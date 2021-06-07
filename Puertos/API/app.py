import os, sys

from pymongo import mongo_client
p = os.path.abspath('.')
sys.path.insert(1, p)

from flask import Flask, request, json, Response
from flask_pymongo import PyMongo
from bson import json_util

app = Flask(__name__)

app.config['MONGO_HOST'] = 'mongo'
app.config['MONGO_PORT'] = '27017'
app.config['MONGO_DBNAME'] = 'project'
app.config['MONGO_USERNAME'] = 'root'
app.config['MONGO_PASSWORD'] = 'root'
app.config['MONGO_AUTH_SOURCE'] = 'admin'

mongo = PyMongo(app,uri="mongodb://root:root@mongo:27017/project?authSource=admin")
db = mongo.db

@app.route('/libros/agregar', methods=['POST'])
def add_one():
    dicc = {
        'Titulo':request.json['Titulo'],
        'Autor':request.json['Autor'],
        'Año Lanzamiento':request.json['Año Lanzamiento'],
        'Categoria':request.json['Categoria'],
        'Editorial':request.json['Editorial'],
        'Idioma':request.json['Idioma'],
        'Nummero de Paginas':request.json['Nummero de Paginas'],
        'Descripcion':request.json['Descripcion']
    }
    db.libros.insert_one(dicc)
    return json.jsonify(message="success")

@app.route('/libros',methods=['GET'])
def get_one():
    libros = db.libros.find()
    respuesta = json_util.dumps(libros)
    return Response(respuesta, mimetype='application/json')

@app.route('/libros/<Titulo>', methods=['GET'])
def get_book(Titulo):
    libro = db.libros.find_one({'Titulo':Titulo})
    respuesta = json_util.dumps(libro)
    return respuesta

@app.route('/libros/<Autor>', methods=['GET'])
def get_book(Autor):
    libro = db.libros.find_one({'Autor':Autor})
    respuesta = json_util.dumps(libro)
    return respuesta

@app.route('/libros/<Idioma>', methods=['GET'])
def get_book(Idioma):
    libro = db.libros.find_one({'Autor':Idioma})
    respuesta = json_util.dumps(libro)
    return respuesta

@app.route('/libros/<Anio>', methods=['GET'])
def get_book(Anio):
    libro = db.libros.find_one({'Año Lanzamiento':Anio})
    respuesta = json_util.dumps(libro)
    return respuesta

@app.route('/libros/<Editorial>', methods=['GET'])
def get_book(Editorial):
    libro = db.libros.find_one({'Año Lanzamiento':Editorial})
    respuesta = json_util.dumps(libro)
    return respuesta

@app.route('/libros/<Editorial>', methods=['GET'])
def delete_one(titulo):
    db.libros.delete_one({'Titulo':titulo})
    return json.jsonify(message="libro Elminado")

@app.route('/libros/<Editorial>', methods=['GET'])
def update_one(titulo):
    busquedadb = db.col.find({"Titulo":titulo})
    d = input("Cuales el dato que desea cambiar del libro?")
    titulo = busquedadb["Titulo"]

    if d == "autor" or d =="Autor":
        autor = input("Digite el dato a cambiar\n")
        db.col.find_one_and_update({"Titulo":titulo},{"$set":{"Autor":autor}})
        libro = db.libros.find_one({"Titulo":titulo})
        respuesta = json_util.dumps(libro)
        return respuesta

    if d == "Año Lanzamiento" or d =="año de lanzamiento" or d =="Año de lanzamiento":
        anoLanzamiento = input("Digite el dato a cambiar\n")
        db.col.find_one_and_update({"Titulo":titulo}, {"$set":{"Año Lanzamiento":anoLanzamiento}})
        libro = db.libros.find_one({"Titulo":titulo})
        respuesta = json_util.dumps(libro)
        return respuesta
        
    elif d == "categoria" or d =="Categoria":
        categoria = input("Digite el dato a cambiar\n")
        db.col.find_one_and_update({"Titulo":titulo}, {"$set":{"Categoria":categoria}})
        libro = db.libros.find_one({"Titulo":titulo})
        respuesta = json_util.dumps(libro)
        return respuesta

    elif d == "editorial" or d =="Editorial":
        editorial = input("Digite el dato a cambiar\n")
        db.col.find_one_and_update({"Titulo":titulo}, {"$set":{"Editorial":editorial}})
        libro = db.libros.find_one({"Titulo":titulo})
        respuesta = json_util.dumps(libro)
        return respuesta
       
    elif d == "idioma" or d =="Idioma":
        idioma = input("Digite el dato a cambiar\n")
        db.col.find_one_and_update({"Titulo":titulo}, {"$set":{"Idioma":idioma}})
        libro = db.libros.find_one({"Titulo":titulo})
        respuesta = json_util.dumps(libro)
        return respuesta
        
    elif d == "numPAginas" or d =="Numero de paginas" or d=="numero de paginas":
        numPaginas = input("Digite el dato a cambiar\n")
        db.col.find_one_and_update({"Titulo":titulo},{"$set":{"Nummero de Paginas":numPaginas}} )
        libro = db.libros.find_one({"Titulo":titulo})
        respuesta = json_util.dumps(libro)
        return respuesta
        
    elif d == "descripcion" or d =="Descripcion":
        descripcion = input("Digite el dato a cambiar\n")
        db.col.find_one_and_update({"Titulo":titulo},{"$set":{"Descripcion":descripcion}})
        libro = db.libros.find_one({"Titulo":titulo})
        respuesta = json_util.dumps(libro)
        return respuesta
    
    else:
        return json.jsonify(message="Dato no espesificado, intentelo de nuevo plis :D")
    
if __name__ == '__main__':
    app.run(debug=True)