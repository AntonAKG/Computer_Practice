import asyncio
import numpy as np
from method.not_indicative import NotIndicative
from method.indicative import Indicate

from draw_picture import DrawGraph

async def main() -> None:
    vertices = [1, 2, 3, 4, 5, 6, 7]  # number 21
    edges = [(1, 2), (2, 3), (3, 4), (5, 4), (3, 5), (6, 5), (6, 2), (7, 6)]  # number 21

    vertices_indicative = [1, 2, 3, 4, 5, 6, 7, 8]  # number 15
    edges_indicative = [(1, 2), (2, 3), (1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 4)]  # number 15

    obj_not = NotIndicative(vertices, edges)
    obj = Indicate(vertices_indicative, edges_indicative)

    ### NotIndicative ###
    data_full = await obj_not.degrees_of_vertices()

    for key, val in data_full.items():
        print(f'Степінь {key} вершини: {val}')

    data_semi = await obj_not.semi_degree()

    for num, value in data_semi.items():
        print(f'Напівстерінь {num} вершини: входу {value[0]}, виходу {value[1]}')

    print("матриця суміжності: ")
    await obj_not.print_adjacency_matrix()

    print("матриця інцидентності: ")
    await  obj_not.incident_matrices()

    ### Indicative ###
    data_full_in = await obj.degrees_of_vertices()

    for key, val in data_full_in.items():
        print(f'Степінь {key} вершини: {val}')

    print("матриця суміжності: ")
    await obj.print_adjacency_matrix()

    print("матриця інцидентності: ")
    await obj.incident_matrices()

    # await DrawGraph.draw_not()
    # await DrawGraph.draw_indicate()

if __name__ == '__main__':
    asyncio.run(main())
