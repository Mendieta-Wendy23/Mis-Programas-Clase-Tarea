import tkinter as tk

# --- CLASE DUEÑO:
class Dueno:
    def __init__(self, nombre, telefono, direccion, ciudad):
        self.nombre = nombre          # Nombre completo del dueño
        self.telefono = telefono      # Teléfono de contacto
        self.direccion = direccion    # Dirección donde vive
        self.ciudad = ciudad          # Ciudad donde vive

    def mostrar_datos(self):
        # Regresa los datos del dueño en texto
        datos = "Dueño: " + self.nombre + "\n"
        datos += "Telefono: " + self.telefono + "\n"
        datos += "Direccion: " + self.direccion + "\n"
        datos += "Ciudad: " + self.ciudad
        return datos

# --- CLASE MASCOTA:
class Mascota:
    def __init__(self, nombre, especie, edad, tamano, peso, raza, enfermedad, dueno):
        self.nombre = nombre          # Nombre de la mascota
        self.especie = especie        # Perro o Gato
        self.edad = edad              # Edad en años
        self.tamano = tamano          # Mini, Pequeño, Mediano, Grande
        self.peso = peso              # Peso en kg
        self.raza = raza              # Raza del animal
        self.enfermedad = enfermedad  # Si tiene alguna enfermedad
        self.dueno = dueno            # AQUÍ GUARDAMOS EL OBJETO DUENO
        self.esterilizada = False     # Al inicio no está esterilizada
        self.vacunas = []             # Lista vacía para guardar vacunas

    def mostrar_datos(self):
        # Juntamos datos de mascota + datos del dueño
        datos = "----- DATOS DE LA MASCOTA -----\n"
        datos += "Nombre: " + self.nombre + "\n"
        datos += "Especie: " + self.especie + "\n"
        datos += "Edad: " + str(self.edad) + "\n"
        datos += "Tamaño: " + self.tamano + "\n"
        datos += "Peso: " + str(self.peso) + "\n"
        datos += "Raza: " + self.raza + "\n"
        datos += "Enfermedad: " + self.enfermedad + "\n"
        datos += "Esterilizada: " + str(self.esterilizada) + "\n"
        datos += "Vacunas: " + str(self.vacunas) + "\n"
        datos += "\n----- DATOS DEL DUEÑO -----\n"
        datos += self.dueno.mostrar_datos()  # Llamamos al mostrar_datos del dueño
        return datos

# CLASE VETERINARIA: Maneja toda la lista de mascotas
class Veterinaria:
    def __init__(self):
        self.mascotas = []  # Lista donde se guardan todas las mascotas

    def registrar_mascota(self, nombre, especie, edad, tamano, peso, raza, enfermedad, 
                          nombre_dueno, telefono, direccion, ciudad):
        # 1. Primero creamos el objeto Dueno con sus datos
        dueno = Dueno(nombre_dueno, telefono, direccion, ciudad)
        # 2. Luego creamos la Mascota y le pasamos el dueño
        mascota = Mascota(nombre, especie, int(edad), tamano, float(peso), raza, enfermedad, dueno)
        self.mascotas.append(mascota)  # La metemos a la lista
        return "Mascota registrada correctamente"

    def buscar_mascota(self, nombre):
        for mascota in self.mascotas:  # Recorremos todas las mascotas
            if mascota.nombre.lower() == nombre.lower():  # Comparamos nombres en minúsculas
                return mascota.mostrar_datos()  # Si la encontramos regresamos sus datos
        return "Mascota no encontrada"

    def aplicar_vacuna(self, nombre, vacuna):
        for mascota in self.mascotas:
            if mascota.nombre.lower() == nombre.lower():
                mascota.vacunas.append(vacuna)  # Agregamos la vacuna a su lista
                return "Vacuna registrada para " + mascota.nombre
        return "Mascota no encontrada"

    def esterilizar_mascota(self, nombre):
        for mascota in self.mascotas:
            if mascota.nombre.lower() == nombre.lower():
                if mascota.edad >= 6:  # Checamos si tiene 6 años o más
                    mascota.esterilizada = True
                    return "Esterilización registrada para " + mascota.nombre
                else:
                    return "La mascota aún no cumple la edad recomendada"
        return "Mascota no encontrada"

    def mostrar_descuentos(self):
        texto = "------ DESCUENTOS ------\n"
        texto += "1. Vacuna antirrábica con 20% de descuento\n"
        texto += "2. Vacuna triple felina con juguete gratis\n"
        texto += "3. Baño gratis en la segunda vacuna\n"
        texto += "4. Consulta gratis en vacunación completa"
        return texto

    def centros_vacunacion(self, ciudad):
        if ciudad.lower() == "apizaco":
            return "Veterinaria Apizaco Centro\nClínica Animal San Martín"
        elif ciudad.lower() == "tlaxcala":
            return "Veterinaria Tlaxcala Centro\nPatitas Felices"
        elif ciudad.lower() == "nativitas":
            return "Veterinaria Nativitas\nAnimal Care Nativitas"
        elif ciudad.lower() == "texoloc":
            return "Veterinaria Texoloc\nHuellitas Texoloc"
        else:
            return "No hay centros registrados para " + ciudad

# Creamos el objeto veterinaria que usan todas las ventanas
vet = Veterinaria()

# --- FUNCIONES PARA ABRIR CADA VENTANA ---

# 1. VENTANA REGISTRAR: Pide datos de mascota y dueño
def abrir_registrar():
    v1 = tk.Toplevel()  # Toplevel abre una ventana nueva
    v1.title("Registrar Mascota")
    v1.geometry("400x700")
    v1.config(bg="#ADD8E6")

    def registrar():
        # Validamos que edad y peso sean números
        try:
            resultado = vet.registrar_mascota(
                e_nombre.get(), e_especie.get(), e_edad.get(), e_tamano.get(),
                e_peso.get(), e_raza.get(), e_enfermedad.get(), 
                e_dueno.get(), e_telefono.get(), e_direccion.get(), e_ciudad.get()
            )
            resultado_label.config(text=resultado, fg="green")
            # Borramos todas las cajas después de registrar
            e_nombre.delete(0, tk.END); e_especie.delete(0, tk.END); e_edad.delete(0, tk.END)
            e_tamano.delete(0, tk.END); e_peso.delete(0, tk.END); e_raza.delete(0, tk.END)
            e_enfermedad.delete(0, tk.END); e_dueno.delete(0, tk.END); e_telefono.delete(0, tk.END)
            e_direccion.delete(0, tk.END); e_ciudad.delete(0, tk.END)
        except:
            resultado_label.config(text="Error: Edad y Peso deben ser números", fg="red")

    tk.Label(v1, text="REGISTRAR MASCOTA", bg="#ADD8E6", font=("Arial", 14, "bold")).pack(pady=5)
    
    # Datos de la mascota
    tk.Label(v1, text="--- DATOS MASCOTA ---", bg="#ADD8E6", font=("Arial", 10, "bold")).pack()
    tk.Label(v1, text="Nombre:", bg="#ADD8E6").pack()
    e_nombre = tk.Entry(v1); e_nombre.pack()
    tk.Label(v1, text="Especie (Perro/Gato):", bg="#ADD8E6").pack()
    e_especie = tk.Entry(v1); e_especie.pack()
    tk.Label(v1, text="Edad:", bg="#ADD8E6").pack()
    e_edad = tk.Entry(v1); e_edad.pack()
    tk.Label(v1, text="Tamaño:", bg="#ADD8E6").pack()
    e_tamano = tk.Entry(v1); e_tamano.pack()
    tk.Label(v1, text="Peso:", bg="#ADD8E6").pack()
    e_peso = tk.Entry(v1); e_peso.pack()
    tk.Label(v1, text="Raza:", bg="#ADD8E6").pack()
    e_raza = tk.Entry(v1); e_raza.pack()
    tk.Label(v1, text="Enfermedad:", bg="#ADD8E6").pack()
    e_enfermedad = tk.Entry(v1); e_enfermedad.pack()
    
    # Datos del dueño
    tk.Label(v1, text="--- DATOS DUEÑO ---", bg="#ADD8E6", font=("Arial", 10, "bold")).pack(pady=(10,0))
    tk.Label(v1, text="Nombre dueño:", bg="#ADD8E6").pack()
    e_dueno = tk.Entry(v1); e_dueno.pack()
    tk.Label(v1, text="Telefono:", bg="#ADD8E6").pack()
    e_telefono = tk.Entry(v1); e_telefono.pack()
    tk.Label(v1, text="Direccion:", bg="#ADD8E6").pack()
    e_direccion = tk.Entry(v1); e_direccion.pack()
    tk.Label(v1, text="Ciudad:", bg="#ADD8E6").pack()
    e_ciudad = tk.Entry(v1); e_ciudad.pack()
    
    tk.Button(v1, text="Registrar", command=registrar, bg="white").pack(pady=10)
    resultado_label = tk.Label(v1, text="", bg="white", width=40, height=2)
    resultado_label.pack()

# 2. VENTANA BUSCAR
def abrir_buscar():
    v2 = tk.Toplevel()
    v2.title("Buscar Mascota")
    v2.geometry("450x450")
    v2.config(bg="#ADD8E6")

    def buscar():
        resultado = vet.buscar_mascota(e_buscar.get())
        caja_texto.delete("1.0", tk.END)
        caja_texto.insert(tk.END, resultado)

    tk.Label(v2, text="BUSCAR MASCOTA", bg="#ADD8E6", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(v2, text="Nombre de la mascota:", bg="#ADD8E6").pack()
    e_buscar = tk.Entry(v2, width=30); e_buscar.pack()
    tk.Button(v2, text="Buscar", command=buscar, bg="white").pack(pady=10)
    caja_texto = tk.Text(v2, height=18, width=50); caja_texto.pack()

# 3. VENTANA VACUNAR
def abrir_vacunar():
    v3 = tk.Toplevel()
    v3.title("Aplicar Vacuna")
    v3.geometry("400x300")
    v3.config(bg="#ADD8E6")

    def vacunar():
        resultado = vet.aplicar_vacuna(e_nombre.get(), e_vacuna.get())
        resultado_label.config(text=resultado)
        e_nombre.delete(0, tk.END); e_vacuna.delete(0, tk.END)

    tk.Label(v3, text="APLICAR VACUNA", bg="#ADD8E6", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(v3, text="Nombre mascota:", bg="#ADD8E6").pack()
    e_nombre = tk.Entry(v3); e_nombre.pack()
    tk.Label(v3, text="Vacuna aplicada:", bg="#ADD8E6").pack()
    e_vacuna = tk.Entry(v3); e_vacuna.pack()
    tk.Button(v3, text="Aplicar", command=vacunar, bg="white").pack(pady=10)
    resultado_label = tk.Label(v3, text="", bg="white", width=35, height=2)
    resultado_label.pack()

# 4. VENTANA CENTROS
def abrir_centros():
    v4 = tk.Toplevel()
    v4.title("Centros de Vacunación")
    v4.geometry("400x300")
    v4.config(bg="#ADD8E6")

    def ver_centros():
        resultado = vet.centros_vacunacion(e_ciudad.get())
        caja_texto.delete("1.0", tk.END)
        caja_texto.insert(tk.END, resultado)

    tk.Label(v4, text="CENTROS DE VACUNACIÓN", bg="#ADD8E6", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(v4, text="Ciudad:", bg="#ADD8E6").pack()
    e_ciudad = tk.Entry(v4); e_ciudad.pack()
    tk.Button(v4, text="Ver Centros", command=ver_centros, bg="white").pack(pady=10)
    caja_texto = tk.Text(v4, height=8, width=40); caja_texto.pack()

# 5. VENTANA DESCUENTOS
def abrir_descuentos():
    v5 = tk.Toplevel()
    v5.title("Descuentos")
    v5.geometry("400x250")
    v5.config(bg="#ADD8E6")

    tk.Label(v5, text="DESCUENTOS", bg="#ADD8E6", font=("Arial", 14, "bold")).pack(pady=10)
    texto = vet.mostrar_descuentos()
    caja_texto = tk.Text(v5, height=8, width=45); caja_texto.pack()
    caja_texto.insert(tk.END, texto)

# 6. VENTANA ESTERILIZAR
def abrir_esterilizar():
    v6 = tk.Toplevel()
    v6.title("Esterilización")
    v6.geometry("400x250")
    v6.config(bg="#ADD8E6")

    def esterilizar():
        resultado = vet.esterilizar_mascota(e_nombre.get())
        resultado_label.config(text=resultado)

    tk.Label(v6, text="ESTERILIZACIÓN", bg="#ADD8E6", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(v6, text="Nombre mascota:", bg="#ADD8E6").pack()
    e_nombre = tk.Entry(v6); e_nombre.pack()
    tk.Button(v6, text="Esterilizar", command=esterilizar, bg="white").pack(pady=10)
    resultado_label = tk.Label(v6, text="", bg="white", width=40, height=3, wraplength=300)
    resultado_label.pack()

# VENTANA PRINCIPAL: 
menu = tk.Tk()
menu.title("Sistema Veterinaria")
menu.geometry("300x450")
menu.config(bg="#ADD8E6")

tk.Label(menu, text="MENU PRINCIPAL", bg="#ADD8E6", font=("Arial", 16, "bold")).pack(pady=20)

# Cada botón abre su ventana
tk.Button(menu, text="1. Registrar mascota", command=abrir_registrar, width=25, height=2).pack(pady=5)
tk.Button(menu, text="2. Buscar mascota", command=abrir_buscar, width=25, height=2).pack(pady=5)
tk.Button(menu, text="3. Aplicar vacuna", command=abrir_vacunar, width=25, height=2).pack(pady=5)
tk.Button(menu, text="4. Centros de vacunación", command=abrir_centros, width=25, height=2).pack(pady=5)
tk.Button(menu, text="5. Ver descuentos", command=abrir_descuentos, width=25, height=2).pack(pady=5)
tk.Button(menu, text="6. Esterilización", command=abrir_esterilizar, width=25, height=2).pack(pady=5)
tk.Button(menu, text="7. Salir", command=menu.destroy, width=25, height=2, bg="#FF6B6B").pack(pady=10)

menu.mainloop()
