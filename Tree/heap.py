class MinHeap:
    def __init__(self):
        """
        For convenience the [0] element of the list is reserved and we start with the [1] element.
        """
        self._heap = [(None, None)]

    def insert(self, key, value=None):
        self._heap.append((key, value))
        i = len(self._heap)-1
        self.sift_up(i)

    def remove(self):
        # TODO: Implement
        pass

    def sift_up(self, index):
        parent_index = self.get_parent_index(index)
        if parent_index:
            if self._heap[parent_index][0] > self._heap[index][0]:
                parent = self._heap[parent_index]
                self._heap[parent_index] = self._heap[index]
                self._heap[index] = parent
                self.sift_up(parent_index)

    @staticmethod
    def get_parent_index(index):
        parent_index = index / 2
        if index < 1:
            return None
        else:
            return parent_index

    def get_left_child(self, index):
        left_child = 2 * index
        if index < len(self._heap):
            return left_child
        else:
            return None

    def get_right_child(self, index):
        right_child = 2 * index + 1
        if index < len(self._heap):
            return index
        else:
            return None
