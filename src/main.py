import numpy as np
import networkx as nx
import matplotlib as plt

nodes = [(3, 2), (4, 2), (1, 6), (7, 3)]
edges = [(1, 3, 2), (0, 2, 3), (0, 1, 4)]

N = len(nodes)
adjacency_matrix = np.zeros((N, N))

# bidirectional graph
for u, v, weight in edges:
    adjacency_matrix[u, v] = weight
    adjacency_matrix[v, u] = weight

#construct graph
graph = nx.from_numpy_matrix(adjacency_matrix)