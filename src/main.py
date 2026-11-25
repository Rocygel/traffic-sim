import matplotlib.pyplot as plt
import networkx as nx
from graph import Graph

NODES = [(3, 2), (4, 2), (1, 6), (7, 3)]
EDGES = [(1, 3, 2), (0, 2, 3), (0, 1, 4)]

def visual(graph, ax):
    ax.clear()
    pos = graph.positions()

    nx.draw(graph.graph,
            pos=pos,
            ax=ax,
            width=widths,
            with_labels=True,
            node_size=500,
            )


def main():
    graph = Graph(nodes = NODES, edges = EDGES)

    fig, ax = plt.subplots()
    visual(graph, ax)
    plt.show()


if __name__ == "__main__":
    main()