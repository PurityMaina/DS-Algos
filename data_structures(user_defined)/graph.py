# non-linear data structure consisting on nodes and edges
# nodes or vertex
# edges - connects two nodes or vertices
# weight - value of the edge
# implementation using a dict, keys are nodes, values are the nodes adjacent neighbours

# Python program for
# validation of a graph

# import dictionary for graph
from collections import defaultdict

# function for adding edge to graph
graph = defaultdict(list)


def addEdge(graph, u, v):
    graph[u].append(v)


# definition of function
def generate_edges(graph):
    edges = []

    # for each node in graph
    for node in graph:

        # for each neighbour node of a single node
        for neighbour in graph[node]:
            # if edge exists then append
            edges.append((node, neighbour))
    return edges


# declaration of graph as dictionary
addEdge(graph, 'a', 'c')
addEdge(graph, 'b', 'c')
addEdge(graph, 'b', 'e')
addEdge(graph, 'c', 'd')
addEdge(graph, 'c', 'e')
addEdge(graph, 'c', 'a')
addEdge(graph, 'c', 'b')
addEdge(graph, 'e', 'b')
addEdge(graph, 'd', 'c')
addEdge(graph, 'e', 'c')

# Driver Function call
# to print generated graph
print(generate_edges(graph))