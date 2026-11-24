import matplotlib as plt
import networkx as nx
from graph import Graph

NODES = [(3, 2), (4, 2), (1, 6), (7, 3)]
EDGES = [(1, 3, 2), (0, 2, 3), (0, 1, 4)]

def visual(graph):
    ax.clear()
    pos = graph.positions()
    nx_draw_graph = graph.graph

    nx.draw(nx_draw_graph)

# bidirectional graph
for u, v, weight in edges:
    adjacency_matrix[u, v] = weight
    adjacency_matrix[v, u] = weight

#construct graph
graph = nx.from_numpy_matrix(adjacency_matrix)


def main():

    graph = Graph(nodes = NODES, edges = EDGES)

    fig, ax = plt.subplots()
    visual(graph, ax)
    plt.show()


if __name__ == "__main__":
    main()