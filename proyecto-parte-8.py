import tkinter as tk
import webbrowser

# --- CLASE DUEÑO:
class Dueno:
    def __init__(self, nombre, telefono, direccion, ciudad):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.ciudad = ciudad

    def mostrar_datos(self):
        datos = "Dueño: " + self.nombre + "\n"
        datos += "Telefono: " + self.telefono + "\n"
        datos += "Direccion: " + self.direccion + "\n"
        datos += "Ciudad: " + self.ciudad
        return datos

# --- CLASE MASCOTA:
class Mascota:
    def __init__(self, id_mascota, nombre, especie, edad_meses, tamano, peso, raza, enfermedad, dueno):
        self.id_mascota = id_mascota
        self.nombre = nombre
        self.especie = especie
        self.edad_meses = edad_meses
        self.tamano = tamano
        self.peso = peso
        self.raza = raza
        self.enfermedad = enfermedad
        self.dueno = dueno
        self.esterilizada = False
        self.vacunas = []

    def mostrar_datos(self):
        datos = "----- DATOS DE LA MASCOTA -----\n"
        datos += "ID: " + str(self.id_mascota) + "\n"
        datos += "Nombre: " + self.nombre + "\n"
        datos += "Especie: " + self.especie + "\n"

        if self.edad_meses >= 12:
            datos += "Edad: " + str(self.edad_meses // 12) + " años\n"
        else:
            datos += "Edad: " + str(self.edad_meses) + " meses\n"

        datos += "Tamaño: " + self.tamano + "\n"
        datos += "Peso: " + str(self.peso) + "\n"
        datos += "Raza: " + self.raza + "\n"
        datos += "Enfermedad: " + self.enfermedad + "\n"
        datos += "Esterilizada: " + str(self.esterilizada) + "\n"
        datos += "Vacunas: " + str(self.vacunas) + "\n"

        datos += "\n----- DATOS DEL DUEÑO -----\n"
        datos += self.dueno.mostrar_datos()
        return datos

# --- CLASE REGISTRO:
class Registro:
    def __init__(self):
        self.mascotas = []
        self.siguiente_id = 1

    def registrar_mascota(self, nombre, especie, edad, unidad_edad, tamano, peso, raza,
                          enfermedad, nombre_dueno, telefono, direccion, ciudad):
        dueno = Dueno(nombre_dueno, telefono, direccion, ciudad)
        edad = int(edad)
        edad_meses = edad * 12 if unidad_edad == "Años" else edad

        mascota = Mascota(
            self.siguiente_id, nombre, especie, edad_meses, tamano, float(peso),
            raza, enfermedad, dueno
        )
        self.mascotas.append(mascota)
        id_generado = self.siguiente_id
        self.siguiente_id += 1
        return "Mascota registrada correctamente. ID asignado: " + str(id_generado)

    def buscar_mascota(self, id_mascota):
        for mascota in self.mascotas:
            if mascota.id_mascota == int(id_mascota):
                return mascota.mostrar_datos()
        return "Mascota no encontrada"

    def aplicar_vacuna(self, id_mascota, vacuna):
        for mascota in self.mascotas:
            if mascota.id_mascota == int(id_mascota):
                mascota.vacunas.append(vacuna)
                return "Vacuna registrada para " + mascota.nombre
        return "Mascota no encontrada"

    def esterilizar_mascota(self, id_mascota):
        for mascota in self.mascotas:
            if mascota.id_mascota == int(id_mascota):
                if mascota.edad_meses >= 6:
                    mascota.esterilizada = True
                    return "Esterilización registrada para " + mascota.nombre
                else:
                    return "La mascota aún no cumple la edad recomendada"
        return "Mascota no encontrada"

    def mostrar_descuentos(self):
        texto = "------ DESCUENTOS ------\n"
        texto += "Vacuna antirrábica con 20% de descuento\n"
        texto += "Vacuna triple felina con juguete gratis\n"
        texto += "Baño gratis en la segunda vacuna\n"
        texto += "Consulta gratis en vacunación completa"
        return texto

    def centros_vacunacion(self, ciudad):
        ciudad = ciudad.lower()
        if ciudad == "apizaco":
            return "Veterinaria Apizaco Centro\nClínica Animal San Martín"
        elif ciudad == "tlaxcala":
            return "Veterinaria Tlaxcala Centro\nPatitas Felices"
        elif ciudad == "nativitas":
            return "Veterinaria Nativitas\nAnimal Care Nativitas"
        elif ciudad == "texoloc":
            return "Veterinaria Texoloc\nHuellitas Texoloc"
        else:
            return "No hay centros registrados para " + ciudad

registro = Registro()

# --- VENTANA REGISTRAR
def abrir_registrar():
    v1 = tk.Toplevel()
    v1.title("Registrar Mascota")
    v1.geometry("400x750")
    v1.config(bg="#FFD93D")

    def registrar():
        try:
            resultado = registro.registrar_mascota(
                e_nombre.get(), e_especie.get(), e_edad.get(), unidad_edad.get(),
                e_tamano.get(), e_peso.get(), e_raza.get(), e_enfermedad.get(),
                e_dueno.get(), e_telefono.get(), e_direccion.get(), e_ciudad.get()
            )
            resultado_label.config(text=resultado, fg="green")
            for entry in [e_nombre, e_especie, e_edad, e_tamano, e_peso, e_raza, e_enfermedad, e_dueno, e_telefono, e_direccion, e_ciudad]:
                entry.delete(0, tk.END)
        except:
            resultado_label.config(text="Error: Edad y Peso deben ser números", fg="red")

    tk.Label(v1, text="REGISTRAR MASCOTA", bg="#FFD93D", font=("Poppins", 14, "bold")).pack(pady=5)
    tk.Label(v1, text="--- DATOS MASCOTA ---", bg="#FFD93D", font=("Poppins", 10, "bold")).pack()

    tk.Label(v1, text="Nombre:", bg="#FFD93D").pack()
    e_nombre = tk.Entry(v1)
    e_nombre.pack()

    tk.Label(v1, text="Especie (Perro/Gato):", bg="#FFD93D").pack()
    e_especie = tk.Entry(v1)
    e_especie.pack()

    tk.Label(v1, text="Edad:", bg="#FFD93D").pack()
    e_edad = tk.Entry(v1)
    e_edad.pack()

    tk.Label(v1, text="Unidad:", bg="#FFD93D").pack()
    unidad_edad = tk.StringVar(v1)
    unidad_edad.set("Meses")
    combo_unidad = tk.OptionMenu(v1, unidad_edad, "Meses", "Años")
    combo_unidad.pack()

    tk.Label(v1, text="Tamaño:", bg="#FFD93D").pack()
    e_tamano = tk.Entry(v1)
    e_tamano.pack()

    tk.Label(v1, text="Peso:", bg="#FFD93D").pack()
    e_peso = tk.Entry(v1)
    e_peso.pack()

    tk.Label(v1, text="Raza:", bg="#FFD93D").pack()
    e_raza = tk.Entry(v1)
    e_raza.pack()

    tk.Label(v1, text="Enfermedad:", bg="#FFD93D").pack()
    e_enfermedad = tk.Entry(v1)
    e_enfermedad.pack()

    tk.Label(v1, text="--- DATOS DUEÑO ---", bg="#FFD93D", font=("Poppins", 10, "bold")).pack(pady=(10, 0))

    tk.Label(v1, text="Nombre dueño:", bg="#FFD93D").pack()
    e_dueno = tk.Entry(v1)
    e_dueno.pack()

    tk.Label(v1, text="Telefono:", bg="#FFD93D").pack()
    e_telefono = tk.Entry(v1)
    e_telefono.pack()

    tk.Label(v1, text="Direccion:", bg="#FFD93D").pack()
    e_direccion = tk.Entry(v1)
    e_direccion.pack()

    tk.Label(v1, text="Ciudad:", bg="#FFD93D").pack()
    e_ciudad = tk.Entry(v1)
    e_ciudad.pack()

    tk.Button(v1, text="Registrar", command=registrar, bg="white").pack(pady=10)
    resultado_label = tk.Label(v1, text="", bg="white", width=45, height=2)
    resultado_label.pack()

# 2. VENTANA BUSCAR
def abrir_buscar():
    v2 = tk.Toplevel()
    v2.title("Buscar Mascota")
    v2.geometry("450x450")
    v2.config(bg="#FFD93D")

    def buscar():
        resultado = registro.buscar_mascota(e_buscar.get())
        caja_texto.delete("1.0", tk.END)
        caja_texto.insert(tk.END, resultado)

    tk.Label(v2, text="BUSCAR MASCOTA", bg="#FFD93D", font=("Poppins", 14, "bold")).pack(pady=10)
    tk.Label(v2, text="ID de la mascota:", bg="#FFD93D").pack()
    e_buscar = tk.Entry(v2, width=30)
    e_buscar.pack()
    tk.Button(v2, text="Buscar", command=buscar, bg="white").pack(pady=10)
    caja_texto = tk.Text(v2, height=18, width=50)
    caja_texto.pack()

# 3. VENTANA VACUNAR
def abrir_vacunar():
    v3 = tk.Toplevel()
    v3.title("Aplicar Vacuna")
    v3.geometry("400x300")
    v3.config(bg="#FFD93D")

    def vacunar():
        resultado = registro.aplicar_vacuna(e_id.get(), e_vacuna.get())
        resultado_label.config(text=resultado)
        e_id.delete(0, tk.END)
        e_vacuna.delete(0, tk.END)

    tk.Label(v3, text="APLICAR VACUNA", bg="#FFD93D", font=("Poppins", 14, "bold")).pack(pady=10)
    tk.Label(v3, text="ID mascota:", bg="#FFD93D").pack()
    e_id = tk.Entry(v3)
    e_id.pack()
    tk.Label(v3, text="Vacuna aplicada:", bg="#FFD93D").pack()
    e_vacuna = tk.Entry(v3)
    e_vacuna.pack()
    tk.Button(v3, text="Aplicar", command=vacunar, bg="white").pack(pady=10)
    resultado_label = tk.Label(v3, text="", bg="white", width=35, height=2)
    resultado_label.pack()

# 4. VENTANA CENTROS - CON MAPA DE ESTADOS DE MÉXICO
def abrir_centros():
    v4 = tk.Toplevel()
    v4.title("Centros de Vacunación")
    v4.geometry("400x400")
    v4.config(bg="#FFD93D")

    def abrir_maps():
        estado = estado_var.get()
        if estado and estado!= "-- Elige un estado --":
            busqueda = f"centros de vacunación veterinaria {estado} México"
            url = f"https://www.google.com/maps/search/{busqueda.replace(' ', '+')}"
            webbrowser.open(url)
            resultado_label.config(text=f"Abriendo Google Maps: {estado}", fg="green")
        else:
            resultado_label.config(text="Selecciona un estado primero", fg="red")

    def ver_centros_locales():
        ciudad = estado_var.get()
        if ciudad!= "-- Elige un estado --":
            resultado = registro.centros_vacunacion(ciudad)
            caja_texto.delete("1.0", tk.END)
            caja_texto.insert(tk.END, resultado)
        else:
            caja_texto.delete("1.0", tk.END)
            caja_texto.insert(tk.END, "Selecciona un estado")

    tk.Label(v4, text="CENTROS DE VACUNACIÓN", bg="#FFD93D", font=("Poppins", 14, "bold")).pack(pady=10)
    tk.Label(v4, text="Selecciona tu estado para ver\ncentros en Google Maps:", bg="#FFD93D", font=("Poppins", 10)).pack(pady=5)

    estados = [
        "-- Elige un estado --", "Aguascalientes", "Baja California", "Baja California Sur",
        "Campeche", "Chiapas", "Chihuahua", "Ciudad de México", "Coahuila", "Colima",
        "Durango", "Estado de México", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco",
        "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla",
        "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora",
        "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"
    ]

    estado_var = tk.StringVar(v4)
    estado_var.set(estados[0])

    menu_estados = tk.OptionMenu(v4, estado_var, *estados)
    menu_estados.config(width=25, font=("Poppins", 10))
    menu_estados.pack(pady=10)

    tk.Button(v4, text="🗺️ Abrir en Google Maps", command=abrir_maps, bg="#CE1126", fg="white",
              font=("Poppins", 11, "bold"), width=20).pack(pady=10)

    resultado_label = tk.Label(v4, text="", bg="white", width=40, height=2, font=("Poppins", 9))
    resultado_label.pack(pady=5)

    tk.Label(v4, text="--- O ver centros guardados ---", bg="#FFD93D", font=("Poppins", 9)).pack(pady=(10,5))
    tk.Button(v4, text="Ver centros locales", command=ver_centros_locales, bg="white").pack()
    caja_texto = tk.Text(v4, height=4, width=40, font=("Poppins", 9))
    caja_texto.pack(pady=5)

# 5. VENTANA DESCUENTOS
def abrir_descuentos():
    v5 = tk.Toplevel()
    v5.title("Descuentos")
    v5.geometry("400x250")
    v5.config(bg="#FFD93D")

    tk.Label(v5, text="DESCUENTOS", bg="#FFD93D", font=("Poppins", 14, "bold")).pack(pady=10)
    texto = registro.mostrar_descuentos()
    caja_texto = tk.Text(v5, height=8, width=45, font=("Poppins", 9))
    caja_texto.pack()
    caja_texto.insert(tk.END, texto)

# 6. VENTANA ESTERILIZAR
def abrir_esterilizar():
    v6 = tk.Toplevel()
    v6.title("Esterilización")
    v6.geometry("400x250")
    v6.config(bg="#FFD93D")

    def esterilizar():
        resultado = registro.esterilizar_mascota(e_id.get())
        resultado_label.config(text=resultado)

    tk.Label(v6, text="ESTERILIZACIÓN", bg="#FFD93D", font=("Poppins", 14, "bold")).pack(pady=10)
    tk.Label(v6, text="ID mascota:", bg="#FFD93D").pack()
    e_id = tk.Entry(v6)
    e_id.pack()
    tk.Button(v6, text="Esterilizar", command=esterilizar, bg="white").pack(pady=10)
    resultado_label = tk.Label(v6, text="", bg="white", width=40, height=3, wraplength=300)
    resultado_label.pack()

# VENTANA PRINCIPAL CON HUELLITA
menu = tk.Tk()
menu.title("Registro de Mascotas 🐾")
menu.geometry("320x480")
menu.config(bg="#FFD93D")

tk.Label(menu, text="🐾 MENU PRINCIPAL 🐾", bg="#FFD93D", font=("Poppins", 16, "bold"), fg="#FF6B35").pack(pady=20)

tk.Button(menu, text="1. Registrar mascota", command=abrir_registrar, width=25, height=2, font=("Poppins", 10)).pack(pady=5)
tk.Button(menu, text="2. Buscar mascota", command=abrir_buscar, width=25, height=2, font=("Poppins", 10)).pack(pady=5)
tk.Button(menu, text="3. Aplicar vacuna", command=abrir_vacunar, width=25, height=2, font=("Poppins", 10)).pack(pady=5)
tk.Button(menu, text="4. Centros de vacunación", command=abrir_centros, width=25, height=2, font=("Poppins", 10)).pack(pady=5)
tk.Button(menu, text="5. Ver descuentos", command=abrir_descuentos, width=25, height=2, font=("Poppins", 10)).pack(pady=5)
tk.Button(menu, text="6. Esterilización", command=abrir_esterilizar, width=25, height=2, font=("Poppins", 10)).pack(pady=5)
tk.Button(menu, text="7. Salir", command=menu.destroy, width=25, height=2, bg="#FF6B6B", fg="white", font=("Poppins", 10)).pack(pady=10)

menu.mainloop()
