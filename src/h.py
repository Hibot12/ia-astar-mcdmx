"""Heurística h(n) para A* en el Metro de CDMX.

La tabla heurística se autogenera desde el grafo `Mapa` (grafo.py) con los pesos
actuales, por lo que permanece alineada si cambian los weights del grafo.

Propiedades:
- h es minorante y consistente (usa el coste real óptimo precalculado).
- A* es admisible y óptimo con esta h.
"""

from typing import Dict

import networkx as nx
from .grafo import Mapa  # Grafo con pesos 'weight' declarado en grafo.py

HeuristicTable = Dict[str, Dict[str, int]]


def _build_heuristic_table(grafo: nx.Graph) -> HeuristicTable:
    """Precalcula las distancias mínimas (suma de `weight`) entre todas las estaciones."""
    return {
        origen: {
            destino: int(coste)
            for destino, coste in distancias.items()
            if destino != origen
        }
        for origen, distancias in nx.all_pairs_dijkstra_path_length(grafo, weight="weight")
    }


_HEURISTIC_TABLE = _build_heuristic_table(Mapa)


def h(c: str, t: str) -> int:
    """
    Heurística h(n) para A*: coste estimado mínimo entre `c` y `t` usando la tabla precalculada.
    """
    if c == t:
        return 0

    try:
        return _HEURISTIC_TABLE[c][t]
    except KeyError as exc:  # pragma: no cover - señalamos la pareja faltante.
        pareja = f"{c!r} -> {t!r}"
        raise KeyError(f"No existe heurística precalculada para {pareja}") from exc
