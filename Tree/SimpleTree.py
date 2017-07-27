from itertools import chain


class Node:
    def __init__(self, val='def', *nodes):
        self._children = list(nodes)
        self._value = val

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @value.deleter
    def value(self):
        self._value = None

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, *nodes):
        self._children = list(nodes)

    @children.deleter
    def children(self, *nodes):
        for node in list(nodes):
            self._children.remove(node)

    def add_children(self, *nodes):
        self._children.append(nodes)

    def __iter__(self):
        return chain(self._children)


if __name__ == "__main__":
    tree = Node('Root')
    tree.children = Node('1', Node('1.1'), Node('1.2'), Node('1.3')), Node('2', Node('2.1'), Node('2.2'),
                                                                           Node('2.3')), Node('3'), Node('4')
    for node in tree:
        print(node)
        print(',')
