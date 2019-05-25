"""
Eulerian Path - Create a program which will take as an input a graph
and output either a Eulerian path or a Eulerian cycle, or state that
it is not possible. A Eulerian Path starts at one node and traverses
every edge of a graph through every node and finishes at another node.
A Eulerian cycle is a eulerian Path that starts and finishes at the same node.
"""
from copy import copy


def is_connected(graph):
    """
    is_connected - Checks if a graph in the form of a dictionary is
    connected or not, using Breadth-First Search Algorithm (BFS)
    :param graph:
    :return:
    """
    start_node = list(graph)[0]
    color = {v: 'white' for v in graph}
    color[start_node] = 'gray'
    start = [start_node]
    while start:
        u_graph = start.pop()
        for v_graph in graph[u_graph]:
            if color[v_graph] == 'white':
                color[v_graph] = 'gray'
                start.append(v_graph)
            color[u_graph] = 'black'
    return list(color.values()).count('black') == len(graph)


def odd_degree_nodes(graph):
    """
    odd_degree_nodes - returns a list of all G odd degrees nodes
    :param graph:
    :return:
    """
    odd_degree_node = []
    for u_graph in graph:
        if len(graph[u_graph]) % 2 != 0:
            odd_degree_node.append(u_graph)
    return odd_degree_node


def from_dict(graph):
    """
    from_dict - return a list of tuples links from a graph G in a
    dictionary format
    :param graph:
    :return:
    """
    links = []
    for u_graph in graph:
        for v_graph in graph[u_graph]:
            links.append((u_graph, v_graph))
    return links


def fleury(graph):
    """
    fleury(G) - return eulerian trail from graph G or a
    string 'Not Eulerian Graph' if it's not possible to trail a path
    checks if G has eulerian cycle or trail
    """
    odn = odd_degree_nodes(graph)
    if len(odn) > 2 or len(odn) == 1:
        return 'Not Eulerian Graph'
    g_graph = copy(graph)
    trail = []
    if len(odn) == 2:
        u_graph = odn[0]
    else:
        u_graph = list(g_graph)[0]
    while from_dict(g_graph):
        current_vertex = u_graph
        bridge = False
        for u_graph in g_graph[current_vertex]:
            g_graph[current_vertex].remove(u_graph)
            g_graph[u_graph].remove(current_vertex)
            bridge = not is_connected(g_graph)
            if bridge:
                g_graph[current_vertex].append(u_graph)
                g_graph[u_graph].append(current_vertex)
            else:
                break
        if bridge:
            g_graph[current_vertex].remove(u_graph)
            g_graph[u_graph].remove(current_vertex)
            g_graph.pop(current_vertex)
        trail.append((current_vertex, u_graph))
    return trail


if __name__ == '__main__':
    # testing seven bridges of konigsberg
    print('Konigsberg')
    G = {0: [2, 2, 3], 1: [2, 2, 3], 2: [0, 0, 1, 1, 3], 3: [0, 1, 2]}
    print(fleury(G))

    # testing an eulerian cycle
    print('1st Eulerian Cycle')
    G = {0: [1, 4, 6, 8], 1: [0, 2, 3, 8], 2: [1, 3], 3: [1, 2, 4, 5], 4: [0, 3],
         5: [3, 6], 6: [0, 5, 7, 8], 7: [6, 8], 8: [0, 1, 6, 7]}
    print(fleury(G))

    # testing another eulerian cycle
    print('2nd Eulerian Cycle')
    G = {1: [2, 3, 4, 4], 2: [1, 3, 3, 4], 3: [1, 2, 2, 4], 4: [1, 1, 2, 3]}
    print(fleury(G))

    # testing an eulerian trail
    print('Eulerian Trail')
    G = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
    print(fleury(G))
