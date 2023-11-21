'''Crea una función llamada devolver_distintos() que reciba 3 integers como
parámetros. Si la suma de los 3 numeros es mayor a 15 , va a devolver elnúmero
mayor .Si la suma de los 3 numeros es menor a 10 , va a devolver elnúmero
menor .Si la suma de los 3 números es un valor entre 10 y 15(incluidos) va a devolver
el número de valor intermedio
.'''

def devolver_distintos(num1, num2, num3):
    suma_numeros = num1 + num2 + num3

    if suma_numeros > 15:
        return max(num1, num2, num3)
    elif suma_numeros < 10:
        return min(num1, num2, num3)
    else:
        # La suma está entre 10 y 15
        return suma_numeros // 2  # Devuelve el valor intermedio

# Ejemplo de uso
resultado = devolver_distintos(5, 3, 2)
print(resultado)

