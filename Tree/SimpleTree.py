class Node:
    __slots__ = ['_elements']

    def __init__(self, val, *children):
        self._elements = [val] + list(children)

    @property
    def children(self):
        return self._elements[1:]

    @children.setter
    def children(self, lst):
        self._elements = self._elements[:1] + list(lst)

    @children.deleter
    def children(self):
        self._elements = self._elements[:1]

    @property
    def value(self):
        return self._elements[0]

    def __repr__(self):
        return "<{}: {} :: {} child nodes>".format(self.__class__.__name__, self.value, len(self.children))

    """
    Iterate in pre-order depth-first search order (DFS)
    """

    def __iter__(self):
        yield self
        for child in self.children:
            yield from child

    def values(self):
        for node in self:
            yield node.value


if __name__ == "__main__":
    tree = Node('Root')
    tree.children = Node('1', Node('1.1'), Node('1.2'), Node('1.3')), Node('2', Node('2.1'), Node('2.2'),
                                                                           Node('2.3')), Node('3'), Node('4')
    for node in tree:
        print(node.values)
