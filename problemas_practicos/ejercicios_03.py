'''Escribe una función que requiera una cantidad indefinida de argumentos.
Lo que hará esta función es devolver True si enalgún momento se ha
ingresado al numero cero repetido dos veces consecutivas
.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False'''

def ceros(*args):
    count_cero = 0
    for i in range(len(args) - 1):  # Iterar hasta el penúltimo elemento
        if args[i] == 0 and args[i+1] == 0:
            count_cero += 1

    return count_cero > 0

# Ejemplos de uso
print(ceros(5, 6, 1, 0, 0, 9, 3, 5))  # Debería devolver True
print(ceros(6, 0, 5, 1, 0, 3, 0, 1))  # Debería devolver False
