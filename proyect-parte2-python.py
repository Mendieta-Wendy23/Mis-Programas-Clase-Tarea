class Mascota:

    def __init__(self, nombre, especie, edad, tamano,
                 peso, raza, enfermedad, dueno,
                 telefono, direccion, ciudad):

        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.tamano = tamano
        self.peso = peso
        self.raza = raza
        self.enfermedad = enfermedad
        self.dueno = dueno
        self.telefono = telefono
        self.direccion = direccion
        self.ciudad = ciudad
        self.esterilizada = False
        self.vacunas = []

    def mostrar_datos(self):

        print("\n----- DATOS DE LA MASCOTA -----")
        print("Nombre:", self.nombre)
        print("Especie:", self.especie)
        print("Edad:", self.edad)
        print("Tamaño:", self.tamano)
        print("Peso:", self.peso)
        print("Raza:", self.raza)
        print("Enfermedad:", self.enfermedad)
        print("Dueño:", self.dueno)
        print("Telefono:", self.telefono)
        print("Direccion:", self.direccion)
        print("Ciudad:", self.ciudad)
        print("Esterilizada:", self.esterilizada)
        print("Vacunas:", self.vacunas)


class Veterinaria:

    def __init__(self):
        self.mascotas = []

    def registrar_mascota(self):

        nombre = input("Nombre: ")
        especie = input("Perro o Gato: ")
        edad = int(input("Edad: "))
        tamano = input("Tamaño (Mini, Pequeño, Mediano, Grande): ")
        peso = float(input("Peso: "))
        raza = input("Raza: ")
        enfermedad = input("Enfermedad: ")

        dueno = input("Nombre del dueño: ")
        telefono = input("Telefono: ")
        direccion = input("Direccion: ")
        ciudad = input("Ciudad: ")

        mascota = Mascota(
            nombre, especie, edad, tamano,
            peso, raza, enfermedad,
            dueno, telefono, direccion, ciudad
        )

        self.mascotas.append(mascota)

        print("\nMascota registrada correctamente")

    def buscar_mascota(self):

        nombre = input("Nombre de la mascota: ")

        for mascota in self.mascotas:

            if mascota.nombre.lower() == nombre.lower():

                mascota.mostrar_datos()
                return

        print("Mascota no encontrada")

    def aplicar_vacuna(self):

        nombre = input("Nombre de la mascota: ")

        for mascota in self.mascotas:

            if mascota.nombre.lower() == nombre.lower():

                vacuna = input("Vacuna aplicada: ")

                mascota.vacunas.append(vacuna)

                print("Vacuna registrada")
                return

        print("Mascota no encontrada")

    def esterilizar_mascota(self):

        nombre = input("Nombre de la mascota: ")

        for mascota in self.mascotas:

            if mascota.nombre.lower() == nombre.lower():

                if mascota.edad >= 6:

                    mascota.esterilizada = True

                    print("La mascota puede ser esterilizada")
                    print("Esterilización registrada")

                else:

                    print("La mascota aún no cumple la edad recomendada")

                return

        print("Mascota no encontrada")

    def mostrar_descuentos(self):

        print("\n------ DESCUENTOS ------")
        print("1. Vacuna antirrábica con 20% de descuento")
        print("2. Vacuna triple felina con juguete gratis")
        print("3. Baño gratis en la segunda vacuna")
        print("4. Consulta gratis en vacunación completa")

    def centros_vacunacion(self):

        ciudad = input("Ciudad: ")

        if ciudad.lower() == "apizaco":
            print("Veterinaria Apizaco Centro")
            print("Clínica Animal San Martín")

        elif ciudad.lower() == "tlaxcala":
            print("Veterinaria Tlaxcala Centro")
            print("Patitas Felices")

        elif ciudad.lower() == "nativitas":
            print("Veterinaria Nativitas")
            print("Animal Care Nativitas")

        elif ciudad.lower() == "texoloc":
            print("Veterinaria Texoloc")
            print("Huellitas Texoloc")

        else:
            print("No hay centros registrados")


veterinaria = Veterinaria()

opcion = 0

while opcion != 7:

    print("\n===== SISTEMA DE VACUNACIÓN Y CUIDADO DE MASCOTAS =====")
    print("1. Registrar mascota")
    print("2. Buscar mascota")
    print("3. Aplicar vacuna")
    print("4. Centros de vacunación")
    print("5. Ver descuentos")
    print("6. Esterilización")
    print("7. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        veterinaria.registrar_mascota()

    elif opcion == 2:
        veterinaria.buscar_mascota()

    elif opcion == 3:
        veterinaria.aplicar_vacuna()

    elif opcion == 4:
        veterinaria.centros_vacunacion()

    elif opcion == 5:
        veterinaria.mostrar_descuentos()

    elif opcion == 6:
        veterinaria.esterilizar_mascota()

    elif opcion == 7:
        print("Gracias por utilizar el sistema")

    else:
        print("Opción no válida")
