import requests as consulta

categorias = consulta.get('https://api.chucknorris.io/jokes/categories')
print("catergorias: ",categorias.json())
lista_categoria = categorias.json()
print("ultimo dato de lista categoria: ",lista_categoria[len(lista_categoria)-1])
response = consulta.get('https://api.chucknorris.io/jokes/random?category=animal')

print("codigo hhtp de respuesta ",response.status_code)
print("cabecera: ",response.headers['content-type'])
print("encoding: ",response.encoding)
print("respuesta en string: ",response.text)
print("respuesta en json: ",response.json())