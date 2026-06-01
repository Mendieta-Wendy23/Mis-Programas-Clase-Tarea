import tkinter as tk

def mostrar():
    cadenaejemplo = "Hola Time of Software\nEsto es una cadena\nmultilinea"
    resultado.config(text=cadenaejemplo)

ventana = tk.Tk()
ventana.title("Cadena Multilínea")
ventana.geometry("350x250")
ventana.config(bg="#C1E1C1")

tk.Label(ventana, text="Ejemplo de Cadena Multilínea", bg="#C1E1C1").pack(pady=10)

tk.Button(ventana, text="Mostrar Texto", command=mostrar).pack(pady=10)

resultado = tk.Label(ventana, text="", bg="#C1E1C1")
resultado.pack(pady=10)

ventana.mainloop()
