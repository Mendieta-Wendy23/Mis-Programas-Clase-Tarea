dia=input("Dia de la semana: ")

match dia:
    case "Lunes":
       print("Apenas empieza la semana")
    case "Martes": 
       print("Ya paso un dia, vamos!!")
    case "Miercoles":
      print("Ombligo de la semana")
    case "Jueves":
      print("Falta un dia mas!!")
    case "Viernes":
      print("Ultimo dia!!")
    case "Sabado":
      print("Por fin fin de semana!!")
    case "Domingo":
      print("Disfrura!!")
    case _:
      print("No valido")
