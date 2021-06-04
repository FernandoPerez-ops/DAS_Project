import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)


from abc import ABC, abstractclassmethod, abstractmethod
from Nucleo.Clases.libros import libros

class Bibliotecario(ABC):
    #listo
    @abstractmethod
    def checkIfExist(self,titulo:str):
        pass
    @abstractmethod
    def guardarLibro(self, libro:libros):
        pass
    @abstractmethod
    def guardarMuchosLibros(self, listaLibros:list):
        pass
    @abstractmethod
    def libroPorTitulo(self, titulo:str) -> libros:
        pass
    @abstractmethod
    def librosPorAutor(self, autor:str) -> list:
        pass
    @abstractmethod
    def librosPorAno(self,ano:int) -> list:
        pass
    @abstractmethod
    def librosPorIdioma(self,idioma:str) -> list:
        pass
    @abstractmethod
    def librosPorEditorial(self,editorial:str) -> list:
        pass
    pass
