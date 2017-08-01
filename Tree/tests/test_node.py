from unittest import TestCase
from Tree.trees import BinaryTreeNode


class TestNode(TestCase):
    def test_left(self):
        self.assertEqual(BinaryTreeNode(0).left, None)
        left_node = BinaryTreeNode(1)
        node_with_left_child = BinaryTreeNode(0, left=left_node)
        self.assertEqual(node_with_left_child.left, left_node)

    def test_right(self):
        self.assertEqual(BinaryTreeNode(0).right, None)
        right_node = BinaryTreeNode(1)
        node_with_right_child = BinaryTreeNode(0, right=right_node)
        self.assertEqual(node_with_right_child.right, right_node)

    def test_value(self):
        self.assertEqual(BinaryTreeNode(0).value, None)
        self.assertEqual(BinaryTreeNode(0, 'Test').value, 'Test')
        self.assertNotEqual(BinaryTreeNode(0, 'Test').value, None)
        self.assertNotEqual(BinaryTreeNode(0, 'Test').value, 'Bla')
        self.assertNotEqual(BinaryTreeNode(0, None).value, 'Test')

    def test_key(self):
        self.assertEqual(BinaryTreeNode(0), BinaryTreeNode(0))
        self.assertEqual(BinaryTreeNode(0).key, 0)
        self.assertNotEqual(BinaryTreeNode(0), BinaryTreeNode(1))
        self.assertNotEqual(BinaryTreeNode(0).key, 1)

    def test_delete(self):
        root = BinaryTreeNode(8)
        root.insert(3)
        root.insert(10)
        root.delete(10)
        self.assertEqual(root.right, None)
        root.delete(3)
        self.assertEqual(root.left, None)
        root.insert(10)
        root.insert(3)
        root.delete(8)
        self.assertEqual(root.key, 10)
        self.assertEqual(root.left.key, 3)
        self.assertEqual(root.right, None)

        root = BinaryTreeNode(8)
        root.insert(3)
        root.insert(1)
        root.insert(4)
        root.insert(6)
        root.insert(7)
        root.insert(10)
        root.insert(13)
        root.insert(14)
        root.delete(3)
        self.assertEqual(root.lookup(3), (None, None))
        node, parent = root.lookup(6)
        self.assertEqual(node.left, None)
        self.assertEqual(node.right.key, 7)
        self.assertEqual(parent.key, 4)
        self.assertEqual(parent.left.key, 1)

    def test_lookup(self):
        root = BinaryTreeNode(8)
        root.insert(3)
        root.insert(1)
        root.insert(4)
        root.insert(6)
        root.insert(7)
        root.insert(10)
        root.insert(13)
        root.insert(14)
        node, parent = root.lookup(4)
        self.assertEqual(node.key, 4)
        node, parent = root.lookup(8)
        self.assertEqual(parent, None)
        self.assertEqual(root.lookup(92), (None, None))

    def test_insert(self):
        root = BinaryTreeNode(8)
        root.insert(3)
        self.assertEqual(root.left.key, 3)
        self.assertEqual(root.right, None)
        root.insert(1)
        self.assertEqual(root.left.left.key, 1)
        root.insert(4)
        self.assertEqual(root.left.right.key, 4)
        root.insert(10)
        self.assertEqual(root.right.key, 10)
        root.insert(11)
        self.assertEqual(root.right.right.key, 11)
        root.insert(9)
        self.assertEqual(root.right.left.key, 9)
