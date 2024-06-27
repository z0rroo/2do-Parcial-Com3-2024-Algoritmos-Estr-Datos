#################### EJERCICIO 1 #################### EJERCICIO 1 ####################
from datetime import datetime

class Fecha:
    def __init__(self, dia=None, mes=None, año=None):
        if dia is None and mes is None and año is None:
            now = datetime.now()
            self.dia = now.day
            self.mes = now.month
            self.año = now.year
        else:
            self.dia = dia
            self.mes = mes
            self.año = año

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.año}"

    def siguiente_fecha(self):
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            if self.dia < 31:
                self.dia += 1
            else:
                self.dia = 1
                if self.mes < 12:
                    self.mes += 1
                else:
                    self.mes = 1
                    self.año += 1
        elif self.mes == 2:
            if (self.año % 4 == 0 and self.año % 100 != 0) or (self.año % 400 == 0):
                if self.dia < 29:
                    self.dia += 1
                else:
                    self.dia = 1
                    self.mes += 1
            else:
                if self.dia < 28:
                    self.dia += 1
                else:
                    self.dia = 1
                    self.mes += 1
        else:
            if self.dia < 30:
                self.dia += 1
            else:
                self.dia = 1
                self.mes += 1

    def calcular_dif_fecha(self, otra_fecha):
        if otra_fecha is None:
            otra_fecha = Fecha()
        fecha1 = datetime(self.año, self.mes, self.dia)
        fecha2 = datetime(otra_fecha.año, otra_fecha.mes, otra_fecha.dia)
        delta = abs((fecha1 - fecha2).days)
        return delta

def obtener_fecha_valida(mensaje):
    while True:
        try:
            entrada = input(mensaje + " (formato DD/MM/AAAA o en blanco para fecha actual): ")
            if entrada == "":
                return Fecha()
            dia, mes, año = map(int, entrada.split('/'))
            return Fecha(dia, mes, año)
        except ValueError:
            print("Fecha no válida. Por favor, intente de nuevo.")

def calcular_diferencia_fechas(fecha_actual):
    print("Ingrese la fecha para calcular la diferencia (o en blanco para usar la fecha actual):")
    fecha1 = obtener_fecha_valida("Fecha 1")
    fecha2 = obtener_fecha_valida("Fecha 2")
    diferencia = fecha1.calcular_dif_fecha(fecha2)
    print(f"La diferencia entre {fecha1} y {fecha2} es de {diferencia} días.")

def main():
    fecha = Fecha()
    while True:
        print("\n- Menú de opciones:")
        print("1. Mostrar fecha actual")
        print("2. Avanzar a la siguiente fecha")
        print("3. Calcular diferencia de fechas")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            fecha = Fecha()
            print("Fecha actual:", fecha)
        elif opcion == "2":
            if 'fecha' in locals():
                fecha.siguiente_fecha()
                print("Fecha avanzada:", fecha)
            else:
                print("Debe mostrar la fecha actual primero.")
        elif opcion == "3":
            if 'fecha' in locals():
                calcular_diferencia_fechas(fecha)
            else:
                print("Debe mostrar la fecha actual primero.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

#################### EJERCICIO 2 #################### EJERCICIO 2 ####################

from datetime import datetime

class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }

    def cambiar_datos(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.datos:
                self.datos[key] = value
            else:
                print(f"El atributo '{key}' no es válido para un Alumno.")

    def antiguedad(self):
        fecha_ingreso = self.datos["FechaIngreso"]
        hoy = datetime.today().date()
        años_inscripcion = hoy.year - fecha_ingreso.year - ((hoy.month, hoy.day) < (fecha_ingreso.month, fecha_ingreso.day))
        return años_inscripcion

    def __str__(self):
        return f"Nombre: {self.datos['Nombre']}, DNI: {self.datos['DNI']}, Fecha de Ingreso: {self.datos['FechaIngreso']}, Carrera: {self.datos['Carrera']}"

def obtener_datos_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    dni = int(input("Ingrese el DNI del alumno (solo números): "))
    fecha_str = input("Ingrese la fecha de ingreso del alumno (formato YYYY-MM-DD): ")
    fecha_ingreso = datetime.strptime(fecha_str, '%Y-%m-%d').date()
    carrera = input("Ingrese la carrera del alumno: ")

    return nombre, dni, fecha_ingreso, carrera

def menu():
    print("\nMenú de opciones:")
    print("1. Ingresar datos de un nuevo alumno")
    print("2. Mostrar datos del alumno")
    print("3. Modificar datos del alumno")
    print("4. Calcular antigüedad del alumno")
    print("5. Salir")

def main():
    alumno = None
    while True:
        menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            nombre, dni, fecha_ingreso, carrera = obtener_datos_alumno()
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            print("Datos del alumno ingresados correctamente.")

        elif opcion == '2':
            if alumno:
                print("\nDatos del alumno:")
                print(alumno)
            else:
                print("Aún no se ha ingresado ningún alumno.")

        elif opcion == '3':
            if alumno:
                print("\nModificar datos del alumno:")
                opcion_modificar = input("Ingrese el número de dato que desea modificar:\n"
                                         "1. Nombre\n"
                                         "2. DNI\n"
                                         "3. Fecha de Ingreso\n"
                                         "4. Carrera\n"
                                         "Opción: ")
                if opcion_modificar == '1':
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    alumno.cambiar_datos(Nombre=nuevo_nombre)
                elif opcion_modificar == '2':
                    nuevo_dni = int(input("Ingrese el nuevo DNI: "))
                    alumno.cambiar_datos(DNI=nuevo_dni)
                elif opcion_modificar == '3':
                    nueva_fecha_str = input("Ingrese la nueva fecha de ingreso (formato YYYY-MM-DD): ")
                    nueva_fecha = datetime.strptime(nueva_fecha_str, '%Y-%m-%d').date()
                    alumno.cambiar_datos(FechaIngreso=nueva_fecha)
                elif opcion_modificar == '4':
                    nueva_carrera = input("Ingrese la nueva carrera: ")
                    alumno.cambiar_datos(Carrera=nueva_carrera)
                else:
                    print("Opción no válida.")
            else:
                print("Aún no se ha ingresado ningún alumno.")

        elif opcion == '4':
            if alumno:
                antiguedad = alumno.antiguedad()
                print(f"La antigüedad del alumno es de {antiguedad} años.")
            else:
                print("Aún no se ha ingresado ningún alumno.")

        elif opcion == '5':
            break

        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()

#################### EJERCICIO 3 #################### EJERCICIO 3 ####################

import random
from datetime import datetime, timedelta

class GeneradorNombres:
    def __init__(self):
        self.nombres = [
            "Juan", "María", "José", "Ana", "Pedro", "Luis", "Laura", "Diego", "Sofía", "Carlos",
            "Fernanda", "Miguel", "Valentina", "Javier", "Isabela", "Alejandro", "Camila", "Ricardo", "Daniela"
        ]
        self.apellidos = [
            "García", "Martínez", "González", "Rodríguez", "López", "Hernández", "Pérez", "Sánchez", "Romero", "Díaz",
            "Torres", "Ruiz", "Gómez", "Vázquez", "Castro", "Ramírez", "Suárez", "Flores", "Mendoza", "Aguilar"
        ]
    
    def nombre_aleatorio(self):
        nombre = random.choice(self.nombres)
        apellido = random.choice(self.apellidos)
        return f"{nombre} {apellido}"

class Alumno:
    def __init__(self):
        self.nombre = GeneradorNombres().nombre_aleatorio()
        self.dni = random.randint(10000000, 48999999)
        self.fecha_ingreso = self.generar_fecha_ingreso()
        self.carrera = random.choice([
            'Programación', 'Comunicación Digital', 'Gestión de las Organizaciones', 'Acompañante Terapéutico',
            'Logística y Transporte', 'Diseño y Desarrollo de Producto', 'Ciencia de Datos', 'Administración'
            ])

    def generar_fecha_ingreso(self):
        hoy = datetime.today()
        start_date = hoy - timedelta(days=4*365)
        end_date = hoy
        fecha_aleatoria = start_date + (end_date - start_date) * random.random()
        return fecha_aleatoria.date()

    def __str__(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}, Fecha Ingreso: {self.fecha_ingreso}, Carrera: {self.carrera}"

class Nodo:
    def __init__(self, alumno=None, siguiente=None, anterior=None):
        self.alumno = alumno
        self.siguiente = siguiente
        self.anterior = anterior

class listadobenlazada:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0
    
    def vacia(self):
        return self.size == 0
    
    def agregar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.vacia():
            self.head = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.last
            self.last.siguiente = nuevo_nodo
        self.last = nuevo_nodo
        self.size += 1
    
    def lista_alumno(self, cantidad_alumnos=5):
        lista = listadobenlazada()
        for _ in range(cantidad_alumnos):
            alumno = Alumno()
            lista.agregar_al_final(alumno)
        return lista
    
    def __iter__(self):
        self._iter_actual = self.head
        return self
    
    def __next__(self):
        if self._iter_actual is None:
            raise StopIteration
        else:
            alumno = self._iter_actual.alumno
            self._iter_actual = self._iter_actual.siguiente
            return alumno

def cantidad(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    cantidad_alumnos = cantidad("Ingrese la cantidad de alumnos a generar: ")
    
    lista = listadobenlazada()
    lista = lista.lista_alumno(cantidad_alumnos)
    
    print(f"Lista de {cantidad_alumnos} alumnos:")
    for alumno in lista:
        print(alumno)

#################### EJERCICIO 4 #################### EJERCICIO 4 ####################

import random
from datetime import datetime, timedelta

class GeneradorNombres:
    def __init__(self):
        self.nombres = [
            "Juan", "María", "José", "Ana", "Pedro", "Luis", "Laura", "Diego", "Sofía", "Carlos",
            "Fernanda", "Miguel", "Valentina", "Javier", "Isabela", "Alejandro", "Camila", "Ricardo", "Daniela"
        ]
        self.apellidos = [
            "García", "Martínez", "González", "Rodríguez", "López", "Hernández", "Pérez", "Sánchez", "Romero", "Díaz",
            "Torres", "Ruiz", "Gómez", "Vázquez", "Castro", "Ramírez", "Suárez", "Flores", "Mendoza", "Aguilar"
        ]
    
    def nombre_aleatorio(self):
        nombre = random.choice(self.nombres)
        apellido = random.choice(self.apellidos)
        return f"{nombre} {apellido}"

class Alumno:
    def __init__(self):
        self.nombre = GeneradorNombres().nombre_aleatorio()
        self.dni = random.randint(10000000, 48999999)
        self.fecha_ingreso = self.generar_fecha_ingreso()
        self.carrera = random.choice([
            'Programación', 'Comunicación Digital', 'Gestión de las Organizaciones', 'Acompañante Terapéutico',
            'Logística y Transporte', 'Diseño y Desarrollo de Producto', 'Ciencia de Datos', 'Administración'
            ])

    def generar_fecha_ingreso(self):
        hoy = datetime.today()
        start_date = hoy - timedelta(days=4*365)
        end_date = hoy
        fecha_aleatoria = start_date + (end_date - start_date) * random.random()
        return fecha_aleatoria.date()

    def __str__(self):
        fecha_formato = self.fecha_ingreso.strftime("%d/%m/%Y")
        return f"Nombre: {self.nombre}, DNI: {self.dni}, Fecha Ingreso: {self.fecha_ingreso}, Carrera: {self.carrera}"

class Nodo:
    def __init__(self, alumno=None, siguiente=None, anterior=None):
        self.alumno = alumno
        self.siguiente = siguiente
        self.anterior = anterior

class listadobenlazada:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0
    
    def vacia(self):
        return self.size == 0
    
    def agregar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.vacia():
            self.head = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.last
            self.last.siguiente = nuevo_nodo
        self.last = nuevo_nodo
        self.size += 1
    
    def lista_alumno(self, cantidad_alumnos=5):
        lista = listadobenlazada()
        for _ in range(cantidad_alumnos):
            alumno = Alumno()
            lista.agregar_al_final(alumno)
        return lista
    
    def ordenar_por_fecha_ingreso(self):
        if self.size < 2:
            return
        
        current = self.head
        while current:
            min_nodo = current
            siguiente_nodo = current.siguiente
            while siguiente_nodo:
                if siguiente_nodo.alumno.fecha_ingreso < min_nodo.alumno.fecha_ingreso:
                    min_nodo = siguiente_nodo
                siguiente_nodo = siguiente_nodo.siguiente
            if min_nodo != current:
                self._swap(current, min_nodo)
            current = current.siguiente
    
    def _swap(self, nodo1, nodo2):
        temp_alumno = nodo1.alumno
        nodo1.alumno = nodo2.alumno
        nodo2.alumno = temp_alumno
    
    def __iter__(self):
        self._iter_actual = self.head
        return self
    
    def __siguiente__(self):
        if self._iter_actual is None:
            raise StopIteration
        else:
            alumno = self._iter_actual.alumno
            self._iter_actual = self._iter_actual.siguiente
            return alumno

def cantidad(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    cantidad_alumnos = cantidad("Ingrese la cantidad de alumnos a generar: ")
    
    lista = listadobenlazada()
    lista = lista.lista_alumno(cantidad_alumnos)
    lista.ordenar_por_fecha_ingreso()
    
    print("\nLista doblemente enlazada ordenada por fecha de ingreso:")
    for alumno in lista:
        print(alumno)

#################### EJERCICIO 5 #################### EJERCICIO 5 ####################

import os
import random
from datetime import datetime, timedelta

class GeneradorNombres:
    def __init__(self):
        self.nombres = [
            "Juan", "María", "José", "Ana", "Pedro", "Luis", "Laura", "Diego", "Sofía", "Carlos",
            "Fernanda", "Miguel", "Valentina", "Javier", "Isabela", "Alejandro", "Camila", "Ricardo", "Daniela"
        ]
        self.apellidos = [
            "García", "Martínez", "González", "Rodríguez", "López", "Hernández", "Pérez", "Sánchez", "Romero", "Díaz",
            "Torres", "Ruiz", "Gómez", "Vázquez", "Castro", "Ramírez", "Suárez", "Flores", "Mendoza", "Aguilar"
        ]
    
    def nombre_aleatorio(self):
        nombre = random.choice(self.nombres)
        apellido = random.choice(self.apellidos)
        return f"{nombre} {apellido}"

class Alumno:
    def __init__(self):
        self.nombre = GeneradorNombres().nombre_aleatorio()
        self.dni = random.randint(10000000, 48999999)  # DNI aleatorio de 8 dígitos
        self.fecha_ingreso = self.generar_fecha_ingreso()
        self.carrera = random.choice([
            'Programación', 'Comunicación Digital', 'Gestión de las Organizaciones', 'Acompañante Terapéutico',
            'Logística y Transporte', 'Diseño y Desarrollo de Producto', 'Ciencia de Datos', 'Administración'
        ])

    def generar_fecha_ingreso(self):
        hoy = datetime.today()
        start_date = hoy - timedelta(days=4*365)
        end_date = hoy
        fecha_aleatoria = start_date + (end_date - start_date) * random.random()
        return fecha_aleatoria.date()

    def __str__(self):
        return f"{self.nombre},{self.dni},{self.fecha_ingreso},{self.carrera}"

class Nodo:
    def __init__(self, alumno=None, siguiente=None, anterior=None):
        self.alumno = alumno
        self.siguiente = siguiente
        self.anterior = anterior

class listadobenlazada:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0
    
    def vacia(self):
        return self.size == 0
    
    def agregar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.vacia():
            self.head = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.last
            self.last.siguiente = nuevo_nodo
        self.last = nuevo_nodo
        self.size += 1
    
    def lista_alumnos(self, cantidad_alumnos=5):
        lista_alumnos = []
        for _ in range(cantidad_alumnos):
            alumno = Alumno()
            lista_alumnos.append(alumno)
            self.agregar_al_final(alumno)
        return lista_alumnos
    
    def __iter__(self):
        self._iter_actual = self.head
        return self
    
    def __next__(self):
        if self._iter_actual is None:
            raise StopIteration
        else:
            alumno = self._iter_actual.alumno
            self._iter_actual = self._iter_actual.siguiente
            return alumno

class ListaAlumnos:
    def __init__(self):
        self.alumnos = []
    
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)
    
    def guardar_archivo(self, nombre_directorio, nombre_archivo, borrar_en_el_momento=False):
        try:
            os.makedirs(nombre_directorio, exist_ok=True)
            with open(os.path.join(nombre_directorio, nombre_archivo), 'w') as file:
                for alumno in self.alumnos:
                    file.write(f"{alumno}\n")

            print(f"Archivo '{nombre_archivo}' creado y guardado en el directorio '{nombre_directorio}'.")

            if borrar_en_el_momento:
                nueva_ruta = os.path.join(os.getcwd(), "nueva_ruta") 
                os.rename(nombre_directorio, nueva_ruta)
                print(f"Directorio '{nombre_directorio}' movido a '{nueva_ruta}'.")
                os.remove(os.path.join(nueva_ruta, nombre_archivo))
                os.rmdir(nueva_ruta)
                print(f"Archivo '{nombre_archivo}' y directorio '{nueva_ruta}' eliminados.")
            else:
                print("Los archivos no han sido eliminados en este momento.")

        except Exception as e:
            print(f"Ocurrió un error: {e}")

def cantidad(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

def main():
    cantidad_alumnos = cantidad("Ingrese la cantidad de alumnos a generar: ")
    
    lista = listadobenlazada()
    lista_alumnos = ListaAlumnos()

    alumnos_generados = lista.lista_alumnos(cantidad_alumnos)
    for alumno in alumnos_generados:
        lista_alumnos.agregar_alumno(alumno)

    nombre_directorio = "lista_alumnos"
    nombre_archivo = "lista.txt"
    lista_alumnos.guardar_archivo(nombre_directorio, nombre_archivo)
    respuesta = input("¿Desea borrar el directorio y el archivo en este momento? (s/n): ").strip().lower()
    if respuesta == 's':
        lista_alumnos.guardar_archivo(nombre_directorio, nombre_archivo, borrar_en_el_momento=True)

if __name__ == "__main__":
    main()

