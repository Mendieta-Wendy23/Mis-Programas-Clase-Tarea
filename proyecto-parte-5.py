import tkinter as tk  # Importamos tkinter para hacer la ventana

# CLASE MASCOTA: Es el molde para guardar los datos de cada animal
class Mascota:
    # __init__ se ejecuta cuando creas una mascota nueva
    def __init__(self, nombre, especie, edad, tamano, peso, raza, enfermedad, dueno, telefono, direccion, ciudad):
        self.nombre = nombre          # Guardamos el nombre
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

    # Función para mostrar todos los datos en texto
    def mostrar_datos(self):
        datos = "----- DATOS DE LA MASCOTA -----\n"
        datos += "Nombre: " + self.nombre + "\n"
        datos += "Especie: " + self.especie + "\n"
        datos += "Edad: " + str(self.edad) + "\n"
        datos += "Tamaño: " + self.tamano + "\n"
        datos += "Peso: " + str(self.peso) + "\n"
        datos += "Raza: " + self.raza + "\n"
        datos += "Enfermedad: " + self.enfermedad + "\n"
        datos += "Dueño: " + self.dueno + "\n"
        datos += "Telefono: " + self.telefono + "\n"
        datos += "Direccion: " + self.direccion + "\n"
        datos += "Ciudad: " + self.ciudad + "\n"
        datos += "Esterilizada: " + str(self.esterilizada) + "\n"
        datos += "Vacunas: " + str(self.vacunas)
        return datos  # Regresamos todo el texto junto

# CLASE VETERINARIA: Aquí guardamos todas las mascotas y las funciones
class Veterinaria:
    def __init__(self):
        self.mascotas = []  # Lista vacía donde se guardan todas las mascotas

    # Función para registrar una mascota nueva
    def registrar_mascota(self, nombre, especie, edad, tamano, peso, raza, enfermedad, dueno, telefono, direccion, ciudad):
        # Creamos el objeto mascota con los datos que llegaron
        mascota = Mascota(nombre, especie, int(edad), tamano, float(peso), raza, enfermedad, dueno, telefono, direccion, ciudad)
        self.mascotas.append(mascota)  # La metemos a la lista
        return "Mascota registrada correctamente"

    # Función para buscar una mascota por nombre
    def buscar_mascota(self, nombre):
        for mascota in self.mascotas:  
            if mascota.nombre.lower() == nombre.lower(): 
                return mascota.mostrar_datos()  
        return "Mascota no encontrada"  

    # Función para agregar una vacuna a una mascota
    def aplicar_vacuna(self, nombre, vacuna):
        for mascota in self.mascotas:
            if mascota.nombre.lower() == nombre.lower():
                mascota.vacunas.append(vacuna)  # Agregamos la vacuna a su lista
                return "Vacuna registrada"
        return "Mascota no encontrada"

    # Función para esterilizar, solo si tiene 6 meses o más
    def esterilizar_mascota(self, nombre):
        for mascota in self.mascotas:
            if mascota.nombre.lower() == nombre.lower():
                if mascota.edad >= 6:  
                    mascota.esterilizada = True  
                    return "La mascota puede ser esterilizada\nEsterilización registrada"
                else:
                    return "La mascota aún no cumple la edad recomendada"
        return "Mascota no encontrada"

    # Función que regresa el texto de los descuentos
    def mostrar_descuentos(self):
        texto = "------ DESCUENTOS ------\n"
        texto += "1. Vacuna antirrábica con 20% de descuento\n"
        texto += "2. Vacuna triple felina con juguete gratis\n"
        texto += "3. Baño gratis en la segunda vacuna\n"
        texto += "4. Consulta gratis en vacunación completa"
        return texto

    # Función que regresa centros según la ciudad
    def centros_vacunacion(self, ciudad):
        texto = ""
        if ciudad.lower() == "apizaco":
            texto = "Veterinaria Apizaco Centro\nClínica Animal San Martín"
        elif ciudad.lower() == "tlaxcala":
            texto = "Veterinaria Tlaxcala Centro\nPatitas Felices"
        elif ciudad.lower() == "nativitas":
            texto = "Veterinaria Nativitas\nAnimal Care Nativitas"
        elif ciudad.lower() == "texoloc":
            texto = "Veterinaria Texoloc\nHuellitas Texoloc"
        else:
            texto = "No hay centros registrados"
        return texto

# VENTANA PRINCIPAL 
v = tk.Tk()  # Creamos la ventana
v.title("Sistema de Vacunación de Mascotas")  # Título de la ventana
v.geometry("600x700")  # Tamaño: 600 de ancho x 700 de alto
v.config(bg="#ADD8E6")  # Color de fondo azul pastel

vet = Veterinaria()  # Creamos el objeto veterinaria para usar sus funciones

# FUNCIONES DE LOS BOTONES
# Cada botón ejecuta una de estas funciones

def registrar():
    # .get() agarra el texto que escribió el usuario en cada caja
    resultado = vet.registrar_mascota(
        e_nombre.get(), e_especie.get(), e_edad.get(), e_tamano.get(),
        e_peso.get(), e_raza.get(), e_enfermedad.get(), e_dueno.get(),
        e_telefono.get(), e_direccion.get(), e_ciudad.get()
    )
    caja_resultado.delete("1.0", tk.END)  # Borramos lo que había en la caja de resultado
    caja_resultado.insert(tk.END, resultado)  # Ponemos el nuevo resultado
    # Borramos todas las cajas para que queden vacías otra vez
    e_nombre.delete(0, tk.END)
    e_especie.delete(0, tk.END)
    e_edad.delete(0, tk.END)
    e_tamano.delete(0, tk.END)
    e_peso.delete(0, tk.END)
    e_raza.delete(0, tk.END)
    e_enfermedad.delete(0, tk.END)
    e_dueno.delete(0, tk.END)
    e_telefono.delete(0, tk.END)
    e_direccion.delete(0, tk.END)
    e_ciudad.delete(0, tk.END)

def buscar():
    resultado = vet.buscar_mascota(e_buscar.get())  # Buscamos con lo que escribió
    caja_resultado.delete("1.0", tk.END)
    caja_resultado.insert(tk.END, resultado)  # Mostramos el resultado
    e_buscar.delete(0, tk.END)  # Borramos la caja

def vacunar():
    resultado = vet.aplicar_vacuna(e_vacuna_nombre.get(), e_vacuna.get())
    caja_resultado.delete("1.0", tk.END)
    caja_resultado.insert(tk.END, resultado)
    e_vacuna_nombre.delete(0, tk.END)
    e_vacuna.delete(0, tk.END)

def esterilizar():
    resultado = vet.esterilizar_mascota(e_esterilizar.get())
    caja_resultado.delete("1.0", tk.END)
    caja_resultado.insert(tk.END, resultado)
    e_esterilizar.delete(0, tk.END)

def ver_descuentos():
    resultado = vet.mostrar_descuentos()  # No ocupa datos, solo muestra texto
    caja_resultado.delete("1.0", tk.END)
    caja_resultado.insert(tk.END, resultado)

def ver_centros():
    resultado = vet.centros_vacunacion(e_centro.get())
    caja_resultado.delete("1.0", tk.END)
    caja_resultado.insert(tk.END, resultado)
    e_centro.delete(0, tk.END)

tk.Label(v, text="SISTEMA VETERINARIA", bg="#ADD8E6", font=("Arial", 14, "bold")).pack(pady=5)

# SECCIÓN REGISTRAR MASCOTA
tk.Label(v, text="--- REGISTRAR MASCOTA ---", bg="#ADD8E6", font=("Arial", 12)).pack()

tk.Label(v, text="Nombre:", bg="#ADD8E6").pack()  
e_nombre = tk.Entry(v)  
e_nombre.pack() 

tk.Label(v, text="Especie (Perro/Gato):", bg="#ADD8E6").pack()
e_especie = tk.Entry(v); e_especie.pack()

tk.Label(v, text="Edad:", bg="#ADD8E6").pack()
e_edad = tk.Entry(v); e_edad.pack()

tk.Label(v, text="Tamaño:", bg="#ADD8E6").pack()
e_tamano = tk.Entry(v); e_tamano.pack()

tk.Label(v, text="Peso:", bg="#ADD8E6").pack()
e_peso = tk.Entry(v); e_peso.pack()

tk.Label(v, text="Raza:", bg="#ADD8E6").pack()
e_raza = tk.Entry(v); e_raza.pack()

tk.Label(v, text="Enfermedad:", bg="#ADD8E6").pack()
e_enfermedad = tk.Entry(v); e_enfermedad.pack()

tk.Label(v, text="Dueño:", bg="#ADD8E6").pack()
e_dueno = tk.Entry(v); e_dueno.pack()

tk.Label(v, text="Telefono:", bg="#ADD8E6").pack()
e_telefono = tk.Entry(v); e_telefono.pack()

tk.Label(v, text="Direccion:", bg="#ADD8E6").pack()
e_direccion = tk.Entry(v); e_direccion.pack()

tk.Label(v, text="Ciudad:", bg="#ADD8E6").pack()
e_ciudad = tk.Entry(v); e_ciudad.pack()

# Botón: command=registrar significa que ejecuta la función registrar() cuando le das clic
tk.Button(v, text="Registrar Mascota", command=registrar, bg="white").pack(pady=5)

# SECCIÓN BUSCAR
tk.Label(v, text="Nombre a buscar:", bg="#ADD8E6").pack(pady=(10,0))
e_buscar = tk.Entry(v); e_buscar.pack()
tk.Button(v, text="Buscar Mascota", command=buscar, bg="white").pack(pady=2)

# SECCIÓN VACUNA
tk.Label(v, text="Nombre mascota:", bg="#ADD8E6").pack(pady=(5,0))
e_vacuna_nombre = tk.Entry(v); e_vacuna_nombre.pack()
tk.Label(v, text="Vacuna aplicada:", bg="#ADD8E6").pack()
e_vacuna = tk.Entry(v); e_vacuna.pack()
tk.Button(v, text="Aplicar Vacuna", command=vacunar, bg="white").pack(pady=2)

# SECCIÓN ESTERILIZAR
tk.Label(v, text="Nombre a esterilizar:", bg="#ADD8E6").pack(pady=(5,0))
e_esterilizar = tk.Entry(v); e_esterilizar.pack()
tk.Button(v, text="Esterilizar", command=esterilizar, bg="white").pack(pady=2)

# SECCIÓN CENTROS
tk.Label(v, text="Ciudad:", bg="#ADD8E6").pack(pady=(5,0))
e_centro = tk.Entry(v); e_centro.pack()
tk.Button(v, text="Ver Centros", command=ver_centros, bg="white").pack(pady=2)

# BOTÓN DESCUENTOS
tk.Button(v, text="Ver Descuentos", command=ver_descuentos, bg="white").pack(pady=5)

# RESULTADOs:
tk.Label(v, text="RESULTADO:", bg="#ADD8E6", font=("Arial", 11, "bold")).pack()
caja_resultado = tk.Text(v, height=8, width=60) 
caja_resultado.pack(pady=5)

v.mainloop()  # Esto hace que la ventana no se cierre y esté esperando clics
