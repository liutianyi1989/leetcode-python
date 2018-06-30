import unittest

from .linkedlist import LinkedList

#python -m unittest linkedlist_test.py
class TestLinkedList(unittest.TestCase):

    def test_init(self):
        data = [1,2,3,4,5]
        l = LinkedList(data)
        print(l.len())