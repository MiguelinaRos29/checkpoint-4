import math
import decimal

  

# -------------------------------------------------------
# Exercise 1: Crear una lista, tupla, float, integer,
#             decimal y diccionario
# -------------------------------------------------------

mi_lista = ["banana", "manzana", "uva", "pera"]

mi_tupla = ("Python", "JavaScript", "Java", "C++")

mi_float = 25.7689

mi_integer = 42

mi_decimal = decimal.Decimal("3.14159")

mi_diccionario = {
    "nombre": "Miguelina",
    "edad": 22,
    "curso": "Python",
    "nivel": "Intermedio"
}

print("=" * 50)
print("EXERCISE 1 - Estructuras de datos creadas")
print("=" * 50)
print(f"Lista:        {mi_lista}")
print(f"Tupla:        {mi_tupla}")
print(f"Float:        {mi_float}")
print(f"Integer:      {mi_integer}")
print(f"Decimal:      {mi_decimal}")
print(f"Diccionario:  {mi_diccionario}")


# -------------------------------------------------------
# Exercise 2: Redondear el float hacia arriba
# math.ceil() siempre redondea hacia el número entero mayor
# -------------------------------------------------------

float_redondeado = math.ceil(mi_float)

print("\n" + "=" * 50)
print("EXERCISE 2 - Float redondeado hacia arriba")
print("=" * 50)
print(f"Float original:    {mi_float}")
print(f"Redondeado arriba: {float_redondeado}")


# -------------------------------------------------------
# Exercise 3: Obtener la raíz cuadrada del float
# math.sqrt() calcula la raíz cuadrada
# -------------------------------------------------------

raiz_cuadrada = math.sqrt(mi_float)

print("\n" + "=" * 50)
print("EXERCISE 3 - Raíz cuadrada del float")
print("=" * 50)
print(f"Float:          {mi_float}")
print(f"Raíz cuadrada:  {raiz_cuadrada:.4f}")


# -------------------------------------------------------
# Exercise 4: Seleccionar el primer elemento del diccionario
# Usamos list() para obtener las claves en orden y acceder
# al primer elemento con índice [0]
# -------------------------------------------------------

primera_clave = list(mi_diccionario.keys())[0]
primer_elemento = {primera_clave: mi_diccionario[primera_clave]}

print("\n" + "=" * 50)
print("EXERCISE 4 - Primer elemento del diccionario")
print("=" * 50)
print(f"Diccionario completo: {mi_diccionario}")
print(f"Primer elemento:      {primer_elemento}")


# -------------------------------------------------------
# Exercise 5: Seleccionar el segundo elemento de la tupla
# Los índices en Python empiezan en 0, por eso usamos [1]
# -------------------------------------------------------

segundo_elemento_tupla = mi_tupla[1]

print("\n" + "=" * 50)
print("EXERCISE 5 - Segundo elemento de la tupla")
print("=" * 50)
print(f"Tupla:             {mi_tupla}")
print(f"Segundo elemento:  {segundo_elemento_tupla}")


# -------------------------------------------------------
# Exercise 6: Agregar un elemento al final de la lista
# .append() agrega un elemento al final sin modificar el resto
# -------------------------------------------------------

mi_lista.append("mango")

print("\n" + "=" * 50)
print("EXERCISE 6 - Elemento agregado al final de la lista")
print("=" * 50)
print(f"Lista actualizada: {mi_lista}")


# -------------------------------------------------------
# Exercise 7: Reemplazar el primer elemento de la lista
# Accedemos al índice [0] y asignamos el nuevo valor
# -------------------------------------------------------

mi_lista[0] = "fresa"

print("\n" + "=" * 50)
print("EXERCISE 7 - Primer elemento reemplazado")
print("=" * 50)
print(f"Lista actualizada: {mi_lista}")


# -------------------------------------------------------
# Exercise 8: Ordenar la lista alfabéticamente
# .sort() ordena la lista en su lugar (modifica el original)
# -------------------------------------------------------

mi_lista.sort()

print("\n" + "=" * 50)
print("EXERCISE 8 - Lista ordenada alfabéticamente")
print("=" * 50)
print(f"Lista ordenada: {mi_lista}")


# -------------------------------------------------------
# Exercise 9: Usar reasignación para agregar un elemento
#             a la tupla
#
# Las tuplas son INMUTABLES, no se pueden modificar directamente.
# La solución es convertirla a lista, agregar el elemento,
# y luego volver a convertirla a tupla usando reasignación (+=).
# -------------------------------------------------------

print("\n" + "=" * 50)
print("EXERCISE 9 - Reasignación para agregar elemento a la tupla")
print("=" * 50)
print(f"Tupla original: {mi_tupla}")

mi_tupla += ("Swift",)   # El operador += reasigna la variable
                          # con una nueva tupla combinada

print(f"Tupla nueva:    {mi_tupla}")

print("\n ¡Todos los ejercicios completados con éxito!")
