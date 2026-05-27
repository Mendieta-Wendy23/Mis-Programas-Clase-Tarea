import tkinter as tk
v = tk.Tk()
v. title("Edad para votar")
v.geometry("300x400")
v.configure(background="#E36B2C")
def verificar():
    if int(en.get()) >=18:
        r.config(text="Ya puede votar")
e=tk.Label(v, text="Ingrese su edad", font=("Franklin Gothic Demi Cond", 12))
e.pack(padx=5, pady=10)
en=tk.Entry()
en.pack(padx=10, pady=20)
r=tk.Label(v, font=("Franklin Gothic Demi Cond", 12))
r.pack()
b=tk.Button(v,
            text="verificar",
                  command=verificar
)
b.pack()
v.mainloop()
