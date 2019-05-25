"""
Graph from links - Create a program that will
create a graph or network from a series of links.
"""


def check_node(node, graph):
    """Checks whether a node is in a graph"""
    return node in graph


def from_links(links):
    """
    Takes a list of links in the form of tuples, or lists,
    with two elements describing the connected nodes
    and returns a graph in the form of a dictionary.
    Example input: [(1,2),(1,4),(2,3),(3,4)] or [[1,2],[1,4],(,3),(3,4)]
    Example output (fm input): {1:[2,4],2:[1,3],3:[2,4],4:[1,3]}
    """

    graph = {}

    for link in links:

        for node in link:
            if not check_node(node, graph):
                graph[node] = []

        graph[link[0]].append(link[1])
        graph[link[1]].append(link[0])
    return graph


if __name__ == '__main__':
    LINK_1 = from_links([(1, 2), (1, 4), (2, 3), (3, 4)])
    LINK_2 = from_links([[1, 2], [1, 4], [2, 3], [3, 4]])
    print(LINK_1, '\n', LINK_2)
    assert(LINK_1 == {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]})
    assert(LINK_2 == {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]})
    print(LINK_1, '\n', LINK_2)
