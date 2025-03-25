import matplotlib.pyplot as plt
import networkx as nx
import random

def random_graph_edges(n, l): #from lab 1, task 3
    graph = nx.Graph()
    nodes = list(range(n))
    graph.add_nodes_from(nodes)
    edges = set()
    while len(edges) < l:
        u, v = random.sample(nodes, 2)
        if (u, v) not in edges and (v, u) not in edges:
            edges.add((u, v))
    graph.add_edges_from(edges)
    return graph

def find_connected_components(graph): # from lab2, task 3
    def dfs(v, component_id, component):
        comp[v] = component_id
        component.append(v)
        for neighbor in graph.neighbors(v):
            if comp[neighbor] == -1:
                dfs(neighbor, component_id, component)

    comp = {v: -1 for v in graph.nodes}
    components = []
    component_id = 0

    for v in graph.nodes:
        if comp[v] == -1:
            component_id += 1
            component = []
            dfs(v, component_id, component)
            components.append(component)

    components.sort(key=len, reverse=True)
    return components

def randomize_graph(graph, iterations=500): #from lab2, task 2 (modified)
    for i in range(iterations):
        edges = list(graph.edges())
        edges_count = len(edges)
        edge1 = random.randrange(edges_count)
        edge2 = random.randrange(edges_count)
        if edge1 == edge2:
            continue

        (a, b) = edges[edge1]
        (c, d) = edges[edge2]

        if a != c and a != d and b != c and b != d:
            if not graph.has_edge(a, d) and not graph.has_edge(b, c):
                graph.remove_edge(a, b)
                graph.remove_edge(c, d)
                graph.add_edge(a, d)
                graph.add_edge(b, c)
        if len(find_connected_components(graph))==1: #new line
            return graph #new line
    return None #changed line

def give_random_weights(graph, lowerbound, higerbound):
    for edge in graph.edges():
        graph.edges[edge]['weight']=random.randint(lowerbound,higerbound)
    return graph

def random_connected_weighted_graph(n,l):
    if l<n-1:
        print("Not enough edges to create connected graph")
        return None
    for i in range(100):
        graph=random_graph_edges(n,l)
        graph=randomize_graph(graph)
        if graph is not None:
            break
    if graph is None:
        return None
    return give_random_weights(graph,1,11)
    
def draw(graph: nx.Graph, name: str):
    pos = nx.circular_layout(graph)

    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16)

    edge_labels = {(u, v): graph.edges[u, v]['weight'] for u, v in graph.edges()}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=12, label_pos=0.45, rotate=False)  # Adjust label_pos

    plt.savefig(name + ".png")
    plt.clf()

def main():
    graph=random_connected_weighted_graph(6,10)
    if graph is not None:
        draw(graph,"cw1")

if __name__ == "__main__":
    main()
