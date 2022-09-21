
print("Bienvenido a las pruebas de:\nJESUS ALONSO")

############# TYPOS DE DATOS ######################
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

############### OPERADORES ########################
# variables -> multiplicación prioridad
var = 5 + 5 + 5 * 2
print("Prioridad MULT [5 + 5 + 5 * 2] = ", var)

################ CADENAS, STRINGS ###########################
# Encontrando los primeros 4 caracteres
var = "abcdefghijkl"
print("En el string", var, "los primeros 4 caracteres son: ", var[0:4])
print("Cadena original min:", var, "cadena convertida a may UPPER()", var.upper())

################# VARIABLES ###########################
# Concatenar, strings
var = var + "-mnopqrstuvwxyz"
print("Todo el abcedario sumando dos strings en var: ", var)


################### TUPLAS ##########################
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


# ordenando los elementos de un tuple
print("Tuple original:", My_tuple_1)
print("Ahora, ordenada:")
print(sorted(My_tuple_1))

################# LISTAS ######################
# En las listas se usan los corchetes cerrados [] para su definición
# El acceso a los elementos es exactamente igual como lo hacíamos
# con las tuples, sin embargo, tenemos un par de comandos diferentes
my_list = ['JesusAlonso', 1975, "MNA", 2022]

# Puedo usar la misma operación que las tuplas para agregar
# más elementos, pero si la coma al final como en las tuplas, recuerdan?
my_list = my_list + ["QuintoElementoAdicionado"]
print(my_list)

# Otra forma es con el comando extend si deseo adicionar más
# elementos al mismo tiempo
my_list.extend(["SextoElemento", "SeptimoElemento"])
print(my_list)

# O en su defecto con el comando Append, pero solo adicionará
# un elemento más, ojo que puede adicionar una lista interna,
my_list.append(["Octavo1","Octavo2"])
print(my_list)

#### ERROR EN EL CURSO
#### POR CIERTO, Hay un error en la presentación del slide 26, 27
#### se refiere a que puede tomar una TUPLE 
#### y asignar un nuevo elemento a[0] = "Nuevo", es un error
#### en el título, pues esto funciona solo con LISTAS

# esto solo funciona con listas
my_list[0] = "MaverickAlonso"
print(my_list)

my_string = "1,2,3,4,5,6,7,8,9,10"
print(my_string)

# Fantastico el uso del comando split para convertir en elementos
# individuales}
my_list2 = my_string.split(",")
print(my_list2)

# obvie el elemento 1 y muestre los demas.
my_list3 = ["a","b","c"]
print(my_list3[1:])

############## SETS ####################
# Puedo convertir listas en SETS, y puedo realizar operaciones
# de union, intersección, y preguntar si es un subset de un set
# o no, así también, los SETS, no pueden ser modificados
# y tampoco habrán duplicados, aún así defina mismos elementos
# uso {} llaves para definir sets, parentesis para tuplas y
# [] para listas, remindder :) 

my_set = {"1","2","3","1","2","4"}
print(my_set)

# Convirtiendo my_list2 anterior en SET
my_set2 = set(my_list2)
print(my_set2)

# ya que tenemos números en los dos sets, hagamos intersercción
my_set3 = my_set & my_set2
print(my_set3)

# unión también, recuerda, solo quedarán los no repetidos
my_set3.union(my_set2)
print(my_set3)

# hace parte my_set3 sus elementos están en set?
print(my_set3.issubset(my_set))










