import math
from dataclasses import dataclass
from queue import PriorityQueue
from typing import Optional

from networkx import Graph
from cw1 import random_connected_weighted_graph, draw


@dataclass
class DijkstraResult:
    start: int
    distance_to_node: list[float]
    previous_nodes: list[int]

def dijkstra(graph: Graph, start: int) -> DijkstraResult:
    nodes_len = len(graph.nodes)
    # odległości
    ds: list[float] = [math.inf] * nodes_len
    # poprzednie węzły
    ps: list[Optional[int]] = [None] * nodes_len
    ds[start] = 0

    queue: PriorityQueue = PriorityQueue()
    queue.put((0, start))

    S = set()

    def relax(u: int, v: int):
        w = graph.edges[u, v]['weight']
        if ds[v] > ds[u] + w:
            ds[v] = ds[u] + w
            ps[v] = u
            # kolejka w pythonie jest trochę uboga... nie da się aktualizować wartości w środku więc wsadzamy jeszcze raz
            queue.put((ds[v], v))

    while len(S) < nodes_len:
        _, u = queue.get()
        # ponieważ wsadzamy elementy kilka razy, musimy je czyścić tutaj
        if u in S:
            continue
        S.add(u)
        for v in graph.neighbors(u):
            if v not in S:
                relax(u, v)

    return DijkstraResult(start, ds, ps)

# budujemy ścieżkę na podstawie wyniku dijkstry
def shortest_path_to(result: DijkstraResult, destination: int) -> list[int]:
    if result.start == destination:
        return []

    prev = result.previous_nodes[destination]
    path = [destination, prev]
    while prev != result.start:
        prev = result.previous_nodes[prev]
        path.append(prev)

    path.reverse()
    return path


def main():
    nodes = 8
    graph = random_connected_weighted_graph(nodes, 10)
    draw(graph, "cw_2")
    start_node = 0
    result = dijkstra(graph, start_node)

    for destination in range(nodes):
        if destination == start_node:
            continue

        shortest_path = shortest_path_to(result, destination)
        print(
            f"Shortest path from {start_node} to {destination}: {shortest_path} with distance: {result.distance_to_node[destination]}")


if __name__ == "__main__":
    main()
