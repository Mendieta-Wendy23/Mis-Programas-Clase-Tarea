import tkinter as tk

def mostrar():
    resultado.config(text="1 2 3 4 5\n1,2,3,4,5")

ventana = tk.Tk()
ventana.title("Separador")
ventana.geometry("300x200")
ventana.config(bg="#C1E1C1")

titulo = tk.Label(ventana, text="Ejemplo de sep", bg="#C1E1C1")
titulo.pack(pady=10)

boton = tk.Button(ventana, text="Mostrar", command=mostrar)
boton.pack(pady=10)

resultado = tk.Label(ventana, text="", bg="#C1E1C1")
resultado.pack(pady=10)

ventana.mainloop()
