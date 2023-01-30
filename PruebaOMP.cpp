// Por: JESUS ESTEINER ALONSO MORNEO
// Código: A01793554
// 
// COMPUTO EN LA NUBE
// Maestría en Inteligencia Artificial Aplicada MNA
//
// TAREA 1: PROGRAMACION DE UNA SOLUCION PARALELA

// Llamado de las librerías
// en especial, OMP.H ya configurada e instalada que nos permita 
// utilizar las funciones de la librería OpenMP.
#include <iostream>
#include <omp.h>
#include <cstdlib>


// Definimos unas variables constantes que nos ayudarán a "jugar"
// parametrizar los datos que utilizaremos en el proceso de 
// paralelización.
#define N 1000
#define chunk 100
#define mostrar 10

// función que nos permite imprimir los primeros "mostrar" elementos
// de los arreglos definidos.   
// N = Número de posiciones en cada uno de los arreglos, definiremos 3 arreglos
// llamados a, b, c

void imprimeArreglo(float* d);

int main()
{

    // Definición de los arreglos
    std::cout << "Sumando Arreglos en Paralelo!\n";
    float a[N], b[N], c[N];
    int i;

    // Ciclo FOR que permite el recorrido de los dos primeros
    // arreglos a y b, y al mismo tiempo vamos asignado unos 
    // valores a cada una de las posiciones utilizando la función
    // de generación de números random

    // Para el arreglo a, usamos la fórmula: El valor de i por un número aleatorio 
    // que es generado por la función rand() de c++

    // igualmente, asignamos el valor del valor de i, más 3, y multiplicamos 
    // por un valor aleatorio generado por el sistema.  Con esto, obtendremos los datos
    // aleatorio y las matrices llenas de a y b
    for (i = 0; i < N; i++)
    {
        a[i] = i * rand();
        b[i] = (i + 3) * rand();
    }
    
    // Se inicializa una variable entera, pedazos, que nos permite poder dividir en partes
    // y paralelizar la sumatoria de los valores contenidos en los arreglos a y b, resultado que
    // llevaremos al arreglo c mediante un FOR.

    // chunk fue definida como constante con un valor inicial de 150
    int pedazos = chunk;

    // El estándar OpenMP, API que expresa paralelismo multihilo en sistemas de memoria compartida
    // Componentes:

    // - Directivas #pragma de compilación
    //      - informan al compilador para optimizar código siguiente
    //
    //      #pragma omp <directiva> {<cláusula>}* <\n>
    //      
    //      funciones de la libreria
    //      variables de entorno
    //
    // De esta manera, un bucle es fácilmmente paralelizable en Openmp
    //
    // Reglas:
    //  - No dependencia entre iteraciones
    //  - Prohibidas instrucciones break, exit(), goto...
    //  - Forma CANÓNICA -> for (i=INICIO; i {>,<,>=,<=}, i++,i--,++i,--i
    //  - Una sola instrucción en un bloque
    //
    // Cláusulas utilizadas:
    //  - shared(a, b, c, pedazos) -> Especifica que las variables, a, b, c y pedazos
    //                                  deben compartirse entre todos los subprocesos.
    //  - private(i) -> Existe una copia de las variables i en el for para cada hilo, 
    //  -               es decir, Especifica que cada subproceso debe tener su propia 
    //  -               instancia de una variable.
    //  - schedule(static, pedazos) -> Cómo se distribuyen los hilos en cada trabajo,
    //      --> Se aplica a la directiva for.
    // 
    //      --> schedule(<tipo>[,<tamaño>])
    //      --> Para este caso, el uso del tipo <static> muestra las iteracciones
    //      --> contiguas por cada hilo, es decir, el valor chunk, 150 en nuestro caso.
    #pragma omp parallel for shared(a, b, c, pedazos) private(i) schedule(static, pedazos)

    // Recorrido de los arreglos, asignado la sumatoria de los arreglos a y b al arreglo c
    // en la misma posición
    for (i = 0; i < N; i++)
        c[i] = a[i] + b[i];

    // Impresión de resultados al llamar a la función imprimeArreglo pasándole como parámetro
    // el arreglo a imprimir, adicionalmente, usará el valor de la constante "mostrar" definida en
    // valor de 20, para que se pueda observar por pantalla los resultados de la suma
    std::cout << "Imprimiendo los primeros " << mostrar << " valores del arreglo a: " << std::endl;
    imprimeArreglo(a);

    std::cout << "Imprimiendo los primeros " << mostrar << " valores del arreglo b: " << std::endl;
    imprimeArreglo(b);

    std::cout << "Imprimiendo los primeros " << mostrar << " valores del arreglo c: " << std::endl;
    imprimeArreglo(c);
}

void imprimeArreglo(float* d)
{ 
    for (int x = 0; x < mostrar; x++)
        std::cout << d[x] << " - ";
    std::cout << std::endl;
}
