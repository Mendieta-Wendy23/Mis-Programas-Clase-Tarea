# EJERCICIO 2 - PYTHON
# Diccionario para buscar productos
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

productos = {
    "A001": Producto("Lapiz", 8.50),
    "A002": Producto("Cuaderno", 35.00),
    "A003": Producto("Pluma", 12.00)
}

print("Codigos disponibles:")
print("A001 = Lapiz")
print("A002 = Cuaderno")
print("A003 = Pluma")
codigo = input("Codigo a buscar: ")

if codigo in productos:
    producto = productos[codigo]
    print("Producto:", producto.nombre) 
    print("Precio: $", producto.precio)
else:
    print("Codigo no encontrado")
