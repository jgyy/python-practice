"""
Connected Graph - Create a program which takes a graph as
an input and outputs whether every node is connected or not.
"""


def is_connected(graph):
    """
    is_connected - Checks if a graph in the form of a dictionary is
    connected or not, using Breadth-First Search Algorithm (BFS)
    :param graph:
    :return:
    """
    start_node = list(graph.keys())[0]
    color = {v: 'white' for v in graph.keys()}
    color[start_node] = 'gray'
    start = [start_node]
    while start:
        graph_u = start.pop()
        for graph_v in graph[graph_u]:
            if color[graph_v] == 'white':
                color[graph_v] = 'gray'
                start.append(graph_v)
            color[graph_u] = 'black'
    return list(color.values()).count('black') == len(graph.keys())


if __name__ == '__main__':
    # testing seven bridges of konigsberg
    G = {0: [2, 2, 3], 1: [2, 2, 3], 2: [0, 0, 1, 1, 3], 3: [0, 1, 2]}
    print('Is Konigsberg connected? ', is_connected(G))

    # testing an eulerian cycle
    G = {0: [1, 4, 6, 8], 1: [0, 2, 3, 8], 2: [1, 3], 3: [1, 2, 4, 5], 4: [0, 3],
         5: [3, 6], 6: [0, 5, 7, 8], 7: [6, 8], 8: [0, 1, 6, 7]}
    print('Is 1st Eulerian Cycle connected? ', is_connected(G))

    # testing another eulerian cycle
    G = {1: [2, 3, 4, 4], 2: [1, 3, 3, 4], 3: [1, 2, 2, 4], 4: [1, 1, 2, 3]}
    print('Is 2nd Eulerian Cycle connected? ', is_connected(G))

    # testing an eulerian trail
    G = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
    print('Is Eulerian Trail connected? ', is_connected(G))
