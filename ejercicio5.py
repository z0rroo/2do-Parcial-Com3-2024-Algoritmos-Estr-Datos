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
