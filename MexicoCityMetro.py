import heapq


class MexicoCityMetro:

    def __init__(self):
        # Inicializamos el constructor.
        self.grafo = {}

    def load_metro_data(self, filename=None):
        """
          - L1 (granate): Observatorio → Balderas
          - L3 (verde claro): Universidad → Juárez
          - L7 (naranja): Barranca del Muerto → Polanco
          - L9 (marrón): Tacubaya → Lázaro Cárdenas
          - L12 (verde oscuro): Mixcoac → Eje Central
        Transbordos: Mixcoac (L7–L12), Zapata (L3–L12), Tacubaya (L1–L7–L9), Centro Médico (L3–L9), Balderas (L1–L3).
        """

        # Línea 1: Observatorio → Balderas.
        l1 = [
            "Observatorio",
            "Tacubaya",
            "Juanacatlán",
            "Chapultepec",
            "Sevilla",
            "Insurgentes",
            "Cuauhtémoc",
            "Balderas",
        ]
        for e in l1:
            self.añadir_estacion(e)
        self.añadir_conexion("Observatorio", "Tacubaya", 2)
        self.añadir_conexion("Tacubaya", "Juanacatlán", 3)
        self.añadir_conexion("Juanacatlán", "Chapultepec", 2)
        self.añadir_conexion("Chapultepec", "Sevilla", 2)
        self.añadir_conexion("Sevilla", "Insurgentes", 2)
        self.añadir_conexion("Insurgentes", "Cuauhtémoc", 2)
        self.añadir_conexion("Cuauhtémoc", "Balderas", 2)

        # Línea 3: Universidad → Juárez.
        l3 = [
            "Universidad",
            "Copilco",
            "Miguel Ángel de Quevedo",
            "Viveros",
            "Coyoacán",
            "Zapata",
            "División del Norte",
            "Eugenia",
            "Etiopía",
            "Centro Médico",
            "Hospital General",
            "Niños Héroes",
            "Balderas",
            "Juárez",
        ]
        for e in l3:
            self.añadir_estacion(e)
        self.añadir_conexion("Universidad", "Copilco", 3)
        self.añadir_conexion("Copilco", "Miguel Ángel de Quevedo", 2)
        self.añadir_conexion("Miguel Ángel de Quevedo", "Viveros", 2)
        self.añadir_conexion("Viveros", "Coyoacán", 2)
        self.añadir_conexion("Coyoacán", "Zapata", 2)
        self.añadir_conexion("Zapata", "División del Norte", 2)
        self.añadir_conexion("División del Norte", "Eugenia", 2)
        self.añadir_conexion("Eugenia", "Etiopía", 2)
        self.añadir_conexion("Etiopía", "Centro Médico", 2)
        self.añadir_conexion("Centro Médico", "Hospital General", 2)
        self.añadir_conexion("Hospital General", "Niños Héroes", 2)
        self.añadir_conexion("Niños Héroes", "Balderas", 2)
        self.añadir_conexion("Balderas", "Juárez", 2)

        # Línea 7: Barranca del Muerto → Polanco.
        l7 = [
            "Barranca del Muerto",
            "Mixcoac",
            "San Antonio",
            "San Pedro de los Pinos",
            "Tacubaya",
            "Constituyentes",
            "Auditorio",
            "Polanco",
        ]
        for e in l7:
            self.añadir_estacion(e)
        self.añadir_conexion("Barranca del Muerto", "Mixcoac", 3)
        self.añadir_conexion("Mixcoac", "San Antonio", 2)
        self.añadir_conexion("San Antonio", "San Pedro de los Pinos", 2)
        self.añadir_conexion("San Pedro de los Pinos", "Tacubaya", 2)
        self.añadir_conexion("Tacubaya", "Constituyentes", 2)
        self.añadir_conexion("Constituyentes", "Auditorio", 2)
        self.añadir_conexion("Auditorio", "Polanco", 2)

        # Línea 9: Tacubaya → Lázaro Cárdenas.
        l9 = [
            "Tacubaya",
            "Patriotismo",
            "Chilpancingo",
            "Centro Médico",
            "Lázaro Cárdenas",
        ]
        for e in l9:
            self.añadir_estacion(e)
        self.añadir_conexion("Tacubaya", "Patriotismo", 2)
        self.añadir_conexion("Patriotismo", "Chilpancingo", 2)
        self.añadir_conexion("Chilpancingo", "Centro Médico", 2)
        self.añadir_conexion("Centro Médico", "Lázaro Cárdenas", 2)

        # Línea 12: Mixcoac → Eje Central.
        # Nota: Se incluye "Zapata" también.
        l12 = [
            "Mixcoac",
            "Insurgentes Sur",
            "Hospital 20 de Noviembre",
            "Zapata",
            "Parque de los Venados",
            "Eje Central",
        ]
        for e in l12:
            self.añadir_estacion(e)
        self.añadir_conexion("Mixcoac", "Insurgentes Sur", 2)
        self.añadir_conexion("Insurgentes Sur", "Hospital 20 de Noviembre", 2)
        self.añadir_conexion("Hospital 20 de Noviembre", "Zapata", 2)
        self.añadir_conexion("Zapata", "Parque de los Venados", 2)
        self.añadir_conexion("Parque de los Venados", "Eje Central", 2)

    def añadir_estacion(self, nombre_estacion):
        if nombre_estacion not in self.grafo:
            self.grafo[nombre_estacion] = []

    def añadir_conexion(self, estacion1, estacion2, tiempo):
        # Aseguramos que la arista se añada siempre, aunque alguna estación no existiera aún.
        if estacion1 not in self.grafo:
            self.añadir_estacion(estacion1)
        if estacion2 not in self.grafo:
            self.añadir_estacion(estacion2)
        self.grafo[estacion1].append((estacion2, tiempo))
        self.grafo[estacion2].append((estacion1, tiempo))

    def get_vecino(self, estacion):
        return self.grafo.get(estacion, [])

    def heuristica(self, estacion1, estacion2):
        # Por ahora devolvemos 0 para que A* se comporte como Dijkstra (admisible).
        return 0

    def a_star(self, estacion_orig, estacion_dest):
        # Verificamos si ambas estaciones existen.
        if not self.estacion_exists(estacion_orig):
            print(f"Error: Estacion de origen: '{estacion_orig}' no existe")
            return None, None

        if not self.estacion_exists(estacion_dest):
            print(f"Error: Estacion de destino: '{estacion_dest}' no existe")
            return None, None
        # Caso en el que el origen y el destino son el mismo.
        if estacion_dest == estacion_orig:
            return [estacion_orig], 0

        # Inicializamos las puntuaciones.
        g_puntacion = {}
        for estacion in self.grafo:
            g_puntacion[estacion] = float("inf")
        g_puntacion[estacion_orig] = 0

        f_puntuacion = {}
        for estacion in self.grafo:
            f_puntuacion[estacion] = float("inf")
        f_puntuacion[estacion_orig] = self.heuristica(estacion_orig, estacion_dest)

        # Diccionario auxiliar para reconstruir el camino óptimo.
        prev = {}
        for estacion in self.grafo:
            prev[estacion] = None

        # Cola de prioridad ordenada por f(n) = g(n) + h(n).
        cola_prioridad = []
        heapq.heappush(cola_prioridad, (f_puntuacion[estacion_orig], estacion_orig))

        # Conjunto de estaciones ya exploradas.
        visitadas = set()

        while cola_prioridad:
            f_actual, estacion_actual = heapq.heappop(cola_prioridad)

            if estacion_actual == estacion_dest:
                camino = self.reconstruct_path(prev, estacion_orig, estacion_dest)
                return camino, g_puntacion[estacion_dest]

            if estacion_actual in visitadas:
                continue

            visitadas.add(estacion_actual)

            for vecino, tiempo_viaje in self.get_vecino(estacion_actual):
                if vecino in visitadas:
                    continue
                g_tentativo = g_puntacion[estacion_actual] + tiempo_viaje

                if g_tentativo < g_puntacion[vecino]:
                    # Relajamos la arista si encontramos un camino más corto.
                    prev[vecino] = estacion_actual
                    g_puntacion[vecino] = g_tentativo

                    # Actualizamos el valor estimado y lo reinsertamos en la cola.
                    h_puntacion = self.heuristica(vecino, estacion_dest)
                    f_puntuacion[vecino] = g_puntacion[vecino] + h_puntacion
                    heapq.heappush(cola_prioridad, (f_puntuacion[vecino], vecino))

        print(f"No encontramos un camino de '{estacion_orig}' a '{estacion_dest}'")
        return None, None

    def reconstruct_path(self, previous_estacions, start, end):
        # Si no hay registro del nodo final, no existe un camino válido.
        if end not in previous_estacions:
            return None

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous_estacions[current]
        path.reverse()
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
