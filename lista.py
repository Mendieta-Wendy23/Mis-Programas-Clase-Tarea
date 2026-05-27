usuario1=["Wendy","2025-2026","Programacion","648375"]
usuario2=["Ayelen","2025-2026","Turismo","629493"]
print("De que usuario desea saber informacion?")
print("Usuario 1")
print("Usuario 2")
eleccion=int(input("Ingrese 1 o 2 segun su preferencia : "))
if eleccion==1:
    print("Datos del primer usuario")
    print("Nombre: ",usuario1[0])
    print("Ciclo: ",usuario1[1])
    print("Especialidad: ",usuario1[2])
    print("Matricula: ",usuario1[3])
elif eleccion==2:
    print("Datos del segundo usuario")
    print("Nombre: ",usuario2[0])
    print("Ciclo: ",usuario2[1])
    print("Especialidad: ",usuario2[2])
    print("Matricula: ",usuario2[3])
else:
    print("Opcion no valida")
