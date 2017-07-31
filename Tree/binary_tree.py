class Node:
    """
    Binary Tree implementation.
    + The left child nodes key is always smaller then the parents.
    + The right child nodes key is always greater the the parents.
    """
    def __init__(self, key, value=None, parent=None, left=None, right=None):
        """
        Constructor

        This constructor allows for manually setting the child nodes. This should be donne carefully
        and is best avoided.

        Parameters
        ----------
        key : value comparable by >,<,==
            Value by which the nodes are ordered inside the tree.
        value : object
            Object to be stored in this node.
        parent : Node
            Parent node.
        left : Node
            Left child node.
        right : Node
            Right child node.
        """
        self._left = left
        self._right = right
        self._parent = parent
        self._value = value
        self._key = key

    def __eq__(self, other):
        """
        A node is equal to another if all their attributes and their child nodes are equal.

        Parameters
        ----------
        other : Node
            Node to compare this Node to.

        Returns
        -------
        bool
            True if the nodes are equal, False if not.
        """
        if not other:
            return False
        if not self.__dict__ == other.__dict__:
            return False
        return self.left == other.left and self.right == other.right

    def __iter__(self):
        """
        Iterator returning this Node and it's child Nodes in order of their keys.

        Returns
        -------
        Iter
            Iterator returning Nodes.
        """
        if self.left:
            yield from self.left
        yield self
        if self.right:
            yield from self.right

    @property
    def left(self):
        """
        Returns the left child property's value.

        Returns
        -------
        Node
            Left child of this Node.

        """
        return self._left

    @left.setter
    def left(self, left):
        """
        Setter for the left child property.

        Parameters
        ----------
        left : Node
            Value to set as left child.

        """
        self._left = left

    @property
    def right(self):
        """
        Returns the right child property's value.

        Returns
        -------
        Node
            Right child of this Node.

        """
        return self._right

    @right.setter
    def right(self, right):
        """
        Setter for the right child property.

        Parameters
        ----------
        right : Node
            Value to set as right child.

        """
        self._right = right

    @property
    def parent(self):
        """
        Returns the parent property's value.

        Returns
        -------
        Node
            The parent Node.

        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent property.

        Parameters
        ----------
        parent : Node
            Node to set as parent.

        """
        self._parent = parent

    @property
    def value(self):
        """
        Getter for the nodes value.

        Returns
        -------
        object
            The object stored as the nodes value.

        """
        return self._value

    @value.setter
    def value(self, val):
        """
        Setter for the nodes value.

        Parameters
        ----------
        val : object
            Object to be stored as the nodes value.

        """
        self._value = val

    @property
    def key(self):
        """
        Getter for the nodes key.

        Returns
        -------
        value comparable by >,<,==
            The key set to order this node in the tree.

        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Setter for the nodes key.

        Parameters
        ----------
        key : value comparable by >,<,==
            The value to order this node in the tree by.

        """
        self._key = key

    # TODO: Use parent attr.
    def delete(self, key):
        """
        Finds and deletes a node by the given key from the tree.

        Parameters
        ----------
        key : value comparable by >,<,==
            Key of the Node to be deleted.

        """
        n = self.lookup(key)
        if n:
            if n.left and n.right:
                y = n.successor()
                self.delete(y.key)
                n.key = y.key
                n.value = y.value
            elif n.left:
                if n.parent:
                    n.left.parent = n.parent
                    if n.parent.left is n:
                        n.parent.left = n.left
                    else:
                        n.parent.right = n.left
                else:
                    n.key = n.left.key
                    n.value = n.left.value
                    n.left = n.left.left
                    n.right = n.left.right
            elif n.right:
                if n.parent:
                    n.right.parent = n.parent
                    if n.parent.left is n:
                        n.parent.left = n.right
                    else:
                        n.parent.right = n.right
                else:
                    n.key = n.right.key
                    n.value = n.right.value
                    n.left = n.right.left
                    n.right = n.right.right
            else:
                if n.parent:
                    if n.parent.left is n:
                        n.parent.left = None
                    else:
                        n.parent.right = None

    def lookup(self, key):
        """
        Returns the Node with the given key.

        Parameters
        ----------
        key : value comparable by >,<,==
            Key of the Node to return.

        Returns
        -------
        Node
            The Node matching the given key.

        """
        if key == self.key:
            return self
        elif key < self.key:
            if self.left:
                return self.left.lookup(key)
            else:
                return None
        else:
            if self.right:
                return self.right.lookup(key)
            else:
                return None

    def insert(self, key, value=None):
        """
        Inserts a given key value pair as Node into the tree.
        Overriding any Node with the same key!

        Parameters
        ----------
        key : value comparable by >,<,==
            Key to insert the Node (value) by.

        value : object
            Object to be stored in the tree.

        """
        if self.key == key:
            self.value = value
        elif self.key > key:
            if self.left is None:
                self.left = Node(value=value, key=key, parent=self)
            else:
                self.left.insert(value=value, key=key)
        elif self.key < key:
            if self.right is None:
                self.right = Node(value=value, key=key, parent=self)
            else:
                self.right.insert(value=value, key=key)

    def get_min(self):
        """
        Gets the Node with the minimal key in this tree.

        EG. gets the outermost left leaf of this tree.

        Returns
        -------
        Node
            Node with minimal key.

        """
        min_node = self
        while min_node.left:
            min_node = min_node.left
        return min_node

    def get_max(self):
        """
        Gets the Node with the maximal key in this tree.

        Eg. gets the outermost right leaf of this tree.

        Returns
        -------
        Node
            Node with maximal key.

        """
        max_node = self
        while max_node.right:
            max_node = max_node.right
        return max_node

    def successor(self):
        """
        Gets the Node with the next higher key.

        Returns
        -------
        Node
            Node with next higher key.

        """
        n = self
        if n.right:
            return n.right.get_min()
        p = n.parent
        while p and n is p.right:
            n = p
            p = p.parent
        return p

    def predecessor(self):
        """
        Gets the Node with the next lower key.

        Returns
        -------
        Node
            Node with the next lower key.

        """
        n = self
        if n.left:
            return n.left.get_max()
        p = n.parent
        while p and n is p.left:
            n = p
            p = p.parent
        return p

    # TODO: Methods to implement in teh future:

    def get_leafs(self):
        pass

    def min_depth(self):
        pass

    def max_depth(self):
        pass

    def merge_with_binary_tree(self, binary_tree):
        pass

if __name__ == '__main__':
    root = Node(8)
    root.insert(3)
    root.insert(1)
    root.insert(4)
    root.insert(6)
    root.insert(7)
    root.insert(10)
    root.insert(13)
    root.insert(14)

    root2 = root

    print(root == root2)
    print(root == root2.right)
    root2.delete(10)
    root2.delete(1)
    root2.delete(20)

    for node in root:
        print(node.key)
    for node in root2:
        print(node.key)
