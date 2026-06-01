import tkinter as tk

def mostrar_mensaje():
    resultado.config(text="¡Hola Time of Software!\nEste es mi primer programa con Python")

ventana = tk.Tk()
ventana.title("Mi Primer Programa")
ventana.geometry("350x200")
ventana.config(bg="#C1E1C1")

titulo = tk.Label(ventana, text="Programa de Bienvenida", bg="#C1E1C1")
titulo.pack(pady=10)

boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton.pack(pady=10)

resultado = tk.Label(ventana, text="", bg="#C1E1C1")
resultado.pack(pady=10)

ventana.mainloop()
