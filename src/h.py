# -*- coding: utf-8 -*-
"""
Heurística h(n) para A* en el Metro de CDMX.

    La tabla heurística se AUTOGENERA desde el grafo 'Mapa' (grafo.py) con los
    pesos actuales. Así, siempre está actualizada si cambian los weights del grafo.

Propiedades:
    - h es minorante y consistente (usa el coste real óptimo precalculado).
    - A* es admisible y óptimo con esta h.
"""

from __future__ import annotations

import networkx as nx
from .grafo import Mapa  # Grafo con pesos 'weight' declarado en grafo.py


def _construir_tabla_dict(G: nx.Graph) -> dict[str, dict[str, int]]:
    """
    Construye un diccionario con los costes mínimos (sumas de 'weight') entre
    todos los pares de estaciones del grafo.

    Se hace una sola vez al importar el módulo.
    """
    tabla: dict[str, dict[str, int]] = {}
    for origen, distancias in nx.all_pairs_dijkstra_path_length(G, weight="weight"):
        tabla_origen: dict[str, int] = {}
        for destino, coste in distancias.items():
            if destino != origen:
                tabla_origen[destino] = int(coste)
        tabla[origen] = tabla_origen
    return tabla


# ---------------------------------------------------------------------------
# Tabla heurística: se genera desde grafo.py
# ---------------------------------------------------------------------------
_TABLA_HEURISTICA = _construir_tabla_dict(Mapa)


def h(c: str, t: str) -> int:
    """
    Heurística h(n) para A*: coste estimado mínimo entre 'c' y 't'.
    Implementación:
        Consultar la tabla precalculada (coste real óptimo).

    Devuelve:
        int: coste heurístico (nunca sobreestima).
    """
    if c == t:
        return 0

    try:
        tabla_origen = _TABLA_HEURISTICA[c]
    except KeyError as exc:
        msg = f"Estación desconocida en heurística (origen): {c!r}"
        raise KeyError(msg) from exc

    try:
        return tabla_origen[t]
    except KeyError as exc:
        msg = f"Estación desconocida en heurística (destino): {t!r}"
        raise KeyError(msg) from exc
