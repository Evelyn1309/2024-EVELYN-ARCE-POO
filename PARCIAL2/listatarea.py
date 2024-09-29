import tkinter as tk
from tkinter import messagebox

# Crea la ventana
ventana = tk.Tk()  # Inicializa la ventana principal de la aplicación
ventana.title("LISTAS DE TAREAS")  # Establece el título de la ventana
ventana.geometry("600x600")  # Define el tamaño de la ventana


def add_task(event=None):  # Se acepta un parámetro  para permitir que la función sea llamada
    task = entry_task.get()  # Obtiene el texto ingresado
    if task:  # Verifica si se ingresó algún texto
        listbox_tasks.insert(tk.END, task)  # Añade la tarea al final de la lista
        entry_task.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        # Mustra un mensaje de advertencia
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")


def complete_task():
    try:
        # Obtiene el índice de la tarea seleccionada
        selected_task_index = listbox_tasks.curselection()[0]
        task_text = listbox_tasks.get(selected_task_index)  # Obtiene el texto de la tarea
        listbox_tasks.delete(selected_task_index)  # Elimina la tarea de la lista
        # Añade  al final la tarea  modificada significando que está completada
        listbox_tasks.insert(tk.END, f"[Tarea Completada] {task_text}")
    except IndexError:
        # Mustra un mensaje de advertencia
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para marcarla como completada")


def delete_task():
    try:
        # Obtiene el índice de la tarea
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)  # Elimina la tarea de la lista
    except IndexError:
        # MUstra un mensaje
        messagebox.showwarning("Advertencia", "Por favor selecciona para eliminarla")


# Campo de entrada
entry_task = tk.Entry(ventana, width=50, )  # Crea un campo de entrada
entry_task.pack(pady=20)  # Añade el campo de entrada
entry_task.bind("<Return>", add_task)  # Vincula la tecla Enter a la función add_task

# Lista para mostrar las tareas
listbox_tasks = tk.Listbox(ventana, width=50, height=15, background='#FAEBD7',
                           selectmode=tk.SINGLE)  # Crea una lista para mostrar las tareas
listbox_tasks.pack(pady=20)

# Botón para añadir tareas
button_add = tk.Button(ventana, text="Añadir ", command=add_task, background='#228B22')  # Crea un botón para añadir
# tareas
button_add.pack(pady=5)  # Añadir el botón a la ventana

# Botón para marcar tareas
button_complete = tk.Button(ventana, text="Marcar como Completada",
                            command=complete_task, background='#1E90FF')  # Crea un botón para marcar tareas como
# completadas
button_complete.pack(pady=5)  # Añade el botón a la ventana

# Botón para eliminar
button_delete = tk.Button(ventana, text="Eliminar Tarea", command=delete_task, background='#B22222')  # Crea un botón
# para eliminar
button_delete.pack(pady=5)  # Añadir el botón

# Iniciar el bucle de la aplicación
ventana.mainloop()
