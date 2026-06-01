import tkinter as tk

def restar():
    minuendo = int(entrada1.get())
    sustraendo = int(entrada2.get())
    resultado.config(text="Resultado de la resta: " + str(minuendo - sustraendo))

ventana = tk.Tk()
ventana.title("Resta de Enteros")
ventana.geometry("350x250")
ventana.config(bg="#C1E1C1")

tk.Label(ventana, text="Introduzca el minuendo:", bg="#C1E1C1").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Introduzca el sustraendo:", bg="#C1E1C1").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Restar", command=restar).pack(pady=10)

resultado = tk.Label(ventana, text="", bg="#C1E1C1")
resultado.pack(pady=10)

ventana.mainloop()
