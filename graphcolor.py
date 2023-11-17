class GraphGreedyColoring:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}
        
    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        
        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]

    def greedy_coloring(self):
        result = {}
        for vertex in range(self.V):
            used_colors = set(result.get(neigh, -1) for neigh in self.graph.get(vertex, []))
            for color in range(self.V):
                if color not in used_colors:
                    result[vertex] = color
                    break

        for vertex, color in result.items():
            print(f"Vertex {vertex} is colored with color {color}")

# Example usage
g = GraphGreedyColoring(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("Greedy Coloring:")
g.greedy_coloring()




class GraphBacktrackingColoring:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.colors = [-1] * vertices

    def is_safe(self, v, c, c_count):
        for i in range(self.V):
            if self.graph[v][i] and c_count[i] == c:
                return False
        return True

    def graph_coloring_util(self, m, c_count):
        if -1 not in self.colors:
            return True
        v = self.colors.index(-1)
        for c in range(1, m + 1):
            if self.is_safe(v, c, c_count):
                self.colors[v] = c
                if self.graph_coloring_util(m, c_count):
                    return True
                self.colors[v] = -1
        return False

    def graph_coloring(self, m):
        c_count = [0] * self.V
        if not self.graph_coloring_util(m, c_count):
            print("Solution does not exist")
            return

        print(f"Backtracking Coloring with {m} colors:")
        for v, color in enumerate(self.colors):
            print(f"Vertex {v} is colored with color {color}")

# Example usage
g = GraphBacktrackingColoring(5)
g.graph = [[0, 1, 1, 1, 0],
           [1, 0, 1, 0, 1],
           [1, 1, 0, 1, 0],
           [1, 0, 1, 0, 1],
           [0, 1, 0, 1, 0]]

m = 3  # Number of colors
g.graph_coloring(m)

