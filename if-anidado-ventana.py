import tkinter as tk
v=tk.Tk()
v.title("Calificaciones")
v.geometry("500x600")
v.configure(background="#7cbfb6")
c=tk.Label(v, text="Ingrese su calificacion de 0-10:", font=("Malgun Gothic", 12))
c.pack(padx=5, pady=10)
ent=tk.Entry()
ent.pack(padx=10, pady=20)
r=tk.Label(v, text="", font=("Malgun Gothic", 12))
r.pack()
b=tk.Button(v,
            text="Evaluar calificacion",
            command=lambda: r.config(
                text="Excelente" if int(ent.get())>=9
                else "Aprobaste" if int(ent.get())>=6
                else "Reprobaste"
            )
            
 )
b.pack()
v.mainloop()
