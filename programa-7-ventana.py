import tkinter as tk

def restar():
    minuendo = float(entrada1.get())
    sustraendo = float(entrada2.get())
    resultado.config(text="Resultado de la resta: " + str(minuendo - sustraendo))

ventana = tk.Tk()
ventana.title("Resta de Números")
ventana.geometry("350x250")
ventana.config(bg="#C1E1C1")

tk.Label(ventana, text="Minuendo:", bg="#C1E1C1").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Sustraendo:", bg="#C1E1C1").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Restar", command=restar).pack(pady=10)

resultado = tk.Label(ventana, text="", bg="#C1E1C1")
resultado.pack(pady=10)

ventana.mainloop()
