import requests as consulta

categorias = consulta.get('https://api.chucknorris.io/jokes/categories')
lista_categoria = categorias.json()
lista_categoria_dic=[]
num=0
for i in lista_categoria:
    num = num +1
    lista_categoria_dic.append({"clave":num, "valor":i})

for diccionario in lista_categoria_dic:
    print(f"{diccionario['clave']} - {diccionario['valor']}")  

seleccion = int(input("Seleccione un numero para categoria: ") )
categoria_seleccionada=None
for diccionario in lista_categoria_dic:
    if diccionario['clave'] == seleccion:
        categoria_seleccionada = diccionario['valor']

response = consulta.get(f'https://api.chucknorris.io/jokes/random?category={categoria_seleccionada}')

print("respuesta en json:",response.json())