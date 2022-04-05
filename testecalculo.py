from abc import ABC, abstractclassmethod
from ast import Sub

class TesteCalculo(ABC):
    @abstractclassmethod
    def calcular(self, v1, v2):
        pass


class Dividir(TesteCalculo):
    def calcular( v1, v2):
        return(v1/v2)

class Somar(TesteCalculo):
    def calcular( v1, v2):
        return(v1+v2)

class Multiplicar(TesteCalculo):
    def calcular( v1, v2):
        return(v1*v2)

class Subtrair(TesteCalculo):
    def calcular( v1, v2):
        return(v1-v2)