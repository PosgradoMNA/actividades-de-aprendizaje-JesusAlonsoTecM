# impresión de prueba
from ast import Try


print("Bienvenido a las pruebas de:\nJESUS ALONSO")

# enteros
var = 1
print("Valor Entero: ", var)
print(type(var))

# float
var = 1.67
print("Valor Float: ", var)
print(type(var))

# booleano
var = True
print("Valor Booleano: ", var)
print(type(var))

# variables -> multiplicación prioridad
var = 5 + 5 + 5 * 2
print("Prioridad MULT [5 + 5 + 5 * 2] = ", var)

# Encontrando los primeros 4 caracteres
var = "abcdefghijkl"
print("En el string", var, "los primeros 4 caracteres son: ", var[0:4])
print("Cadena original min:", var, "cadena convertida a may UPPER()", var.upper())

# Concatenar, strings
var = var + "-mnopqrstuvwxyz"
print("Todo el abcedario sumando dos strings en var: ", var)

# Hablemos ahora de Tuples
# se inicializan usando los paréntesis ()
My_tuple_1 = (10,9,6,5,10,8,9,6,2)
My_tuple_2 = ("PrimerElemento", 10, 1.5, "CuartoElemento")

print("Ambos deben ser tipo [tuple]:")
print(type(My_tuple_1))
print(type(My_tuple_2))

# Concatenar dos elementos de un tuple
print("Elemento 1:")
print(My_tuple_1[0])
print("Elemento 2: ")
print(My_tuple_1[1])
print("=Resultado: ")
print( My_tuple_1[0] + My_tuple_1[1] )

# Esto es emocionante, negative index
print(My_tuple_2[-4])  # --> "PrimerElemento"

# operaciones con Tuples son posibles
# presta atención a la coma al final del "QuintoElemento",
# esto le indica que no es un string, sino que es una tuple
# lo que permite concatenarlos.

My_tuple_3 = My_tuple_2 + ("QuintoElemento",)
print(My_tuple_3)

print("Tuples son Inmutables, qué es eso?")
print("Si intentamos modificar un elemento será un error:")

# La intrucción Try/Except permite capturar el error
try:
    My_tuple_1[0] = 1  # Error!
except:
    print("Este mensaje dice indica que programar")
    print("VariableTuple[0] = 1")
    print("asignando un valor a un tuple, generará un error")


















