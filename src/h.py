import networkx as nx
from typing import Dict
from .grafo import Mapa


# Construimos la tabla de heurísticas precalculando caminos mínimos reales (Dijkstra)
def build_heuristic_table(grafo: nx.Graph) -> Dict[str, Dict[str, float]]:
    tabla: Dict[str, Dict[str, float]] = {}

    # Usamos weight="weight" para que la heurística sea admisible y consistente
    # (coste real mínimo posible entre dos nodos)
    for origen, distancias in nx.all_pairs_dijkstra_path_length(grafo, weight="weight"):
        tabla[origen] = {}
        for destino, coste in distancias.items():
            if destino == origen:
                continue
            tabla[origen][destino] = float(coste)

    return tabla


# Variable global con la tabla precalculada
m = build_heuristic_table(Mapa)


def h(c: str, t: str) -> float:
    """
    Devuelve la heurística h(n) estimada desde el nodo c hasta el objetivo t.
    Al usar Dijkstra sobre el grafo estático, h(n) = coste real óptimo,
    lo que garantiza que A* encuentre la solución óptima.
    """
    if c == t:
        return 0.0

    if c not in m:
        raise KeyError(c)

    if t not in m[c]:
        raise KeyError(t)

    return m[c][t]
