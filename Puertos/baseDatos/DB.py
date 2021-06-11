import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from pymongo import MongoClient
from Nucleo.Clases.libros import libros
from Interfaces.interfacedb import Bibliotecario

class BibliotecarioEx(Bibliotecario):
    ### ATENCION AQUI: poner el puerto de tu base de mongo

    mongo_client = MongoClient('mongodb://root:root@mongo:27017/')
    db = mongo_client["project"]
    col = db["libros"]

    def guardarLibro(self, libros: libros):
        titulo = libros.getTitulo()
        autor = libros.getAutor()
        anoLanzamiento = libros.getAnoLanzamiento()
        categoria = libros.getCategoria()
        editorial = libros.getEditorial()
        idioma = libros.getIdioma()
        numPaginas = libros.getNumPaginas()
        descripcion = libros.getDescripcion()
        dicc = {
            "Titulo" : titulo,
            "Autor" : autor,
            "Año Lanzamiento" : anoLanzamiento,
            "Categoria" : categoria,
            "Editorial" : editorial,
            "Idioma" : idioma,
            "Nummero de Paginas" : numPaginas,
            "Descripcion" : descripcion
        }

        self.col.insert_one(dicc)
        if self.col.count_documents({"Titulo":libros.getTitulo()}, limit = 1) != 0:
            return True
        else:
            return False
            pass
        pass
    def checkIfExist(self, titulo: str):
        if self.col.count_documents({"Titulo":titulo}, limit = 1) != 0:
            return True
        else:
            return False

    def guardarMuchosLibros(self, listaLibros:list):
        guardado=[]
        for i in range(0,len(listaLibros)):
            titulo = listaLibros[i].getTitulo()
            autor = listaLibros[i].getAutor()
            anoLanzamiento = listaLibros[i].getAnoLanzamiento()
            categoria = listaLibros[i].getCategoria()
            editorial = listaLibros[i].getEditorial()
            idioma = listaLibros[i].getIdioma()
            numPaginas = listaLibros[i].getNumPaginas()
            descripcion = listaLibros[i].getDescripcion()
            dicc = {
                "Titulo" : titulo,
                "Autor" : autor,
                "Año Lanzamiento" : anoLanzamiento,
                "Categoria" : categoria,
                "Editorial" : editorial,
                "Idioma" : idioma,
                "Nummero de Paginas" : numPaginas,
                "Descripcion" : descripcion
            }
            guardado.append(dicc)
        
        self.col.insert_many(guardado)

    def libroPorTitulo(self, titulo: str):
        busquedalibro = self.col.find_one({"Titulo":titulo})
        titulo = busquedalibro["Titulo"]
        autor = busquedalibro["Autor"]
        anoLanzamiento = busquedalibro["Año Lanzamiento"]
        categoria = busquedalibro["Categoria"]
        editorial = busquedalibro["Editorial"]
        idioma = busquedalibro["Idioma"]
        numPaginas = busquedalibro["Nummero de Paginas"]
        descripcion = busquedalibro["Descripcion"]
        buscarnombre = libros(titulo,autor,anoLanzamiento,categoria,editorial,idioma,numPaginas,descripcion)
        
        return buscarnombre
    
    def librosPorAutor(self, autor: str):
        busquedaautores=[]
        busquedadb = self.col.find({"Autor":autor})

        for i in busquedadb:
            titulo = i["Titulo"]
            autor = i["Autor"]
            anoLanzamiento = i["Año Lanzamiento"]
            categoria = i["Categoria"]
            editorial = i["Editorial"]
            idioma = i["Idioma"]
            numPaginas = i["Nummero de Paginas"]
            descripcion = i["Descripcion"]
            autores = libros(titulo,autor,anoLanzamiento,categoria,editorial,idioma,numPaginas,descripcion)
            busquedaautores.append(autores)
        return busquedaautores
    
    def librosPorAno(self, ano: int):
        busquedalanza=[]
        busquedadb = self.col.find({"Año Lanzamiento":ano})

        for i in busquedadb:
            titulo = i["Titulo"]
            autor = i["Autor"]
            anoLanzamiento = i["Año Lanzamiento"]
            categoria = i["Categoria"]
            editorial = i["Editorial"]
            idioma = i["Idioma"]
            numPaginas = i["Nummero de Paginas"]
            descripcion = i["Descripcion"]
            alanzamiento = libros(titulo,autor,anoLanzamiento,categoria,editorial,idioma,numPaginas,descripcion)
            busquedalanza.append(alanzamiento)
        return busquedalanza
    
    def librosPorEditorial(self, editorial: str):
        busquedaedit=[]
        busquedadb = self.col.find({"Editorial":editorial})

        for i in busquedadb:
            titulo = i["Titulo"]
            autor = i["Autor"]
            anoLanzamiento = i["Año Lanzamiento"]
            categoria = i["Categoria"]
            editorial = i["Editorial"]
            idioma = i["Idioma"]
            numPaginas = i["Nummero de Paginas"]
            descripcion = i["Descripcion"]
            editoriales = libros(titulo,autor,anoLanzamiento,categoria,editorial,idioma,numPaginas,descripcion)
            busquedaedit.append(editoriales)
        return busquedaedit



    def librosPorIdioma(self, idioma: str):
        busquedaidioma=[]
        busquedadb = self.col.find({"Editorial":idioma})

        for i in busquedadb:
            titulo = i["Titulo"]
            autor = i["Autor"]
            anoLanzamiento = i["Año Lanzamiento"]
            categoria = i["Categoria"]
            editorial = i["Editorial"]
            idioma = i["Idioma"]
            numPaginas = i["Nummero de Paginas"]
            descripcion = i["Descripcion"]
            idiomas = libros(titulo,autor,anoLanzamiento,categoria,editorial,idioma,numPaginas,descripcion)
            busquedaidioma.append(idiomas)
        return busquedaidioma

    def librosupdateT(self, titulo: str):
        busquedadb = self.col.find({"Titulo":titulo})
        d = input("Cuales el dato que desea cambiar del libro?")

        titulo = busquedadb["Titulo"]
        if d == "autor" or d =="Autor":
            autor = input("Digite el dato a cambiar\n")
            self.col.find_one_and_update({"Titulo":titulo},{"$set":{"Autor":autor}} )

        if d == "Año Lanzamiento" or d =="año de lanzamiento" or d =="Año de lanzamiento":
            anoLanzamiento = input("Digite el dato a cambiar\n")
            self.col.find_one_and_update({"Titulo":titulo}, {"$set":{"Año Lanzamiento":anoLanzamiento}})
        
        elif d == "categoria" or d =="Categoria":
            categoria = input("Digite el dato a cambiar\n")
            self.col.find_one_and_update({"Titulo":titulo}, {"$set":{"Categoria":categoria}})

        elif d == "editorial" or d =="Editorial":
            editorial = input("Digite el dato a cambiar\n")
            self.col.find_one_and_update({"Titulo":titulo}, {"$set":{"Editorial":editorial}})
       
        elif d == "idioma" or d =="Idioma":
            idioma = input("Digite el dato a cambiar\n")
            self.col.find_one_and_update({"Titulo":titulo}, {"$set":{"Idioma":idioma}})
        
        elif d == "numPAginas" or d =="Numero de paginas" or d=="numero de paginas":
            numPaginas = input("Digite el dato a cambiar\n")
            self.col.find_one_and_update({"Titulo":titulo},{"$set":{"Nummero de Paginas":numPaginas}} )
        
        elif d == "descripcion" or d =="Descripcion":
            descripcion = input("Digite el dato a cambiar\n")
            self.col.find_one_and_update({"Titulo":titulo},{"$set":{"Descripcion":descripcion}})
        else:
            print("Dato no espesificado, intentelo de nuevo plis :D")
        
        busquedalibro = self.col.find_one({"Titulo":titulo})
        titulo = busquedalibro["Titulo"]
        autor = busquedalibro["Autor"]
        anoLanzamiento = busquedalibro["Año Lanzamiento"]
        categoria = busquedalibro["Categoria"]
        editorial = busquedalibro["Editorial"]
        idioma = busquedalibro["Idioma"]
        numPaginas = busquedalibro["Nummero de Paginas"]
        descripcion = busquedalibro["Descripcion"]
        buscarnombre = libros(titulo,autor,anoLanzamiento,categoria,editorial,idioma,numPaginas,descripcion)
        return buscarnombre

    def borrarlibro(self, titulo: str):
        busquedadb = self.col.delete_one({"Titulo":titulo})
        if self.col.count_documents({"Titulo":libros.getTitulo()}, limit = 1) != 0:
            return "Libro no eliminado"
        else:
            return "libro Elminado"