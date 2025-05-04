import math

from cw1 import draw, random_connected_weighted_graph
from cw2 import dijkstra
from networkx import Graph

def create_distances_matrix(graph: Graph) -> list[list[float]]:
    nodes = len(graph)
    # inicjalizacja pustej tablicy
    distances_matrix = [[math.inf for _ in range(nodes)]
                        for _ in range(nodes)]

    for start_node in range(nodes):
        result = dijkstra(graph, start_node)
        for destination in range(nodes):
            distances_matrix[start_node][destination] = result.distance_to_node[destination]

    return distances_matrix

def main():
    nodes = 8
    graph = random_connected_weighted_graph(nodes, 10)
    draw(graph, "cw_3")

    distances_matrix = create_distances_matrix(graph)


    for i in range(nodes):
        for j in range(nodes):
            print(distances_matrix[i][j], end=" ")
        print()


if __name__ == "__main__":
    main()
