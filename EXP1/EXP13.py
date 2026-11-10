from collections import deque


class Graph:
    def __init__(self):
        # Using an adjacency list to represent the graph
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    # BFS Traversal Algorithm
    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        traversal_result = []

        while queue:
            vertex = queue.popleft()
            traversal_result.append(vertex)

            # Visit all adjacent vertices in sorted order for deterministic output
            for neighbor in sorted(self.graph.get(vertex, [])):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_result

    # DFS Traversal Algorithm
    def dfs(self, start_vertex):
        visited = set()
        traversal_result = []
        self._dfs_recursive(start_vertex, visited, traversal_result)
        return traversal_result

    def _dfs_recursive(self, vertex, visited, traversal_result):
        visited.add(vertex)
        traversal_result.append(vertex)

        # Visit all adjacent vertices in sorted order for deterministic output
        for neighbor in sorted(self.graph.get(vertex, [])):
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited, traversal_result)


# Driver code constructing the example graph and displaying traversals
if __name__ == "__main__":
    # Constructing the graph matching the example:
    #         A
    #        / \
    #       B   C
    #      / \   \
    #     D   E   F

    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')

    start_node = 'A'

    # Perform BFS and DFS
    bfs_result = g.bfs(start_node)
    dfs_result = g.dfs(start_node)

    # Display results matching the expected output format
    print("For the graph:")
    print("        A")
    print("       / \\")
    print("      B   C")
    print("     / \\   \\")
    print("    D   E   F\n")

    print(f"BFS Traversal: {' '.join(bfs_result)}")
    print(f"DFS Traversal: {' '.join(dfs_result)}")
    
    print("\nStep-by-Step Traversal")
    print("BFS (Breadth First Search):")
    print(" → ".join(bfs_result))
    print("DFS (Depth First Search):")
    print(" → ".join(dfs_result))
