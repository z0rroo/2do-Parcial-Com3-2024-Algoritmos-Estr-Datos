## Ejercicio 2: ##
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

