class Graph:
    def __init__(self, edges=[]):
        print('init')
        self._edges = dict()
        self.add_edges(edges)

    @property
    def edges(self):
        print('prop')
        return self._edges

    @edges.setter
    def edges(self, edges=[]):
        print('setter')
        self._edges.clear()
        self.add_edges(edges)

    @edges.deleter
    def edges(self):
        print('deleter')
        self._edges.clear()

    def add_edges(self, edges=[]):
        print('add')
        for edge in edges:
            print(edge)
            if edge[0] in self._edges:
                self._edges[edge[0]] += [edge[1]]
            else:
                self._edges[edge[0]] = [edge[1]]

    def dfs(self):
        pass

    def bfs(self):
        pass


if __name__ == "__main__":
    edges = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 5)]
    g = Graph(edges)
    print(g.edges)
