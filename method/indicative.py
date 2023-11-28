from method.not_indicative import NotIndicative


class Indicate(NotIndicative):
    """

    Indicate Class
    ==============

    This class inherits from the `NotIndicative` class and provides additional functionality related to indicating degrees of vertices, printing adjacency matrix, and incident matrices.

    Methods
    -------
    __init__(vertices: list, edges: list)
        Initializes an Indicate object with the given vertices and edges.

    degrees_of_vertices()
        Computes the degrees of vertices in the graph.

    print_adjacency_matrix()
        Prints the adjacency matrix of the graph.

    incident_matrices()
        Computes the incident matrices of the graph.

    """
    def __init__(self, vertices: list, edges: list):
        super().__init__(vertices, edges)

    async def degrees_of_vertices(self):
        return await super().degrees_of_vertices()

    async def print_adjacency_matrix(self):
        await super().print_adjacency_matrix()

    async def incident_matrices(self):
        await super().incident_matrices()
