# En un sistema de gestión de biblioteca desarrollado con Programación Orientada a Objetos (POO),
# la acción de 'prestar un libro'
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # Indica si el libro está disponible para préstamo
        self.prestatario = None  # Quién ha tomado prestado el libro, si aplica

    def prestar(self, usuario):
        if self.disponible:
            self.disponible = False
            self.prestatario = usuario
            print(f"El libro '{self.titulo}' ha sido prestado a {usuario}.")
        else:
            print(f"El libro '{self.titulo}' no está disponible para préstamo.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            self.prestatario = None
            print(f"El libro '{self.titulo}' ha sido devuelto y está disponible.")


# Ejemplo 2
# Un programa en Python que simule la fabricación de caramelos utilizando los principios de la Programación Orientada a
# Objetos (POO
class Ingrediente:
    def __init__(self, nombre, cantidad, unidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad = unidad

    def __str__(self):
        return f"{self.cantidad} {self.unidad} de {self.nombre}"


class Caramelo:
    def __init__(self, tipo, sabor, color):
        self.tipo = tipo
        self.sabor = sabor
        self.color = color

    def __str__(self):
        return f"Caramelo de tipo '{self.tipo}' con sabor a '{self.sabor}' y color '{self.color}'"


class Receta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = []
        self.instrucciones = []

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def agregar_instruccion(self, instruccion):
        self.instrucciones.append(instruccion)


class FabricaCaramelos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.recetas = []

    def agregar_receta(self, receta):
        self.recetas.append(receta)

    def fabricar_caramelo(tipo, sabor, color, receta):
        print(
            f"Iniciando la fabricación del caramelo de tipo '{tipo}', sabor '{sabor}' y color '{color}' usando la receta '{receta.nombre}'...")
        for instruccion in receta.instrucciones:
            print(f"Ejecutando: {instruccion}")
        caramelo = Caramelo(tipo, sabor, color)
        print(f"Caramelo fabricado: {caramelo}")
        return caramelo

    def __str__(self):
        return f"Fábrica de Caramelos '{self.nombre}' con {len(self.recetas)} receta(s)."
