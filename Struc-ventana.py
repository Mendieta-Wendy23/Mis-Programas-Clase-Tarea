import tkinter as tk

class Alumno:
    def __init__(self, nombre, carrera, semestre):
        self.nombre = nombre
        self.carrera = carrera
        self.semestre = semestre

v = tk.Tk()
v.title("Registro")
v.geometry("800x550")
v.configure(background="#C19ADE")

a = tk.Label(v, text="Nombre", font=("Eras Demi ITC", 12))
a.pack(padx=5, pady=10)

entrada_nombre = tk.Entry()
entrada_nombre.pack(padx=10, pady=10)

a = tk.Label(v, text="Carrera", font=("Eras Demi ITC", 12))
a.pack(padx=5, pady=10)

entrada_carrera = tk.Entry()
entrada_carrera.pack(padx=10, pady=10)

a = tk.Label(v, text="Semestre", font=("Eras Demi ITC", 12))
a.pack(padx=5, pady=10)

entrada_semestre = tk.Entry()
entrada_semestre.pack(padx=10, pady=10)
r = tk.Label(v, font=("Eras Demi ITC", 12))
r.pack()

b = tk.Button(
    v,
    text="Registrar",
    command=lambda: r.config(
        text=f"Nombre: {entrada_nombre.get()}\n"
             f"Carrera: {entrada_carrera.get()}\n"
             f"Semestre: {entrada_semestre.get()}"
    )
)

b.pack()

v.mainloop()
