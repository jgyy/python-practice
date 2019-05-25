"""
Dijkstra’s Algorithm - Create a program that finds
the shortest path through a graph using its edges.
"""


def dijkstra(graph, node):
    """
    Simulate the dijkstra algorithm in a graph
    in case we have a disjoint graph
    """
    distance_to = {node: 0}
    distance_path = {}
    while distance_to:
        # in case we have a disjoint graph
        op_node = min(distance_to)
        distance_path[op_node] = distance_to[op_node]
        del distance_to[op_node]
        for x_path, x_len in graph[op_node].items():
            if x_path not in distance_path:
                if x_path not in distance_to:
                    distance_to[x_path] = distance_path[op_node] + x_len
                elif distance_to[x_path] > distance_path[op_node] + x_len:
                    distance_to[x_path] = distance_path[op_node] + x_len
    return distance_path
