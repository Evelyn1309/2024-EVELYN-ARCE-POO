# Desarrolo un sistema de gestión de inventarios simple para una tienda, que permitra añadir, actualizar, eliminar y
# buscar productos utilizando una estructura de datos personalizada.
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):  # definimos las varibles que vamos a utilizar
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto  # OBTENCION DE VALORES DE CADA ATRIBUTP

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    #  modificacion del valor de cantidad y precio
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Representacion de  nuestro producto como tipo string
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []  # inicializacion  de la lista de productos  de la tienda vacía

    def añadir(self, producto):  # Comprobacion de la  existe un producto con el mismo ID
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print(f"Error: Ya existe un producto con el ID {producto.get_id()}.")
        else:
            self.productos.append(producto)  # Si el ID es únicob y no existe se añade el producto al inventario
            print(f"Producto {producto.get_nombre()} añadido correctamente.")

    def eliminar(self, id_producto):  # Busqueda de un producto en la lista de productos por su clave unica
        producto = self.buscar_por_id(id_producto)
        if producto:
            self.productos.remove(producto)  # Si lo encuentra este lo elimib¡nara y dara el siguiente mensaje
            print(f"Producto con ID {id_producto} eliminado correctamente.")
        else:
            print(f"No se encontró un producto con el ID {id_producto}.")

    def actualizar(self, id_producto, cantidad=None, precio=None):  # Busqueda de un producto en la lista de
        # productos por su clave unica
        producto = self.buscar_por_id(id_producto)
        if producto:  # Si lo encuentra este sera actualizado
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print(f"Producto con ID {id_producto} actualizado correctamente.")
        else:
            print(f"No se encontró un producto con el ID {id_producto}.")

    def buscar_por_id(self, id_producto):  # Funcion para la busqueda de un producto por su nombre
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None

    def buscar_por_nombre(self, nombre):  # Funcion para la busqueda de un producto por su nombre
        resultados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):  # Funcion para mostrar productos
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def mostrar_menu():
    print("\n------------------------------//// Menú de Tienda ////----------------------------------------")
    print("1. Buscar producto")
    print("2. Añadir producto")
    print("3. Eliminar producto ")
    print("4. Actualizar ")
    print("5. Mostrar todos los productos ")
    print("6. Salir")


def main():
    # Esta funcion crea una instancia de la clase Inventario
    inventario = Inventario()
    producto1 = Producto("001", "Manzana", 50, 0.5)
    producto2 = Producto("002", "Naranjas", 30, 0.6)
    producto3 = Producto("003", "Cloro", 2, 1.6)
    producto4 = Producto("004", "Acondicionador", 10, 5.6)
    producto5 = Producto("004", "Arroz", 17, 2.6)

    inventario.añadir(producto1)
    inventario.añadir(producto2)
    inventario.añadir(producto3)
    inventario.añadir(producto4)
    inventario.añadir(producto5)

    while True:
        # Muestra el menú y se pide que selecione una opcion
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Opción  1 para buscar productos por su  nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                # Muestra los productos encontrados
                for producto in resultados:
                    print(producto)
            else:
                print(f"No se encontraron productos con el nombre '{nombre}'.")

        elif opcion == "2":
            # Opción 1 para añadir un nuevo producto
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            # Crea un nuevo producto y lo añade al inventario
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "3":
            # Opción 2 para eliminar un producto
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "4":
            # Opción  3 para actualizar la cantidad o el precio de algun producto producto
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (o presione Enter para no cambiarla): ")
            precio = input("Ingrese el nuevo precio (o presione Enter para no cambiarlo): ")
            # Convierte los valores ingresados si el usuario los ha proporcionado
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "5":
            # Opción 5 muestra todos los productos
            inventario.mostrar_productos()

        elif opcion == "6":
            # Opción 6 para salir del sistema
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            # Si se ingresa una opción no válida mesaje para que lo intente denuevo
            print("Opción no válida, por favor intenta de nuevo.")


if __name__ == "__main__":
    main()
