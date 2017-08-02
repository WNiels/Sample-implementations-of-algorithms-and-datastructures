from enum import Enum


class BinaryTreeNode:
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
        parent : BinaryTreeNode
            Parent node.
        left : BinaryTreeNode
            Left child node.
        right : BinaryTreeNode
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
        other : BinaryTreeNode
            TreeNode to compare this TreeNode to.

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
        Iterator returning this BinaryTreeNode and it's child Nodes in order of their keys.

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
        BinaryTreeNode
            Left child of this TreeNode.

        """
        return self._left

    @left.setter
    def left(self, left):
        """
        Setter for the left child property.

        Parameters
        ----------
        left : BinaryTreeNode
            Value to set as left child.

        """
        self._left = left

    @property
    def right(self):
        """
        Returns the right child property's value.

        Returns
        -------
        BinaryTreeNode
            Right child of this TreeNode.

        """
        return self._right

    @right.setter
    def right(self, right):
        """
        Setter for the right child property.

        Parameters
        ----------
        right : BinaryTreeNode
            Value to set as right child.

        """
        self._right = right

    @property
    def parent(self):
        """
        Returns the parent property's value.

        Returns
        -------
        BinaryTreeNode
            The parent TreeNode.

        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent property.

        Parameters
        ----------
        parent : BinaryTreeNode
            TreeNode to set as parent.

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
            Key of the BinaryTreeNode to be deleted.

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

    def delete(self, node):
        self.delete(node.key)

    def lookup(self, key):
        """
        Returns the TreeNode with the given key.

        Parameters
        ----------
        key : value comparable by >,<,==
            Key of the TreeNode to return.

        Returns
        -------
        BinaryTreeNode
            The TreeNode matching the given key.

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
        Inserts a given key value pair as BinaryTreeNode into the tree.
        Overriding any BinaryTreeNode with the same key!

        Parameters
        ----------
        key : value comparable by >,<,==
            Key to insert the BinaryTreeNode (value) by.

        value : object
            Object to be stored in the tree.

        """
        return self.insert(BinaryTreeNode(key=key, value=value))

    def insert(self, node):
        if self.key == node.key:
            self.value = node.value
        elif self.key > node.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        elif self.key < node.key:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)
        return node

    def get_min(self):
        """
        Gets the TreeNode with the minimal key in this (sub-)tree.

        EG. gets the outermost left leaf of this tree.

        Returns
        -------
        BinaryTreeNode
            TreeNode with minimal key.

        """
        min_node = self
        while min_node.left:
            min_node = min_node.left
        return min_node

    def get_max(self):
        """
        Gets the TreeNode with the maximal key in this (sub-)tree.

        Eg. gets the outermost right leaf of this tree.

        Returns
        -------
        BinaryTreeNode
            TreeNode with maximal key.

        """
        max_node = self
        while max_node.right:
            max_node = max_node.right
        return max_node

    def successor(self):
        """
        Gets the TreeNode with the next higher key.

        Returns
        -------
        BinaryTreeNode
            TreeNode with next higher key.

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
        Gets the TreeNode with the next lower key.

        Returns
        -------
        BinaryTreeNode
            TreeNode with the next lower key.

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


class AVLTreeNode:
    def __init__(self, key, value=None, parent=None, left=None, right=None):
        self._key = key
        self._value = value
        self._balance = 0
        self._parent = parent
        self._left = left
        self._right = right

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @value.deleter
    def value(self):
        self._value = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node

    @parent.deleter
    def parent(self):
        self._parent = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @left.deleter
    def left(self):
        self._left = None

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

    @right.deleter
    def right(self):
        self._right = None


class Color(Enum):
    """

    """
    RED = 1
    BLACK = 2


class RBTree:
    """

    """

    def __init__(self):
        """

        """
        self._root = None

    def __str__(self):
        # result = ''
        # for i in self:
        #     result += ', '+str(i.key)
        ret = str(self.root)
        ret += "---"
        return ret

    def __iter__(self):
        """
        Iterator returning this BinaryTreeNode and it's child Nodes in order of their keys.

        Returns
        -------
        Iter
            Iterator returning Nodes.
        """
        if self.root:
            yield from self.root

    @property
    def root(self):
        """

        Returns
        -------

        """
        return self._root

    @root.setter
    def root(self, node):
        """

        Parameters
        ----------
        node

        Returns
        -------

        """
        self._root = node

    class RBTreeNode:
        """

        """

        def __init__(self, key, value=None, parent=None, left=None, right=None):
            self._key = key
            self._value = value
            self._color = Color.RED
            self._parent = parent
            self._left = left
            self._right = right

        def __iter__(self):
            """
            Iterator returning this BinaryTreeNode and it's child Nodes in order of their keys.

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

        def __str__(self, level=0):
            ret = ''
            if self.right:
                ret += self.right.__str__(level + 1)
            ret += "\t" * level + repr(self.key) + repr(self.color) + "\n"
            if self.left:
                ret += self.left.__str__(level + 1)
            return ret

        @property
        def key(self):
            return self._key

        @key.setter
        def key(self, key):
            self._key = key

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = value

        @value.deleter
        def value(self):
            self._value = None

        @property
        def color(self):
            return self._color

        @color.setter
        def color(self, color):
            self._color = color

        @property
        def parent(self):
            return self._parent

        @parent.setter
        def parent(self, node):
            self._parent = node

        @parent.deleter
        def parent(self):
            self._parent = None

        @property
        def left(self):
            return self._left

        @left.setter
        def left(self, node):
            self._left = node

        @left.deleter
        def left(self):
            self._left = None

        @property
        def right(self):
            return self._right

        @right.setter
        def right(self, node):
            self._right = node

        @right.deleter
        def right(self):
            self._right = None

        def successor(self):
            """
            Gets the TreeNode with the next higher key.

            Returns
            -------
            BinaryTreeNode
                TreeNode with next higher key.

            """
            # TODO: für RBTree anpassen oder als Node funktion?
            n = self
            if n.right:
                return n.right.get_min()
            p = n.parent
            while p and n is p.right:
                n = p
                p = p.parent
            return p

        def get_min(self):
            """
            Gets the TreeNode with the minimal key in this (sub-)tree.

            EG. gets the outermost left leaf of this tree.

            Returns
            -------
            BinaryTreeNode
                TreeNode with minimal key.

            """
            min_node = self
            while min_node.left:
                min_node = min_node.left
            return min_node

        def get_max(self):
            """
            Gets the TreeNode with the maximal key in this (sub-)tree.

            Eg. gets the outermost right leaf of this tree.

            Returns
            -------
            BinaryTreeNode
                TreeNode with maximal key.

            """
            max_node = self
            while max_node.right:
                max_node = max_node.right
            return max_node

    def insert(self, key, value=None):
        """

        Parameters
        ----------
        key
        value

        Returns
        -------

        """
        print(self)
        y = None
        x = self.root
        while x is not None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        z = self.RBTreeNode(key=key, value=value)
        if y is None:
            self.root = z
        else:
            z.parent = y
            if z.key < y.key:
                y.left = z
            else:
                y.right = z
        self._insert_fixup(z)
        return z

    def _insert_fixup(self, z):
        # TODO: Siehe Screenshot, rotes Blatt mir rotem Parent!
        """

        Parameters
        ----------
        z

        Returns
        -------

        """
        while z.parent and z.parent.color is Color.RED:
            if z.parent is z.parent.parent.left:
                y = z.parent.parent.right
                if y and y.color is Color.RED:
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    y.color = Color.BLACK
                    z = z.parent.parent
                else:
                    if z is z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self._right_rotate(z)
            else:
                y = z.parent.parent.left
                if y and y.color is Color.RED:
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    y.color = Color.BLACK
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self._left_rotate(z)
        self.root.color = Color.BLACK

    def _left_rotate(self, x):
        """

        Parameters
        ----------
        x

        Returns
        -------

        """
        if x.right:
            y = x.right
            x.right = y.left
            y.left = x
            y.parent = x.parent
            if x.parent is None:
                self.root = y
            else:
                if x.parent.left is x:
                    x.parent.left = y
                else:
                    x.parent.right = y

    def _right_rotate(self, y):
        """

        Parameters
        ----------
        y

        Returns
        -------

        """
        if y.left:
            x = y.left
            y.left = x.right
            x.right = y
            x.parent = y.parent
            if y.parent is None:
                self.root = x
            else:
                if y.parent.left is y:
                    y.parent.left = x
                else:
                    y.parent.right = x

    def delete(self, z):
        """

        Parameters
        ----------
        z

        Returns
        -------

        """
        y = z
        orgicolor = y.color
        if z.left is None:
            x = z.right
            self._transplant(z, z.right)
        else:
            if z.right is None:
                x = z.left
                self._transplant(z, z.left)
            else:
                y = z.successor()
                orgicolor = y.color
                x = y.right
                if y.parent is z:
                    x.parent = y
                else:
                    self._transplant(y, y.right)
                    y.right = z.right
                    y.right.parent = y
                self._transplant(z, y)
                y.left = z.left
                y.left.parent = y
                y.color = z.color
        if orgicolor is Color.BLACK:
            self._delete_fixup(x)

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        else:
            if u is u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
        v.parent = u.parent

    def _delete_fixup(self, x):
        while x is not self.root and x.color is Color.BLACK:
            if x is x.parent.left:
                w = x.parent.right
                if w.color is Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color is Color.BLACK and w.right.color is Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color is Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color is Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color is Color.BLACK and w.left.color is Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color is Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = Color.BLACK


class TreeNode:
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
            A user chosen value to be stored in this BinaryTreeNode.
        children : TreeNode
            Child nodes of this node.

        """
        self._elements = [val] + list(children)

    @property
    def children(self):
        """
        Gets the child nodes.

        Returns
        -------
            *BinaryTreeNode
                List of child nodes.

        """
        return self._elements[1:]

    @children.setter
    def children(self, *children):
        """
        Sets the child nodes, deleting any current child nodes.

        Parameters
        ----------
        children : TreeNode
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
        for node in self.bfs(last):
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


if __name__ == '__main__':
    tree = RBTree()
    tree.insert(12)
    tree.insert(6)
    tree.insert(19)
    tree.insert(16)
    tree.insert(13)
    tree.insert(14)
    tree.insert(17)
    tree.insert(18)
