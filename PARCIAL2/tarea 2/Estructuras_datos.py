import os


# Inicializamos  un producto con su key, nombre, cantidad y precio.
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Representacion del producto como una cadena de texto.
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    # Creaacion de un  Producto a partir de una línea de texto.
    @classmethod
    def from_string(cls, linea):
        id_producto, nombre, cantidad, precio = linea.strip().split(',')
        return cls(id_producto, nombre, int(cantidad), float(precio))

    # Convierte el producto a cadena de texto y lo  guarda en el archivo.
    def to_string(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio:.2f}"


class Inventario:  # Inicializa la lista de productos y el nombre nuestro archivo .
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):  # Obtiene  los productos desde nuestro archivo.
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as file:  # esta funcion abre y cierra el archivo y es en tipo lectur
                    for linea in file:
                        producto = Producto.from_string(linea)
                        self.productos.append(producto)
                print("Inventario cargado exitosamente desde el archivo.")
            else:
                print(f"Archivo '{self.archivo}' no encontrado. Se creará uno nuevo al guardar.")
        except FileNotFoundError:
            print(f"Archivo '{self.archivo}' no encontrado. Se creará uno nuevo al guardar.")
        except PermissionError:
            print(f"Permiso denegado al intentar leer el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):  # Guarda los productos en el archivo.
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(producto.to_string() + '\n')
            print("Inventario guardado exitosamente en el archivo.")
        except PermissionError:
            print(f"Permiso denegado al intentar escribir en el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def añadir(self, producto):  # Añade un nuevo producto al inventario si no existe otro con el mismo ID.
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print(f"Error: Ya existe un producto con el ID {producto.get_id()}.")
        else:
            self.productos.append(producto)
            self.guardar_inventario()
            print(f"Producto {producto.get_nombre()} añadido correctamente.")

    def eliminar(self, id_producto):  # Elimina un producto del inventario
        producto = self.buscar_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} eliminado correctamente.")
        else:
            print(f"No se encontró un producto con el ID {id_producto}.")

    def actualizar(self, id_producto, cantidad=None, precio=None):  # Actuliza el producto
        producto = self.buscar_por_id(id_producto)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} actualizado correctamente.")
        else:
            print(f"No se encontró un producto con el ID {id_producto}.")

    def buscar_por_id(self, id_producto):  # busca nuestro producto
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None

    def buscar_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):  # muestra los productos que se encuentran en inventerio.txt
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def mostrar_menu():  # Menu
    print("\n------------------------------//// Menú de Tienda ////----------------------------------------")
    print("1. Buscar producto")
    print("2. Añadir producto")
    print("3. Eliminar producto")
    print("4. Actualizar producto")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():  # Funcionalidad de lista de opciones
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print(f"No se encontraron productos con el nombre '{nombre}'.")

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir(producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar(id_producto)

        elif opcion == "4":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (o presione Enter para no cambiarla): ")
            precio = input("Ingrese el nuevo precio (o presione Enter para no cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar(id_producto, cantidad, precio)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")


if __name__ == "__main__":
    main()
