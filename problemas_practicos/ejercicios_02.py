'''Escribe una función (puedes ponerle cualquier nombre quequieras)
que reciba cualquier palabra como parámetro, y quedevuelva todas sus letras únicas
(sin repetir) pero en ordenalfabético. Por ejemplo si al invocar esta función
pasamos la palara "entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
Ejercicio 2'''
def juego_palabras(palabra):
    lista = list(palabra)
    lista.sort()
    lista = list(set(lista))
    lista.sort()
    return lista

print(juego_palabras("entretenido"))