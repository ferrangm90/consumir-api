class ViewApi():
    def __init__(self):
        self.seleccion=None

    def mostrar_categorias(self,modelo):
        for diccionario in modelo.lista_categoria_dic:
            print(f"{diccionario['clave']} - {diccionario['valor']}")      

    def seleccionar_categoria(self):
        self.seleccion = int(input("Seleccione un numero para categoria: ") )

    def mostrar_jokes(self,modelo): 
        print("respuesta en json:",modelo.jokes.json())  