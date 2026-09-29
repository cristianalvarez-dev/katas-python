"""
Proyecto 3: Katas Python - Cristian Álvarez

Resolución de las 40 katas del Proyecto 3. Cada ejercicio va encabezado
con su enunciado en un comentario.
"""


# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(texto):
    # Paso a minúsculas para que 'E' y 'e' cuenten como la misma letra
    texto = texto.lower()
    letras = "abcdefghijklmnñopqrstuvwxyzáéíóúü"
    frecuencias = {}

    for letra in texto:
        # Solo cuento los caracteres que están en letras: descarto espacios, signos de puntuación y números
        if letra in letras:
            # get() devuelve 0 si la letra aún no está en el diccionario
            frecuencias[letra] = frecuencias.get(letra, 0) + 1

    return frecuencias


texto_prueba = "Esto es un texto y es de prueba"
print(frecuencia_letras(texto_prueba))

assert frecuencia_letras("Hola hola") == {'h': 2, 'o': 2, 'l': 2, 'a': 2}
assert frecuencia_letras("") == {}
assert frecuencia_letras("a, a.") == {'a': 2}
print("Kata 1 OK")


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def doble(numero):
    return numero * 2


lista_doble = list(map(doble, lista_numeros))
print(lista_doble)

assert doble(3) == 6
assert lista_doble == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
assert list(map(doble, [])) == []
print("Kata 2 OK")


# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

# Recorro cada palabra de la lista con for y compruebo si la palabra objetivo está contenida dentro de ella usando el operador "in". Si está, la añado a la lista de resultados con append().
# Comparo en minúsculas para que la búsqueda no distinga mayúsculas ("IT" encuentra "Nitwit").
# Uso para la lista las palabras del discurso de Dumbledore en el banquete de bienvenida en Harry Potter and the Philosopher's Stone (versión original)
palabras_kata3 = ["Nitwit", "Blubber", "Oddment", "Tweak"]


def buscar_palabras(lista, objetivo):
    resultado = []

    for palabra in lista:
        if objetivo.lower() in palabra.lower():
            resultado.append(palabra)   # guardo la palabra original, sin pasarla a minúsculas

    return resultado


print(buscar_palabras(palabras_kata3, "e"))    # ['Blubber', 'Oddment', 'Tweak']
print(buscar_palabras(palabras_kata3, "IT"))   # ['Nitwit']

# Pruebas
assert buscar_palabras(palabras_kata3, "e") == ["Blubber", "Oddment", "Tweak"]
assert buscar_palabras(palabras_kata3, "IT") == ["Nitwit"]
assert buscar_palabras(palabras_kata3, "Dumbledore") == []
assert buscar_palabras([], "e") == []
print("Kata 3 OK")


# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

# map() puede recibir varias listas: en cada paso toma un elemento de cada una (en la misma posición) y se los pasa juntos a la función. Por eso restar() tiene dos parámetros.
# Si las listas tienen distinta longitud, map() se detiene en la más corta sin avisar, así que lo compruebo antes y lanzo un error.

def restar(num1, num2):
    return num1 - num2


def diferencia_listas(lista1, lista2):
    if len(lista1) != len(lista2):
        raise ValueError("Las dos listas deben tener la misma longitud.")
    return list(map(restar, lista1, lista2))


minuendos_kata4 = [10, 8, 5, 3.5]
sustraendos_kata4 = [3, 8, 9, 1.5]

print(diferencia_listas(minuendos_kata4, sustraendos_kata4))   # [7, 0, -4, 2.0]

# Pruebas
assert diferencia_listas([7, 8, 9], [1, 2, 3]) == [6, 6, 6]
assert diferencia_listas(minuendos_kata4, sustraendos_kata4) == [7, 0, -4, 2.0]
assert diferencia_listas([], []) == []

try:
    diferencia_listas([1, 2, 3], [1])
    print("FALLO: debería lanzar ValueError")
except ValueError:
    pass   # es el comportamiento esperado

print("Kata 4 OK")



# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.


# nota_aprobado=5 es un parámetro con valor por defecto: si no se pasa, vale 5.
# Compruebo la lista vacía antes de dividir para evitar ZeroDivisionError.
# Comparo con la media sin redondear y la redondeo solo al devolverla, para que un 4.996 no apruebe por el redondeo.
# "return media, estado" devuelve una tupla aunque no lleve paréntesis.


def calcular_aprobado(lista, nota_aprobado=5):
    if len(lista) == 0:
        raise ValueError("La lista de notas está vacía.")

    media = sum(lista) / len(lista)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return round(media, 2), estado


notas_kata5 = [7.5, 3, 9, 4.5]

print(calcular_aprobado(notas_kata5))      # (6.0, 'aprobado')
print(calcular_aprobado(notas_kata5, 7))   # (6.0, 'suspenso')

media_kata5, estado_kata5 = calcular_aprobado([7, 8, 8])   # desempaquetado de la tupla
print(f"Media: {media_kata5} - Estado: {estado_kata5}")    # Media: 7.67 - Estado: aprobado

# Pruebas
assert calcular_aprobado(notas_kata5) == (6.0, "aprobado")    # caso normal
assert calcular_aprobado([7, 7], 7) == (7.0, "aprobado")      # nota_aprobado personalizada y límite exacto

try:
    calcular_aprobado([])
    print("FALLO: debería lanzar ValueError")
except ValueError:
    pass   # lista vacía: es el comportamiento esperado

print("Kata 5 OK")



# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

# Caso base: 0! y 1! valen 1, y ahí la función deja de llamarse a sí misma.
# Valido la entrada porque con negativos o decimales nunca se alcanza el caso base y Python acaba lanzando RecursionError.


def factorial(n):
    if type(n) != int or n < 0:
        raise ValueError("El factorial solo existe para enteros no negativos.")

    if n <= 1:
        return 1                        # caso base
    return n * factorial(n - 1)         # caso recursivo


print(factorial(6))   # 720

# Pruebas
assert factorial(6) == 720    # caso normal
assert factorial(0) == 1      # caso base

try:
    factorial(-3)
    print("FALLO: debería lanzar ValueError")
except ValueError:
    pass   # negativo: es el comportamiento esperado

print("Kata 6 OK")



# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

# Uso join() en lugar de tupla[0] y tupla[1] para que funcione con tuplas de cualquier longitud. map(str, tupla) convierte antes cada elemento a texto, porque join() solo acepta strings.

def tuplas_a_strings(lista):
    return list(map(lambda tupla: " - ".join(map(str, tupla)), lista))


# (número de empleado, nombre, cargo/s)
empleados_kata7 = [
    (101, "Lucía Pérez", "Directora financiera"),
    (102, "Marcos Rey", "Desarrollador", "Jefe de equipo"),
    (103, "Irene Soto"),                                   
]
print(tuplas_a_strings(empleados_kata7))
# ['101 - Lucía Pérez - Directora financiera', '102 - Marcos Rey - Desarrollador - Jefe de equipo', '103 - Irene Soto']

# Pruebas
assert tuplas_a_strings(empleados_kata7) == [
    "101 - Lucía Pérez - Directora financiera",
    "102 - Marcos Rey - Desarrollador - Jefe de equipo",
    "103 - Irene Soto",
]                                         
assert tuplas_a_strings([]) == []         # lista vacía
print("Kata 7 OK")



# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.

# Separo la lógica (dividir) de la interacción con el usuario (pedir_y_dividir) para poder probar la lógica con assert sin tener que escribir por teclado.
# El else solo se ejecuta si el try termina sin errores.


def dividir(texto1, texto2):
    try:
        resultado = float(texto1) / float(texto2)
    except ValueError:
        return "División fallida: debes introducir valores numéricos."
    except ZeroDivisionError:
        return "División fallida: no se puede dividir entre cero."
    else:
        return f"División exitosa. El resultado es: {round(resultado, 2)}"


def pedir_y_dividir():
    numero1 = input("Introduce el primer número: ")
    numero2 = input("Introduce el segundo número: ")
    print(dividir(numero1, numero2))

print(dividir("78", "6"))   # ejemplo de comprobación

# Pruebas
assert dividir("15", "4") == "División exitosa. El resultado es: 3.75"         # caso normal
assert dividir("siete", "2") == "División fallida: debes introducir valores numéricos."   # no numérico
assert dividir("7", "0") == "División fallida: no se puede dividir entre cero."          # entre cero
print("Kata 8 OK")



# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

# Guardo las prohibidas en minúsculas y en un set: in es más rápido en un set y comparar en minúsculas evita que "tigre" o "TIGRE" pasen el filtro.
# filter() se queda solo con los elementos para los que es_permitida() devuelve True.

mascotas_prohibidas_kata9 = {"mapache", "tigre", "serpiente pitón", "cocodrilo", "oso"}


def es_permitida(mascota):
    return mascota.lower() not in mascotas_prohibidas_kata9


def filtrar_permitidas(lista):
    return list(filter(es_permitida, lista))


mascotas_kata9 = ["Hurón", "tigre", "Loro", "Oso", "Tortuga", "SERPIENTE PITÓN"]
print(filtrar_permitidas(mascotas_kata9))   # ['Hurón', 'Loro', 'Tortuga']

# Pruebas
assert filtrar_permitidas(mascotas_kata9) == ["Hurón", "Loro", "Tortuga"]       # mayúsculas mezcladas
assert filtrar_permitidas(["Cocodrilo", "Mapache"]) == []                      # todas prohibidas
assert filtrar_permitidas([]) == []                                            # lista vacía
print("Kata 9 OK")



# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

# ListaVaciaError hereda de Exception, por eso se puede lanzar con raise y capturar con except.
# Compruebo con len(lista) == 0 si la lista está vacía antes de dividir.


class ListaVaciaError(Exception):
    """Se lanza cuando se intenta calcular el promedio de una lista vacía."""
    pass


def calcular_promedio(lista):
    if len(lista) == 0:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")
    return sum(lista) / len(lista)


numeros_kata10 = [8, 6.5, 9, 7.5]

# Manejo del error: la función se llama dentro de try y el except captura la excepción
for lista in (numeros_kata10, []):
    try:
        print("El promedio es:", calcular_promedio(lista))
    except ListaVaciaError as e:
        print("Error:", e)
# El promedio es: 7.75
# Error: No se puede calcular el promedio de una lista vacía.

# Pruebas
assert calcular_promedio(numeros_kata10) == 7.75     # caso normal

try:
    calcular_promedio([])
    print("FALLO: debería lanzar ListaVaciaError")
except ListaVaciaError:
    pass   # lista vacía: es el comportamiento esperado

print("Kata 10 OK")



# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

# Los dos errores se tratan como excepciones: int() lanza ValueError si el texto no es un número entero, y yo lanzo EdadFueraDeRangoError si está fuera de 0-120.
# Separo la validación (validar_edad) de la interacción (pedir_edad) para poder probarla con assert.


class EdadFueraDeRangoError(Exception):
    """Se lanza cuando la edad no está entre 0 y 120."""
    pass


def validar_edad(texto):
    edad = int(texto)   # lanza ValueError si no es un número entero
    if edad < 0 or edad > 120:
        raise EdadFueraDeRangoError(f"{edad} no es una edad válida: debe estar entre 0 y 120.")
    return edad


def pedir_edad():
    try:
        edad = validar_edad(input("Introduce tu edad: "))
    except ValueError:
        print("Error: debes introducir un número entero.")
    except EdadFueraDeRangoError as e:
        print("Error:", e)
    else:
        print(f"Tu edad es: {edad}")

print("Edad válida:", validar_edad("38"))   # Edad válida: 38

# Ejemplos: simulan lo que escribiría el usuario
for entrada in ("42", "-5", "cuarenta"):
    try:
        print("Edad válida:", validar_edad(entrada))
    except ValueError:
        print(f"'{entrada}' no es un número entero.")
    except EdadFueraDeRangoError as e:
        print("Error:", e)
# Edad válida: 42
# Error: -5 no es una edad válida: debe estar entre 0 y 120.
# 'cuarenta' no es un número entero.

# Pruebas
assert validar_edad("42") == 42                           # caso normal

try:
    validar_edad("150")
    print("FALLO: debería lanzar EdadFueraDeRangoError")
except EdadFueraDeRangoError:
    pass                                                  # fuera de rango

try:
    validar_edad("cuarenta")
    print("FALLO: debería lanzar ValueError")
except ValueError:
    pass                                                  # no numérico

print("Kata 11 OK")


# 12. Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

# split() divide la frase en palabras por los espacios.
# Con strip() quito los signos de puntuación de los extremos de cada palabra, para que por ejemplo "hola," mida 4 y no 5.


def longitudes_palabras(frase):
    palabras = frase.split()
    return list(map(lambda palabra: len(palabra.strip(".,;:¡!¿?")), palabras))


frase_kata12 = "Hola, esta frase es una prueba"
print(longitudes_palabras(frase_kata12))   # [4, 4, 5, 2, 3, 6]

# Pruebas
assert longitudes_palabras("¿Qué tal, Ana?") == [3, 3, 3]     # ignora la puntuación
assert longitudes_palabras("uno   dos") == [3, 3]              # espacios múltiples
assert longitudes_palabras("") == []                           # frase vacía
print("Kata 12 OK")


# 13. Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

# Paso cada carácter a minúsculas antes de crear el set: así "A" y "a" cuentan como una sola letra y no se repiten. sorted() da siempre el mismo orden, porque un set no tiene orden.


def mayus_minus(letra):
    return (letra.upper(), letra.lower())


def generar_tuplas(caracteres):
    letras_unicas = set(map(lambda c: c.lower(), caracteres))
    return list(map(mayus_minus, sorted(letras_unicas)))


caracteres_kata13 = {"x", "Q", "q", "m"}
print(generar_tuplas(caracteres_kata13))   # [('M', 'm'), ('Q', 'q'), ('X', 'x')]

# Pruebas
assert generar_tuplas({"x", "Q", "q", "m"}) == [("M", "m"), ("Q", "q"), ("X", "x")]   # "Q" y "q" una sola vez
assert generar_tuplas("banana") == [("A", "a"), ("B", "b"), ("N", "n")]               # también con un string
assert generar_tuplas(set()) == []                                                    # conjunto vacío
print("Kata 13 OK")



# 14. Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

# palabra[:1] da la primera letra (y "" si la palabra está vacía, sin error, a diferencia de palabra[0]).
# Comparo en minúsculas para que "r" encuentre también las palabras que empiezan por "R".


def palabras_que_empiezan(lista, letra):
    return list(filter(lambda palabra: palabra[:1].lower() == letra.lower(), lista))


# Regiones de la Tierra Media
regiones_kata14 = ["Mordor", "rohan", "Moria", "Gondor", "Rivendel", "Isengard"]
print(palabras_que_empiezan(regiones_kata14, "m"))   # ['Mordor', 'Moria']

# Pruebas
assert palabras_que_empiezan(regiones_kata14, "R") == ["rohan", "Rivendel"]   # sin distinguir mayúsculas
assert palabras_que_empiezan(regiones_kata14, "z") == []                      # ninguna coincide
assert palabras_que_empiezan(["", "Lothlórien"], "l") == ["Lothlórien"]       # palabra vacía sin error
print("Kata 14 OK")



# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

# La lambda recibe la lista completa y usa map() para sumar 3 a cada elemento, así se puede reutilizar con cualquier lista.

sumar_tres = lambda lista: list(map(lambda numero: numero + 3, lista))

numeros_kata15 = [-3, 0, 7.5, 100]
print(sumar_tres(numeros_kata15))   # [0, 3, 10.5, 103]

# Pruebas
assert sumar_tres(numeros_kata15) == [0, 3, 10.5, 103]   # negativos, cero y decimales
assert sumar_tres([]) == []                              # lista vacía
print("Kata 15 OK")



# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

# split() divide el texto en palabras por los espacios y filter() se queda con las que miden más de n.
# Uso > y no >= porque el enunciado pide palabras "más largas que n".

def palabras_largas(cadena, n):
    palabras = cadena.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))


texto_kata16 = "el cielo está enladrillado quién lo desenladrillará"
print(palabras_largas(texto_kata16, 5))   # ['enladrillado', 'desenladrillará']

# Pruebas
assert palabras_largas(texto_kata16, 4) == ["cielo", "enladrillado", "quién", "desenladrillará"]   # caso normal
assert palabras_largas(texto_kata16, 5) == ["enladrillado", "desenladrillará"]                     # 5 letras no es "más largo que 5"
assert palabras_largas("", 3) == []                                                                # texto vacío
print("Kata 16 OK")



# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().

# Multiplicar el acumulado por 10 desplaza el número una posición a la izquierda y deja hueco para el siguiente dígito: [5, 7, 2] → 5 → 57 → 572.

from functools import reduce


def combinar(acumulado, digito):
    return acumulado * 10 + digito


def numeros(lista):
    resultado = reduce(combinar, lista)
    return resultado


digitos_kata17 = [3, 0, 9, 1]
print(numeros(digitos_kata17))   # 3091

# Pruebas
assert numeros(digitos_kata17) == 3091   # caso normal, con un 0 en medio
assert numeros([0, 4, 2]) == 42          # el 0 inicial no cuenta, igual que al escribir 042
print("Kata 17 OK")



# 18. Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

# Cada estudiante es un diccionario. filter() pasa cada uno a mayor_nota(), que accede a su calificación por la clave y devuelve True si es 90 o más.

estudiantes_kata18 = [
    {"nombre": "Lucas", "edad": 21, "calificacion": 88},
    {"nombre": "Sofía", "edad": 19, "calificacion": 97},
    {"nombre": "Hugo", "edad": 23, "calificacion": 90},
    {"nombre": "Martina", "edad": 20, "calificacion": 89},
    {"nombre": "Leo", "edad": 22, "calificacion": 74},
]


def mayor_nota(estudiante):
    return estudiante["calificacion"] >= 90


estudiantes_destacados = list(filter(mayor_nota, estudiantes_kata18))
print(estudiantes_destacados)
# [{'nombre': 'Sofía', 'edad': 19, 'calificacion': 97}, {'nombre': 'Hugo', 'edad': 23, 'calificacion': 90}]

# Pruebas
assert [e["nombre"] for e in estudiantes_destacados] == ["Sofía", "Hugo"]   # 90 entra y 89 no
assert list(filter(mayor_nota, [])) == []                                   # lista vacía
print("Kata 18 OK")



# 19. Crea una función lambda que filtre los números impares de una lista dada.

# numero % 2 da 0 en los pares y 1 en los impares, así que "!= 0" es True solo para los impares.
# filter() se queda con los números para los que la lambda devuelve True.

numeros_kata19 = [-7, 0, 13, 22, 35, 48]

impares = list(filter(lambda numero: numero % 2 != 0, numeros_kata19))

print(impares)   # [-7, 13, 35]

# Pruebas
assert impares == [-7, 13, 35]                                          # incluye un negativo
assert list(filter(lambda numero: numero % 2 != 0, [2, 4, 6])) == []    # ningún impar
print("Kata 19 OK")



# 20. Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

# Uso isinstance para comprobar si un dato es de un tipo determinado (en este caso int).
# filter() se queda solo con los elementos para los que la lambda devuelve True.

elementos_kata20 = [3, "tres", 15, "quince", 0, "cero"]


def retorno_int(lista):
    numeros = list(filter(lambda x: isinstance(x, int), lista))
    return numeros


print(retorno_int(elementos_kata20))   # [3, 15, 0]

# Pruebas
assert retorno_int(elementos_kata20) == [3, 15, 0]    # caso normal, incluido el 0
assert retorno_int(["solo", "texto"]) == []           # ningún entero
print("Kata 20 OK")


# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.

# La lambda eleva el número al cubo con el operador ** y la función cubo() la llama con el número recibido.


def cubo(numero):
    calcular = lambda x: x ** 3
    return calcular(numero)


print(cubo(-2))    # -8

# Pruebas
assert cubo(-2) == -8       # negativo: el cubo conserva el signo
assert cubo(1.5) == 3.375   # decimal
print("Kata 21 OK")



# 22. Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

# reduce() recorre la lista multiplicando: x = 1, y = 2 → 1 * 2 = 2; luego 2 * 3 = 6...
# Cuando no quedan más números, devuelve el resultado acumulado.

from functools import reduce

numeros_kata22 = [3, 5, 2, 4]


def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)


print(producto_total(numeros_kata22))   # 120

# Pruebas
assert producto_total(numeros_kata22) == 120    # 3 * 5 * 2 * 4
assert producto_total([7, 0, 9]) == 0           # cualquier 0 anula el producto
print("Kata 22 OK")



# 23. Concatena una lista de palabras. Usa la función reduce().

from functools import reduce

palabras_kata23 = ["Más", "vale", "tarde", "que", "nunca"]


def concatenar(lista):
    return reduce(lambda x, y: x + " " + y, lista)


print(concatenar(palabras_kata23))   # Más vale tarde que nunca

# Pruebas
assert concatenar(palabras_kata23) == "Más vale tarde que nunca"   # caso normal
assert concatenar(["Hola"]) == "Hola"                              # una sola palabra: sin espacios extra
print("Kata 23 OK")



# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

from functools import reduce

restas_kata24 = [100, 25, 10, 5]  


def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)


print(diferencia_total(restas_kata24))   # 60

# Pruebas
assert diferencia_total(restas_kata24) == 60    # caso normal
assert diferencia_total([10, 30]) == -20        # el resultado puede ser negativo
print("Kata 24 OK")


# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

# La cadena llega como parámetro. len() cuenta todos los caracteres: letras, espacios y signos.

def caracteres_cadena(frase):
    return len(frase)

frase_kata25 = "Un vaso es un vaso y un plato es un plato."
print(caracteres_cadena(frase_kata25))   # 42

# Pruebas
assert caracteres_cadena(frase_kata25) == 42   # cuenta también espacios y signos
assert caracteres_cadena("") == 0              # cadena vacía
print("Kata 25 OK")



# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

# La lambda calcula el resto con el operador %. Los dos números llegan en una lista: lista[0] es el dividendo y lista[1] el divisor.

numeros_kata26 = [47, 5]


def division_numeros(lista):
    resto = lambda x, y: x % y
    return resto(lista[0], lista[1])


print(division_numeros(numeros_kata26))   # 2

# Pruebas
assert division_numeros(numeros_kata26) == 2    # 47 = 5 * 9 + 2
assert division_numeros([20, 4]) == 0           # división exacta: resto 0
print("Kata 26 OK")



# 27. Crea una función que calcule el promedio de una lista de números.

promedio_kata27 = [14, 18, 16, 20]


def promedio_lista(lista):
    suma = sum(lista)
    cantidad = len(lista)
    return suma / cantidad


print(promedio_lista(promedio_kata27))   # 17.0

# Pruebas
assert promedio_lista(promedio_kata27) == 17.0   # caso normal
assert promedio_lista([1, 2]) == 1.5                 # resultado con decimales
print("Kata 27 OK")



# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

dias_kata28 = ["lunes", "martes", "miércoles", "martes", "lunes"]


def primer_duplicado(lista):
    vistos = []

    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.append(elemento)

    return "No hay duplicados"


print(primer_duplicado(dias_kata28))   # martes

# Pruebas
assert primer_duplicado(dias_kata28) == "martes"               # "martes" se repite antes que "lunes"
assert primer_duplicado([1, 2, 3]) == "No hay duplicados"      # sin repetidos
print("Kata 28 OK")



# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

def enmascarar(variable):
    texto = str(variable)

    if len(texto) <= 4:
        return texto

    return "#" * (len(texto) - 4) + texto[-4:]


print(enmascarar(4539123456781234))   # ############1234

# Pruebas
assert enmascarar(4539123456781234) == "############1234"   # número: se convierte a texto
assert enmascarar("Hola") == "Hola"                          # 4 caracteres: no se oculta nada
print("Kata 29 OK")



# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.


def es_anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")

    return sorted(palabra1) == sorted(palabra2)


print(es_anagrama("Saco", "cosa"))   # True

# Pruebas
assert es_anagrama("Delira", "lidera") is True    # mismas letras, sin distinguir mayúsculas
assert es_anagrama("pato", "tapa") is False       # distintas letras
print("Kata 30 OK")



# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.


def buscar_nombre():
    nombres = input("Introduce los nombres: ").lower().split()
    nombre_buscado = input("Introduce el nombre que quieres buscar: ").lower()

    if nombre_buscado in nombres:
        print(f"El nombre '{nombre_buscado}' fue encontrado en la lista.")
    else:
        raise Exception(f"El nombre '{nombre_buscado}' no se encuentra en la lista.")


print("expecto" in "Expecto Patronum".lower().split())   # True
print("accio" in "Expecto Patronum".lower().split())   # False


# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.


empleados_kata32 = [
    {"nombre": "Michael", "apellido": "Scott", "profesion": "Director regional"},
    {"nombre": "Dwight", "apellido": "Schrute", "profesion": "Ayudante del director regional"},
    {"nombre": "Jim", "apellido": "Halpert", "profesion": "Vendedor"},
    {"nombre": "Pam", "apellido": "Beesly", "profesion": "Recepcionista"},
    {"nombre": "Kevin", "apellido": "Malone", "profesion": "Contable"},
]


def buscar_empleado(nombre_completo, empleados):
    nombre_completo = nombre_completo.lower()

    for empleado in empleados:
        nombre = empleado["nombre"].lower()
        apellido = empleado["apellido"].lower()

        nombre_empleado = nombre + " " + apellido

        if nombre_empleado == nombre_completo:
            return f"{empleado['nombre']} trabaja como {empleado['profesion']}"

    return "Esta persona no trabaja aquí."


print(buscar_empleado("Michael Scott", empleados_kata32))   # Michael trabaja como Director regional

# Pruebas
assert buscar_empleado("dwight schrute", empleados_kata32) == "Dwight trabaja como Ayudante del director regional"   # sin distinguir mayúsculas
assert buscar_empleado("Ron Swanson", empleados_kata32) == "Esta persona no trabaja aquí."                          # no está en la lista
print("Kata 32 OK")



# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista1_kata33 = [10, 20, 30]
lista2_kata33 = [4, 7, 15]


def suma(lista1, lista2):
    sumas = lambda x, y: x + y

    resultado = []

    for x, y in zip(lista1, lista2):
        resultado.append(sumas(x, y))

    return resultado


print(suma(lista1_kata33, lista2_kata33))   # [14, 27, 45]

# Pruebas
assert suma(lista1_kata33, lista2_kata33) == [14, 27, 45]   # caso normal
assert suma([], []) == []                                   # listas vacías
print("Kata 33 OK")



# 34. Crea la clase Arbol
# Define un árbol genérico con un tronco y ramas como atributos.
# Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
# Código a seguir:
# Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# Implementar el método quitar_rama para eliminar una rama en una posición específica.
# Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.
# Caso de uso:
#   a. Crear un árbol.
#   b. Hacer crecer el tronco una unidad.
#   c. Añadir una nueva rama.
#   d. Hacer crecer todas las ramas una unidad.
#   e. Añadir dos nuevas ramas.
#   f. Retirar la rama situada en la posición 2.
#   g. Obtener información sobre el árbol.


class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    def quitar_rama(self, posicion):
        self.ramas.pop(posicion)

    def info_arbol(self):
        return f"Longitud del tronco: {self.tronco}, número de ramas: {len(self.ramas)}, longitudes de ramas: {self.ramas}"


arbol = Arbol()             # a. Crear un árbol
arbol.crecer_tronco()       # b. Hacer crecer el tronco una unidad
arbol.nueva_rama()          # c. Añadir una nueva rama             → [1]
arbol.crecer_ramas()        # d. Hacer crecer todas las ramas      → [2]
arbol.nueva_rama()          # e. Añadir dos nuevas ramas           → [2, 1, 1]
arbol.nueva_rama()
arbol.quitar_rama(2)        # f. Retirar la rama en la posición 2  → [2, 1]

print(arbol.info_arbol())   # g. Longitud del tronco: 2, número de ramas: 2, longitudes de ramas: [2, 1]

# Pruebas
assert arbol.tronco == 2 and arbol.ramas == [2, 1]                   # estado final del caso de uso
assert Arbol().info_arbol() == "Longitud del tronco: 1, número de ramas: 0, longitudes de ramas: []"   # árbol recién creado
print("Kata 34 OK")


# 35. Crea la clase UsuarioBanco
# Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
# Código a seguir:
# Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
# Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
# Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
# Implementar agregar_dinero para aumentar el saldo del usuario.
# Caso de uso:
#   a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#   b. Agregar 20 unidades al saldo de Bob.
#   c. Transferir 80 unidades de Bob a Alicia.
#   d. Retirar 50 unidades del saldo de Alicia.

# transferir_dinero recibe el dinero "desde otro usuario": sale de otro_usuario y entra en self. Por eso "transferir de Bob a Alicia" se escribe alicia.transferir_dinero(bob, 80).
# Si no hay saldo suficiente se lanza ValueError antes de tocar ningún saldo.


class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No hay saldo suficiente para sacar esa cantidad.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene saldo suficiente para transferir.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad


# a. Creo los usuarios de Alicia y Bob
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

print(f"El saldo inicial de Alicia es: {alicia.saldo}")
print(f"El saldo inicial de Bob es: {bob.saldo}")

# b. Agrego 20 unidades al saldo de Bob
bob.agregar_dinero(20)
print(f"El saldo de Bob después de agregar 20 es: {bob.saldo}")

# c. Transferir 80 unidades de Bob a Alicia
# Con los datos del enunciado, Bob solo tiene 70 (50 + 20) después del paso b, por lo que no tiene
# saldo suficiente para transferir 80. Esto provoca que salte el ValueError de transferir_dinero().
# Uso try/except para capturar este error y que el programa no se detenga.
try:
    alicia.transferir_dinero(bob, 80)
    print(f"El saldo de Bob tras transferir 80: {bob.saldo}")
    print(f"El saldo de Alicia tras recibir 80: {alicia.saldo}")
except ValueError as e:
    print("Error al transferir:", e)

# d. Retirar 50 unidades del saldo de Alicia
try:
    alicia.retirar_dinero(50)
    print(f"El saldo de Alicia tras retirar 50: {alicia.saldo}")
except ValueError as e:
    print("Error al retirar:", e)

# Pruebas
assert alicia.saldo == 50 and bob.saldo == 70     # la transferencia falló y ningún saldo cambió

carla = UsuarioBanco("Carla", 30, True)
david = UsuarioBanco("David", 200, True)
carla.transferir_dinero(david, 120)
assert carla.saldo == 150 and david.saldo == 80    # transferencia con saldo suficiente: David paga, Carla recibe
print("Kata 35 OK")



# 36. Crea una función llamada procesar_texto
# Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
# Código a seguir:
# Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
# Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
# Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
# Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
# Caso de uso:
# Verificar el funcionamiento completo de procesar_texto.


def contar_palabras(texto):
    palabras = texto.split()
    contador = {}

    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    return contador


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra]
    return " ".join(palabras_filtradas)


def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")


texto_kata36 = "me gusta el café y me gusta el té"

print("Contar palabras:", procesar_texto(texto_kata36, "contar"))
# Contar palabras: {'me': 2, 'gusta': 2, 'el': 2, 'café': 1, 'y': 1, 'té': 1}
print("Reemplazar palabra:", procesar_texto(texto_kata36, "reemplazar", "café", "chocolate"))
# Reemplazar palabra: me gusta el chocolate y me gusta el té
print("Eliminar palabra:", procesar_texto(texto_kata36, "eliminar", "me"))
# Eliminar palabra: gusta el café y gusta el té

# Pruebas
assert procesar_texto(texto_kata36, "contar")["gusta"] == 2                                                     # contar
assert procesar_texto(texto_kata36, "reemplazar", "café", "chocolate") == "me gusta el chocolate y me gusta el té"   # reemplazar
assert procesar_texto(texto_kata36, "eliminar", "me") == "gusta el café y gusta el té"                          # eliminar
print("Kata 36 OK")



# 37. Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.

# Tramos elegidos: 0-5 noche, 6-11 día (mañana), 12-19 tarde, 20-23 noche.


def indicar_momento_dia():
    try:
        hora = int(input("Introduce la hora (0-23): "))

        if hora < 0 or hora > 23:
            print("Error: la hora debe estar entre 0 y 23.")
        elif hora >= 0 and hora < 6:
            print("Es de noche.")
        elif hora >= 6 and hora < 12:
            print("Es de día (mañana).")
        elif hora >= 12 and hora < 20:
            print("Es de tarde.")
        else:
            print("Es de noche.")

    except ValueError:
        print("Error: debes introducir un número válido.")


# Ejemplo de la lógica de la función con una hora fija (sin input)
hora_kata37 = 15
if hora_kata37 >= 12 and hora_kata37 < 20:
    print(f"A las {hora_kata37} h es de tarde.")   # A las 15 h es de tarde.



# 38. Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
# Reglas:
#   0 - 69: insuficiente
#   70 - 79: bien
#   80 - 89: muy bien
#   90 - 100: excelente

def calificacion_texto():
    try:
        nota = int(input("Introduce tu nota (0-100): "))

        if nota < 0 or nota > 100:
            print("Error: la nota debe estar entre 0 y 100.")
        elif nota >= 0 and nota <= 69:
            print("Insuficiente.")
        elif nota > 69 and nota <= 79:
            print("Bien.")
        elif nota >= 80 and nota <= 89:
            print("Muy bien.")
        else:
            print("Excelente.")

    except ValueError:
        print("Error: debes introducir un número válido.")


# Ejemplo de la lógica de la función con una nota fija (sin input)
nota_kata38 = 84
if nota_kata38 >= 80 and nota_kata38 <= 89:
    print(f"Con un {nota_kata38}, la calificación es: Muy bien.")   # Con un 84, la calificación es: Muy bien.


# 39. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

# Rectángulo: área = base × altura
# Círculo: área = π × radio²
# Triángulo: área = (base × altura) / 2
# Desempaqueto la tupla datos en las variables de cada fórmula. Importo math para usar el valor de π.
# Para el círculo la tupla lleva un solo elemento, por eso se escribe con coma: (radio,).

import math


def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        radio = datos[0]
        return math.pi * radio ** 2

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    else:
        raise ValueError("Figura no válida. Usa 'rectangulo', 'circulo' o 'triangulo'.")


print(calcular_area("rectangulo", (7, 2)))    # 14
print(calcular_area("circulo", (1,)))         # 3.141592653589793
print(calcular_area("triangulo", (10, 3)))    # 15.0

# Pruebas
assert calcular_area("rectangulo", (7, 2)) == 14                # rectángulo
assert round(calcular_area("circulo", (1,)), 2) == 3.14         # círculo: redondeo porque π tiene infinitos decimales
assert calcular_area("triangulo", (10, 3)) == 15.0              # triángulo
print("Kata 39 OK")


# 40. Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
#   a. Solicitar al usuario el precio original de un artículo.
#   b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
#   c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
#   d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
#   e. Mostrar el precio final de la compra, considerando o no el descuento.
#   f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.

# El cupón es un importe fijo en euros (no un porcentaje). Si es mayor que el precio, el precio final se queda en 0 para que no salga negativo.
# Acepto "sí" con y sin tilde; cualquier otra respuesta se trata como "no".
# Prueba manual (con python -i katas_python.py y llamando a calcular_compra()):
#   precio 50, "si", cupón 15  → "El precio final de tu compra es: 35.0€"
#   precio 50, "no"            → "El precio final de tu compra es: 50.0€"
#   precio 50, "sí", cupón 0   → "El cupón no es válido..." y precio final 50.0€
#   precio 20, "si", cupón 30  → precio final 0€
#   precio "abc"               → "Error: debes introducir valores numéricos válidos."


def calcular_compra():
    try:
        # a. Solicitar el precio original
        precio_original = float(input("Introduce el precio original del artículo: "))

        # b. Preguntar si tiene cupón de descuento
        tiene_cupon = input("¿Tienes un cupón de descuento? (si/no): ").lower()

        if tiene_cupon == "sí" or tiene_cupon == "si":
            # c. Solicitar el valor del cupón
            valor_cupon = float(input("Introduce el valor del cupón de descuento: "))

            # d. Aplicar el descuento si el cupón es válido
            if valor_cupon > 0:
                precio_final = precio_original - valor_cupon

                # Para evitar que el precio final sea negativo
                if precio_final < 0:
                    precio_final = 0

                print(f"Se ha aplicado un descuento de {valor_cupon}€.")
            else:
                print("El cupón no es válido. No se aplicará ningún descuento.")
                precio_final = precio_original

        elif tiene_cupon == "no":
            precio_final = precio_original

        else:
            print("Respuesta no válida. Se asume que no tienes cupón.")
            precio_final = precio_original

        # e. Mostrar el precio final
        print(f"El precio final de tu compra es: {precio_final}€")

    except ValueError:
        print("Error: debes introducir valores numéricos válidos.")


# Ejemplo de la lógica de la función con datos fijos (sin input)
precio_kata40 = 60
cupon_kata40 = 15
if cupon_kata40 > 0:
    precio_final_kata40 = precio_kata40 - cupon_kata40
    print(f"Precio: {precio_kata40}€ - Cupón: {cupon_kata40}€ - Precio final: {precio_final_kata40}€")
    # Precio: 60€ - Cupón: 15€ - Precio final: 45€