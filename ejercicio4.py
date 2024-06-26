## Ejercicio 4: ##
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
        self.dni = random.randint(10000000, 99999999)  # DNI aleatorio de 8 dígitos
        self.fecha_ingreso = self.generar_fecha_ingreso()
        self.carrera = random.choice([
            'Programación', 'Comunicación Digital', 'Gestión de las Organizaciones', 'Acompañante Terapéutico',
            'Logística y Transporte', 'Diseño y Desarrollo de Producto', 'Ciencia de Datos', 'Administración'
            ])

    def generar_fecha_ingreso(self):
        # Generar una fecha aleatoria en los últimos 4 años
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

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0
    
    def esta_vacia(self):
        return self.size == 0
    
    def agregar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
        self.cola = nuevo_nodo
        self.size += 1
    
    def lista_alumno(self, cantidad_alumnos=5):
        lista = ListaDoblementeEnlazada()
        for _ in range(cantidad_alumnos):
            alumno = Alumno()
            lista.agregar_al_final(alumno)
        return lista
    
    def ordenar_por_fecha_ingreso(self):
        if self.size < 2:
            return
        
        # Implementación del algoritmo de ordenación de selección
        current = self.cabeza
        while current:
            min_node = current
            next_node = current.siguiente
            while next_node:
                if next_node.alumno.fecha_ingreso < min_node.alumno.fecha_ingreso:
                    min_node = next_node
                next_node = next_node.siguiente
            
            # Swap current node with min_node
            if min_node != current:
                self._swap(current, min_node)
            
            current = current.siguiente
    
    def _swap(self, node1, node2):
        temp_alumno = node1.alumno
        node1.alumno = node2.alumno
        node2.alumno = temp_alumno
    
    def __iter__(self):
        self._iter_actual = self.cabeza
        return self
    
    def __next__(self):
        if self._iter_actual is None:
            raise StopIteration
        else:
            alumno = self._iter_actual.alumno
            self._iter_actual = self._iter_actual.siguiente
            return alumno

def obtener_numero_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    cantidad_alumnos = obtener_numero_entero("Ingrese la cantidad de alumnos a generar: ")
    
    lista = ListaDoblementeEnlazada()
    lista = lista.lista_alumno(cantidad_alumnos)
    lista.ordenar_por_fecha_ingreso()
    
    print("\nLista doblemente enlazada ordenada por fecha de ingreso:")
    for alumno in lista:
        print(alumno)
