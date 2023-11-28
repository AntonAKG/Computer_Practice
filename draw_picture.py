import networkx as nx
import matplotlib.pyplot as plt


class DrawGraph:
    @classmethod
    async def draw_indicate(cls):
        graph = nx.Graph()

        graph.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])

        graph.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 4)])

        pos = nx.circular_layout(graph)
        nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black",
                edge_color="black", linewidths=1, font_weight="bold")

        plt.title('Oрієнтований граф')
        plt.show()

    @classmethod
    async def draw_not(cls):
        graph = nx.DiGraph()

        graph.add_nodes_from([1, 2, 3, 4, 5, 6, 7])

        graph.add_edges_from([(1, 2), (2, 3), (3, 4), (5, 4), (3, 5), (6, 5), (6, 2), (7, 6)])

        pos = nx.circular_layout(graph)
        nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black",
                edge_color="black", linewidths=1, font_weight="bold")

        plt.title('Неорієнтований граф')
        plt.show()
