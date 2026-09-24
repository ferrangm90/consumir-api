import requests as consulta

class ModelApi:
    def __init__(self):
        self.categorias=None
        self.jokes=None
        self.lista_categoria=[]
        self.lista_categoria_dic=[]

    def consulta_categoria(self):
        self.categorias = consulta.get('https://api.chucknorris.io/jokes/categories')
        self.lista_categoria = self.categorias.json()

    def consulta_jokes(self,categoria_seleccionada):
        self.jokes = consulta.get(f'https://api.chucknorris.io/jokes/random?category={categoria_seleccionada}')

    def crear_diccionario_categoria(self):
        num = 0
        for i in self.lista_categoria:
            num = num +1
            self.lista_categoria_dic.append({"clave":num, "valor":i})