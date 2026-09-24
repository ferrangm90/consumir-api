import requests as consulta
from model import ModelApi
from view import ViewApi

class ControllerApi():
    def __init__(self):
        self.modelo = ModelApi()
        self.modelo.consulta_categoria()
        self.modelo.crear_diccionario_categoria()

        self.vista= ViewApi()
        self.vista.mostrar_categorias(self.modelo)
        self.vista.seleccionar_categoria()

    def logica_seleccion(self):
        categoria_seleccionada=None
        for diccionario in self.modelo.lista_categoria_dic:
            if diccionario['clave'] == self.vista.seleccion:
                categoria_seleccionada = diccionario['valor']

        self.modelo.consulta_jokes(categoria_seleccionada)
        self.vista.mostrar_jokes(self.modelo)