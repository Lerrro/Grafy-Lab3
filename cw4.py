from cw1 import random_connected_weighted_graph, draw
from cw3 import create_distances_matrix


def main():
    nodes = 8
    graph = random_connected_weighted_graph(nodes, 10)
    draw(graph, "cw_4")

    distances_matrix = create_distances_matrix(graph)

    sums = [sum(row) for row in distances_matrix]
    max_dists = [max(row) for row in distances_matrix]

    center_index = sums.index(min(sums))
    center_minimax_index = max_dists.index(min(max_dists))

    print("Suma odległości:", sums)
    print("Odległości od najdalszego:", max_dists)
    print("Centrum:", center_index)
    print("Centrum minimax:", center_minimax_index)

if __name__ == "__main__":
    main()