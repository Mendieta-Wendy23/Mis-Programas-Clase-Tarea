import tkinter as tk  # Importamos tkinter para crear ventanas

contador = 1  # Variable que empezará en 1

v = tk.Tk()  # Creamos la ventana principal
v.title("While True")  # Título de la ventana
v.geometry("300x300")  # Tamaño de la ventana
v.configure(background="#809bce")  # Color de fondo

e = tk.Label(v, text="Presiona el boton", font=("Lucida Console", 12))#Titulo de la ventana
e.pack(padx=5, pady=10)#espacio de ancho por largo

r = tk.Label(v, text="", font=("Lucida Console", 10))
r.pack(padx=10, pady=10)

def mostrar():  # Función del botón

    global contador# Se usa para poder modificar la variable contador que fue creada fuera de la funcion

    while True:# Creamos un ciclo infinito

        r.config(text="Numero: " + str(contador))

        contador = contador + 1# Aumentamos el contador en 1 

        break

b = tk.Button(v, text="Mostrar numero", command=mostrar)# Creamos un boton que ejecuta la funcion mostrar
b.pack(pady=10)# Agregamos espacio vertical al boton

v.mainloop()# Mantiene la ventana abierta funcionando
