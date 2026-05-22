import tkinter as tk
def nose(): 
    
    match (str(entrada.get())):
        case "Lunes": r.configure(text="Apenas empieza la semana resiste!!")
        case "Martes":r.configure(text="Ya pasó un dia, vamos!!")
        case "Miercoles":r.configure(text="Ombligo de la semana")
        case "Jueves": r.configure(text="Falta un día más!!")
        case "Viernes": r.configure(text="Ultimo día!!")
        case "Sabado": r.configure(text="Por fin, fin de semana!!")
        case "Domingo": r.configure(text="Disfruta!!")
        case _: r.configure(text="No valido")
    

v= tk.Tk()
v.title("If")
v.geometry("800x550")
v.configure(background="#E8F5E9")
e=tk.Label(v, text="Día de la semana", font=("Gadugi", 12))
e.pack(padx=5,pady=10)
entrada =tk.Entry()
entrada.pack(padx=10,pady=10)

r=tk.Label(v,text=" ",font=("Gadugi", 12))
r.pack()

b=tk.Button( v, 
            text="Frase",
            command=nose
        )
b.pack()
v.mainloop()
