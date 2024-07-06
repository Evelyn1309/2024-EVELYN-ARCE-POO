# Programa de un sistema básico de gestión de una tienda que incluya conceptos de pricipales de POO
# En la cual la tienda vende diferentes tipos de productos, y se busca organizar y manejar esta información de
# manera eficiente y sencilla ao`licando tambien descuentosa a los productos .
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.__nombre = nombre  # Este es un atributo privado con respecto al nombre
        self.__precio = precio  # Este es un atributo privado con respecto al precio
        self.__cantidad = cantidad  # Este es un atributo privado con respecto a la cantidad

    # Esta funcion nos permite accerder al getter de  los atributos privados
    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    #  Nos permite aceder al metodo setter para modificar los atributos privados
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        self.__precio = precio

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    # Aplicacion del polimorfismo a nuetro codigo
    def detalles(self):
        return f"Producto: {self.__nombre}, Precio: ${self.__precio}, Cantidad: {self.__cantidad}"

    #  aplicar un descuento con el metodo del polimorfismo
    def aplicar_descuento(self, porcentaje):
        self.__precio -= self.__precio * (porcentaje / 100)
        return f"Tolal a pagar  tras aplicar un {porcentaje}% de descuento: ${self.__precio:.2f}"


class Juguetes(Producto):
    # definimos los parametros de nuestra variable
    def __init__(self, nombre, precio, cantidad, garantia):
        super().__init__(nombre, precio, cantidad)
        self.garantia = garantia

    #  Se Sobrescribe el método de los  detalles para la clase Juguetes
    def detalles(self):
        return (f"Juguetes: {self.get_nombre()}, Precio: ${self.get_precio()}"
                f", Cantidad: {self.get_cantidad()}, Garantía: {self.garantia} meses")

    # Sobrescribimos para aplicar_descuento para la clase Juguetes(Polimorfismo)
    def aplicar_descuento(self, porcentaje):
        descuento_adicional = 2  # Descuento  solo para juguetes
        total_descuento = porcentaje + descuento_adicional
        return super().aplicar_descuento(total_descuento)


class RopaInterior(Producto):
    def __init__(self, nombre, precio, cantidad, talla, color):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
        self.color = color

    # Sobrescribimos el método detalles para la clase RopaInterior
    def detalles(self):
        return (f"RopaInterior: {self.get_nombre()}, Precio: ${self.get_precio()}, Cantidad: {self.get_cantidad()}"
                f", Talla: {self.talla}, Color: {self.color}")

    # Sobrescribimos para  aplicar_descuento para la clase RopaInterior aplicando polimorfismo
    def aplicar_descuento(self, porcentaje):
        return super().aplicar_descuento(porcentaje)


# Ejecucion  del programa
producto_limpieza = Producto("Producto cloro", 1.25, 3)
juguetes = Juguetes("Barbie", 20, 10, 1)
ropa = RopaInterior("Bracier", 5, 100, "M", "Rosado")

print(producto_limpieza.detalles())  # Salida de Ejecucion: Producto: Producto Cloro, Precio: $1.25, Cantidad: 3
print(juguetes.detalles())  # Salida de Ejecucion: Juguetes: Barbie, Precio: $20, Cantidad: 10, Garantía: 1 mes
print(ropa.detalles())  # Salida de Ejecucion: Ropa: Bracier, Precio: $5, Cantidad: 100, Talla: M, Color: Rosado

# Aplicar los descuentos a productos
print(producto_limpieza.aplicar_descuento(2))  # Salida: El total a pagar tras aplicar un 20% de descuento: $1.23
print(juguetes.aplicar_descuento(4))  # Salida: El total a pagar tras aplicar un 5% de descuento: $18.80
print(ropa.aplicar_descuento(5))  # Salida: El total a pagar tras aplicar un 10% de descuento: $4.75
