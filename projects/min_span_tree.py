"""
Minimum Spanning Tree - Create a program which takes a connected,
undirected graph with weights and outputs the minimum spanning tree
of the graph i.e., a sub graph that is a tree, contains all the vertices,
and the sum of its weights is the least possible.
"""


def compare_list_by_content(list1, list2):
    """Compares two lists by content. If the lists have
    the same number of elements and the same contents
    regardless of order, returns True. Else, returns False."""
    if len(list1) == len(list2):
        for i in list1:
            if i in list2:
                pass
            else:
                return False
    else:
        return False
    return True


def prime_algorithm(a_graph):
    """This function is an implementation for Prims algorithm.
    Given a weighted graph returns the minimum spanning tree,
    ie a graph with the the least edges required for all
    the nodes to be connected and with the minimum distance."""
    starting_nodes = start_nodes(a_graph)
    visited_nodes = []
    min_span_tree = {}
    current_node = starting_nodes[0]
    visited_nodes.append(current_node)
    while not compare_list_by_content(starting_nodes, visited_nodes):
        node_a = find_minimum_edge(a_graph, visited_nodes)
        min_span_tree[node_a] = a_graph[node_a]
        # Since edges are two way check which of the two nodes is the
        # new visited and add it two the visited nodes list.
        if node_a[1] in visited_nodes:
            visited_nodes.append(node_a[0])
        else:
            visited_nodes.append(node_a[1])
    return min_span_tree


def start_nodes(a_graph):
    """Given a graph in the form of (a, b):x, where a, b are the
    nodes and x the weight, returns a list with all the distinct
    nodes in the graph."""
    starting_nodes = []
    for edge in a_graph:
        if edge[0] not in starting_nodes:
            starting_nodes.append(edge[0])
        if edge[1] not in starting_nodes:
            starting_nodes.append(edge[1])
    return starting_nodes


def find_minimum_edge(a_graph, visited_nodes):
    """Given a graph a list of nodes, find the edge
    with the minimum weight regarding the list and does not
    form a cycle"""
    minimum_distance = 1000
    minimum_edge = None
    for node in visited_nodes:
        for edge in a_graph:
            # Check both nodes of the edge, since edges are two way.
            if node == edge[0]:
                if a_graph[edge] <= minimum_distance:
                    if edge[1] not in visited_nodes:
                        minimum_distance = a_graph[edge]
                        minimum_edge = edge
            elif node == edge[1]:
                if a_graph[edge] <= minimum_distance:
                    if edge[0] not in visited_nodes:
                        minimum_distance = a_graph[edge]
                        minimum_edge = edge
            else:
                pass
    return minimum_edge


def start():
    """Starts the minimum spanning tree program"""
    graph = {}
    add_new = 'y'
    print("Insert the graph.")
    print("---------------------")
    while add_new == 'y':
        print("\nNew edge")
        while True:
            try:
                a_node_edge, b_node_edge = input("Insert the nodes of the edge: ").split()
                break
            except ValueError:
                print("You must give exactly two nodes")
        while True:
            try:
                weight = int(input("Enter the weight of the edge: "))
                break
            except ValueError:
                print("The edge's weight must be an integer.")
        graph[a_node_edge, b_node_edge] = int(weight)
        # Enter loop first time, if the following line wasn't
        # added the user would not be able to add new edge.
        add_new = 'k'
        while add_new not in ('y', 'n'):
            add_new = input("Add another edge? (y/n): ")
    solution = prime_algorithm(graph)
    print("--------------------------")
    print("The minimum spanning tree edges are: ")
    cost = 0
    for edge in solution:
        cost += solution[edge]
        print(edge)
    print("\nTotal cost: ", cost)


if __name__ == "__main__":
    start()
