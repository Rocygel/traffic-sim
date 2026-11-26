import numpy as np
import networkx as nx

class Graph:
    """
    Class for graph depicting some part of a road network.
    """
    def __init__(self, nodes, edges):
        """
        Initialize variable graph based on nodes/edges
        """
        n = len(nodes)
        adjacency_matrix = np.zeros((n, n))
        widths = {}

        for edge in edges:
            u, v, weight = edge[:3]
            width = edge[3]
            adjacency_matrix[u, v] = weight
            adjacency_matrix[v, u] = weight
            widths[(u, v)] = width
            widths[(v, u)] = width

        self.graph = nx.from_numpy_array(adjacency_matrix)
        positions = {i: coord for i, coord in enumerate(nodes)}
        nx.set_node_attributes(self.graph, positions, "pos")

        for (a, b), w in widths.items():
            if self.graph.has_edge(a, b):
                self.graph[a][b]["width"] = w

    def positions(self):
        return nx.get_node_attributes(self.graph, "pos")

    def node_pos(self, node):
        return self.graph.nodes[node]["pos"]

    def edge_weight(self, u, v):
        return self.graph[u][v].get("weight", 1.0)

    def edge_width(self, u, v):
        return self.graph[u][v].get("width", 7.0)

    def edge_widths(self):
        return [self.edge_width(u, v) for u, v in self.graph.edges()]

    def neighbors(self, node):
        return list(self.graph.neighbors(node))