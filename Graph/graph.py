class Graph:
    def __init__(self, edges=[]):
        self._edges = dict()
        self.add_edges(edges)

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, edges=[]):
        self._edges.clear()
        self.add_edges(edges)

    @edges.deleter
    def edges(self):
        self._edges.clear()

    def add_edges(self, edges=[]):
        for edge in edges:
            if edge[0] in self._edges:
                self._edges[edge[0]].add(edge[1])
            else:
                self._edges[edge[0]] = set([edge[1]])

    def get_adj(self, node=None):
        if node in self._edges:
            return self._edges[node]
        else:
            return set()

    def dfs(self, start=None):
        visited = set()
        stack = [start]
        while stack:
            vertex = stack.pop()
            yield vertex
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(self.get_adj(vertex) - visited)
        return

    def bfs(self, start=None):
        visited = set()
        stack = [start]
        while stack:
            vertex = stack.pop(0)
            yield vertex
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(self.get_adj(vertex) - visited)
        return

    def bfs_paths(self, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in self.get_adj(vertex) - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))


if __name__ == "__main__":
    edges = [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'D'), ('B', 'E'), ('C', 'A'), ('C', 'F'), ('D', 'B'), ('E', 'B'),
             ('E', 'F'), ('F', 'C'), ('F', 'E')]
    g = Graph(edges)
    print(g.edges)
    print('dfs')
    for vertex in g.dfs(1):
        print(vertex)
    print('bfs')
    for vertex in g.bfs(1):
        print(vertex)
    print('bfs_path')
    for path in g.bfs_paths(1, 5):
        print(path)
