import tkinter as tk
v = tk. Tk()
v.title("Verificacion de clave")
v.geometry("500x500")
v.configure(background="#809bce")
c = tk.Label(v, text="Ingrese la clave: ", font=("Lucida Console", 12))
c.pack(padx=5, pady=10)
en =tk.Entry(v, show="")
en.pack(padx=10, pady=20)
r = tk. Label(v, text="", font=("Lucida Console", 12))
r.pack()
b= tk.Button(v,
             text="comprobar",
             command=lambda: r.config(
                 text=("incorrecta","Acceso concedido")[en.get() == "1709"]
             ))
b.pack()
v.mainloop()
