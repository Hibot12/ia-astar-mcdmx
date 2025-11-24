import heapq
from .grafo import Mapa
from .h import h


def buscar_nodo_inicial(nombre_input):
    # busca un nodo en el grafo que coincida con el nombre del usuario
    # ej si usuario pone tacubaya devuelve tacubaya_l1 el primero que pille
    for nodo in Mapa.nodes():
        if nombre_input.lower() in nodo.lower():
            return nodo
    return None


def calcular_ruta(origen_txt, destino_txt):
    # ejecuta a estrella y devuelve camino y tiempo total
    # si hay error devuelve mensaje de error y none

    nodo_inicio = buscar_nodo_inicial(origen_txt)
    # buscamos un nodo concreto del destino para usarlo de referencia en la heuristica
    nodo_destino_ref = buscar_nodo_inicial(destino_txt)

    if not nodo_inicio:
        return f"Error: No encuentro la estación '{origen_txt}'", None
    if not nodo_destino_ref:
        return f"Error: No encuentro la estación '{destino_txt}'", None

    # inicializacion a estrella
    g_puntuacion = {nodo: float("inf") for nodo in Mapa.nodes()}
    g_puntuacion[nodo_inicio] = 0

    f_puntuacion = {nodo: float("inf") for nodo in Mapa.nodes()}

    try:
        f_puntuacion[nodo_inicio] = h(nodo_inicio, nodo_destino_ref)
    except:
        f_puntuacion[nodo_inicio] = 0

    cola = []
    # heapq ordena por el primer elemento de la tupla f_score
    heapq.heappush(cola, (f_puntuacion[nodo_inicio], nodo_inicio))

    came_from = {}
    visitados = set()

    while cola:
        _, actual = heapq.heappop(cola)

        # comprobar si hemos llegado al destino ignorando sufijo de linea
        # ej si estamos en pantitlan_l9 y el destino es pantitlan exito
        nombre_actual_limpio = actual.split("_")[0] if "_" in actual else actual
        if destino_txt.lower() in nombre_actual_limpio.lower():
            camino = reconstruir_camino(came_from, actual)
            tiempo_total = g_puntuacion[actual]
            return camino, tiempo_total

        if actual in visitados:
            continue
        visitados.add(actual)

        for vecino in Mapa.neighbors(actual):
            peso = Mapa[actual][vecino]["weight"]
            g_tentativo = g_puntuacion[actual] + peso

            if g_tentativo < g_puntuacion[vecino]:
                came_from[vecino] = actual
                g_puntuacion[vecino] = g_tentativo

                # calculamos h hacia el nodo de referencia del destino
                coste_h = h(vecino, nodo_destino_ref)

                f_puntuacion[vecino] = g_tentativo + coste_h
                heapq.heappush(cola, (f_puntuacion[vecino], vecino))

    return "No se encontró ruta posible entre estas estaciones.", None


def reconstruir_camino(came_from, actual):
    camino = [actual]
    while actual in came_from:
        actual = came_from[actual]
        camino.append(actual)
    camino.reverse()
    return camino
