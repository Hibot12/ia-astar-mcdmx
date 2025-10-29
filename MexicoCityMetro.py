import heapq


class MexicoCityMetro:

    def __init__(self):
        # inicializamos el constructor
        self.grafo = {}

    def load_metro_data(self, filename=None):

        # linea 1 --- Rosa
        # Estaciones linea 1
        linea1_estaciones = [
            "Observatorio",
            "Tacubaya",
            "Juanacatlán",
            "Chapultepec",
            "Sevilla",
            "Insurgentes",
            "Cuauhtémoc",
            "Balderas",
            "Salto del Agua",
            "Isabel la Católica",
            "Pino Suárez",
            "Merced",
            "Candelaria",
            "San Lázaro",
            "Moctezuma",
            "Balbuena",
            "Boulevard Puerto Aéreo",
            "Gómez Farías",
            "Zaragoza",
            "Pantitlán",
        ]

        # Añadimos cada estacion al grafo
        for estacion in linea1_estaciones:
            self.añadir_estacion(estacion)

        self.añadir_conexion("Observatorio", "Tacubaya", 2)
        self.añadir_conexion("Tacubaya", "Juanacatlán", 3)
        self.añadir_conexion("Juanacatlán", "Chapultepec", 2)
        self.añadir_conexion("Chapultepec", "Sevilla", 2)
        self.añadir_conexion("Sevilla", "Insurgentes", 2)
        self.añadir_conexion("Insurgentes", "Cuauhtémoc", 2)
        self.añadir_conexion("Cuauhtémoc", "Balderas", 2)
        self.añadir_conexion("Balderas", "Salto del Agua", 2)
        self.añadir_conexion("Salto del Agua", "Isabel la Católica", 2)
        self.añadir_conexion("Isabel la Católica", "Pino Suárez", 2)
        self.añadir_conexion("Pino Suárez", "Merced", 2)
        self.añadir_conexion("Merced", "Candelaria", 3)
        self.añadir_conexion("Candelaria", "San Lázaro", 2)
        self.añadir_conexion("San Lázaro", "Moctezuma", 2)
        self.añadir_conexion("Moctezuma", "Balbuena", 2)
        self.añadir_conexion("Balbuena", "Boulevard Puerto Aéreo", 2)
        self.añadir_conexion("Boulevard Puerto Aéreo", "Gómez Farías", 2)
        self.añadir_conexion("Gómez Farías", "Zaragoza", 2)
        self.añadir_conexion("Zaragoza", "Pantitlán", 3)

        # linea 3 --- Verde Oliva
        # Estaciones de la linea 3
        linea3_estaciones = [
            "Indios Verdes",
            "Deportivo 18 de Marzo",
            "Potrero",
            "La Raza",
            "Tlatelolco",
            "Guerrero",
            "Hidalgo",
            "Juárez",
            "Balderas",
            "Niños Héroes",
            "Hospital General",
            "Centro Médico",
            "Etiopía",
            "Eugenia",
            "División del Norte",
            "Zapata",
            "Coyoacán",
            "Viveros",
            "Miguel Ángel de Quevedo",
            "Copilco",
            "Universidad",
        ]

        # Añadimos cada estacion al grafo
        for estacion in linea3_estaciones:
            self.añadir_estacion(estacion)

        # las conexiones entre estaciones y su tiempo del recorrido en min
        self.añadir_conexion("Indios Verdes", "Deportivo 18 de Marzo", 3)
        self.añadir_conexion("Deportivo 18 de Marzo", "Potrero", 2)
        self.añadir_conexion("Potrero", "La Raza", 2)
        self.añadir_conexion("La Raza", "Tlatelolco", 2)
        self.añadir_conexion("Tlatelolco", "Guerrero", 2)
        self.añadir_conexion("Guerrero", "Hidalgo", 2)
        self.añadir_conexion("Hidalgo", "Juárez", 2)
        self.añadir_conexion("Juárez", "Balderas", 2)
        self.añadir_conexion("Balderas", "Niños Héroes", 2)
        self.añadir_conexion("Niños Héroes", "Hospital General", 2)
        self.añadir_conexion("Hospital General", "Centro Médico", 2)
        self.añadir_conexion("Centro Médico", "Etiopía", 2)
        self.añadir_conexion("Etiopía", "Eugenia", 2)
        self.añadir_conexion("Eugenia", "División del Norte", 2)
        self.añadir_conexion("División del Norte", "Zapata", 2)
        self.añadir_conexion("Zapata", "Coyoacán", 2)
        self.añadir_conexion("Coyoacán", "Viveros", 2)
        self.añadir_conexion("Viveros", "Miguel Ángel de Quevedo", 2)
        self.añadir_conexion("Miguel Ángel de Quevedo", "Copilco", 2)
        self.añadir_conexion("Copilco", "Universidad", 3)

        # linea 7 - Naranja
        linea7_estaciones = [
            "El Rosario",
            "Aquiles Serdán",
            "Camarones",
            "Refinería",
            "Tacuba",
            "San Joaquín",
            "Polanco",
            "Auditorio",
            "Constituyentes",
            "Tacubaya",
            "San Pedro de los Pinos",
            "San Antonio",
            "Mixcoac",
            "Barranca del Muerto",
        ]

        # Añadimos cada estacion al grafo
        for estacion in linea7_estaciones:
            self.añadir_estacion(estacion)

        # las conexiones entre estaciones y su tiempo del recorrido en min
        self.añadir_conexion("El Rosario", "Aquiles Serdán", 2)
        self.añadir_conexion("Aquiles Serdán", "Camarones", 2)
        self.añadir_conexion("Camarones", "Refinería", 2)
        self.añadir_conexion("Refinería", "Tacuba", 2)
        self.añadir_conexion("Tacuba", "San Joaquín", 2)
        self.añadir_conexion("San Joaquín", "Polanco", 2)
        self.añadir_conexion("Polanco", "Auditorio", 2)
        self.añadir_conexion("Auditorio", "Constituyentes", 2)
        self.añadir_conexion("Constituyentes", "Tacubaya", 2)
        self.añadir_conexion("Tacubaya", "San Pedro de los Pinos", 2)
        self.añadir_conexion("San Pedro de los Pinos", "San Antonio", 2)
        self.añadir_conexion("San Antonio", "Mixcoac", 2)
        self.añadir_conexion("Mixcoac", "Barranca del Muerto", 3)

        # linea 9 -- Marron
        linea9_estaciones = [
            "Tacubaya",
            "Patriotismo",
            "Chilpancingo",
            "Centro Médico",
            "Lázaro Cárdenas",
            "Chabacano",
            "Jamaica",
            "Mixiuhca",
            "Velódromo",
            "Ciudad Deportiva",
            "Puebla",
            "Pantitlán",
        ]

        # Añadimos cada estacion al grafo
        for estacion in linea9_estaciones:
            self.añadir_estacion(estacion)

        # las conexiones entre estaciones y su tiempo del recorrido en min
        self.añadir_conexion("Tacubaya", "Patriotismo", 2)
        self.añadir_conexion("Patriotismo", "Chilpancingo", 2)
        self.añadir_conexion("Chilpancingo", "Centro Médico", 2)
        self.añadir_conexion("Centro Médico", "Lázaro Cárdenas", 2)
        self.añadir_conexion("Lázaro Cárdenas", "Chabacano", 2)
        self.añadir_conexion("Chabacano", "Jamaica", 2)
        self.añadir_conexion("Jamaica", "Mixiuhca", 2)
        self.añadir_conexion("Mixiuhca", "Velódromo", 2)
        self.añadir_conexion("Velódromo", "Ciudad Deportiva", 2)
        self.añadir_conexion("Ciudad Deportiva", "Puebla", 2)
        self.añadir_conexion("Puebla", "Pantitlán", 3)

        # linea 12 -- Oro
        linea12_estaciones = [
            "Mixcoac",
            "Insurgentes Sur",
            "Hospital 20 de Noviembre",
            "Parque de los Venados",
            "Eje Central",
            "Ermita",
            "Mexicaltzingo",
            "Atlalilco",
            "Culhuacán",
            "San Andrés Tomatlán",
            "Lomas Estrella",
            "Calle 11",
            "Periférico Oriente",
            "Tezonco",
            "Olivos",
            "Nopalera",
            "Zapotitlán",
            "Tlaltenco",
            "Tláhuac",
        ]

        # Añadimos cada estacion al grafo
        for estacion in linea12_estaciones:
            self.añadir_estacion(estacion)

        # las conexiones entre estaciones y su tiempo del recorrido en min
        self.añadir_conexion("Mixcoac", "Insurgentes Sur", 2)
        self.añadir_conexion("Insurgentes Sur", "Hospital 20 de Noviembre", 2)
        self.añadir_conexion("Hospital 20 de Noviembre", "Parque de los Venados", 2)
        self.añadir_conexion("Parque de los Venados", "Eje Central", 2)
        self.añadir_conexion("Eje Central", "Ermita", 2)
        self.añadir_conexion("Ermita", "Mexicaltzingo", 2)
        self.añadir_conexion("Mexicaltzingo", "Atlalilco", 2)
        self.añadir_conexion("Atlalilco", "Culhuacán", 2)
        self.añadir_conexion("Culhuacán", "San Andrés Tomatlán", 2)
        self.añadir_conexion("San Andrés Tomatlán", "Lomas Estrella", 2)
        self.añadir_conexion("Lomas Estrella", "Calle 11", 2)
        self.añadir_conexion("Calle 11", "Periférico Oriente", 2)
        self.añadir_conexion("Periférico Oriente", "Tezonco", 3)
        self.añadir_conexion("Tezonco", "Olivos", 2)
        self.añadir_conexion("Olivos", "Nopalera", 2)
        self.añadir_conexion("Nopalera", "Zapotitlán", 2)
        self.añadir_conexion("Zapotitlán", "Tlaltenco", 2)
        self.añadir_conexion("Tlaltenco", "Tláhuac", 2)

    def añadir_estacion(self, nombre_estacion):
        if nombre_estacion not in self.grafo:
            self.grafo[nombre_estacion] = []

    def añadir_conexion(self, estacion1, estacion2, tiempo):
        # Añadimos una conexion duplex entre las dos estaciones
        # Porque puedes ir de una estacion a la otra en ambas direciones
        if estacion1 in self.grafo and estacion2 in self.grafo:
            self.grafo[estacion1].append((estacion2, tiempo))
            self.grafo[estacion2].append((estacion1, tiempo))
        else:
            self.añadir_estacion(estacion1)
            self.añadir_estacion(estacion2)

    def get_vecino(self, estacion):
        return self.grafo.get(estacion, [])

    def heuristica(self, estacion1, estacion2):
        # Por ahora devolvemos 0 para que A* se comporte como Dijkstra
        return 0

    def a_star(self, estacion_orig, estacion_dest):
        # verificamos si ambas estaciones existen
        if not self.estacion_exists(estacion_orig):
            print(f"Error: Estacion de origen: '{estacion_orig}' no existe")
            return None, None

        if not self.estacion_exists(estacion_dest):
            print(f"Error: Estacion de destino: '{estacion_dest}' no existe")
            return None, None
        # caso en el que el origen y el destino son lo mismo
        if estacion_dest == estacion_orig:
            return [estacion_orig], 0

        # inicializamos las puntuaciones
        # g_coste: coste actual de la estacion origen a cada estacion
        # creamos un diccionario donde Keys: todas las estaciones de self.grafo
        # Values:float(inf) --> infinito para cada valor para inicializar
        g_puntacion = {}
        for estacion in self.grafo:
            g_puntacion[estacion] = float("inf")
        g_puntacion[estacion_orig] = 0

        # f_puntuacion es un diccionario que almacena el coste estimado total (g + h)
        # f(n)=g(n)+h(n) donde h(n) es la heuristica

        f_puntuacion = {}
        for estacion in self.grafo:
            f_puntuacion[estacion] = float("inf")
        f_puntuacion[estacion_orig] = self.heuristica(estacion_orig, estacion_dest)

        # prev es un diccionario que vamos a utilizar para reconstruir el camino
        # guarda de que estacion venimos para llegar a cada estacion
        prev = {}
        for estacion in self.grafo:
            prev[estacion] = None

        # heapq siempre mantiene el elemento mas pequeño al frente
        cola_prioridad = []
        heapq.heappush(cola_prioridad, (f_puntuacion[estacion_orig], estacion_orig))

        # creamos un set que guarda el conjunto de estaciones ya visitadas
        visitadas = set()

        # se sigue iterando hasta que no quedan valores en la cola de prioridad
        while cola_prioridad:
            # sacamos la estacion con el f_puntuacion mas baja
            # heappop automaticamente saca el elemento minimo, porque el heapq se guarda el elemento mas pequeno al principio
            f_actual, estacion_actual = heapq.heappop(cola_prioridad)

            # verificamos si la estacion actual es la estacion destino
            if estacion_actual == estacion_dest:
                camino = self.reconstruct_path(prev, estacion_orig, estacion_dest)
                return camino, g_puntacion[estacion_dest]

            # si ya hemos visitado esa estacion la saltamos y continuamos
            if estacion_actual in visitadas:
                continue

            # maracamos la estacion como visitada
            visitadas.add(estacion_actual)

            # examinamos todas los vecinos de la estacion actual
            for vecino, tiempo_viaje in self.get_vecino(estacion_actual):
                # saltamos el vecino si ya le hemos visitado
                if vecino in visitadas:
                    continue
                # calculamos el coste tentativo para llegar al vecino, pasando por la estacion actual
                # calculamos este coste tentativo para evaluar is es mejor que el coste actual que
                # tenemos registrado.
                g_tentativo = g_puntacion[estacion_actual] + tiempo_viaje

                # verificamos si este camino al vecino es mejor que el mejor conocido
                if g_tentativo < g_puntacion[vecino]:
                    # si lo es lo actualizamos con el nuevo mejor camino
                    prev[vecino] = estacion_actual
                    g_puntacion[vecino] = g_tentativo

                    # ahora calculamos la heuristica para el vecino
                    h_puntacion = self.heuristica(vecino, estacion_dest)
                    # tambien hay que actualizar el coste total estimado (f = g + h)
                    f_puntuacion[vecino] = g_puntacion[vecino] + h_puntacion
                    # lo añadimos a la cola heapq para que luego lo podemos explorar
                    heapq.heappush(cola_prioridad, (f_puntuacion[vecino], vecino))

        # si salimos del bucle sin encontrar el destino, eso signifca que no hay camino
        print(f"No encontramos un camino de '{estacion_orig}' a '{estacion_dest}'")
        return None, None

    def reconstruct_path(self, previous_estacions, start, end):
        # 1. CHECK IF PATH EXISTS:
        # If previous_estacions[end] is None and end != start, no path exists
        if end not in previous_estacions:
            return None

        # 2. BUILD PATH BACKWARDS:
        # Start from end estacion and work backwards to start
        path = []
        current = end

        # 3. TRAVERSE BACKWARDS:
        # Keep following previous_estacions until you reach None
        while current is not None:
            path.append(current)
            current = previous_estacions[current]

        # 4. REVERSE PATH:
        # The path was built backwards, so reverse it
        path.reverse()

        # 5. RETURN THE PATH:
        return path

    def get_all_estacions(self):
        return list(self.grafo.keys())

    def estacion_exists(self, estacion_name):
        return estacion_name in self.grafo


def main():
    metro = MexicoCityMetro()
    metro.load_metro_data()


if __name__ == "__main__":
    main()
