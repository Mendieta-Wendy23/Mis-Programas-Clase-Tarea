import tkinter as tk  # Importamos tkinter para crear ventanas

# Creamos un diccionario llamado alumno
alumno = {

    "nombre": "Wendy",  # Guardamos el nombre del alumno

    "carrera": "Programacion",  # Guardamos la carrera

    "semestre": 2  # Guardamos el semestre
}

# Creamos la ventana principal
v = tk.Tk()

v.title("Datos del Alumno")  # Titulo de la ventana

v.geometry("400x300")  # Tamaño de la ventana

v.configure(background="#B39DDB")  # Color de fondo

# Creamos un titulo
titulo = tk.Label(v,
                  text="Informacion del Alumno",
                  font=("Lucida Console", 14),
                  bg="#B39DDB")

titulo.pack(pady=15)

# Mostramos el nombre guardado en el diccionario
nombre = tk.Label(v,
                  text="Nombre: " + alumno["nombre"],
                  font=("Lucida Console", 11),
                  bg="#B39DDB")

nombre.pack(pady=10)

# Mostramos la carrera guardada en el diccionario
carrera = tk.Label(v,
                   text="Carrera: " + alumno["carrera"],
                   font=("Lucida Console", 11),
                   bg="#B39DDB")

carrera.pack(pady=10)

# Mostramos el semestre guardado en el diccionario
semestre = tk.Label(v,
                    text="Semestre: " + str(alumno["semestre"]),
                    font=("Lucida Console", 11),
                    bg="#B39DDB")

semestre.pack(pady=10)

# Mantiene la ventana abierta
v.mainloop()
