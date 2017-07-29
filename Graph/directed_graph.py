import uuid


class Vertex:
    def __init__(self, vertex_id=None, value=None):
        if vertex_id is None:
            self._vertex_id = uuid.uuid4()
        else:
            self._vertex_id = vertex_id
        self._value = value
        self._adj = []

    @property
    def id(self):
        return self._vertex_id

    @property
    def value(self):
        return self._value


class Edge:
    def __init__(self, v1, v2, weight=0):
        self._v1 = v1
        self._v2 = v2
        self._weight = weight
    pass


class Graph:
    pass
