def cuadrado(l):
    ac = l * l
    return ac
def triangulo(b, h):
    at = (b * h) / 2
    return at
def rectangulo(b, h):
    ar = (b * h)
    return ar

def main():
    print("PROGRAMA DE AREAS DE FIGURAS")
    opcion = 0
    while opcion != 4:
        print("\nElija la figura que desea")
        print("1. Area de triangulo")
        print("2. Area de rectangulo")
        print("3. Area de cuadrado")
        print("4. Salir")
        opcion = int(input("Opcion: "))

        match opcion:
            case 1:
                print("1. Eligio el area del triangulo")
                bt = int(input("Ingrese la base: "))
                ht = int(input("Ingrese la altura: "))
                resultado = triangulo(bt, ht)
                print("El area es:", resultado)
            case 2:
                print("2. Eligio el area del rectangulo")
                br = int(input("Ingrese la base: "))
                hr = int(input("Ingrese la altura: "))
                resultado = rectangulo(br, hr)
                print("El area es:", resultado)
            case 3:
                print("3. Eligio el area del cuadrado")
                lado = int(input("Ingrese el lado: "))
                resultado = cuadrado(lado)
                print("El area es:", resultado)
            case 4:
                print("Gracias por usar el sistema")
            case _:
                print("Opcion no valida")
main()
