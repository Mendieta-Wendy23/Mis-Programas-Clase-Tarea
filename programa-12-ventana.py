import tkinter as tk

def dividir():
    dividendo = float(entrada1.get())
    divisor = float(entrada2.get())
    resultado_division = round(dividendo / divisor, 1)
    resultado.config(text="Resultado de la división: " + str(resultado_division))

ventana = tk.Tk()
ventana.title("División con Redondeo")
ventana.geometry("350x250")
ventana.config(bg="#C1E1C1")

tk.Label(ventana, text="Dividendo:", bg="#C1E1C1").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Divisor:", bg="#C1E1C1").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Dividir", command=dividir).pack(pady=10)

resultado = tk.Label(ventana, text="", bg="#C1E1C1")
resultado.pack(pady=10)

ventana.mainloop()
