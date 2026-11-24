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
        adjacency_matrix = np.zeros(n, n)

        for u, v, weight in edges:
            adjacency_matrix[u, v] = weight
            adjacency_matrix[v, u] = weight

        self.graph = nx.from_numpy_array(adjacency_matrix)

        #positions = 
        nx.set_node_attributes(self.graph, positions, "pos")

    def positions(self):
        return nx.get_node_attributes(self.graph, "pos")

    def node_pos(self, node):
        return self.graph.nodes[node]["pos"]

    def edge_weight(self, u, v):
        return self.graph[u][v].get("weight", 1.0)

    def neighbors(self, node):
        return list(self.graph.neighbors(node))