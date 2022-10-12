
print("########################################")
print("Bienvenido PYTHON FOR DATA SCIENCE (IBM)")
print("ALUMNO: JESUS ESTEINER ALONSO")
print("CODIGO: A1793554")
print("########################################")
print("MODULO 1, 2, 3, 4 - Ya CALIFICADOS checados")
print("MODULO 5:  Desarrollo al ejecutar y revisar el archivo")
print("MODULO 6: DATA ANALYSIS WITH PYTHON")

# checando modulo DATA ANALYSIS WITH PYTHON
# Le llamaré modulo 6

# Extraemos la librería numpy
import numpy as np
import pandas as pd
import os

modulo = 6
if modulo >= 6:
    # Importando Data 
    # # Cargamos el archivo que está en la siguiente carpeta de Google-Colab:
    misdatos = pd.read_csv("cereals.csv")
    
    # evidencia de manejo de datos para DATA SCIENCES

    ################### DETALLES DE MIS DATOS LEIDOS
    print(misdatos.describe())
    print(misdatos.info())
    print(misdatos.describe(include='all'))

    #################### CREANDO MI DATAFRAME
    df = pd.DataFrame(misdatos)
    print(df)

    #################### LIMPIANDO MIS DATOS
    df_cleaned = df.dropna(axis=0, inplace=True)
    print(df_cleaned)

    input("enter")

elif modulo >= 5:
    ##################### MODULO 5 - EVIDENCIA DE CURSO ################
    print("Modulo 5 - Evidencia")



    # Creeemos un arreglo 
    a = np.array([0,1,2,3,4])

    # Fomrato para acceder al arreglo usando numpy 
    # guardando en la variable a
    print("Indice 1:", a[0])
    print("Indice 2:", a[1])

    # Número de elementos del arreglo con numpy
    print("Número de elementos: ", a.size)

    # Podemos cambiar un elemento del arreglo direcctamente
    a[0] = 100
    print("Indice 1 con valor cambiado:", a[0])

    # Extraer ahora una parte del arreglo y generar uno nuevo
    b = a[1:4]
    print("Tenemos el arreglo original")
    print(a)
    print("Del cual extraimos tres datos:")
    print(b)
    
    ################ OPERACIONES CON LOS VECTORES NUMPY ##############
    # Tomemos los valores del primero y multiplicamos por 2 
    # todos los componentes.
    c = a*2
    print("Valores originales arreglo numpy a:", a)
    print("Valores guardados en variable c, a*2:", c)

    ############## FUNCIONES CON NUMPY ######################
    print("Promedio de datos del arreglo a:", a.mean())
    print("Máximo valor en el arreglo a:", a.max())
    print("Minimo valor en el arreglo a:", a.min())

    # funcion linspace numpy
    x = np.linspace(0, 2*np.pi,100)
    y = np.sin(x)

    # libreria en python para poder graficar 
    import matplotlib.pyplot as plt

    # Dibuje el seno de los datos en x
    plt.plot(x,y)

    # multiplicar arreglos
    d = np.array([1,-1])*np.array([1,1])
    print(d)

    # producto de dos arreglos
    d = np.dot(np.array([1,-1]),np.array([1,1]))
    print(d)

    ##################### MULTIDIMENSIONAL ARRAYS ##################
    a = [[1,2,3],[4,5,6],[7,8,9]]
    b = np.array(a)

    print("Arreglo 3x3 creado:")
    print(a)
    print("Dimension del arreglo anterior:",b.shape)

    #################### MULTIPLICACION DE MATRICES ###############
    A = np.array([[1,2],[3,4],[5,6],[7,8]])
    B = np.array([[1,2,3],[4,5,6],[7,8,9]])

    try:
        print(np.dot(B,A))
    except:
        print("ArrEglo A: [[1,2],[3,4],[5,6],[7,8]]")
        print("Arreglo B: [[1,2,3],[4,5,6],[7,8,9]]")
        print("Se intentó ejecutar esto: print(np.dot(B,A))")
        print("Error ocurrido pues no tienen la misma dimensión los arreglos")


    ######################## API interfaces.
    # Utilizando librerias API con PANDAS
    import pandas as pd

    dict_ = {'Nombres': ["JESUS", "ESTEINER", "ALONSO"],\
             'Edades': [37, 45, 67]}

    df = pd.DataFrame(dict_)

    # usando pandas podemos obtener los datos del dict
    # con la siguiente función
    print(df.head())

    ######################## REST Apis
    # Usemos un servidor de NBA usado en el ejemplo
    #
    # !IMPORTANTE! debe instalar desde comandos esta libreria
    # pues no se encuentre an el estándar de PYTHON
    #
    # pip install nba_api
    from nba_api.stats.static import teams
    nba_teams = teams.get_teams()
    
    # Datos recibidos del REST API
    print("Datos recibidos del API con formato JSON")
    print(nba_teams)

    # Para poder ver los datos ordenados a través de un frame
    # debemos hacer una función para transformar un JSON a DICT
    def one_dict(list_dict):
        keys=list_dict[0].keys()
        out_dict={key:[] for key in keys}

        for dict_ in list_dict:
            for key, value in dict_.items():
                out_dict[key].append(value)
        return out_dict

    # Llamemos la función y convirtamos el JSON en DICTIONARIO
    dict_nba_team=one_dict(nba_teams)
    df_teams=pd.DataFrame(dict_nba_team)
    
    # Imprimamos la lista recibida en dataframe ordenado 
    print(df_teams.head())


elif modulo >= 4:

    ##################### MODULO 4 - READING FILES WITH OPEN ############

    # La apertura de un archivo puede realizar con el comando 
    # open, pero este puede referirse de una mejor manera como 
    # objeto usando el comando with
    with open("hello.py", "r") as file1:
        
        # nombre del archivo leido
        print(file1.name)
        
        # cómo fue abierto el archivo, modo lectura, escritura
        print(file1.mode)

        # Si deseo immprimir solo línea específica
        Linea100 = file1.readlines(100)

        # imprimir linea 10
        print(Linea100)

        # ahora lea toda la info, estoy leyendo este
        # mismo archivo, con los datos que se están ejecutando
        # debería mostrar todo este código completo del texto
        FullFile = file1.read()

        # Ahora imprima exactamente este archivo que estas
        # leyendo
        print(FullFile)

    # cierre el archivo
    file1.close()
    
    # La siguiente linea creará un nuevo archivo llamado
    # Archivo CSV

    # Creemos dos lineas simulando un archivo CSV que una vez
    # creada, vamos a usar para el siguiente ejercicio con la libreria
    # PANDAS.
    with open("pandas.csv","w") as file2:
        
        # Creando un archivo CSV desde PYTHON,
        # este archivo lo usaremos para probar como leer archivo CSV
        # con la libreria PANDAS
        file2.write("Nombre, Id, Deuda\nJESUS ALONSO, A1793554, 20000")

    # cierre objeto, archivo
    file2.close()
    
    ####################################################
    ##### LECTURA DE ARCHIVOS USANDO LA LIBRERIA PANDAS
    ####################################################
    import pandas as pd
    
    # Leer el archivo con panda tipo CSV
    file3 = pd.read_csv("pandas.csv")

    ######################################################
    # imprimir información del archivo creado con este mismo
    # programa CSV
    print(file3.head())

    ############### Manejo y creacion de DATAFRAMS con PANDA
    df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
    
    # imprima el data fram y su contenido
    print(df.head())

    # Imprime si el primer valor del frame es igual a 1, True BOOL
    print(df['a'] == 1)

    # Podemos guardar el frame tipo CSV
    df.to_csv("DataFrame.csv")


else:
    ###################
    ### MODULO 1, 2, 3
    ###################

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

    ################## DICTIONARIOS ####################
    # De lo mejor, de lo mejor en python

    my_dict = {"Jesus": 1975, "Maria": 1976, "José": 1977}
    print(my_dict)

    # Operaciones: (Digamos, nombres y año de nacimiento)
    # Dame el valor de acuerdo al la key
    print("Cuál es el año de nacimiento de JESUS:")
    print(my_dict["Jesus"])

    # Dejame ver todas las keys
    print("Todas las llaves contenidas en el dict:")
    print(my_dict.keys())

    # Ahora los valores
    print("Dejame ver todos los valores en el dict:")
    print(my_dict.values())


    ################## COMPARISON OPERATORADORES
    a = 1
    b = 3
    if a == b:
        print(a, "es igual a ", b)
    else:
        print(a, "NO es igual a ", b)

    # ahora con otro operador y otro statment adicional
    if a > b:
        print(a, "es mayor que ", b)
    elif b > a and a < b:
        print(b, "es mayor que ", a, " y ", a, " es menor que ", b)
    elif a < b:
        print(a, "es menor que ", b)
    else:
        print( a, "es igual a ", b)
        
    ###################### CICLOS, LOOPS ##########################
    # usaremos las listas anteriormente definidas
    # imprimeindo los elementos de una lista con for 
    for cValue in my_list:
        print("imprimendo cada elemento", cValue)

    # usando el argumento de la función enumerate
    for i, cValue in enumerate(my_list):
        print("Este es el índice: ", i)
        print("Este es el valor usando indice: ", my_list[i])
        print("Este es el valor directo: ", cValue)

    # usando el while como loop
    # i contendrá el número de elementos
    i = len(my_list) - 1  # Restar 1 pues arranca el indice en 0, no en 1

    # ordenando la lista antes de imprimirla con la función sort
    my_list.sort()

    while i > 0:
        print("Imprimiendo con while lista de elementos: ", my_list[i])
        i-=1


