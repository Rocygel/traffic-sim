import matplotlib.pyplot as plt
import networkx as nx
from graph import Graph
from vehicle import Car, Fleet

NODES = [(3, 2), (4, 2), (1, 6), (7, 3)]
EDGES = [(1, 3, 10/3), (0, 2, 10/3), (0, 1, 10/5)]
VEHICLE_TYPES = [Car, Car]

def visual(graph, fleet, ax):
    ax.clear()
    pos = graph.positions()

    nx.draw(graph.graph,
            pos=pos,
            ax=ax,
            #width=widths,
            with_labels=True,
            node_size=500,
            )

    vehicle_cords = [vehicle.cords(graph) for vehicle in fleet.vehicles]
    for vehicle in fleet.vehicles:
        x, y = vehicle.cords(graph)
        ax.scatter(x, y, color="crimson", s=70, zorder=5)
        ax.annotate(
            str(vehicle.id),
            (x, y),
            textcoords="offset points",
            xytext=(0, 8),
            ha="center",
            fontsize=9,
            fontweight="bold",
            color="crimson",
            zorder=6,
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.75),
        )


def main():
    graph = Graph(nodes = NODES, edges = EDGES)
    fleet = Fleet(graph = graph, vehicle_types = VEHICLE_TYPES)

    for t in range(5):
        

        fig, ax = plt.subplots()
        visual(graph, fleet, ax)
        ax.set_title(f"Time step {t}")
        fleet.step_all()
    
    plt.show()


if __name__ == "__main__":
    main()