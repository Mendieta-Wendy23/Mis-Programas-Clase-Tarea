import tkinter as tk

def mostrar():
    lista = ["ordenador", "teclado", "raton"]
    resultado.config(text=str(lista))

ventana = tk.Tk()
ventana.title("Lista")
ventana.geometry("350x200")
ventana.config(bg="#C1E1C1")

tk.Label(ventana, text="Ejemplo de Lista", bg="#C1E1C1").pack(pady=10)

tk.Button(ventana, text="Mostrar Lista", command=mostrar).pack(pady=10)

resultado = tk.Label(ventana, text="", bg="#C1E1C1")
resultado.pack(pady=10)

ventana.mainloop()
