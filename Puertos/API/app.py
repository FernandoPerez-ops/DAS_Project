from flask import Flask, request, json, Response
from flask_pymongo import PyMongo
from bson import json_util, ObjectId

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
def get_all():
    libros = db.libros.find()
    respuesta = json_util.dumps(libros)
    return Response(respuesta, mimetype='application/json')

@app.route('/libros/Titulo/<Titulo>', methods=['GET'])
def get_bookT(Titulo):
    libro = db.libros.find_one({'Titulo':Titulo})
    respuesta = json_util.dumps(libro)
    return respuesta

@app.route('/libros/Autor/<Autor>', methods=['GET'])
def get_bookA(Autor):
    libro = db.libros.find_one({'Autor':Autor})
    respuesta = json_util.dumps(libro)
    return respuesta

@app.route('/libros/Idioma/<Idioma>', methods=['GET'])
def get_bookI(Idioma):
    libro = db.libros.find_one({'Autor':Idioma})
    respuesta = json_util.dumps(libro)
    return respuesta

@app.route('/libros/Anio/<Anio>', methods=['GET'])
def get_bookAn(Anio):
    libro = db.libros.find_one({'Año Lanzamiento':Anio})
    respuesta = json_util.dumps(libro)
    return respuesta

@app.route('/libros/Editorial/<Editorial>', methods=['GET'])
def get_bookE(Editorial):
    libro = db.libros.find_one({'Año Lanzamiento':Editorial})
    respuesta = json_util.dumps(libro)
    return respuesta

@app.route('/libros/borrar/<id>', methods=['DELETE'])
def del_book(id):
    db.libros.delete_one({"_id":ObjectId(id)})
    return json.jsonify(message="success")

@app.route('/libros/actualizar/<id>', methods=['PUT'])
def update_book(id):
    Titulo=request.json['Titulo']
    Autor=request.json['Autor']
    Anio=request.json['Año Lanzamiento']
    Categoria=request.json['Categoria']
    Editorial=request.json['Editorial']
    Idioma=request.json['Idioma']
    nPags=request.json['Nummero de Paginas']
    Descripcion=request.json['Descripcion']

    db.libros.update_one({"_id":ObjectId(id)},{"$set":{
        "Titulo":Titulo,
        "Autor":Autor,
        "Año Lanzamiento":Anio,
        "Categoria":Categoria,
        "Editorial":Editorial,
        "Idioma":Idioma,
        "Nummero de Paginas":nPags,
        "Descripcion":Descripcion
    }})
    return json.jsonify(message="success")

if __name__ == '__main__':
    app.run(debug=True)