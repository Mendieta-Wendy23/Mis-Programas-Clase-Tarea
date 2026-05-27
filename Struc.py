class Alumno:
    def __init__(self, nombre, carrera, semestre):
        self.nombre = nombre
        self.carrera = carrera
        self.semestre = semestre

    def registrarse(self):
        print("Datos del alumno")
        print(f"Nombre: {self.nombre}")
        print(f"Carrera: {self.carrera}")
        print(f"Semestre: {self.semestre}")


nombre = input("Ingrese su nombre: ")
carrera = input("Ingrese su carrera: ")
semestre = input("Ingrese su semestre: ")

alumno1 = Alumno(nombre, carrera, semestre)

alumno1.registrarse()
