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

    def get_adj(self, node=None):
        if node is not None:
            return self._edges[node]

    def dfs(self, node=None, goal=None, visited=[]):
        print('Aufruf')
        yield node
        if node is goal:
            raise StopIteration
        else:
            if node not in visited:
                stack = self.get_adj(node)
                print('Node '+str(node)+' :: '+str(stack))
                while not len(stack) is 0:
                    current = stack.pop()
                    visited += [current]
                    self.dfs(node=current, goal=goal, visited=visited)

    def bfs(self):
        pass


if __name__ == "__main__":
    edges = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 5)]
    g = Graph(edges)
    print(g.edges)

    print(g.get_adj(1))

    for node in g.dfs(node=1, goal=5):
        print(node)
