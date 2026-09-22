import requests as consulta

categorias = consulta.get('https://api.chucknorris.io/jokes/categories')
print("catergorias: ",categorias.json())
lista_categoria = categorias.json()
lista_categoria_dic = []
num=0
for i in lista_categoria:
    num = num + 1
    lista_categoria_dic.append({"clave": num, "valor":i})

for diccionario in lista_categoria_dic:
    print(f"{diccionario['clave']} - {diccionario['valor']}")

seleccion = input("Seleccione una categoria: ")
categoria_seleccionada=None

for diccionario in lista_categoria_dic:
    if diccionario['clave'] == int(seleccion):
        categoria_seleccionada = diccionario['valor']
        #print(f"Categoria seleccionada: {diccionario['valor']}")

#print("ultimo dato de lista categoria: ",lista_categoria[len(lista_categoria)-1])
response = consulta.get(f'https://api.chucknorris.io/jokes/random?category={categoria_seleccionada}')

#print("codigo hhtp de respuesta ",response.status_code)
#print("cabecera: ",response.headers['content-type'])
#print("encoding: ",response.encoding)
#print("respuesta en string: ",response.text)
print("respuesta en json: ",response.json())

['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']