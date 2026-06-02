 #Importar la librería para crear la ventana
import tkinter as tk

# Lista donde se guardarán las mascotas registradas
mascotas = []

# Función para registrar una mascota
def registrar_mascota():

    # Obtener los datos escritos por el usuario
    nombre = entrada_nombre.get()
    especie = entrada_especie.get()
    edad = entrada_edad.get()
    tamano = entrada_tamano.get()

    # Guardar los datos en la lista
    mascotas.append({
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "tamano": tamano
    })

    # Mostrar mensaje de registro
    resultado.config(text="Mascota registrada correctamente")

# Función para buscar una mascota
def buscar_mascota():

    # Obtener el nombre a buscar
    nombre = entrada_nombre.get()

    # Recorrer la lista de mascotas
    for mascota in mascotas:

        # Comparar el nombre escrito con el nombre registrado
        if mascota["nombre"] == nombre:

            # Mostrar los datos de la mascota encontrada
            resultado.config(
                text="Nombre: " + mascota["nombre"] +
                "\nEspecie: " + mascota["especie"] +
                "\nEdad: " + mascota["edad"] +
                "\nTamaño: " + mascota["tamano"]
            )
            return

    # Mensaje si no se encuentra la mascota
    resultado.config(text="Mascota no encontrada")

# Función para aplicar vacuna
def aplicar_vacuna():

    # Mostrar mensaje de vacuna aplicada
    resultado.config(text="Vacuna aplicada correctamente")

# Función para verificar esterilización
def esterilizacion():

    # Obtener la edad
    edad = int(entrada_edad.get())

    # Verificar si tiene la edad recomendada
    if edad >= 6:
        resultado.config(text="La mascota puede ser esterilizada")
    else:
        resultado.config(text="La mascota aun no cumple la edad recomendada")

# Función para mostrar descuentos
def descuentos():

    resultado.config(
        text="1. Vacuna antirrabica 20% descuento\n"
             "2. Triple felina + juguete gratis\n"
             "3. Baño gratis segunda vacuna\n"
             "4. Consulta gratis esquema completo"
    )

# Función para mostrar centros de vacunación
def centros():

    resultado.config(
        text="Apizaco:\n"
             "Veterinaria Apizaco Centro\n"
             "Clinica Animal San Martin"
    )

# Crear la ventana principal
ventana = tk.Tk()

# Título de la ventana
ventana.title("Veterinaria")

# Tamaño de la ventana
ventana.geometry("600x500")

# Color de fondo
ventana.config(bg="#C1E1C1")

# Título principal del sistema
tk.Label(
    ventana,
    text="SISTEMA DE VACUNACION DE MASCOTAS",
    bg="#C1E1C1",
    font=("Arial", 14, "bold")
).pack(pady=10)

# Etiqueta y caja de texto para nombre
tk.Label(ventana, text="Nombre", bg="#C1E1C1").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

# Etiqueta y caja de texto para especie
tk.Label(ventana, text="Especie", bg="#C1E1C1").pack()
entrada_especie = tk.Entry(ventana)
entrada_especie.pack()

# Etiqueta y caja de texto para edad
tk.Label(ventana, text="Edad", bg="#C1E1C1").pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

# Etiqueta y caja de texto para tamaño
tk.Label(ventana, text="Tamaño", bg="#C1E1C1").pack()
entrada_tamano = tk.Entry(ventana)
entrada_tamano.pack()

# Botón para registrar mascota
tk.Button(
    ventana,
    text="Registrar Mascota",
    command=registrar_mascota
).pack(pady=5)

# Botón para buscar mascota
tk.Button(
    ventana,
    text="Buscar Mascota",
    command=buscar_mascota
).pack(pady=5)

# Botón para aplicar vacuna
tk.Button(
    ventana,
    text="Aplicar Vacuna",
    command=aplicar_vacuna
).pack(pady=5)

# Botón para esterilización
tk.Button(
    ventana,
    text="Esterilizacion",
    command=esterilizacion
).pack(pady=5)

# Botón para ver descuentos
tk.Button(
    ventana,
    text="Ver Descuentos",
    command=descuentos
).pack(pady=5)

# Botón para mostrar centros de vacunación
tk.Button(
    ventana,
    text="Centros de Vacunacion",
    command=centros
).pack(pady=5)

# Botón para cerrar el programa
tk.Button(
    ventana,
    text="Salir",
    command=ventana.destroy
).pack(pady=5)

# Etiqueta donde se mostrarán resultados y mensajes
resultado = tk.Label(
    ventana,
    text="",
    bg="#C1E1C1"
)
resultado.pack(pady=15)

# Mantener la ventana abierta
ventana.mainloop()  
