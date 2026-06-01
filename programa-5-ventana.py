import tkinter as tk

def sumar():
    sumando1 = float(entrada1.get())
    sumando2 = float(entrada2.get())
    resultado.config(text="Resultado de la suma: " + str(sumando1 + sumando2))

ventana = tk.Tk()
ventana.title("Suma de Decimales")
ventana.geometry("350x250")
ventana.config(bg="#C1E1C1")

tk.Label(ventana, text="Primer sumando:", bg="#C1E1C1").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Segundo sumando:", bg="#C1E1C1").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Sumar", command=sumar).pack(pady=10)

resultado = tk.Label(ventana, text="", bg="#C1E1C1")
resultado.pack(pady=10)

ventana.mainloop()
