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
        self._heap = [0]

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

    def build_heap(self, *args):
        """
        Ads the given arguments to the heap.

        Parameters
        ----------
        args : comparable
            Args to add to the heap.

        """
        self._heap.extend(args)
        self._build_max_heap()

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
        return int(math.floor(index / 2))

    def _max_heapify(self, index):
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
            self._swap(index, largest)
            self._max_heapify(largest)

    def _build_max_heap(self):
        """
        Start's sorting the list to match heap criteria.

        Working bottom up.

        Returns
        -------

        """
        i = math.floor(len(self._heap) / 2)
        while i >= 1:
            self._max_heapify(i)
            i -= 1

    def _swap(self, first_index, second_index):
        """
        Swaps the position of the objects at the given indexes.

        Parameters
        ----------
        first_index : int
            Index of the first object to _swap.
        second_index : int
            Index of the second object to _swap.

        Returns
        -------

        """
        first_node = self._heap[first_index]
        self._heap[first_index] = self._heap[second_index]
        self._heap[second_index] = first_node

    def increase_key(self, i, new_key):
        if new_key > self._heap[i]:
            self._heap[i] = new_key
            parent = self.parent(i)
            while i > 0 and parent > 0 and self._heap[i] > self._heap[parent]:
                self._swap(i, parent)
                i = parent
                parent = self.parent(i)

    def insert(self, key):
        i = len(self._heap)
        self._heap.insert(i, -1)
        self.increase_key(i, key)

    def extract_max(self):
        """
        Returns the max key, and removes it from the heap.

        Returns
        -------
        comparable
            Maximal key.
        """
        return self.remove(1)

    def find_max(self):
        """
        Returns the max key, without removing it.

        Returns
        -------
        comparable
            Maximal key
        """
        return self._heap[1]

    def delete_max(self):
        """
        Deletes the max key.

        Returns
        -------

        """
        self.remove(1)

    def remove(self, i):
        removed = self._heap[i]
        last_index = self.size() - 1
        self._swap(i, last_index)
        self._heap.remove(removed)
        if i != last_index:
            if i == 1 or self._heap[i] < self._heap[self.parent(i)]:
                self._max_heapify(i)
            else:
                self.increase_key(i, self._heap[i])
        return removed

    def size(self):
        """
        Returns the number of elements in the heap.

        Returns
        -------
        int
            Number of elements in the heap.
        """
        return len(self._heap)

    def is_empty(self):
        """
        Returns weather the heap is empty or not.

        Returns
        -------
        bool
            True if empty, False if not.
        """
        return self.size() < 1

        # TODO: Unittests.


if __name__ == '__main__':
    max_heap = MaxHeap()
    max_heap.build_heap(8, 2, 3, 9, 7, 1, 10, 16, 4, 14)
    print('Build:           ', max_heap)
    max_heap.increase_key(6, 15)
    print('Increase key 6:  ', max_heap)
    max_heap.insert(12)
    print('Insert 12:       ', max_heap)
    max_heap.delete_max()
    print('Delete max:      ', max_heap)
