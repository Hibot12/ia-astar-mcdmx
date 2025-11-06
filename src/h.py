# -*- coding: utf-8 -*-
"""
Heurística h(n) para A* en el Metro de CDMX.

    La matriz heurística se AUTOGENERA desde el grafo 'Mapa' (grafo.py) con los
    pesos actuales. Así, siempre está actualizada si cambian los weights del grafo.

Propiedades:
    - h es minorante y consistente (usa el coste real óptimo precalculado).
    - A* es admisible y óptimo con esta h.
"""

from __future__ import annotations

from typing import Iterable

import networkx as nx
from .grafo import Mapa  # Grafo con pesos 'weight' declarado en grafo.py


def _construir_tabla_matriz(G: nx.Graph) -> tuple[tuple[str, ...], list[list[int]]]:
    """
    Construye una matriz con los costes mínimos (sumas de 'weight') entre
    todos los pares de estaciones del grafo.

    Se hace una sola vez al importar el módulo.
    """
    estaciones = tuple(G.nodes)
    n = len(estaciones)
    matriz = [[0] * n for _ in range(n)]

    for i, origen in enumerate(estaciones):
        distancias = nx.single_source_dijkstra_path_length(G, origen, weight="weight")
        for destino, coste in distancias.items():
            if destino != origen:
                j = _buscar_indice(destino, estaciones)
                if j is not None:
                    matriz[i][j] = int(coste)

    return estaciones, matriz


def _buscar_indice(nombre: str, nombres: Iterable[str]) -> int | None:
    for indice, estacion in enumerate(nombres):
        if estacion == nombre:
            return indice
    return None


# ---------------------------------------------------------------------------
# Tabla heurística: se genera desde grafo.py
# ---------------------------------------------------------------------------
_ESTACIONES, _MATRIZ_HEURISTICA = _construir_tabla_matriz(Mapa)


def h(c: str, t: str) -> int:
    """
    Heurística h(n) para A*: coste estimado mínimo entre 'c' y 't'.
    Implementación:
        Consultar la matriz precalculada (coste real óptimo).

    Devuelve:
        int: coste heurístico (nunca sobreestima).
    """
    if c == t:
        return 0

    origen_idx = _buscar_indice(c, _ESTACIONES)
    destino_idx = _buscar_indice(t, _ESTACIONES)

    if origen_idx is None or destino_idx is None:
        msg = f"Estación desconocida en heurística: {c!r} -> {t!r}"
        raise KeyError(msg)

    return _MATRIZ_HEURISTICA[origen_idx][destino_idx]
