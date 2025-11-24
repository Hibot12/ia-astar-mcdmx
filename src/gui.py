import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import os
import unicodedata

# importamos el algoritmo de busqueda
from .algoritmo import calcular_ruta


class MetroGUI(tk.Tk):
    def __init__(self):
        # inicializamos la ventana de tkinter
        super().__init__()
        # titulo del la GUI de la applicacion
        self.title("Metro Mexico Applicacion")
        # tamaño del GUI mas pequeño para que el mapa no sea gigante
        self.geometry("1100x700")
        # color de fondo de la ventana principal
        self.configure(bg="#2E2E2E")

        # configuracion del tema oscuro
        style = ttk.Style()
        style.theme_use("clam")

        # configuramos los colores de los widgets
        style.configure("TFrame", background="#2E2E2E")
        style.configure(
            "TLabel", background="#2E2E2E", foreground="white", font=("Arial", 10)
        )
        style.configure("TLabelframe", background="#2E2E2E", foreground="white")
        style.configure("TLabelframe.Label", background="#2E2E2E", foreground="white")
        style.configure(
            "TButton", background="#444444", foreground="white", bordercolor="#2E2E2E"
        )
        style.map("TButton", background=[("active", "#555555")])

        # estilo para las entradas de texto
        style.configure(
            "TEntry", fieldbackground="#404040", foreground="white", insertcolor="white"
        )

        # esto crea el contenedor principal con dos columnas left y right
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # esto es el frame izquierdo para los controles
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        # frame derecho para el mapa del metro
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # etiquetas para pedir las estaciones
        self.estacion_orig_label = ttk.Label(
            left_frame, text="Introduzca la estacion de Origen:"
        )
        self.estacion_orig_label.pack(pady=10)

        # esto son las entradas de texto (uno para origen y otro para el destino)
        self.entry_origen = ttk.Entry(left_frame, width=30)
        self.entry_origen.pack(pady=5)

        self.estacion_dest_label = ttk.Label(
            left_frame, text="Introduzca la estacion de Destino:"
        )
        self.estacion_dest_label.pack(pady=10)

        self.entry_destino = ttk.Entry(left_frame, width=30)
        self.entry_destino.pack(pady=5)

        # esto es el boton para demostrar lo que el usuario esta escribiendo
        self.boton = ttk.Button(
            left_frame, text="Buscar la ruta", command=self.mostrar_inputs
        )
        self.boton.pack(pady=10)

        # esto son las etiquetas para mostrar los resultados de la ruta
        self.output_estacion_orig = ttk.Label(
            left_frame, text="", font=("Arial", 10, "bold")
        )
        self.output_estacion_orig.pack(pady=5)
        self.output_estacion_dest = ttk.Label(
            left_frame, text="", font=("Arial", 10, "bold")
        )
        self.output_estacion_dest.pack(pady=5)

        # esto es el frame para mostrar el resultado de la ruta
        result_frame = ttk.LabelFrame(
            left_frame, text="Informacion de la Ruta", padding=10
        )
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # un widget de texto para mostrar el recorrido completo
        # bg oscuro y fg blanco para el tema
        # state disabled para que no se pueda escribir, solo seleccionar
        self.result_text = tk.Text(
            result_frame,
            width=40,
            height=25,
            wrap=tk.WORD,
            font=("Arial", 9),
            bg="#1E1E1E",
            fg="white",
            insertbackground="white",
            state="disabled",
        )
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # esto añade un scrollbar para el widget del texto de informacion de la ruta
        scrollbar = ttk.Scrollbar(result_frame, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)

        # esto crea el canvas para mostrar el mapa del metro
        # fondo oscuro para que cuadre con el tema
        self.canvas = tk.Canvas(right_frame, bg="#2E2E2E", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # bind para redimensionar
        self.canvas.bind("<Configure>", self.on_resize)

        # esto son las coordenadas exactas con respecto a la imagen del metro
        # ------- NOOOO TOCAR !!!!!!!!!!!!! -------------
        self.coords_estacion = {
            "Tacubaya": (179, 305),
            "San Pedro de los Pinos": (178, 371),
            "San Antonio": (179, 411),
            "Mixcoac": (179, 464),
            "Barranca del Muerto": (179, 529),
            "Constituyentes": (179, 236),
            "Auditorio": (178, 165),
            "Polanco": (178, 90),
            "Observatorio": (136, 349),
            "Patriotismo": (269, 305),
            "Chilpancingo": (372, 305),
            "Lazaro Cardenas": (542, 305),  # Sin tilde como lo guardó el usuario
            "Juanacatlan": (220, 263),  # Sin tilde
            "Chapultepec": (257, 226),
            "Sevilla": (299, 185),
            "Insurgentes": (341, 151),
            "Cuauhtemoc": (386, 150),  # Sin tilde
            "Balderas": (436, 151),
            "Juarez": (436, 78),  # Sin tilde
            "Niños Héroes": (436, 187),  # Con tilde como lo guardó el usuario
            "Hospital General": (437, 230),
            "Centro Medico": (436, 304),  # Sin tilde
            "Etiopia": (437, 345),  # Sin tilde
            "Eugenia": (436, 382),
            "Division del Norte": (437, 422),  # Sin tilde
            "Zapata": (436, 463),
            "Coyoacan": (437, 501),  # Sin tilde
            "Viveros": (437, 542),
            "Miguel Ángel de Quevedo": (436, 580),  # Con tildes
            "Copilco": (437, 619),
            "Universidad": (437, 658),
            "Parque de los Venados": (535, 461),
            "Eje Central": (596, 553),
            "Insurgentes Sur": (250, 460),
            "Hospital 20 de Noviembre": (336, 463),
        }
        # ------- NOOOO TOCAR !!!!!!!!!!!!! -------------

        # esto carga el mapa del metro
        self.load_metro_map()

    def load_metro_map(self):
        # este codigo carga el mapa del metro en el GUI
        try:
            # obtener el directorio donde está este script
            script_dir = os.path.dirname(os.path.abspath(__file__))

            # intentar varias rutas posibles para encontrar Metro.png
            possible_paths = [
                os.path.join(script_dir, "Metro.png"),
                os.path.join(script_dir, "..", "Metro.png"),
                os.path.join(script_dir, "..", "src", "Metro.png"),
                "Metro.png",
            ]

            # intentar cada ruta hasta encontrar el archivo
            image_loaded = False
            for path in possible_paths:
                if os.path.exists(path):
                    self.original_image = Image.open(path)
                    self.display_image()
                    image_loaded = True
                    break

            if not image_loaded:
                raise FileNotFoundError("No se encontró Metro.png")

        except Exception as e:
            self.write_result(f"Error cargando mapa: {e}\n")

    def on_resize(self, event):
        # redibuja el mapa cuando se redimensiona la ventana
        self.display_image()

    def get_coords_safe(self, station_name):
        # metodo auxiliar para buscar coordenadas ignorando el nombre de la linea
        # y normalizando acentos para coincidir con el diccionario
        clean_name = station_name.split("_")[0] if "_" in station_name else station_name

        # busqueda directa
        if clean_name in self.coords_estacion:
            return self.coords_estacion[clean_name]

        # busqueda normalizada sin acentos y minusculas
        norm_search = "".join(
            c
            for c in unicodedata.normalize("NFD", clean_name)
            if unicodedata.category(c) != "Mn"
        ).lower()

        for key, coord in self.coords_estacion.items():
            norm_key = "".join(
                c
                for c in unicodedata.normalize("NFD", key)
                if unicodedata.category(c) != "Mn"
            ).lower()
            if norm_search == norm_key:
                return coord
        return None

    def write_result(self, text):
        # funcion auxiliar para escribir en el cuadro de texto de solo lectura
        # habilitamos la escritura
        self.result_text.config(state="normal")
        # escribimos al final
        self.result_text.insert(tk.END, text)
        # deshabilitamos para que el usuario no pueda borrar
        self.result_text.config(state="disabled")

    def clear_result(self):
        # funcion auxiliar para limpiar el cuadro de texto
        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state="disabled")

    def display_image(self, path=None):
        # esta funcion muestra el mapa del metro con la ruta resaltada en ROJO
        # si no tiene la imagen original return
        if not hasattr(self, "original_image"):
            return

        # creamos una copia de la imagen original
        img = self.original_image.copy()

        # si hay una ruta, la dibujamos en ROJO sobre el mapa
        if path and len(path) > 1:
            draw = ImageDraw.Draw(img)

            # dibujamos las lineas de la ruta EN ROJO
            for i in range(len(path) - 1):
                estacion1 = path[i]
                estacion2 = path[i + 1]

                # usamos el metodo seguro para obtener coordenadas
                coord1 = self.get_coords_safe(estacion1)
                coord2 = self.get_coords_safe(estacion2)

                if coord1 and coord2:
                    # si las coordenadas son distintas dibujamos linea
                    # si son iguales es un transbordo visualmente estatico
                    if coord1 != coord2:
                        x1, y1 = coord1
                        x2, y2 = coord2
                        # dibujamos la linea ROJA para la ruta
                        draw.line([(x1, y1), (x2, y2)], fill="#FF0000", width=8)

            # dibujamos circulos en cada estacion de la ruta
            for estacion in path:
                coord = self.get_coords_safe(estacion)
                if coord:
                    x, y = coord
                    radio = 10

                    # hacemos que la estacion de origen sea verde y la de destino sea azul
                    if estacion == path[0]:
                        color = "#00FF00"  # Verde brillante
                    elif estacion == path[-1]:
                        color = "#0000FF"  # Azul brillante
                    elif "_" in estacion and path.count(estacion.split("_")[0]) > 0:
                        # es un nodo de transbordo
                        color = "#FFA500"  # Naranja
                    else:
                        color = "#FF0000"  # Rojo

                    draw.ellipse(
                        [x - radio, y - radio, x + radio, y + radio],
                        fill=color,
                        outline="white",
                        width=3,
                    )

        # esto redimensiona la imagen para ajustar al canvas
        # obtenemos el ancho actual del canvas en pixeles
        canvas_width = self.canvas.winfo_width()
        # obtenemos la altura actual del canvas en pixeles
        canvas_height = self.canvas.winfo_height()

        # esto verifica que el canvas tiene dimensiones validas (que sea mayor que 1 pixel)
        if canvas_width > 1 and canvas_height > 1:
            # calculamos la proporcion de aspecto de la imagen (ancho/alto)
            img_ratio = img.width / img.height
            # calculamos la proporcion de aspecto del canvas
            canvas_ratio = canvas_width / canvas_height

            # aqui determinamos como redimensionar la imagen manteniendo su proporsion
            if img_ratio > canvas_ratio:
                # si la imagen es mas ancha proporcionalmente, ajustamos por el ancho
                new_width = canvas_width
                new_height = int(canvas_width / img_ratio)
            else:
                # si la imagen es mas alto proporcionalmente, ajustamos por la altura
                new_height = canvas_height
                new_width = int(canvas_height * img_ratio)

            # redimensionamos la imagen a las nuevas dimensiones
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # convertimos la imagen a una version que tkinter pueda mostrar
        self.photo = ImageTk.PhotoImage(img)
        # tambien borramos todo el contenido anterior del canvas
        self.canvas.delete("all")
        # dibujamos la nueva imagen en el canvas en la posición (0, 0)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def mostrar_inputs(self):
        # esto es la funcion que funciona cuando el usuario pulsa el boton
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()

        # actualizar etiquetas
        self.output_estacion_orig.config(text=f"Origen: {origen}")
        self.output_estacion_dest.config(text=f"Destino: {destino}")

        # limpiar resultados anteriores
        self.clear_result()

        # validar entrada
        if not origen or not destino:
            self.write_result("⚠️ Por favor introduzca ambas estaciones.\n")
            self.display_image()
            return

        # buscar la ruta usando el algoritmo
        path, length = calcular_ruta(origen, destino)

        # SI ES ERROR (STR) O NONE
        if isinstance(path, str) or path is None:
            self.write_result(f"No se encontró una ruta entre:\n")
            self.write_result(f"   '{origen}' y '{destino}'\n\n")

            # Solo mostramos el mensaje del algoritmo si es un string descriptivo
            if isinstance(path, str):
                self.write_result(
                    f"{path}\n"
                )  # Ya tiene "Error:" dentro en algoritmo.py

            self.display_image()
            return

        # mostrar resultados
        self.write_result("-" * 45 + "\n")
        self.write_result("     RUTA ENCONTRADA \n")
        self.write_result("-" * 45 + "\n\n")

        self.write_result(f"Origen: {origen}\n")
        self.write_result(f"Destino: {destino}\n")
        self.write_result(f"Tiempo Estimado: {length:.1f} minutos\n")
        self.write_result(f"Numero de Estaciones: {len(path)}\n\n")

        self.write_result("RECORRIDO:\n")
        self.write_result("-" * 35 + "\n")

        for i, station_node in enumerate(path, 1):
            # limpiamos el nombre para mostrar
            display_name = station_node
            if "_" in station_node:
                parts = station_node.split("_")
                display_name = f"{parts[0]} ({parts[1].replace('L','Línea ')})"

            # detectar transbordo para mostrar en texto
            prefix = ""
            if i > 1:
                prev_node = path[i - 2]
                prev_name = prev_node.split("_")[0] if "_" in prev_node else prev_node
                curr_name = (
                    station_node.split("_")[0] if "_" in station_node else station_node
                )
                if prev_name == curr_name:
                    prefix = " -> TRANSBORDO -> "
                    self.write_result(f"   {prefix}{display_name}\n")
                    continue

            if i == 1:
                self.write_result(f" {i:2d}. {display_name} ------- INICIO \n")
            elif i == len(path):
                self.write_result(f" {i:2d}. {display_name} ------- DESTINO \n")
            else:
                self.write_result(f" {i:2d}. {display_name}\n")

        # mostrar en el mapa con la ruta en ROJO
        self.display_image(path)


if __name__ == "__main__":
    app = MetroGUI()
    app.mainloop()
