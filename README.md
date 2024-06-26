# 2do PARCIAL - Algoritmos y Estructuras de datos - MIERCOLES 26 - JUNIO - 2024

## Modalidad:

- El parcial estará habilitado para su resolución desde: Miercoles 26/06 @ 18:00hs, hasta: Jueves 27/06 @ 01:45hs. (pueden elegir cuando comenzar el intento)

- Tienen 1 (uno) sólo  intento para resolver la actividad; el tiempo máximo es 4 (cuatro) horas.

- **El tiempo será contabilizado desde el momento que aceptan realizar la actividad en Github Classroom, y cualquier "commit" realizado luego de 4 horas no será aceptado como parte del intento de resolución!!**

- Los resultados sólo será visibles luego de que la actividad cierre.   

<u>NOTA:</u> TODOS LOS EJERCICIOS DEBEN SER REALIZADOS EN UN SOLO ARCHIVO.PY, O SEA LOS MÉTODOS QUE SE VAN AGREGANDO , DEBEN ESTAR EN SUS CORRESPONDIENTES CLASES EN EL ARCHIVO EJERCICIO1.PY
LOS ARCHIVOS RESTANTES QUEDAN POR SI NECESITAN BORRADORES, PERO SOLO MIRAMOS EL PRIMER ARCHIVO


# Ejercicios:

## Ejercicio 1: 

Definir una clase <code>Fecha</code>. Formato: <code>(dd, mm, aaaa)</code>. 

La clase debe contener métodos para facilitar:
 
- <code>calcular_dif_fecha()</code>: Calcular la distancia entre dos fechas. 

Sobrecarga de métodos: 

- <code>\_\_str\_\_</code>
- <code>\_\_add\_\_</code>
- <code>\_\_eq\_\_</code>

<u><b>Importante:</b></u> 
- Cuando creamos (instanciamos) una <code>Fecha</code>, si es llamada sin parámetros, por defecto contendra la "fecha de hoy".

- **Pueden agregar más atributos y métodos, si lo consideran necesario.**  



## Ejercicio 2:


Definir una clase <code>Alumno</code> como un diccionario, el cual contiene los datos:

<code>
{ "Nombre" : 'string',
  "DNI" : 'integer' ,
  "FechaIngreso" : 'Fecha',
  "Carrera" : 'cualquier tipo' }
</code>

La clase debe contener métodos para facilitar:
 
- Cambiar uno o varios datos del Alumno.
- <code>antiguedad()</code>:Calcular la hace cuánto tiempo que el alumno esta inscripto en la carrera. 

Sobrecarga de métodos: 

- <code>\_\_str\_\_</code>
- <code>\_\_eq\_\_</code>

<u><b>Importante:</b></u> 
- Un Alumno puede estar inscripto en sólo una carrera.
- Pueden agregar más atributos y métodos, si lo consideran necesario.  



## Ejercicio 3:


Crear una clase <code>ListaDoblementeEnlazada</code> cuyos nodos contengan como dato objetos del tipo <code>Alumno</code>. Implementar un **Iterador** para la lista enlazada (será útil en el siguiente ejercicio). 
La lista tendrá un método <code>lista_ejemplo()</code> el cual retorna un *lista doblemente enlazada de alumnos* cargada con datos aleatorios (random).

<u><b>Importante:</b></u> 
- Pueden agregar más atributos y métodos, si lo consideran necesario. 


## Ejercicio 4:


Implementar una función que permita ordenar la Lista Doblemente Enlazada "de Alumnos" (ejer. anterior). Pueden utilizar cualquier método de ordenación, pero deben implentarlo (no pueden usar el método <code>sort</code> de Python).
   

El criterio de ordenación es: **Fecha de Ingreso** 

<u><b>Importante:</b></u> 
- No usar el método <code>sort</code> de Python.
- Pueden agregar más atributos y funciones/métodos, si lo consideran necesario. 

## Ejercicio 5:


Se debe crear un directorio en el cual guardaremos en un archivo una "lista de alumnos". Luego, deberán mover el directorio a una nueva ruta (<code>path</code>). Finalmente deben borrar el nuevo archivo y el nuevo directorio. 
**NO útilizar el módulo <code>shutil</code> (pueden usa el módulo <code>os</code>)**. 

<u>En resumen</u>: crear directorio; guardar en un archivo una "lista de alumnos"; mover el directorio; borrar archivo y directorio. 

<u><b>Importante:</b></u> 
- **NO USAR <code>shutil</code>**
- Recodar el manejo de excepciones, si las hay.
- Pueden agregar más atributos y funciones/métodos, si lo consideran necesario.
