'''La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
letras a su elección y a partir de ese momento nuestro código va a procesar esa información
para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:
1. Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
encuentren absolutamente todas las letras es pasar, tanto el texto original como las
letras a buscar, a minúsculas.
2. Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y
para lograr esta parte, recuerda que hay un método de string que permite transformarlo
en una lista y que luego hay una función que permite averiguar el largo de una lista.
3. Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí
claramente echaremos mano de la indexación.
4. Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de
las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro
que permita unir esos elementos con espacios intermedios? Piénsalo.
5. Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del
texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:
puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la
manera de expresarle al usuario tu respuesta.'''

texto = input("Ingrese el texto a analizar:")
letras_1 = input("Ingrese la primer letra").lower()
letras_2 = input("Ingrese la segunda letra").lower()
letras_3 = input("Ingrese la tercer letra").lower()

texto_minuscula = texto.lower()
texto_list = texto_minuscula.split(" ")
print(texto_list)
primer_letra = texto_list[0][0]
ultima_letra = texto_list[-1][-1]
repite_1 = texto_minuscula.lower().count(letras_1)
repite_2 = texto_minuscula.lower().count(letras_2)
repite_3 = texto_minuscula.lower().count(letras_3)

print("la cantidad de veces que se repite la primer letra es: ", repite_1)
print("la cantidad de veces que se repite la segunda letra es: ", repite_2)
print("la cantidad de veces que se repite la tercerer letra es: ", repite_3)
print("La cantidad de palabras que contiene el texto es: ", len(texto_list))
print("Primer letra del texto: ", primer_letra)
print("Ultima letra del texto: ", ultima_letra)
texto_list.reverse()
texto_invertido = ' '.join(texto_list)
print("El texto invertido es, ", texto_invertido)
contiene_python = "python" in texto
print("El texto incluye la palabra 'Python''? :", contiene_python)




