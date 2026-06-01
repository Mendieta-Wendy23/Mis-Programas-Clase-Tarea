import tkinter as tk

def mostrar():
    resultado.config(text="Hola Time of Software")

ventana = tk.Tk()
ventana.title("Cadenas")
ventana.geometry("350x200")
ventana.config(bg="#C1E1C1")

tk.Label(ventana, text="Ejemplo de Cadena", bg="#C1E1C1").pack(pady=10)

tk.Button(ventana, text="Mostrar Texto", command=mostrar).pack(pady=10)

resultado = tk.Label(ventana, text="", bg="#C1E1C1")
resultado.pack(pady=10)

ventana.mainloop()
