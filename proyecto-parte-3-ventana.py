import tkinter as tk
from tkinter import messagebox

mascotas = []

def registrar_mascota():
    nombre = entrada_nombre.get()
    especie = entrada_especie.get()
    edad = entrada_edad.get()
    tamano = entrada_tamano.get()

    mascotas.append({
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "tamano": tamano
    })

    messagebox.showinfo(
        "Registro",
        "Mascota registrada correctamente"
    )

def buscar_mascota():
    nombre = entrada_nombre.get()

    for mascota in mascotas:
        if mascota["nombre"].lower() == nombre.lower():

            resultado.config(
                text=f"Nombre: {mascota['nombre']}\n"
                     f"Especie: {mascota['especie']}\n"
                     f"Edad: {mascota['edad']}\n"
                     f"Tamaño: {mascota['tamano']}"
            )
            return

    resultado.config(text="Mascota no encontrada")

def aplicar_vacuna():
    messagebox.showinfo(
        "Vacunación",
        "Vacuna registrada correctamente"
    )

def esterilizacion():
    edad = int(entrada_edad.get())

    if edad >= 6:
        messagebox.showinfo(
            "Esterilización",
            "La mascota puede ser esterilizada"
        )
    else:
        messagebox.showwarning(
            "Esterilización",
            "La mascota aún no cumple la edad recomendada"
        )

def descuentos():

    texto = (
        "1. Vacuna antirrábica 20% descuento\n"
        "2. Triple felina + juguete gratis\n"
        "3. Baño gratis segunda vacuna\n"
        "4. Consulta gratis esquema completo"
    )

    resultado.config(text=texto)

def centros():

    texto = (
        "Apizaco:\n"
        "Veterinaria Apizaco Centro\n"
        "Clínica Animal San Martín"
    )

    resultado.config(text=texto)

ventana = tk.Tk()
ventana.title("Veterinaria")
ventana.geometry("600x500")
ventana.config(bg="#C1E1C1")

tk.Label(
    ventana,
    text="SISTEMA DE VACUNACIÓN DE MASCOTAS",
    bg="#C1E1C1",
    font=("Arial", 14, "bold")
).pack(pady=10)

tk.Label(ventana, text="Nombre", bg="#C1E1C1").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Especie", bg="#C1E1C1").pack()
entrada_especie = tk.Entry(ventana)
entrada_especie.pack()

tk.Label(ventana, text="Edad", bg="#C1E1C1").pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

tk.Label(ventana, text="Tamaño", bg="#C1E1C1").pack()
entrada_tamano = tk.Entry(ventana)
entrada_tamano.pack()

tk.Button(
    ventana,
    text="Registrar Mascota",
    command=registrar_mascota
).pack(pady=5)

tk.Button(
    ventana,
    text="Buscar Mascota",
    command=buscar_mascota
).pack(pady=5)

tk.Button(
    ventana,
    text="Aplicar Vacuna",
    command=aplicar_vacuna
).pack(pady=5)

tk.Button(
    ventana,
    text="Esterilización",
    command=esterilizacion
).pack(pady=5)

tk.Button(
    ventana,
    text="Ver Descuentos",
    command=descuentos
).pack(pady=5)

tk.Button(
    ventana,
    text="Centros de Vacunación",
    command=centros
).pack(pady=5)

tk.Button(
    ventana,
    text="Salir",
    command=ventana.destroy
).pack(pady=5)

resultado = tk.Label(
    ventana,
    text="",
    bg="#C1E1C1"
)
resultado.pack(pady=15)

ventana.mainloop()
