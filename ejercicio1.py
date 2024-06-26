### Ejercicio 1: Class de Fecha ###
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
            entrada = input(mensaje + " (formato DD/MM/AAAA o dejar en blanco para fecha actual): ")
            if entrada == "":
                return Fecha()
            dia, mes, año = map(int, entrada.split('/'))
            return Fecha(dia, mes, año)
        except ValueError:
            print("Fecha inválida. Por favor, intente nuevamente.")

def calcular_diferencia_fechas(fecha_actual):
    print("Ingrese la fecha para calcular la diferencia (o dejar en blanco para usar la fecha actual):")
    fecha1 = obtener_fecha_valida("Fecha 1")
    fecha2 = obtener_fecha_valida("Fecha 2")
    diferencia = fecha1.calcular_dif_fecha(fecha2)
    print(f"La diferencia entre {fecha1} y {fecha2} es de {diferencia} días.")

def main():
    fecha = Fecha()
    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar fecha actual")
        print("2. Avanzar a la siguiente fecha")
        print("3. Calcular diferencia entre fechas")
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
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
