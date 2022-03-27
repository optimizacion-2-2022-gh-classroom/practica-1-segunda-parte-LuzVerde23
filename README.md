<p align = "center">
    <img src="images/logo_itam.png" width="300" height="110" />

---

## Tabla de contenido:
    
1. [Integrantes y roles asignados](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23#acerca-de-este-proyecto)
    
2. [Acerca de esta proyecto](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23/blob/main/README.md#acerca-de-este-proyecto)
    
3. [Estructura básica del proyecto](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23/blob/main/README.md#estructura-b%C3%A1sica-del-proyecto-)
    
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
    
---  

## Estructura básica del proyecto
    
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
 
