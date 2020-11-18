# BiblioCAT :books:

## Introducción
Las libros nos permiten descubrir múndos de fantasia así como entender mejor el mundo en el que vivimos. Nos permiten aprender todo tipo de cosas, desde "Teo va a la escuela" a "Compilers: Principles, Techniques, and Tools".


Las librerias de Cataluña tienen un sistema de intercanvio de libros, de forma que, quando alguien se dirige a una biblioteca a buscar un libro para aprender a programar Haskell, y el/la bibliotecario/a le diga "I eso qué és?!?!?", haya la posibilidad de pedirle a otra biblioteca que tenga el libro que el/la valiente aspirante/a a aprender Haskell pedia.


## Especificaciones
* Lo que les gustaria a las bibliotecas és maximizar el tiempo en que los libros estan generando valor, es decir, el tiempo en que un libro esta en manos de algún usuario. *Cada libro genera un valor X. Se tendra maximizar teniendo en quenta el tiempo màximo T*
* Se ha de tener en cuenta, que mientras un libro esta siendo transportado este *NO* genera valor. 
* Dependiendo del lector, i el libro que vaia a leer (en funcion de si le gusta mas o menos), variarà el *tiempo T* en que se lee el libro.
* Si hay varias personas que quieren leer un libro, estas se añadiran a una lista de espera, i esperaran a recibir noticias de la biblioteca quando esté disponible.
* Una persona, como màximo, podra tener tres libros a la vez. *OJO: NO tres libros por biblioteca, tres libros en TOTAL*. 


## Input File
``` 
tiempo = "T", tiempo_global
biblioteca = "L", id, { % { tiempo transporte id j | j <- [ 0 .. id_max] }  % }
id = % numero unico por tipo %
tiempo transporte id j = % tiempo de tranporte de un libro desde la
              - libreria id hasta j
              %
libro = "B", id, id biblioteca, valor
valor = % numero %
lector = "R", id, id biblioteca, { id libro, tiempo lectura }
tiempo lectura = % numero de tiempo que se
                 - tarda en leer el libro id libro
                 %
```

Por ejemplo:
```
T 6
L 0 0 2 3
L 1 3 0 4
L 2 3 4 0
B 0 0 5
B 1 0 3
B 2 1 10
B 3 2 2
B 4 2 8
R 0 0 0 10 1 2
R 1 0 1 1 2 10 3 3
R 2 1 0 1 1 1 2 1 3 1 4 1
R 3 2 2 5 4 5
```

Vemos que el valor del tiempo T en el que se ha de realizar la optimización es de 
6.

En este ejemplo, hay tres bibliotecas (L), donde el coste de llevar un libro
de la biblioteca ''0'' hasta la ''1'' es de 2 i el coste de llevar
un libro de la biblioteca ''1'' hasta la ''0'' es de 3. Además, el coste de
llevar un libro de una biblioteca a si misma siempre es de 0.


En el caso de los libros (B),  el primer argumento es el id del libro, 
el segundo es el id de la biblioteca donde se encuentra
en el estado inicial, y el tercero es el valor que produce el libro en
ser leido por un lector.


Finalmente, se puede apreciar que el lector con id ``0'', que esta afiliado
a la biblioteca ''0'', quiere leer los libros ''0'' y ''1'', que tardará en
hacerlo ''10'' y ''2'' respectivamente.

## Output File
## Gramàtica:
```
mover libro = id libro, "m", id biblioteca
leer libro = id libro, "r", id lector
```


El orden de sentencias en el fichero importa.
Por ejemplo, dado el fichero inicial:
```
T 10
L 0 0
B 0 0 5
B 1 0 5
B 2 0 5
B 3 0 5
R 0 0 0 5 1 5 2 5 3 10
```

Con el output:
```
0 r 0
1 r 0
2 r 0
3 r 0
```

Generará un valor de 15 puntos, pues el ultimo
libro se lee fuera del timepo establecido (10).
Este se leerá a partir del dia 5 (empezando en 0),
pues los 5 primeros esta ya leiendo 3 libros.


Mientras, este fichero:

```
0 r 0
3 r 0
1 r 0
2 r 0
```

Generará 20 puntos, pues todos los libros son leidos
en el terminio.


Sigamos con otro ejemplo:
```
T 10
L 0 0
B 0 0 5
B 1 0 5
B 2 0 5
B 3 0 5
B 4 0 5
R 0 0 0 5 1 5 2 5 3 10 4 3
R 1 0 4 3
```

Entonces, este fichero:
```
0 r 0
1 r 0
2 r 0
4 r 0
4 r 1
```
Generará 15 puntos, ya que:
+ El lector 0 tiene los 5 primeros dias ocupados.
+ El libro 4 está hasta el octavo dia ocupado, los
   5 primeros sin hacer nada, y del $[5, 8)$ esta
   siendo leido por el lector 1
+ El libro 4 se empieza a leer del 8o dia hasta el 11o.

Mientras, el siguiente output:
```
0 r 0
1 r 0
2 r 0
4 r 1
4 r 0
```
Generará 20 puntos, pues el libro 4 es leido por dos
lectores.

## Entrega i Evaluación
Para hacer vàlida vuestra participación nos tendreis que entregar el output de vuestro programa con el formato correcto descrito en el apartado anterior. Para comprovar la score de vuestra solución, podeis descargaros y ejecutar el programa que utilizaremos para determinar vuestra score: [LINK A GITHUB]. 


# Creadors del repte
+ quimpm
+ sergisi
