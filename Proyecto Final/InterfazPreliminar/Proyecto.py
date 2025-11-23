import tkinter as tk
from tkinter import ttk, messagebox

#Datos para ejemplo: ISBN, Título, Autor, Año, breve descripcion
LIBROS_DB = [
    {"isbn": "9780553381689", "titulo": "A Game of Thrones", "autor": "George R.R. Martin", "ano": 1996,
     "descripcion": "En Poniente, las familias nobles luchan por el control del Trono de Hierro mientras se avecina un invierno implacable."},

    {"isbn": "9780553108033", "titulo": "A Clash of Kings", "autor": "George R.R. Martin", "ano": 1998,
     "descripcion": "Múltiples reyes reclaman el trono, mientras la guerra fractura el reino y los peligros en el Norte se intensifican."},

    {"isbn": "9780553573427", "titulo": "A Storm of Swords", "autor": "George R.R. Martin", "ano": 2000,
     "descripcion": "Traiciones, batallas y alianzas inesperadas marcan la brutal lucha por el poder en los Siete Reinos."},

    {"isbn": "9780553801476", "titulo": "A Feast for Crows", "autor": "George R.R. Martin", "ano": 2005,
     "descripcion": "El reparto del poder tras la guerra revela nuevas intrigas, conspiraciones y luchas por el control político."},

    {"isbn": "9780553801506", "titulo": "A Dance with Dragons", "autor": "George R.R. Martin", "ano": 2011,
     "descripcion": "Jon Snow, Daenerys y Tyrion enfrentan decisiones clave en medio de guerras, dragones y amenazas antiguas."},

    {"isbn": "9780743273565", "titulo": "The Da Vinci Code", "autor": "Dan Brown", "ano": 2003,
     "descripcion": "Robert Langdon investiga un asesinato en el Louvre y descubre una conspiración milenaria ligada a la Iglesia."},

    {"isbn": "9780307474278", "titulo": "Angels & Demons", "autor": "Dan Brown", "ano": 2000,
     "descripcion": "Una sociedad secreta planea destruir el Vaticano mientras Langdon descifra símbolos antiguos para detenerla."},

    {"isbn": "9780385504201", "titulo": "The Lost Symbol", "autor": "Dan Brown", "ano": 2009,
     "descripcion": "Langdon sigue pistas masónicas en Washington D.C. para descubrir un antiguo secreto oculto en la capital."},

    {"isbn": "9780385537131", "titulo": "Inferno", "autor": "Dan Brown", "ano": 2013,
     "descripcion": "Una amenaza biológica inspirada en Dante pone en riesgo a la humanidad, y Langdon debe descifrar códigos para detenerla."},

    {"isbn": "9780385514231", "titulo": "Origin", "autor": "Dan Brown", "ano": 2017,
     "descripcion": "Un futurista revela una teoría sobre el origen y el destino de la humanidad, desafiando la fe y la ciencia."},

    {"isbn": "9780451524935", "titulo": "1984", "autor": "George Orwell", "ano": 1949,
     "descripcion": "Un futuro totalitario donde el Gran Hermano controla cada aspecto de la vida y manipula la verdad."},

    {"isbn": "9780451526342", "titulo": "Animal Farm", "autor": "George Orwell", "ano": 1945,
     "descripcion": "Una granja gobernada por animales se convierte en una sátira del autoritarismo y la corrupción del poder."},

    {"isbn": "9780156027328", "titulo": "Brave New World", "autor": "Aldous Huxley", "ano": 1932,
     "descripcion": "Una sociedad futurista donde la tecnología controla la felicidad, la genética y el comportamiento humano."},

    {"isbn": "9780060850524", "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "ano": 1953,
     "descripcion": "Un bombero encargado de quemar libros comienza a cuestionar su papel en una sociedad sin pensamiento crítico."},

    {"isbn": "9780743273565", "titulo": "The Great Gatsby", "autor": "F. Scott Fitzgerald", "ano": 1925,
     "descripcion": "Jay Gatsby persigue el sueño americano en una historia de riqueza, amor y tragedia en los años 20."},

    {"isbn": "9780141439600", "titulo": "Wuthering Heights", "autor": "Emily Brontë", "ano": 1847,
     "descripcion": "Una historia pasional y oscura que explora amor, venganza y tormento entre Heathcliff y Catherine."},

    {"isbn": "9780142437209", "titulo": "Moby Dick", "autor": "Herman Melville", "ano": 1851,
     "descripcion": "El capitán Ahab obsesionado persigue a la ballena blanca en una travesía llena de simbolismo y tragedia."},

    {"isbn": "9780140449266", "titulo": "The Odyssey", "autor": "Homero", "ano": -800,
     "descripcion": "Odiseo enfrenta monstruos, dioses y desafíos épicos en su regreso a Ítaca."},

    {"isbn": "9780486264721", "titulo": "The Iliad", "autor": "Homero", "ano": -750,
     "descripcion": "La guerra de Troya narrada con héroes, dioses y conflictos entre gloria, honor y destino."},

    {"isbn": "9780141442464", "titulo": "Jane Eyre", "autor": "Charlotte Brontë", "ano": 1847,
     "descripcion": "Una joven enfrenta adversidades sociales y emocionales mientras busca amor e independencia."},

    {"isbn": "9780679783268", "titulo": "Crime and Punishment", "autor": "Fyodor Dostoevsky", "ano": 1866,
     "descripcion": "Un estudiante comete un crimen y enfrenta un conflicto psicológico entre culpa, moral y redención."},

    {"isbn": "9780140449136", "titulo": "The Brothers Karamazov", "autor": "Fyodor Dostoevsky", "ano": 1880,
     "descripcion": "Una compleja historia sobre fe, moral, crimen y filosofía en una familia rusa conflictiva."},

    {"isbn": "9780553803709", "titulo": "Foundation", "autor": "Isaac Asimov", "ano": 1951,
     "descripcion": "Hari Seldon predice la caída del Imperio Galáctico y crea una Fundación para preservar el conocimiento."},

    {"isbn": "9780553293357", "titulo": "Foundation and Empire", "autor": "Isaac Asimov", "ano": 1952,
     "descripcion": "La Fundación enfrenta amenazas internas y externas que ponen a prueba su estabilidad."},

    {"isbn": "9780553293364", "titulo": "Second Foundation", "autor": "Isaac Asimov", "ano": 1953,
     "descripcion": "La misteriosa Segunda Fundación trabaja desde las sombras para preservar el futuro de la humanidad."},

    {"isbn": "9780345339683", "titulo": "The Hobbit", "autor": "J.R.R. Tolkien", "ano": 1937,
     "descripcion": "Bilbo Bolsón es arrastrado a una aventura con enanos, dragones y tesoros legendarios."},

    {"isbn": "9780618640157", "titulo": "The Fellowship of the Ring", "autor": "J.R.R. Tolkien", "ano": 1954,
     "descripcion": "Un grupo diverso se une para destruir un anillo que podría esclavizar a la Tierra Media."},

    {"isbn": "9780618640188", "titulo": "The Two Towers", "autor": "J.R.R. Tolkien", "ano": 1954,
     "descripcion": "La Comunidad se divide mientras la guerra contra Sauron y Saruman amenaza toda la Tierra Media."},

    {"isbn": "9780618640195", "titulo": "The Return of the King", "autor": "J.R.R. Tolkien", "ano": 1955,
     "descripcion": "Aragorn reclama su destino mientras el Anillo Único se enfrenta a su destrucción final."},

    {"isbn": "9780547928227", "titulo": "The Silmarillion", "autor": "J.R.R. Tolkien", "ano": 1977,
     "descripcion": "El origen de la Tierra Media, los elfos, los anillos de poder y la historia de Morgoth y Sauron."},

    {"isbn": "9780141439846", "titulo": "Frankenstein", "autor": "Mary Shelley", "ano": 1818,
     "descripcion": "Victor Frankenstein crea una criatura consciente que lo confronta con las consecuencias de su ambición."},

    {"isbn": "9780679723165", "titulo": "Lolita", "autor": "Vladimir Nabokov", "ano": 1955,
     "descripcion": "El profesor Humbert Humbert relata su obsesión amorosa y perturbadora con una niña llamada Lolita."},

    {"isbn": "9780747532743", "titulo": "Harry Potter and the Philosopher's Stone", "autor": "J.K. Rowling", "ano": 1997,
     "descripcion": "Un niño descubre que es mago y entra a un mundo de magia, amistad y peligros oscuros."},

    {"isbn": "9780439064873", "titulo": "Harry Potter and the Chamber of Secrets", "autor": "J.K. Rowling", "ano": 1998,
     "descripcion": "Una misteriosa cámara es abierta y criaturas peligrosas acechan a los estudiantes de Hogwarts."},

    {"isbn": "9780439136365", "titulo": "Harry Potter and the Prisoner of Azkaban", "autor": "J.K. Rowling", "ano": 1999,
     "descripcion": "Un peligroso prisionero escapa de Azkaban y parece estar tras Harry."},

    {"isbn": "9780439139601", "titulo": "Harry Potter and the Goblet of Fire", "autor": "J.K. Rowling", "ano": 2000,
     "descripcion": "Un torneo mágico pone a prueba habilidades, valentía y revela el regreso de un poder oscuro."},

    {"isbn": "9780439358071", "titulo": "Harry Potter and the Order of the Phoenix", "autor": "J.K. Rowling", "ano": 2003,
     "descripcion": "Harry enfrenta la incredulidad del Ministerio mientras se prepara para enfrentar a Voldemort."},

    {"isbn": "9780439785969", "titulo": "Harry Potter and the Half-Blood Prince", "autor": "J.K. Rowling", "ano": 2005,
     "descripcion": "Las reliquias del pasado revelan secretos sobre Voldemort y cómo vencerlo."},

    {"isbn": "9780545010221", "titulo": "Harry Potter and the Deathly Hallows", "autor": "J.K. Rowling", "ano": 2007,
     "descripcion": "Harry enfrenta su destino final mientras la guerra mágica llega a su clímax."},

    {"isbn": "9780441172719", "titulo": "Dune", "autor": "Frank Herbert", "ano": 1965,
     "descripcion": "En Arrakis, Paul Atreides descubre su destino en medio de profecías, poder y supervivencia."},

    {"isbn": "9780441013593", "titulo": "Dune Messiah", "autor": "Frank Herbert", "ano": 1969,
     "descripcion": "Paul, ahora emperador, enfrenta las consecuencias de su ascenso y las profecías que lo persiguen."},

    {"isbn": "9780441104024", "titulo": "Children of Dune", "autor": "Frank Herbert", "ano": 1976,
     "descripcion": "La familia Atreides lucha por el control de Arrakis mientras el destino de la humanidad pende de un hilo."},

    {"isbn": "9780061122415", "titulo": "To Kill a Mockingbird", "autor": "Harper Lee", "ano": 1960,
     "descripcion": "Una niña presencia las injusticias raciales en el sur de Estados Unidos a través del juicio de un hombre inocente."},

    {"isbn": "9781501128035", "titulo": "It", "autor": "Stephen King", "ano": 1986,
     "descripcion": "Un grupo de amigos enfrenta a una entidad maléfica que se alimenta del miedo en un pueblo de Maine."},

    {"isbn": "9780307743657", "titulo": "The Shining", "autor": "Stephen King", "ano": 1977,
     "descripcion": "Una familia pasa el invierno en un hotel aislado, donde fuerzas sobrenaturales toman el control."},

    {"isbn": "9781476787817", "titulo": "Pet Sematary", "autor": "Stephen King", "ano": 1983,
     "descripcion": "Un cementerio antiguo tiene el poder de traer a los muertos, pero con consecuencias horribles."},

    {"isbn": "9780140283334", "titulo": "Lord of the Flies", "autor": "William Golding", "ano": 1954,
     "descripcion": "Un grupo de niños varados en una isla se organiza, pero pronto cae en el caos y la barbarie."},

    {"isbn": "9780743482837", "titulo": "Hamlet", "autor": "William Shakespeare", "ano": 1603,
     "descripcion": "El príncipe Hamlet busca vengar la muerte de su padre, enfrentando dilemas morales y políticos."},

    {"isbn": "9781451673319", "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "ano": 1953,
     "descripcion": "Un futuro donde los libros están prohibidos y los bomberos los queman, hasta que uno comienza a leer."},

    {"isbn": "9780060850524", "titulo": "The Alchemist", "autor": "Paulo Coelho", "ano": 1988,
     "descripcion": "Un pastor andaluz sigue su Leyenda Personal en una travesía espiritual hacia Egipto."},

    {"isbn": "9780307588371", "titulo": "The Girl with the Dragon Tattoo", "autor": "Stieg Larsson", "ano": 2005,
     "descripcion": "Un periodista y una hacker investigan un misterio familiar oculto desde hace décadas."},

    {"isbn": "9780062316110", "titulo": "The Fault in Our Stars", "autor": "John Green", "ano": 2012,
     "descripcion": "Dos jóvenes con cáncer se enamoran mientras enfrentan su propia mortalidad con humor y dolor."},

    {"isbn": "9780307387899", "titulo": "The Road", "autor": "Cormac McCarthy", "ano": 2006,
     "descripcion": "Un padre y su hijo luchan por sobrevivir en un mundo destruido y desolado."},

    {"isbn": "9780439354447", "titulo": "Eragon", "autor": "Christopher Paolini", "ano": 2002,
     "descripcion": "Un joven granjero encuentra un huevo de dragón que lo lleva a convertirse en Jinete de Dragón."},

    {"isbn": "9780439554892", "titulo": "The Hunger Games", "autor": "Suzanne Collins", "ano": 2008,
     "descripcion": "En un futuro distópico, jóvenes luchan a muerte en un espectáculo televisado."},

    {"isbn": "9780439023518", "titulo": "Catching Fire", "autor": "Suzanne Collins", "ano": 2009,
     "descripcion": "Katniss se convierte en símbolo de rebelión mientras enfrenta un nuevo torneo mortal."},

    {"isbn": "9780545310582", "titulo": "Mockingjay", "autor": "Suzanne Collins", "ano": 2010,
     "descripcion": "La rebelión contra el Capitolio llega a su punto más peligroso y decisivo."},

    {"isbn": "9780060935467", "titulo": "The Kite Runner", "autor": "Khaled Hosseini", "ano": 2003,
     "descripcion": "Una historia de amistad, traición y redención ambientada en Afganistán."},

    {"isbn": "9781439107959", "titulo": "The Book Thief", "autor": "Markus Zusak", "ano": 2005,
     "descripcion": "Narrada por la Muerte, sigue la historia de una niña que roba libros durante la Segunda Guerra Mundial."},

    {"isbn": "9780307269997", "titulo": "The Help", "autor": "Kathryn Stockett", "ano": 2009,
     "descripcion": "Criadas afroamericanas cuentan sus historias de discriminación en los años 60."},

    {"isbn": "9780141036136", "titulo": "The Road", "autor": "Cormac McCarthy", "ano": 2006,
     "descripcion": "Un padre y su hijo luchan por sobrevivir en un mundo postapocalíptico devastado."},

    {"isbn": "9780140280197", "titulo": "A Thousand Splendid Suns", "autor": "Khaled Hosseini", "ano": 2007,
     "descripcion": "Dos mujeres afganas unen fuerzas para sobrevivir a la opresión y la guerra."},

    {"isbn": "9780307346605", "titulo": "Gone Girl", "autor": "Gillian Flynn", "ano": 2012,
     "descripcion": "Una esposa desaparece misteriosamente, y su esposo se convierte en sospechoso principal."},

    {"isbn": "9780553386790", "titulo": "The Martian", "autor": "Andy Weir", "ano": 2011,
     "descripcion": "Un astronauta queda atrapado en Marte y usa su ingenio para sobrevivir solo."}
]

class BibliotecaApp:

    def __init__(self):
        master = tk.Tk()
        self.master = master
        master.title("Biblioteca Virtual - Tkinter")
        master.geometry("1000x650")
        master.configure(bg = "#f0f2f5")  # Simular el color de fondo

        # ---------------- VARIABLES DE CONTROL ----------------
        self.criterio_busqueda = tk.StringVar(value="Título")
        self.termino_busqueda = tk.StringVar()
        self.autor_filtro = tk.StringVar()
        self.criterio_orden = tk.StringVar(value="Título (A-Z)")

        # ---------------- CONSTRUCCIÓN DE LA UI ----------------
        self.crear_widgets()

        # ---------------- CARGA INICIAL DE DATOS ----------------
        self.actualizar_tabla()
        master.mainloop()

    def crear_widgets(self):
        # Título Principal
        ttk.Label(self.master, text="Biblioteca Virtual", font=("Arial", 24, "bold"), background="#f0f2f5").pack(
            pady=(10, 20))

        # --- Panel de Controles (Similar a ft.Container) ---
        panel_controles = ttk.Frame(self.master, padding="15", style='White.TFrame')
        panel_controles.pack(fill='x', padx=30, pady=10)

        # Se requiere un estilo específico para el fondo del Frame
        s = ttk.Style()
        s.configure('White.TFrame', background='white')

        # --- Fila 1 de Controles (Búsqueda) ---
        # Usamos grid dentro del panel_controles

        # Dropdown de Criterio de Búsqueda
        ttk.Combobox(panel_controles,
                     textvariable=self.criterio_busqueda,
                     values=["Título", "ISBN"],
                     state="readonly",
                     width=10
                     ).grid(row=0, column=0, padx=5, pady=10, sticky="ew")

        # Campo de Búsqueda (Input)
        search_input = ttk.Entry(panel_controles,
                                 textvariable=self.termino_busqueda,
                                 width=50
                                 )
        search_input.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        # Bind: Ejecutar búsqueda al presionar Enter
        search_input.bind("<Return>", self.actualizar_tabla)

        # Botón de Búsqueda
        ttk.Button(panel_controles,
                   text="🔍 Buscar",
                   command=self.actualizar_tabla
                   ).grid(row=0, column=2, padx=5, pady=10, sticky="e")

        # --- Fila 2 de Controles (Ordenamiento y Filtro) ---

        # Dropdown de Ordenamiento
        ttk.Label(panel_controles, text="Ordenar por:", background="white").grid(row=1, column=0, padx=5, pady=10,
                                                                                 sticky="w")
        ordenar_dropdown = ttk.Combobox(panel_controles,
                                        textvariable=self.criterio_orden,
                                        values=["Título (A-Z)", "Título (Z-A)", "Año (Más reciente primero)",
                                                "Año (Más antiguo primero)"],
                                        state="readonly"
                                        )
        ordenar_dropdown.grid(row=1, column=1, padx=5, pady=10, sticky="ew")
        # Bind: Ejecutar ordenamiento al cambiar la selección
        ordenar_dropdown.bind("<<ComboboxSelected>>", self.actualizar_tabla)

        # Filtro por Autor
        ttk.Label(panel_controles, text="Filtrar por autor:", background="white").grid(row=1, column=2, padx=5, pady=10,
                                                                                       sticky="w")
        autor_filter = ttk.Entry(panel_controles,
                                 textvariable=self.autor_filtro,
                                 width=30
                                 )
        autor_filter.grid(row=1, column=3, padx=5, pady=10, sticky="ew")
        autor_filter.bind("<Return>", self.actualizar_tabla)

        # Configuración de expansión de columnas en el Frame de Controles
        panel_controles.grid_columnconfigure(1, weight=1)  # El campo de búsqueda se expande
        panel_controles.grid_columnconfigure(3, weight=1)  # El campo de filtro de autor se expande

        # --- Sección de la Tabla (Treeview) ---
        tabla_frame = ttk.Frame(self.master, padding="15", style='White.TFrame')
        tabla_frame.pack(fill='both', expand=True, padx=30, pady=10)

        # 1. Definir el Treeview
        self.tabla_libros_tv = ttk.Treeview(tabla_frame, columns=("ISBN", "Título", "Autor", "Año"), show="headings")
        self.tabla_libros_tv.pack(side="left", fill="both", expand=True)

        # 2. Definir Columnas
        self.tabla_libros_tv.heading("ISBN", text="ISBN")
        self.tabla_libros_tv.heading("Título", text="TÍTULO")
        self.tabla_libros_tv.heading("Autor", text="AUTOR")
        self.tabla_libros_tv.heading("Año", text="AÑO")

        # 3. Anchos de Columna
        self.tabla_libros_tv.column("ISBN", width=150, anchor='center')
        self.tabla_libros_tv.column("Título", width=300, anchor='w')
        self.tabla_libros_tv.column("Autor", width=200, anchor='w')
        self.tabla_libros_tv.column("Año", width=80, anchor='center')

        # 4. Scrollbar
        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tabla_libros_tv.yview)
        self.tabla_libros_tv.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # 5. Bind: Capturar el evento de selección de fila (equivalente a on_select_changed de Flet)
        self.tabla_libros_tv.bind("<<TreeviewSelect>>", self.fila_seleccionada)

    # ---------------- LÓGICA DE LA APLICACIÓN ----------------

    def busqueda_binaria_isbn(self, libros, isbn_buscado):
        """Busca un libro por ISBN usando el algoritmo de búsqueda binaria."""
        bajo, alto = 0, len(libros) - 1
        while bajo <= alto:
            medio = (bajo + alto) // 2
            isbn_medio = libros[medio]['isbn']

            if isbn_medio == isbn_buscado:
                return [libros[medio]]
            elif isbn_medio < isbn_buscado:
                bajo = medio + 1
            else:
                alto = medio - 1
        return []

    def abrir_modal_detalles(self, libro):
        #Crea y abre una ventana Toplevel para mostrar los detalles del libro.
        modal = tk.Toplevel(self.master)
        modal.title(libro["titulo"])
        modal.geometry("500x350")
        modal.transient(self.master)  # Vincula al maestro
        modal.grab_set()  # bloquea la ventana principal

        frame_modal = ttk.Frame(modal, padding="20")
        frame_modal.pack(fill='both', expand=True)

        # Título
        ttk.Label(frame_modal, text=libro["titulo"], font=("Arial", 16, "bold")).pack(pady=5)

        # Metadatos
        ttk.Label(frame_modal, text=f"Autor: {libro['autor']}").pack(anchor='w')
        ttk.Label(frame_modal, text=f"Año: {libro['ano']}").pack(anchor='w')
        ttk.Label(frame_modal, text=f"ISBN: {libro['isbn']}").pack(anchor='w')

        ttk.Separator(frame_modal, orient='horizontal').pack(fill='x', pady=10)

        # Descripción (Usamos un Label multilínea)
        ttk.Label(frame_modal, text=libro["descripcion"], wraplength=450, justify='left').pack(anchor='w')

        # Botón de Cerrar
        ttk.Button(frame_modal, text="Cerrar", command=modal.destroy).pack(pady=20)

        self.master.wait_window(modal)  # Espera a que se cierre el modal

    def fila_seleccionada(self, event):
        #Maneja el evento de clic en una fila del Treeview.

        # 1. Obtener la fila seleccionada
        item_id = self.tabla_libros_tv.focus()
        if not item_id:
            return

        # 2. Recuperar el diccionario del libro guardado en self.datos_libros
        try:
            libro_data = self.datos_libros.get(item_id)
            if libro_data:
                self.abrir_modal_detalles(libro_data)
            else:
                print("No se encontraron datos para esta fila.")
        except Exception as e:
            print(f"Error al obtener datos de la fila: {e}")

    def actualizar_tabla(self, event=None):
        """Función central: Filtra, ordena y recarga el Treeview."""

        termino_busqueda = self.termino_busqueda.get().lower()
        criterio_busqueda = self.criterio_busqueda.get()
        autor_filtro = self.autor_filtro.get().lower()
        orden = self.criterio_orden.get()

        resultados = []

        # --- Lógica de Búsqueda ---
        if termino_busqueda:
            if criterio_busqueda == "ISBN":
                # La búsqueda binaria solo funciona si los datos están ordenados por ISBN
                resultados = self.busqueda_binaria_isbn(LIBROS_DB, termino_busqueda)
            else:  # Búsqueda por Título (lineal)
                resultados = [libro for libro in LIBROS_DB if termino_busqueda in libro["titulo"].lower()]
        else:
            resultados = list(LIBROS_DB)

        # --- Lógica de Filtrado por Autor ---
        if autor_filtro:
            resultados = [libro for libro in resultados if autor_filtro in libro["autor"].lower()]

        # --- Lógica de Ordenamiento ---
        if orden == "Título (A-Z)":
            resultados.sort(key=lambda x: x['titulo'])
        elif orden == "Título (Z-A)":
            resultados.sort(key=lambda x: x['titulo'], reverse=True)
        elif orden == "Año (Más reciente primero)":
            resultados.sort(key=lambda x: x['ano'], reverse=True)
        elif orden == "Año (Más antiguo primero)":
            resultados.sort(key=lambda x: x['ano'])

        # --- Recarga del Treeview ---
        # 1. Limpiar las filas existentes
        self.tabla_libros_tv.delete(*self.tabla_libros_tv.get_children())

        # Reiniciamos el diccionario auxiliar
        self.datos_libros = {}

        # 2. Insertar los nuevos resultados sin usar JSON
        for libro in resultados:
            iid = self.tabla_libros_tv.insert(
                parent='',
                index='end',
                values=(libro["isbn"], libro["titulo"], libro["autor"], libro["ano"])
            )
            # Guardamos el diccionario usando el iid
            self.datos_libros[iid] = libro

if __name__ == "__main__":
    BibliotecaApp()
