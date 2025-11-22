import tkinter as tk        # libreria estandar para interfaces graficas
from tkinter import ttk     # importa widgets mas modernos

# Entrada de datos para ejemplo: ISBN, Título, Autor, Año
LIBROS = [
    (9781617293987, "Manning Publications", "Groves", 2017),
    (9780134685991, "The Pragmatic Programmer", "Hunt", 1999),
    (9780596007122, "Code Complete 2", "McConnell", 2004),
    (9780321125217, "Clean Code", "Martin", 2008),
    (9781788298758, "Python Crash Course", "Matthes", 2015),
    (9781491904244, "Head First Python", "Barry", 2016),
]

def buscar_libro_binario(isbn_a_buscar):
    try:
        isbn_a_buscar = int(isbn_a_buscar)
    except ValueError:
        mostrar_resultados("Error de Búsqueda", "Error: El ISBN debe ser un número entero.")
        return

    libros_ordenados = sorted(LIBROS, key=lambda x: x[0]) # Asegurar orden por ISBN
    inicio, fin = 0, len(libros_ordenados) - 1
    
    while inicio <= fin:
        mitad = (inicio + fin) // 2
        isbn_actual = libros_ordenados[mitad][0]
        
        if isbn_actual == isbn_a_buscar:
            isbn, titulo, autor, año = libros_ordenados[mitad]
            resultado_texto = f"Libro encontrado\nISBN: {isbn}\nTítulo: {titulo}\nAutor: {autor}\nAño: {año}"
            mostrar_resultados("Resultado de Búsqueda Binaria", resultado_texto)
            return
        elif isbn_actual < isbn_a_buscar:
            inicio = mitad + 1
        else:
            fin = mitad - 1
            
    mostrar_resultados("Resultado de Búsqueda Binaria", "Libro no encontrado con ese ISBN.")
    
CRITERIOS = {
    "Título": 1, 
    "Autor": 2, 
    "Año": 3
}

def ordenar_libros(criterio):
    """Ordena los libros según el criterio y muestra la lista en una ventana secundaria."""
    indice_ordenamiento = CRITERIOS.get(criterio, 1) 
    libros_ordenados = sorted(LIBROS, key=lambda x: x[indice_ordenamiento])
    
    resultado_texto = f"Libros ordenados por {criterio}:\n\n"
    # Formatea la salida como una tabla simple
    resultado_texto += f"| {'ISBN':<15} | {'TÍTULO':<25} | {'AUTOR':<15} | {'AÑO':<5} |\n"
    resultado_texto += "-" * 67 + "\n"
    for isbn, titulo, autor, año in libros_ordenados:
        resultado_texto += f"| {isbn:<15} | {titulo:<25} | {autor:<15} | {año:<5} |\n"
        
    mostrar_resultados(f"Lista Ordenada por {criterio}", resultado_texto)

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Biblioteca Virtual | Proyecto Final")
    ventana.geometry("720x480")

    frame_principal = ttk.Frame(ventana, padding="10")
    frame_principal.grid(row=0, column=0, sticky="nsew")
    
    ttk.Label(frame_principal, text="📚 Biblioteca Virtual", font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
    
# -------------------- SECCIÓN DE BÚSQUEDA --------------------
    ttk.Label(frame_principal, text="--- Búsqueda por ISBN (Binaria) ---", font=("Arial", 12, "italic")).grid(row=1, column=0, columnspan=4, pady=(10, 5), sticky="ew")
    ttk.Label(frame_principal, text="ISBN a buscar:", font=("Arial", 10, "bold")).grid(row=2, column=0, padx=5, pady=5, sticky="e")

    isbn_entrada = ttk.Entry(frame_principal, width=20)     #espacio para escribir el ISBN
    isbn_entrada.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    boton_buscar = ttk.Button(
        frame_principal, 
        text="Buscar Libro", 
        command=lambda: buscar_libro_binario(isbn_entrada.get())
        )
    
    boton_buscar.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky="ew")
    
    
# -------------------- SECCIÓN DE ORDENAMIENTO --------------------
    ttk.Label(frame_principal, text="--- Ordenamiento ---", font=("Arial", 12, "italic")).grid(row=3, column=0, columnspan=4, pady=(15, 5), sticky="ew")
    ttk.Label(frame_principal, text="Ordenar por:", font=("Arial", 10, "bold")).grid(row=4, column=0, padx=5, pady=5, sticky="e")
    
    # Criterios de Selección (Combobox)
    criterios_orden = ["Título", "Autor", "Año"]
    
    # Variable de control para el Combobox
    criterio_seleccionado = tk.StringVar(value=criterios_orden[0])      # Valor inicial: Título
    
    #Combobox
    combobox_orden = ttk.Combobox(
        frame_principal, 
        textvariable=criterio_seleccionado, 
        values=criterios_orden,
        state="readonly",       # No permite escribir, solo seleccionar
        width=15
    )
    combobox_orden.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
    
    # Botón de Ordenamiento
    boton_ordenar = ttk.Button(
        frame_principal, 
        text="Ordenar Libros", 
        command=lambda: ordenar_libros(criterio_seleccionado.get())
        )
    
    boton_ordenar.grid(row=4, column=2, columnspan=2, padx=5, pady=5, sticky="ew")

    ventana.mainloop()

def mostrar_resultados(titulo_ventana, contenido_texto):
    #Crea una nueva ventana Toplevel (emergente) para mostrar resultados.

    ventana_resultados = tk.Toplevel()
    ventana_resultados.title(titulo_ventana)
    
    frame_resultados = ttk.Frame(ventana_resultados, padding="10")

    frame_resultados.pack(expand=True, fill="both") #no se usa el .grid, ya que solo se mostrará el cuadro con los resultados
    
    # Widget de Texto (tk.Text) para contenido de múltiples líneas
    texto_widget = tk.Text(frame_resultados, wrap=tk.WORD, width=60, height=15, font=("Courier", 10))
    texto_widget.insert(tk.END, contenido_texto)   
    
    # Deshabilitar la edición
    texto_widget.config(state=tk.DISABLED) 
    texto_widget.pack(padx=5, pady=5, expand=True, fill="both")
    
    # Botón para cerrar
    boton_cerrar = ttk.Button(frame_resultados, text="Cerrar Resultados", command=ventana_resultados.destroy)
    boton_cerrar.pack(pady=10)

if __name__ == "__main__":
    crear_interfaz()