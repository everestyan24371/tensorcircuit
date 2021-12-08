"""
Some common graphs and lattices
"""
# pylint: disable=invalid-name

from functools import partial
from typing import Any, Optional, Sequence, Tuple

import networkx as nx

Graph = Any


def Line1D(
    n: int,
    node_weight: Optional[Sequence[float]] = None,
    edge_weight: Optional[Sequence[float]] = None,
    pbc: bool = True,
) -> Graph:
    """
    1D chain with ``n`` sites

    :param n: [description]
    :type n: int
    :param pbc: [description], defaults to True
    :type pbc: bool, optional
    :return: [description]
    :rtype: Graph
    """

    g = nx.Graph()
    if edge_weight is None:
        edge_weight = 1.0  # type: ignore
    if not isinstance(edge_weight, list):
        edge_weight = [edge_weight for _ in range(n)]  # type: ignore
    if node_weight is None:
        node_weight = 0.0  # type: ignore
    if not isinstance(node_weight, list):
        node_weight = [node_weight for _ in range(n)]  # type: ignore
    for i in range(n):
        g.add_node(i, weight=node_weight[i])
    for i in range(n - 1):
        g.add_edge(i, i + 1, weight=edge_weight[i])
    if pbc is True:
        g.add_edge(n - 1, 0, weight=edge_weight[i])
    return g


def Even1D(n: int, s: int = 0) -> Graph:
    g = nx.Graph()
    for i in range(n):
        g.add_node(i, weight=1.0)
    for i in range(s, n, 2):
        g.add_edge(i, (i + 1) % n, weight=1.0)
    return g


Odd1D = partial(Even1D, s=1)


class Grid2DCoord:
    def __init__(self, n: int, m: int):
        # row first
        self.m = m
        self.n = n
        self.mn = m * n

    def one2two(self, i: int) -> Tuple[int, int]:
        x = i // self.n
        y = i % self.n
        return x, y

    def two2one(self, x: int, y: int) -> int:
        return x * self.n + y

    def all_rows(self, pbc: bool = False) -> Sequence[Tuple[int, int]]:
        r = []
        for i in range(self.mn):
            if (i + 1) % self.n != 0:
                r.append((i, i + 1))
            elif pbc:
                r.append((i, i - self.n + 1))
        return r

    def all_cols(self, pbc: bool = False) -> Sequence[Tuple[int, int]]:
        r = []
        for i in range(self.mn):
            if i + self.n < self.mn:
                r.append((i, i + self.n))
            elif pbc:
                r.append((i, i - (self.m - 1) * self.n))
        return r


def Grid2D(m: int, n: int, pbc: bool = True) -> Graph:
    def one2two(i: int) -> Tuple[int, int]:
        x = i // n
        y = i % n
        return x, y

    def two2one(x: int, y: int) -> int:
        return x * n + y

    g = nx.Graph()
    for i in range(m * n):
        g.add_node(i, weight=0)
    for i in range(m * n):
        x, y = one2two(i)
        if pbc is False and x - 1 < 0:
            pass
        else:
            g.add_edge(i, two2one((x - 1) % m, y), weight=1)
        if pbc is False and y - 1 < 0:
            pass
        else:
            g.add_edge(i, two2one(x, (y - 1) % n), weight=1)
    return g


def Triangle2D(m: int, n: int) -> Graph:
    def one2two(i: int) -> Tuple[int, int]:
        y = i // m
        x = i % m
        return x, y

    def two2one(x: int, y: int) -> int:
        return x + y * m

    g = nx.Graph()
    for i in range(m * n):
        g.add_node(i, weight=0)
    for i in range(m * n):
        x, y = one2two(i)
        g.add_edge(i, two2one((x + 1) % m, y), weight=1)
        g.add_edge(i, two2one(x, (y + 1) % n), weight=1)
        g.add_edge(i, two2one((x + 1) % m, (y - 1) % n), weight=1)
    return g
