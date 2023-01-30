// Por: JESUS ESTEINER ALONSO MORNEO
// C�digo: A01793554
// 
// COMPUTO EN LA NUBE
// Maestr�a en Inteligencia Artificial Aplicada MNA
//
// TAREA 1: PROGRAMACION DE UNA SOLUCION PARALELA

// Llamado de las librer�as
// en especial, OMP.H ya configurada e instalada que nos permita 
// utilizar las funciones de la librer�a OpenMP.
#include <iostream>
#include <omp.h>
#include <cstdlib>


// Definimos unas variables constantes que nos ayudar�n a "jugar"
// parametrizar los datos que utilizaremos en el proceso de 
// paralelizaci�n.
#define N 1000
#define chunk 100
#define mostrar 10

// funci�n que nos permite imprimir los primeros "mostrar" elementos
// de los arreglos definidos.   
// N = N�mero de posiciones en cada uno de los arreglos, definiremos 3 arreglos
// llamados a, b, c

void imprimeArreglo(float* d);

int main()
{

    // Definici�n de los arreglos
    std::cout << "Sumando Arreglos en Paralelo!\n";
    float a[N], b[N], c[N];
    int i;

    // Ciclo FOR que permite el recorrido de los dos primeros
    // arreglos a y b, y al mismo tiempo vamos asignado unos 
    // valores a cada una de las posiciones utilizando la funci�n
    // de generaci�n de n�meros random

    // Para el arreglo a, usamos la f�rmula: El valor de i por un n�mero aleatorio 
    // que es generado por la funci�n rand() de c++

    // igualmente, asignamos el valor del valor de i, m�s 3, y multiplicamos 
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

    // El est�ndar OpenMP, API que expresa paralelismo multihilo en sistemas de memoria compartida
    // Componentes:

    // - Directivas #pragma de compilaci�n
    //      - informan al compilador para optimizar c�digo siguiente
    //
    //      #pragma omp <directiva> {<cl�usula>}* <\n>
    //      
    //      funciones de la libreria
    //      variables de entorno
    //
    // De esta manera, un bucle es f�cilmmente paralelizable en Openmp
    //
    // Reglas:
    //  - No dependencia entre iteraciones
    //  - Prohibidas instrucciones break, exit(), goto...
    //  - Forma CAN�NICA -> for (i=INICIO; i {>,<,>=,<=}, i++,i--,++i,--i
    //  - Una sola instrucci�n en un bloque
    //
    // Cl�usulas utilizadas:
    //  - shared(a, b, c, pedazos) -> Especifica que las variables, a, b, c y pedazos
    //                                  deben compartirse entre todos los subprocesos.
    //  - private(i) -> Existe una copia de las variables i en el for para cada hilo, 
    //  -               es decir, Especifica que cada subproceso debe tener su propia 
    //  -               instancia de una variable.
    //  - schedule(static, pedazos) -> C�mo se distribuyen los hilos en cada trabajo,
    //      --> Se aplica a la directiva for.
    // 
    //      --> schedule(<tipo>[,<tama�o>])
    //      --> Para este caso, el uso del tipo <static> muestra las iteracciones
    //      --> contiguas por cada hilo, es decir, el valor chunk, 150 en nuestro caso.
    #pragma omp parallel for shared(a, b, c, pedazos) private(i) schedule(static, pedazos)

    // Recorrido de los arreglos, asignado la sumatoria de los arreglos a y b al arreglo c
    // en la misma posici�n
    for (i = 0; i < N; i++)
        c[i] = a[i] + b[i];

    // Impresi�n de resultados al llamar a la funci�n imprimeArreglo pas�ndole como par�metro
    // el arreglo a imprimir, adicionalmente, usar� el valor de la constante "mostrar" definida en
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
