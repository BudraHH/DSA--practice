from collections import defaultdict
import heapq


class Node:
    def __init__(self, vertex: int, distance: int) -> None:
        self.vertex = vertex
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

class Edge:
    def __init__(self,dest: int,weight: int) -> None:
        self.dest = dest
        self.weight = weight

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def addEdge(self,src: int,dest: int,weight: int) -> None:
        self.adjList[src].append(Edge(dest,weight))

    def addVertex(self,v: int) -> None:
        self.adjList[v] = []

    def dfs(self, src: int) -> None:
        result = []
        visited = {src}
        stack = [src]

        while stack:
            vertex = stack.pop()
            result.append(vertex)

            for adj in self.adjList[vertex]:
                if adj.dest not in visited:
                    visited.add(adj.dest)
                    stack.append(adj.dest)

        print(result)

    def dijkstra(self,src: int,dest: int) -> None:
        distances = {v : float('inf') for v in self.adjList.keys()}
        distances[src] = 0

        parent = {v : None for v in self.adjList.keys()}


        pq = []
        heapq.heappush(pq,Node(src,0))

        visited = set()

        while pq:
            current_node = heapq.heappop(pq)
            u = current_node.vertex
            if u in visited:
                continue

            if u == dest:
                break

            visited.add(u)
            for adj in self.adjList[u]:
                v = adj.dest
                weight = adj.weight
                new_distance = distances[u] + weight
                if new_distance < distances[v]:
                    distances[v] = new_distance
                    heapq.heappush(pq,Node(v,new_distance))
                    parent[v] = u

        print(f"Distances dictionary: {distances}")

        path =[]
        current = dest
        while current:
            path.append(current)
            current = parent[current]

        path.reverse()

        if not path:
            print("No path found")
            return

        print(path)





if __name__ == '__main__':
    graph = Graph()
    graph.addEdge(0, 1, 1)
    graph.addEdge(0, 2, 2)
    # graph.addEdge(0, 4, 2)
    graph.addEdge(1, 3, 1)
    graph.addEdge(2, 4, 1)
    graph.addEdge(3, 4, 4)
    graph.addEdge(3, 5, 3)
    graph.addEdge(4, 5, 2)
    # graph.addEdge(4, 6, 1)
    graph.addEdge(5, 6, 3)

    graph.dfs(0)
    graph.dijkstra(0, 4)
