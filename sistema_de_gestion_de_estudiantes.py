class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre.capitalize().strip()
        self.edad = edad
        self.calificaciones = []
    def agregar_calificacion(self, calificacion):
        if 0 <= calificacion <= 100:
            self.calificaciones.append(calificacion)
            print(f"calificacion {calificacion} agregada a {self.nombre}.")
        else:
            print("la calificacion debe estar entre 0 y 100.")
    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
    def mostrar_info(self):
        promedio = self.calcular_promedio()
        print(f"nombre: {self.nombre}, edad: {self.edad}, promedio: {promedio:.2f}")
estudiantes = []
def registrar_estudiante():
    nombre = input("ingrese el nombre del estudiante: ")
    try:
        edad = int(input("ingrese la edad: "))
        estudiante = Estudiante(nombre, edad)
        estudiantes.append(estudiante)
        print(f"estudiante '{nombre}' registrado correctamente.")
    except ValueError:
        print("edad invalida, ingrese un numero.")
def agregar_calificacion_estudiante():
    if not estudiantes:
        print("no hay estudiantes registrados.")
        return
    nombre = input("ingrese el nombre del estudiante: ").capitalize().strip()
    for estudiante in estudiantes:
        if estudiante.nombre == nombre:
            try:
                calificacion = float(input("ingrese la calificacion: "))
                estudiante.agregar_calificacion(calificacion)
            except ValueError:
                print("ingrese un numero valido.")
            return
    print("estudiante no encontrado.")
def mostrar_estudiantes():
    if not estudiantes:
        print("no hay estudiantes registrados.")
        return
    print("\n lista de estudiantes:")
    for estudiante in estudiantes:
        estudiante.mostrar_info()
def menu():
    while True:
        print("\n sistema de gestion de estudiantes ")
        print("1. registrar estudiante")
        print("2. agregar calificacion")
        print("3. mostrar estudiantes")
        print("4. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            agregar_calificacion_estudiante()
        elif opcion == "3":
            mostrar_estudiantes()
        elif opcion == "4":
            print("saliendo del sistema de gestion de estudiantes.")
            break
        else:
            print("opcion invalida, intente nuevamente.")
menu()