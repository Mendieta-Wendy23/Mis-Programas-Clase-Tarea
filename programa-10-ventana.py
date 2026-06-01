import tkinter as tk

def dividir():
    dividendo = int(entrada1.get())
    divisor = int(entrada2.get())
    resultado.config(text="Resultado de la división: " + str(dividendo / divisor))

ventana = tk.Tk()
ventana.title("División de Enteros")
ventana.geometry("350x250")
ventana.config(bg="#C1E1C1")

tk.Label(ventana, text="Introduzca el dividendo:", bg="#C1E1C1").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Introduzca el divisor:", bg="#C1E1C1").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Dividir", command=dividir).pack(pady=10)

resultado = tk.Label(ventana, text="", bg="#C1E1C1")
resultado.pack(pady=10)

ventana.mainloop()
