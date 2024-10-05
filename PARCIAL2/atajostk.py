import tkinter as tk
from tkinter import messagebox


# Definición de la clase principal para la aplicación
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Atajos")
        self.root.geometry("600x600")
        root.configure(bg="darkseagreen")
        # Lista donde se almacenarán las tareas
        self.tasks = []

        # Campo de entrada  donde el usuario escribirá nuevas tareas
        self.entry = tk.Entry(root, width=40)  # Ancho del campo
        self.entry.pack(pady=10)  # Posiciona el Entry con un espacio (pady)
        # Asigna un atajo de teclado, "Enter", para añadir tareas desde el campo de entrada
        self.entry.bind("<Return>", self.add_task)

        # Botón para añadir una tarea manualmente
        self.add_button = tk.Button(root, text="Añadir", command=self.add_task_click)
        self.add_button.pack(pady=5)  # Posiciona el botón debajo del Entry

        # Listbox donde se mostrarán todas las tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=20, width=70, background='#E9967A')
        self.task_listbox.pack(pady=10)  # Tamaño y posicionamiento del Listbox

        # Botón para marcar una tarea seleccionada como completada
        self.complete_button = tk.Button(root, text="Marcar como completada", command=self.complete_task,
                                         background='#1E90FF')
        self.complete_button.pack(pady=5)  # Posiciona el botón debajo de la lista

        # Botón para eliminar una tarea seleccionada
        self.delete_button = tk.Button(root, text="Borrar", command=self.delete_task, background='#B22222')
        self.delete_button.pack(pady=5)  # Posiciona el botón debajo de la lista

        # Asignar atajos de teclado para diversas funciones
        root.bind("<f>", self.complete_task)  # Atajo "f" para completar tarea
        root.bind("<e>", self.delete_task)  # Atajo "a" para eliminar tarea
        root.bind("<Delete>", self.delete_task)  # la tecla "Delete" para eliminar
        root.bind("<Escape>", lambda event: root.quit())  # "Escape" para cerrar la app

    # Función para añadir una tarea desde el botón
    def add_task_click(self):
        self.add_task(None)

    # Función que añade una nueva tarea
    def add_task(self, event):
        task = self.entry.get()  # Obtiene el texto del campo de entrada
        if task:  # Si el campo no está vacío
            # Añade la tarea
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()  # Actualiza
            self.entry.delete(0, tk.END)  # Limpia el campo de entrada
        else:
            # Muestra una advertencia si no se ha escrito ninguna tarea
            messagebox.showwarning("Input Error", "Please enter a task.")

    # Función para marcar una tarea como completada
    def complete_task(self, event=None):
        try:
            # Obtiene el índice de la tarea seleccionada
            selected_index = self.task_listbox.curselection()[0]
            # Cambia el estado de completado a True
            self.tasks[selected_index]["completed"] = True
            self.update_task_listbox()  # Actualiza la lista de tareas
        except IndexError:
            # Muestra una advertencia si no hay ninguna tarea seleccionada
            messagebox.showwarning("Selection Error", "Please select a task to complete.")

    # Función para eliminar una tarea seleccionada
    def delete_task(self, event=None):
        try:
            # Obtiene el índice de la tarea seleccionada
            selected_index = self.task_listbox.curselection()[0]
            # Elimina
            del self.tasks[selected_index]
            self.update_task_listbox()  # Actualiza
        except IndexError:
            # Muestra una advertencia si no hay ninguna tarea seleccionada
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    # Función que actualiza el Listbox con las tareas actuales
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Borra todo el contenido del Listbox
        for task in self.tasks:
            task_text = task["task"]  # Obtiene el texto de la tarea
            if task["completed"]:  # Si la tarea está completada entonces Añade la marca de completado al texto
                task_text += " (Completed)"
            # Inserta la tarea en el Listbox
            self.task_listbox.insert(tk.END, task_text)


# Inicialización de la ventana principal y la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = ToDoApp(root)  # Crea una instancia de la clase ToDoApp
    root.mainloop()
