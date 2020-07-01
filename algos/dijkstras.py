# an algorithm for finding the single shortest paths between nodes in a graph
# it is a greedy algorithm
# Library for INT_MAX
import sys

class Graph():
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_solution(self, dist):
        print("Vertex distance from source ")
        for node in range(self.v):
            print(node, "to", dist[node])

    # Find the vertex with minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def min_distance(self, dist, sptree):
        #initialize minimum distance
        min = sys.maxsize

        #search for the vertext in the shortest path tree
        for v in range(self.v):
            if dist[v] < min and sptree[v] == False:
                min = dist[v]
                min_index = v
        return min_index


    # impliment algo for a graph represented using
    # adjacency matrix representation

    def dijkstras(self, src):
        dist = [sys.maxsize] * self.v
        dist[src] = 0
        sptree = [False] * self.v

        for cout in range(self.v):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.min_distance(dist, sptree)

            # min distance vertex in put in the shortest path tree
            sptree[u] = True

            # Update dist value if current distance is greater then new distance
            for v in range(self.v):
                if self.graph[u][v]>0 and sptree[v] == False and \
                dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)

g = Graph(9)
g.graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];
g.dijkstras(0)



