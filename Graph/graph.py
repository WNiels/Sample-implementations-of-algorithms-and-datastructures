class Graph:
    """
    Basic graph implementation.

    This is a basic directed graph implementation storing it's edges as dict.
    """
    def __init__(self, edges=[]):
        """
        Constructor

        Parameters
        ----------
        edges : *(object, object)
            List of 2-tuples, where each tuples first parameter is the starting node
            and it's second parameter it's end node.
        """
        self._edges = dict()
        self.add_edges(edges)

    @property
    def edges(self):
        """
        Edges property.

        Containing all edges and vertices of the graph.

        Returns
        -------
        *(object, object)
            List of 2-tuples representing a List. Each tuples first parameter is the starting node
            and it's second parameter it's end node.
        """
        result = []
        for key in self._edges:
            for val in self._edges[key]:
                result.append((key, val))
        return result

    @edges.setter
    def edges(self, edges=[]):
        """
        Setter for the edges property.

        Deleting all current edges and adding the new ones.

        Parameters
        ----------
        edges : *(object, object)
            List of 2-tuples, where each tuples first parameter is the starting node
            and it's second parameter it's end node.

        Returns
        -------

        """
        self._edges.clear()
        self.add_edges(edges)

    @edges.deleter
    def edges(self):
        """
        Deleter for edges property.

        Removes all edges from edges property.

        Returns
        -------

        """
        self._edges.clear()

    def add_edges(self, edges=[]):
        """
        Adds edges to the graph, if not already contained.

        Parameters
        ----------
        edges : *(object, object)
            List of 2-tuples, where each tuples first parameter is the starting node
            and it's second parameter it's end node.

        Returns
        -------

        """
        for edge in edges:
            if edge[0] not in self._edges:
                self._edges[edge[0]] = set()
            if edge[1] not in self._edges:
                self._edges[edge[1]] = set()
            self._edges[edge[0]].add(edge[1])

    def remove_vertices(self, vertices=[]):
        """
        Removes all given vertices from the graph.
        Also deleting all edges from ot to those vertices.

        Parameters
        ----------
        vertices : *object
            List of vertices o delete from this graph.

        Returns
        -------

        """
        vertices = set(vertices)
        for vertex in vertices:
            self._edges.pop(vertex, None)
        for entry in self._edges:
            self._edges[entry] -= vertices

    def get_vertices(self):
        """
        Generates a list of all vertices in this graph.

        Returns
        -------
        *object
            Set of all vertices contained in this graph.

        """
        vertices = set()
        for key in self._edges:
            vertices.add(key)
            vertices = vertices.union(self._edges[key])
        return vertices

    def get_adj(self, vertex=None):
        """
        Get's all adjacent vertices of a given vertex.

        Parameters
        ----------
        vertex : object
            Vertex to get adjacent vertices of.

        Returns
        -------
        *object
            Set of all adjacent objects.
        """
        if vertex in self._edges:
            return self._edges[vertex]
        else:
            return set()

    def get_isolated(self):
        """
        Gets all isolated vertices of the graph.

        Isolated vertices are vertices without incoming edges.

        Returns
        -------
        *object
            Set of all isolated nodes in the graph.
        """
        isolated = []
        targets = set()
        for element in self._edges.values():
            targets = targets.union(element)
        for vertex in self.get_vertices():
            if vertex not in targets:
                print(vertex)

    def dfs(self, start=None):
        """
        Returns a dfs iterator for the graph.

        Iterator returning all nodes reachable from a given starting vertex in depth-first-search order.

        Parameters
        ----------
        start : object
            Node to start dfs from.

        Returns
        -------
        iterator
            Iterator for this graph in dfs order.

        """
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
        """
        Returns an iterator with paths from start to goal vertex.

        Iterator contains each path from start to goal with depth-first-search.

        Parameters
        ----------
        start : vertex
            Vertex to start path from.
        goal : vertex
            Vertex to end path at.
        path : *vertex
            List of path's vertices used internally for recursion.

        Returns
        -------
        iterator
            Iterator for path's in dfs order.

        """
        if path is None:
            path = [start]
        if start == goal:
            yield path
        for next in self.get_adj(start) - set(path):
            yield from self.dfs_paths(next, goal, path + [next])

    def bfs(self, start=None):
        """
        Returns a bfs iterator for the graph.

        Iterator returning all nodes reachable from a given starting vertex in breadth-first-search order.

        Parameters
        ----------
        start : object
            Node to start bfs from.

        Returns
        -------
        iterator
            Iterator for this graph in bfs order.

        """
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
        """
        Returns an iterator with paths from start to goal vertex.

        Iterator contains each path from start to goal with breadth-first-search.

        Parameters
        ----------
        start : vertex
            Vertex to start path from.
        goal : vertex
            Vertex to end path at.

        Returns
        -------
        iterator
            Iterator for path's in bfs order.

        """
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
    print(g._edges)
