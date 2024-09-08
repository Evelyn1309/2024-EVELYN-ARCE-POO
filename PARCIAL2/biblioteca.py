# Desarrollar un sistema para gestionar una biblioteca digital. El sistema permitirá administrar los libros
# disponibles, las categorías de libros, los usuarios registrados y el historial de préstamos.
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo  # Título del libro
        self.autor = autor  # Autor del libro como tupla (nombre, apellido)
        self.categoria = categoria  # Categoría del libro
        self.isbn = isbn  # ISBN del libro, utilizado como identificador único
        self.prestado = False  # Marca si el libro está prestado

    def __repr__(self):
        return f"'{self.titulo}' de {self.autor[0]} {self.autor[1]}, ISBN: {self.isbn}, Categoría: {self.categoria}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre  # Nombre del usuario
        self.id_usuario = id_usuario  # ID único del usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados por el usuario

    def prestar_libro(self, libro):
        # Añade un libro a la lista de libros prestados
        if libro not in self.libros_prestados:
            self.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo}' prestado a {self.nombre}.")
        else:
            print(f"El libro '{libro.titulo}' ya está prestado a {self.nombre}.")

    def devolver_libro(self, libro):
        # Elimina un libro de la lista de libros prestados
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            print(f"Libro '{libro.titulo}' devuelto por {self.nombre}.")
        else:
            print(f"El libro '{libro.titulo}' no está en la lista de libros prestados de {self.nombre}.")

    def listar_libros_prestados(self):
        # Devuelve la lista de libros prestados
        return self.libros_prestados

    def __repr__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


class Biblioteca:
    def __init__(self):
        # Inicializa la biblioteca con un diccionario de libros y un conjunto de usuarios
        self.libros = {}  # Diccionario que almacena libros con su ISBN como clave
        self.usuarios = {}  # Diccionario para almacenar usuarios con su ID como clave

    def añadir_libro(self, libro):
        # Añade un libro a la colección de la biblioteca
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        # Quita un libro de la colección de la biblioteca usando su ISBN
        if isbn in self.libros:
            del self.libros[isbn]  # Elimina el libro del diccionario
            print(f"Libro con ISBN {isbn} ha sido eliminado.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        # Registra un nuevo usuario en la biblioteca
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        # Da de baja a un usuario de la biblioteca usando su ID
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} ha sido dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        # Facilita el préstamo de un libro a un usuario
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]  # Busca el libro por su ISBN
            if not libro.prestado:  # Verifica si el libro no está prestado
                libro.prestado = True  # Marca el libro como prestado
                usuario = self.usuarios[id_usuario]
                usuario.prestar_libro(libro)
                print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
            else:
                print(f"El libro '{libro.titulo}' ya está prestado.")
        else:
            print(f"Préstamo fallido. Verifique el ISBN {isbn} y el ID del usuario {id_usuario}.")

    def devolver_libro(self, isbn, id_usuario):
        # Facilita la devolución de un libro usando su ISBN
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]  # Busca el libro por su ISBN
            usuario = self.usuarios[id_usuario]
            if libro.prestado:
                libro.prestado = False  # Marca el libro como no prestado
                usuario.devolver_libro(libro)  # Elimina el libro de los libros prestados del usuario
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
            else:
                print(f"El libro '{libro.titulo}' no está prestado.")
        else:
            print(f"Devolución fallida. Verifique el ISBN {isbn} y el ID del usuario {id_usuario}.")

    def buscar_libro(self, criterio, valor):
        # Busca libros en la biblioteca según un criterio (título, autor o categoría)
        resultados = []  # Lista para almacenar los resultados de la búsqueda
        for libro in self.libros.values():
            # Compara el valor de búsqueda con el atributo correspondiente del libro
            if (criterio == "titulo" and valor.lower() in libro.titulo.lower()) or \
                    (criterio == "autor" and valor.lower() in libro.autor[0].lower()) or \
                    (criterio == "categoria" and valor.lower() in libro.categoria.lower()):
                resultados.append(libro)  # Añade el libro a los resultados si coincide
        return resultados  # Devuelve la lista de resultados

    def listar_libros_prestados_usuario(self, id_usuario):
        # Lista todos los libros prestados a un usuario específico
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.listar_libros_prestados()  # Devuelve la lista de libros prestados
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")
            return []


# Ejemplo de uso
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Boulevar", ("Flor", "Salvador"), "Novela", "978-3-16-148410-0")
libro2 = Libro("Don Quijote de la Mancha", ("Miguel", "de Cervantes"), "Novela", "978-3-16-148410-1")
libro3 = Libro("The Tearsmith ", (" Erin ", "Doom"), "Novela", "978-3-16-148410-2")
libro4 = Libro("Después de diciembre ", ("  Joana  ", "Marcús"), "Novela", "978-3-16-148410-3")

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)
biblioteca.añadir_libro(libro4)

# Crear usuario
usuario1 = Usuario("Juan Pérez", "user123")
biblioteca.registrar_usuario(usuario1)

# Prestar libro
biblioteca.prestar_libro("978-3-16-148410-0", "user123")

# Listar libros prestados
print("Libros prestados a user123:", biblioteca.listar_libros_prestados_usuario("user123"))

# Devolver libro
biblioteca.devolver_libro("978-3-16-148410-0", "user123")

# Listar libros prestados después de devolver
print("Libros prestados a user123 después de devolver:", biblioteca.listar_libros_prestados_usuario("user123"))

# Quitar libro
biblioteca.quitar_libro("978-3-16-148410-1")

# Dar de baja usuario
biblioteca.dar_baja_usuario("user123")

print("Programa terminado")
