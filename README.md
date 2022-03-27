<p align = "center">
    <img src="images/logo_itam.png" width="300" height="110" />

---

## Tabla de contenido:
    
1. [Integrantes y roles asignados](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23#acerca-de-este-proyecto)
    
2. [Acerca de este proyecto](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23/blob/main/README.md#acerca-de-este-proyecto)
    
3. [Estructura básica del repositorio](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23/blob/main/README.md#estructura-b%C3%A1sica-del-proyecto-)
    
4. [¿Qué lenguaje utlizamos?](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23/blob/main/README.md#qu%C3%A9-lenguaje-utlizamos)

5. [Ambientes en Contenedor](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23#ambientes-en-contenedor)

6. [Documentación del paquete](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23/blob/main/README.md#documentaci%C3%B3n-del-paquete)
    
7. [Referencias](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23/blob/main/README.md#referencias)
    
---

## Integrantes y roles asignados

|     ***Integrante***      |             ***Usuario de GitHub***             |  ***Rol asignado***        |                       
|:-------------------------:|:-----------------------------------------------:|:--------------------------:|
|  Ita                      |    [sancas96](https://github.com/sancas96)      | Equipo de Programación     | 
|  Luz                      |    [LuzVerde23](https://github.com/LuzVerde23)  | Administrador de proyecto  | 
|  Edgar                    |    [EddOselotl](https://github.com/EddOselotl)  | Equipo de Programación     | 
|  Uriel                    |    [urieluard](https://github.com/urieluard)    | Equipo de Programación     | 

---    

## Acerca de este proyecto
    
Este proyecto contiene la segunda parte de la práctica 1 de la materia de "Temas selectos de Modelado". Los **objetivos** de este trabajo son:
 
+ **Implementar un método numérico para resolver un problema de optimización convexa**
    
+ **Documnentar la implementación del método numérico mediante la paquetería [sphinx](https://www.sphinx-doc.org/en/master/)**
    
La primera parte de esta práctica está documentada en los siguientes repositorios, donde se realizó una investigación sobre los métodos y problemas de optimización de interés para cada integrante de este equipo. Se reportaron ejemplos, planteamientos y paqueterías que permiten resolver este tipo de problemas.

  + [Práctica 1, primera parte (equipo: Ita/Luz)](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-primera-parte-sancas96)
    
  + [Práctica 1, primera parte (equipo: Edgar/Uriel)](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-primera-parte-urieluard)

**El algoritmo que se eligió para su implementación corresponde al conocido con el nombre de Ford-Fulkerson** y se utiliza para resolver el **problema de flujo máximo**. En el cual tenemos un nodo inicial, llamado fuente, un nodo terminal que llamaremos sumidero, arcos y nodos que interconectan toda la red. Con un grafo de este tipo lo que queremos encontrar es el valor del flujo máximo que puede circular por la red.
    
El problema de optimización planteado se puede resolver desde el punto de vista de la programación lineal de la siguiente forma:

#### Variables de Decisión:

Unidades que fluyen desde el nodo i al j (flujo a través de los arcos)
    
#### Función Objetivo: 

Maximizar las unidades que salen del nodo de origen o fuente (s) a los que éste conecta (j, k, l,...) o alternativamente maximizar las unidades que llegan al nodo de destino o sumidero (t) desde los que conectan a él.

#### Restricciones:

* Restricciones de Flujo Máximo: La cantidad de unidades que sale de cada nodo de origen a un nodo de destino no puede superar la capacidad detallada en el arco, por ejemplo, del nodo 1 al nodo 2 sólo se pueden enviar 7 unidades.

* Restricciones de Balance de Flujo en los Nodos: Debe existir un equilibrio entre la cantidad de unidades que llega a un nodo y las que de éste salen.

* No Negatividad e Integralidad: Las variables de decisión deben cumplir las condiciones de no negatividad. Adicionalmente exigiremos que éstas adopten valores enteros aún cuando se podría flexibilizar dicha situación lo que daría origen a un problema de Programación Lineal.

#### Teorema de Ford Fulkerson

_En cualquier red, el flujo máximo que fluye de la fuente al destino es igual a la capacidad del corte mínimo que separa a la fuente del destino_.

Esto quiere decir que el algoritmo concluye cuando el flujo máximo es devuelto y su costo depende del costo de cada iteración y del número de estas.
    
El algoritmo se programó con base en otro llamado ["Búsqueda en anchura (Breadth-first search)"](https://es.wikipedia.org/wiki/B%C3%BAsqueda_en_anchura). Formalmente,se trata de un algoritmo de búsqueda sin información, que expande y examina todos los nodos de un árbol sistemáticamente para buscar una solución. El algoritmo no usa ninguna estrategia heurística.
    
Para myor referencia de los algoritmos de Ford-Fulkerson y de Búsqueda en Anchura consultar el NoteBook [reporte_equipo_2_parte_2_practica_1.ipynb](https://github.com/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-diramtz/blob/main/reporte_equipo_2_parte_2_practica_1.ipynb) y las [referencias](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23#referencias) [3] - [6] que vienen al final de este documento.

#### Uso del Algoritmo

El Algoritmo implementado es capaz de resolver una red o grafo dirigido, que contenga uno y solo un nodo de inyección de flujo (nodo fuente) y otro que sea de solo extracción (nodo sumidero). El ejemplo práctico que se resolvió para comprobar la funcionalidad del algoritmo y el paquete implementado corresponde al de una red eléctrica, en donde nos interesa saber el **flujo máximo de energía eléctica que se puede transmitir desde uno de los nodos ubicados en el norte del país (con alto potencial de generación) hasta otro ubicado en el centro (de los de mayor consumo en el país)**. 

Resolver este problema resulta interesante por los siguientes aspectos:
    
- Para determinar los posibles cuellos de botella (restricciones) que se pueden presentar al tratar de enviar energía desde un punto de la red a otro.
- Encontrar posibles puntos de inyección donde resulte más conveniente instalar generación (que se obtengan mayores flujos máximos por la red)
- Descubrir cuales corredores de trasnmisión (rutas) se ven más utilizadas cuando la inyección de energía se presenta en algún punto de la red.

---  

## Estructura básica del repositorio
    
```
practica-1-segunda-parte-LuzVerde23:
 |
 ├── README.md                                   <- Contiene información relevante del proyecto.
 │
 ├── reporte_equipo_2_parte_2_practica_1.ipynb   <- Note Book con el reporte donde se explica la implementación del método.
 |
 ├── BD                                          <- Bases de datos utilizadas para comprobar el método
 │
 ├── Dockerfiles                                 <- Carpeta con archivo de Docker que crea la imágen del entorno para la ejecución del método
 |
 ├── src                                         <- Archivos y estructura de carpetas necesarias para el paquete
 │
 └── images                                      <- Contiene las imágenes utilizadas en el repositorio.
```    

### ¿Qué lenguaje utlizamos?

<img src="images/logo_python.png" width="270" height="100" />
    
[***Python.org***](https://www.python.org/)

![Versión de Python utilizada (3.7.8)](https://www.python.org/downloads/release/python-378/)

---

## Ambientes en Contenedor

### Binder

En el siguiente botón se realiza el lanzamiento de un ambiente ejeutable donde se podrá interactuar con el paquete realizado (**MaxFlowAeiu**)
    
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23/main?labpath=reporte_equipo_2_parte_2_practica_1.ipynb)

### Docker

De igual forma, en este repositorio se cuenta con un archivo de Docker para crear el contenedor que contiene todas las libreríasy el paquete creado para que pueda ser utilizado desde [Docker](https://www.docker.com/).

<p align = "center">
    <img src="images/Docker-Logo.png" width="300" height="110" />


--- 

## Documentación del paquete

La documentación del paquete realizado se hizo con [Sphinx](https://www.sphinx-doc.org/en/master/) y se puede consultar en este [link](https://optimizacion-2-2022-gh-classroom.github.io/practica-1-segunda-parte-LuzVerde23/index.html).

<p align = "center">
    <img src="images/sphinxheader.png" width="300" height="110" />
    
---

## Referencias
    
* [1] [Palacios E. (2022) Libro de Optimización](https://itam-ds.github.io/analisis-numerico-computo-cientifico/4.optimizacion_en_redes_y_prog_lineal/4.2/Definiciones_generales_de_flujo_en_redes.html)
* [2] [Dumora c. el all. Data Oriented Algorithm for Real Time Estimation of Flow Rates and Flow Directions in Water Distribution Network](https://arxiv.org/pdf/1807.10147.pdf)
* [3] [Max Flow Problem Introduction](https://www.geeksforgeeks.org/max-flow-problem-introduction/)
* [4] [Ford-Fulkerson Algorithm](https://www.programiz.com/dsa/ford-fulkerson-algorithm)
* [5] [Algoritmo de Ford-Fulkerson - Ford–Fulkerson algorithm](https://upwikies.top/wiki/Ford%e2%80%93Fulkerson_algorithm)
* [6] [Oviedo J. (2008) Algoritmo de Ford-Fulkerson Mejorado](http://www.ptolomeo.unam.mx:8080/jspui/bitstream/132.248.52.100/2387/1/gonzalezoviedo.pdf)
* [7] [Building a Smarter (and Cheaper) School Bus System: How a Boston-MIT Partnership Led to New Routes That Are 20% More Efficient and Saved the District $5 Million](https://www.the74million.org/article/building-a-smarter-and-cheaper-school-bus-system-how-a-boston-mit-partnership-led-to-new-routes-that-are-20-more-efficient-use-400-fewer-buses-save-5-million/)
* [8] [Optimazation examples](https://vitalflux.com/convex-optimization-explained-concepts-examples/)
 
