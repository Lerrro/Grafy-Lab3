from networkx import Graph
import networkx as nx
import matplotlib.pyplot as plt

from cw1 import random_connected_weighted_graph

# zmodyfikowany alforytm do rysowania drzewa rozpinającego na istniejącym grafie
def draw(graph: Graph, name: str, tree_graph: Graph = None):
    pos = nx.circular_layout(graph)

    edge_colors = []
    for u, v in list(graph.edges()):
        if tree_graph is not None and tree_graph.has_edge(u, v):
            edge_colors.append('red')
        else:
            edge_colors.append('gray')

    nx.draw(
        graph, pos,
        with_labels=True,
        node_color='lightblue',
        edge_color=edge_colors,
        node_size=2000,
        font_size=16
    )

    edge_labels = {(u, v): graph.edges[u, v]['weight'] for u, v in graph.edges()}
    nx.draw_networkx_edge_labels(
        graph, pos,
        edge_labels=edge_labels,
        font_size=12,
        label_pos=0.45,
        rotate=False
    )

    plt.savefig(name + ".png")
    plt.clf()


def kruskal(graph: Graph) -> Graph:
    # słownik w którym trzymamy root'y stworzonych drzew
    parent = {}

    def find_root(u):
        if parent[u] != u:
            parent[u] = find_root(parent[u])
        return parent[u]

    # można łączyć jeżeli dwa węzły należą do innego drzewa
    def try_connect(u, v):
        root_u, root_v = find_root(u), find_root(v)
        if root_u != root_v:
            # jeżeli połączenie się udało to zmieniamy rodzica jednemu węzłu
            parent[root_v] = root_u
            return True
        return False

    # na początku każdy węzeł jest osobnym drzewem
    for node in graph.nodes:
        parent[node] = node

    edges = sorted(graph.edges(data=True), key=lambda e: e[2]['weight'])
    tree_graph = Graph()

    for u, v, data in edges:
        if try_connect(u, v):
            tree_graph.add_edge(u, v, weight=data['weight'])

    return tree_graph


def main():
    nodes = 8
    graph = random_connected_weighted_graph(nodes, 10)
    draw(graph, "cw_5", kruskal(graph))
    

if __name__ == "__main__":
    main()