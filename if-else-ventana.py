import tkinter as tk 
v= tk.Tk()
v.title("If")
v.geometry("800x550")
v.configure(background="#E8F5E9")
e=tk.Label(v, text="Edad", font=("Gadugi", 12))
e.pack(padx=5,pady=10)
entrada =tk.Entry()
entrada.pack(padx=10,pady=10)
r=tk.Label(v, text=":)", font=("Gadugi", 12))
r.pack()
b=tk.Button( v, 
            text="¿Mayor de edad?",
            command=lambda: r.config(
                text="Mayor de edad" if int(entrada.get())>=18 else "Menor de edad"
            )
        )
b.pack()
v.mainloop()
