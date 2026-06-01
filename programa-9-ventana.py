import tkinter as tk

def multiplicar():
    multiplicando = float(entrada1.get())
    multiplicador = float(entrada2.get())
    resultado.config(text="Resultado de la multiplicación: " + str(multiplicando * multiplicador))

ventana = tk.Tk()
ventana.title("Multiplicación Decimal")
ventana.geometry("350x250")
ventana.config(bg="#C1E1C1")

tk.Label(ventana, text="Multiplicando:", bg="#C1E1C1").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Multiplicador:", bg="#C1E1C1").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Multiplicar", command=multiplicar).pack(pady=10)

resultado = tk.Label(ventana, text="", bg="#C1E1C1")
resultado.pack(pady=10)

ventana.mainloop()
