class Node:
    """
    Representing a node of a tree holding a value and it's child nodes.
    """
    __slots__ = ['_elements']

    def __init__(self, val, *children):
        """
        Constructor.

        Parameters
        ----------
        val : object
            A user chosen value to be stored in this Node.
        children : Node
            Child nodes of this node.

        """
        self._elements = [val] + list(children)

    @property
    def children(self):
        """
        Gets the child nodes.

        Returns
        -------
            *Node
                List of child nodes.

        """
        return self._elements[1:]

    @children.setter
    def children(self, *children):
        """
        Sets the child nodes, deleting any current child nodes.

        Parameters
        ----------
        children : Node
            Nodes to be added as child's.

        Returns
        -------

        """
        self._elements = self._elements[:1] + list(children)

    @children.deleter
    def children(self):
        """
        Removes any child node from this node.

        Returns
        -------

        """
        self._elements = self._elements[:1]

    @property
    def value(self):
        """
        Returns the value held by this node.

        Returns
        -------
        object
            Value held by this node.

        """
        return self._elements[0]

    def __repr__(self):
        """
        String representation of this node.

        Returns
        -------
        str
            String representation of this node.

        """
        return "<{}: {} :: {} child nodes>".format(self.__class__.__name__, self.value, len(self.children))

    def dfs(self):
        """
        Iterator of this tree in depth-first-search order.

        Returns
        -------
        iterator
            Iterator for this tree in dfs order.
        """
        yield self
        for child in self.children:
            yield from child

    def bfs(self, node=None):
        """
        Iterator of this tree in breadth-first-search order.

        Returns
        -------
        iterator
            Iterator for this tree in bfs order.
        """
        yield self
        last = self
        for node in self.bfs(self):
            for child in node.children:
                yield child
                last = child
            if last == node:
                return

    def reverse_bfs(self):
        """
        Iterator of this tree in bottom-up (reversed breadth-first-search) order.

        Returns
        -------
        iterator
            Iterator for this tree in bottom-up order.
        """
        result = list()
        for node in self.bfs():
            result.append(node)
        result.reverse()
        return result

    def __iter__(self):
        """
        Iterator of this tree in depth-first-search order.
        @bfs()

        Returns
        -------
        iterator
            Iterator for this tree in dfs order.
        """
        return self.dfs()

    def values(self):
        for node in self:
            yield node.value


if __name__ == "__main__":
    tree = Node('Root')
    tree.children = Node('1', Node('1.1'), Node('1.2'), Node('1.3')), Node('2', Node('2.1'), Node('2.2'),
                                                                           Node('2.3')), Node('3'), Node('4')
    #                     Root
    #     1               2           3   4
    # 1.1 1.2 1.3     2.1 2.2 2.3

    for node in tree.reverse_bfs():
        print(node.values)
