import math


class MaxHeap:
    """
    MaxHeap implementation.
    """
    def __init__(self):
        """
        Constructor.

        Initializes the list, backing up the heap.
        """
        self._heap = [None]

    def __str__(self):
        """
        String representation of the heap.

        Is the string representation of the list without it's first element.

        Returns
        -------
        str
            String representation.
        """
        return str(self._heap[1:])

    def insert(self, *args):
        """
        Ads the given arguments to the heap.

        Parameters
        ----------
        args : comparable
            Args to add to the heap.

        """
        self._heap.extend(args)
        self.build_max_heap()

    @staticmethod
    def left(index):
        """
        Calculates the left child's index.

        Does not check if the index is in the heaps range!

        Parameters
        ----------
        index : int
            Index to calculate the left child's index for.

        Returns
        -------
        int
            Left child's index.

        """
        return 2 * index

    @staticmethod
    def right(index):
        """
        Calculates the right child's index.

        Does not check if the index is in the heaps range!

        Parameters
        ----------
        index : int
            Index to calculate the right child's index for.

        Returns
        -------
        int
            Right child's index.

        """
        return 2 * index + 1

    @staticmethod
    def parent(index):
        """
        Calculates the parents index.

        Parameters
        ----------
        index : int
            Index to calculate the parent's index for.

        Returns
        -------
        int
            Parent's index.

        """
        return math.floor(index / 2)

    def max_heapify(self, index):
        """
        Build's local heap for a node and it's childes.

        Parameters
        ----------
        index : int
            Nodes index.

        Returns
        -------

        """
        l, r = self.left(index), self.right(index)
        if l < len(self._heap) and self._heap[l] > self._heap[index]:
            largest = l
        else:
            largest = index
        if r < len(self._heap) and self._heap[r] > self._heap[largest]:
            largest = r
        if largest is not index:
            self.swap(index, largest)
            self.max_heapify(largest)

    def build_max_heap(self):
        """
        Start's sorting the list to match heap criteria.

        Working bottom up.

        Returns
        -------

        """
        i = math.floor(len(self._heap) / 2)
        while i >= 1:
            self.max_heapify(i)
            i -= 1

    def swap(self, first_index, second_index):
        """
        Swaps the position of the objects at the given indexes.

        Parameters
        ----------
        first_index : int
            Index of the first object to swap.
        second_index : int
            Index of the second object to swap.

        Returns
        -------

        """
        first_node = self._heap[first_index]
        self._heap[first_index] = self._heap[second_index]
        self._heap[second_index] = first_node

    # TODO: Methods to implement in the future.

    def lookup(self, key):
        pass

    def extract_max(self):
        pass

    def extract_min(self):
        pass

    # TODO: Unittests.


if __name__ == '__main__':
    max_heap = MaxHeap()
    max_heap.insert(8, 2, 3, 9, 7, 1, 10, 16, 4, 14)
    print(max_heap)
