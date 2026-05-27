import tkinter as tk  # Importamos la librería tkinter para crear ventanas

v = tk.Tk()  # Creamos la ventana principal
v.title("Tabla de multiplicar")  # Título que sale arriba en la ventana
v.geometry("300x400")  # Tamaño de la ventana: 300 de ancho x 400 de alto
v.configure(background="#809bce")  # Color de fondo de la ventana en hexadecimal

e = tk.Label(v, text="Ingresa un numero:", font=("Lucida Console", 12))  #pide que el usuario ingrese un numero
e.pack(padx=5, pady=10)  # 5 horizontal y 10 vertical de espacio

en = tk.Entry(v)  # cuadro de texto donde el usuario escribe el número
en.pack(padx=10, pady=10)  

r = tk.Label(v, text="", font=("Lucida Console", 10), justify="left")  # Aqui saldrá la tabla
r.pack(padx=10, pady=10)  # justify="left" alinea el texto a la izquierda

def tabla():  # Función que se ejecuta al dar clic al botón
    num = int(en.get())  # Agarramos lo que escribió el usuario y lo convertimos a número entero
    texto = ""  # Aqui iremos guardando cada línea de la tabla
    for i in range(1, 11):  # Ciclo for que va del 1 al 10
        resultado = num * i  # Multiplicamos el número por i (variable de control)
        texto += f"{num} x {i} = {resultado}\n" #Muestra el resultado
        r.config(text=texto)
b = tk.Button(v, text=" Multiplicar", command=tabla)#Creamos el boton que tendra como nombre multiplicar
b.pack(pady=10)#Le ponemos espacio vertical
v.mainloop()
