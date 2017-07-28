class Graph:
    def __init__(self, edges=[]):
        self._edges = dict()
        self.add_edges(edges)

    @property
    def edges(self):
        result = []
        for key in self._edges:
            for val in self._edges[key]:
                result.append((key, val))
        return result

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

    def remove_vertices(self, vertices=[]):
        vertices = set(vertices)
        for vertex in vertices:
            self._edges.pop(vertex, None)
        for entry in self._edges:
            self._edges[entry] -= vertices

    def get_vertices(self):
        vertices = set()
        for key in self._edges:
            vertices.add(key)
            vertices = vertices.union(self._edges[key])
        return vertices

    def get_adj(self, node=None):
        if node in self._edges:
            return self._edges[node]
        else:
            return set()

    def get_isolated(self):
        isolated = []
        targets = set()
        for element in self._edges.values():
            targets = targets.union(element)
        for vertex in self.get_vertices():
            if vertex not in targets:
                print(vertex)

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

    def dfs_paths(self, start, goal, path=None):
        if path is None:
            path = [start]
        if start == goal:
            yield path
        for next in self.get_adj(start) - set(path):
            yield from self.dfs_paths(next, goal, path + [next])

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
             ('E', 'F'), ('F', 'C'), ('F', 'E'), ('A', 'G'), ('H', 'E')]
    g = Graph(edges)
    print(g.edges)
    print('dfs')
    for vertex in g.dfs('A'):
        print(vertex)
    print('dfs_path')
    for vertex in g.dfs_paths('A', 'F'):
        print(vertex)
    print('bfs')
    for vertex in g.bfs('A'):
        print(vertex)
    print('bfs_path')
    for path in g.bfs_paths('A', 'F'):
        print(path)
    print('All vertices')
    print(g.get_vertices())
    print('Isolated')
    g.get_isolated()
    print('Remove A')
    g.remove_vertices(['A'])
    print(g.get_vertices())
