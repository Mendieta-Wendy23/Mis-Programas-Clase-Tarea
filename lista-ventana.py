import tkinter as tk
from tkinter import messagebox

v = tk.Tk()
v.title("Consulta de Usuarios")
v.geometry("400x350")
v.configure(background="#809bce")

usuario1 = ["wendy", "2025-2026", "programacion", "648375"]
usuario2 = ["Ayelen", "2025-2026", "Turismo", "629493"]

tk.Label(v, text="¿De qué usuario deseas saber información?",
         font=("Lucida Console", 12), bg="#809bce").pack(pady=15)

resultado = tk.Label(v, text="Selecciona una opción",
                     font=("Lucida Console", 11), bg="#809bce", justify="left")
resultado.pack(pady=20)

def mostrar_usuario1():
    texto = f"Datos del primer usuario\nNombre: {usuario1[0]}\nCiclo: {usuario1[1]}\nEspecialidad: {usuario1[2]}\nMatrícula: {usuario1[3]}"
    resultado.config(text=texto)

def mostrar_usuario2():
    texto = f"Datos del segundo usuario\nNombre: {usuario2[0]}\nCiclo: {usuario2[1]}\nEspecialidad: {usuario2[2]}\nMatrícula: {usuario2[3]}"
    resultado.config(text=texto)

def opcion_invalida():
    messagebox.showerror("Error", "Opción no válida. Solo hay usuario 1 y 2")

tk.Button(v, text="Usuario 1 - Wendy", command=mostrar_usuario1,
          font=("Lucida Console", 10)).pack(pady=5)

tk.Button(v, text="Usuario 2 - Ayelen", command=mostrar_usuario2,
          font=("Lucida Console", 10)).pack(pady=5)

tk.Button(v, text="Probar opción 3", command=opcion_invalida,
          font=("Lucida Console", 10)).pack(pady=5)

v.mainloop()
