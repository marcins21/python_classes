from node import Node
from singlelist import SingleList
import unittest

class TestSingleList(unittest.TestCase):
    def test_remove_tail(self):
        my_list = SingleList()
        my_list.insert_head(Node(5))
        my_list.insert_head(Node(50))
        my_list.insert_head(Node(500))
        self.assertEqual(my_list.remove_tail().data, 5)
        self.assertEqual(my_list.remove_tail().data, 50)
        self.assertEqual(my_list.remove_tail().data, 500)
        self.assertEqual(my_list.length, 0)

    def test_join_lists(self):
        my_list1 = SingleList()
        my_list1.insert_head(Node(3))
        my_list1.insert_head(Node(9))
        my_list1.insert_head(Node(6))
        my_list2 = SingleList()
        my_list2.insert_head(Node(7))
        my_list2.insert_head(Node(55))
        my_list2.insert_head(Node(1))

        my_list1.join(my_list2)

        self.assertEqual(my_list1.head.data, 6)
        self.assertEqual(my_list1.head.next.data, 9)
        self.assertEqual(my_list1.tail.data, 7)
        self.assertEqual(my_list1.length, 6)


if __name__ == '__main__':
    unittest.main()