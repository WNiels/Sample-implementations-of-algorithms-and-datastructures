from unittest import TestCase
from Tree.binary_tree import Node


class TestNode(TestCase):
    def test_left(self):
        self.assertEqual(Node(0).left, None)
        left_node = Node(1)
        node_with_left_child = Node(0, left=left_node)
        self.assertEqual(node_with_left_child.left, left_node)

    def test_right(self):
        self.assertEqual(Node(0).right, None)
        right_node = Node(1)
        node_with_right_child = Node(0, right=right_node)
        self.assertEqual(node_with_right_child.right, right_node)

    def test_value(self):
        self.assertEqual(Node(0).value, None)
        self.assertEqual(Node(0, 'Test').value, 'Test')
        self.assertNotEqual(Node(0, 'Test').value, None)
        self.assertNotEqual(Node(0, 'Test').value, 'Bla')
        self.assertNotEqual(Node(0, None).value, 'Test')

    def test_key(self):
        self.assertEqual(Node(0), Node(0))
        self.assertEqual(Node(0).key, 0)
        self.assertNotEqual(Node(0), Node(1))
        self.assertNotEqual(Node(0).key, 1)

    def test_delete(self):
        self.fail()

    def test_lookup(self):
        self.fail()

    def test_insert(self):
        self.fail()
