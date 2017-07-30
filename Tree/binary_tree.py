class Node:
    def __init__(self, key, value=None, left=None, right=None):
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
        left : Node
            Left child node.
        right : Node
            Right child node.
        """
        self._left = left
        self._right = right
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

    def delete(self, key):
        """
        Finds and deletes a node by the given key from the tree.

        Parameters
        ----------
        key : value comparable by >,<,==
            Key of the Node to be deleted.

        """
        node_to_delete, parent = self.lookup(key)
        if node_to_delete:
            if node_to_delete.left and node_to_delete.right:
                successor_parent = node_to_delete
                successor = node_to_delete.right
                while successor.left:
                    successor_parent = successor
                    successor = successor.left
                node_to_delete.value = successor.value
                node_to_delete.key = successor.key
                if successor_parent.left is successor:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right
            elif node_to_delete.left:
                if parent:
                    if parent.left is node_to_delete:
                        parent.left = node_to_delete.left
                    else:
                        parent.right = node_to_delete.left
                else:
                    node_to_delete.key = node_to_delete.left.key
                    node_to_delete.value = node_to_delete.left.value
                    node_to_delete.right = node_to_delete.left.right
                    node_to_delete.left = node_to_delete.left.left
            elif node_to_delete.right:
                if parent:
                    if parent.left is node_to_delete:
                        parent.left = node_to_delete.right
                    else:
                        parent.right = node_to_delete.right
                else:
                    node_to_delete.key = node_to_delete.right.key
                    node_to_delete.value = node_to_delete.right.value
                    node_to_delete.left = node_to_delete.right.left
                    node_to_delete.right = node_to_delete.right.right
            else:
                if parent:
                    if parent.left is node_to_delete:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    del node_to_delete

    def lookup(self, key, parent=None):
        """
        Returns a Node and it's parent (if present) by a given key.

        Parameters
        ----------
        key : value comparable by >,<,==
            Key of the Node to return.
        parent : Node
            Used vor recursion!
            Parent Node of the current Node looked at.

        Returns
        -------
        (Node, Node)
            The Node matching the given key as first and it's parent Node as second parameter.

        """
        if key == self.key:
            return self, parent
        elif key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        else:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None

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
                self.left = Node(value=value, key=key)
            else:
                self.left.insert(value=value, key=key)
        elif self.key < key:
            if self.right is None:
                self.right = Node(value=value, key=key)
            else:
                self.right.insert(value=value, key=key)


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
