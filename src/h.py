"""Heurística h(n) para A* en el Metro de CDMX.

La tabla heurística se autogenera desde el grafo `Mapa` (grafo.py) con los pesos
actuales, por lo que permanece alineada si cambian los weights del grafo.

"""

from typing import Dict

import networkx as nx
from .grafo import Mapa  # Grafo con pesos 'weight' declarado en grafo.py


def build_heuristic_table(grafo: nx.Graph) -> Dict[str, Dict[str, int]]:
    """
    Calcula los costes mínimos (sumas de 'weight') entre todas las estaciones del grafo.
    Se recorre el resultado de all_pairs_dijkstra_path_length y se arma el diccionario a mano.
    """
    tabla: Dict[str, Dict[str, int]] = {}

    for origen, distancias in nx.all_pairs_dijkstra_path_length(grafo, weight="weight"):
        tabla[origen] = {}
        for destino, coste in distancias.items():
            if destino == origen:
                continue
            tabla[origen][destino] = int(coste)

    return tabla


m: Dict[str, Dict[str, int]] = build_heuristic_table(Mapa)


def h(c: str, t: str) -> int:
    """
    Heurística h(n) para A*: coste estimado mínimo entre `c` y `t` usando la tabla precalculada.
    """
    if c == t:
        return 0

    if c not in m:
        raise KeyError(c)

    destinos = m[c]

    if t not in destinos:
        raise KeyError(t)

    return destinos[t]
