import numpy as np


class NotIndicative:
    """

    :class: NotIndicative

    Initialize a NotIndicative object with vertices and edges.

    :param vertices: A list of vertices.
    :param edges: A list of edges.

    """
    def __init__(self, vertices: list, edges: list):
        """
        Initialize a NotIndicative object with vertices and edges.

        :param vertices: A list of vertices.
        :param edges: A list of edges.

        """
        self.vertices = vertices
        self.edges = edges

    async def degrees_of_vertices(self) -> dict:
        """
        Calculates the degree of each vertex in a graph.

        :return: A dictionary where the keys represent the vertices and the values represent their respective degrees.
        :rtype: dict
        """
        number_dict = dict((key, 0) for key in range(1, len(self.vertices) + 1))

        for el in self.edges:
            for key, value in number_dict.items():
                if key == el[0] or key == el[1]:
                    number_dict[key] += 1

        return number_dict

    async def semi_degree(self) -> dict:
        """
        Calculate the semi-degree of each vertex in a graph.

        :return: A dictionary containing the semi-degree of each vertex in the graph.
        :rtype: dict
        """
        number_dict = dict((key, [0, 0]) for key in range(1, len(self.vertices) + 1))

        for el in self.edges:
            number_dict[el[0]][0] += 1
            number_dict[el[1]][1] += 1

        return number_dict

    async def print_adjacency_matrix(self) -> None:
        """
        Prints the adjacency matrix of the given graph represented by a list of edges.

        :return: None
        """
        nodes = set([node for edge in self.edges for node in edge])

        matrix = {node: [0] * len(nodes) for node in nodes}

        for edge in self.edges:
            matrix[edge[0]][edge[1] - 1] = 1

        for row in matrix.values():
            print(row)

    async def incident_matrices(self) -> None:
        """
        Calculate the incident matrices for the vertices and edges of a NotIndicative object.

        :return: None
        """
        matrix = np.zeros((len(self.vertices), len(self.edges)), dtype=int)
        for i, edge in enumerate(self.edges):
            matrix[self.vertices.index(edge[0]), i] = -1
            matrix[self.vertices.index(edge[1]), i] = 1
        print(matrix)
