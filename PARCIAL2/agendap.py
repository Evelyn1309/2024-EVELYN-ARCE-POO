# Desarrollar una aplicación GUI utilizando Tkinter en Python que funcione como una agenda personal. La aplicación
# permitirá al usuario agregar, ver, y eliminar eventos o tareas programadas.
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


# Definición de la clase
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")  # Título
        self.root.geometry("600x400")  # Dimensiones de la ventana

        # Estilo personalizado para etiquetas  y botones
        style = ttk.Style()
        style.configure("TLabel", foreground="blue",
                        font=("Arial", 10, "bold"))  # Estilo de las etiquetas:
        style.configure("TButton", foreground="black",
                        font=("Arial", 9, "bold"))

        # Frame (marco) para el listado de eventos
        self.frame_listado = ttk.Frame(self.root)
        self.frame_listado.pack(fill=tk.BOTH, expand=True, padx=10,
                                pady=10)  # Acomoda el frame en la ventana con margen de 10px

        # TreeView para mostrar la lista de eventos
        # Se definen tres columnas
        self.tree = ttk.Treeview(self.frame_listado, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")  # Encabezado de la columna "Fecha"
        self.tree.heading("Hora", text="Hora")  # Encabezado de la columna "Hora"
        self.tree.heading("Descripción", text="Descripción")  # Encabezado de la columna "Descripción"
        self.tree.pack(fill=tk.BOTH, expand=True)  # Ajusta el TreeView para llenar el espacio disponible

        # Botón para eliminar el evento seleccionado
        self.btn_eliminar = ttk.Button(self.frame_listado, text="Eliminar Evento Seleccionado",
                                       command=self.eliminar_evento)
        self.btn_eliminar.pack(side=tk.BOTTOM, pady=5)

        # Frame para la entrada de nuevos eventos
        self.frame_entrada = ttk.Frame(self.root)
        self.frame_entrada.pack(fill=tk.X, padx=10, pady=5)  # Acomoda el frame horizontalmente

        # Etiquetas y campos de entrada para agregar nuevos
        self.label_fecha = ttk.Label(self.frame_entrada, text="Fecha:", style="TLabel")
        self.label_fecha.grid(row=0, column=0, padx=5, pady=5)  # Etiqueta para "Fecha"
        self.entry_fecha = DateEntry(self.frame_entrada, date_pattern="yyyy-mm-dd")  # Selector de fecha
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        # Hora
        self.label_hora = ttk.Label(self.frame_entrada, text="Hora:", style="TLabel")
        self.label_hora.grid(row=1, column=0, padx=5, pady=5)  # Etiqueta para "Hora"
        self.entry_hora = ttk.Entry(self.frame_entrada)  # Campo de entrada para la hora
        self.entry_hora.grid(row=1, column=1, padx=5, pady=5)

        # Descripción
        self.label_descripcion = ttk.Label(self.frame_entrada, text="Descripción:", style="TLabel")
        self.label_descripcion.grid(row=2, column=0, padx=5, pady=5)  # Etiqueta para "Descripción"
        self.entry_descripcion = ttk.Entry(self.frame_entrada)  # Campo de entrada para la descripción
        self.entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

        # Botón para agregar un nuevo evento
        self.btn_agregar = ttk.Button(self.frame_entrada, text="Agregar Evento", style="TButton",
                                      command=self.agregar_evento)
        self.btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)  # Coloca el botón de agregar

        # Botón para salir de la aplicación
        self.btn_salir = ttk.Button(self.frame_entrada, text="Salir", style="TButton", command=self.root.quit)
        self.btn_salir.grid(row=4, column=0, columnspan=2, pady=5)  # Botón para salir

    # Método para agregar un nuevo evento al TreeView
    def agregar_evento(self):
        fecha = self.entry_fecha.get()  # Obtiene la fecha del DateEntry
        hora = self.entry_hora.get()  # Obtiene la hora del Entry
        descripcion = self.entry_descripcion.get()  # Obtiene la descripción del Entry

        # Valida que los campos no estén vacíos
        if not fecha or not hora or not descripcion:
            # Muestra un mensaje de advertencia si falta algún dato
            messagebox.showwarning("Datos incompletos", "Por favor, complete todos los campos.")
        else:
            # Inserta el nuevo evento en el TreeView
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            # Limpia los campos después de agregar el evento
            self.limpiar_campos()

    # elimina el evento seleccionado del TreeView
    def eliminar_evento(self):
        selected_item = self.tree.selection()  # Obtiene el ítem seleccionado
        if not selected_item:
            # Muestra un mensaje de advertencia si no hay selección
            messagebox.showwarning("Eliminar Evento", "Seleccione un evento para eliminar.")
        else:
            # Pide confirmación antes de eliminar el evento
            confirm = messagebox.askyesno("Confirmar eliminación",
                                          "¿Está seguro de que desea eliminar el evento seleccionado?")
            if confirm:
                # Elimina el evento seleccionado
                self.tree.delete(selected_item)

    #  limpia los campos de entrada después de agregar un evento
    def limpiar_campos(self):
        self.entry_hora.delete(0, tk.END)  # Limpia el campo de la hora
        self.entry_descripcion.delete(0, tk.END)  # Limpia el campo de la descripción


# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
