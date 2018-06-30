import unittest

from .mergetwolists import *

#python -m unittest MergeTwoLists_test.py
class TestMergeTwoLists(unittest.TestCase):

    def test_init(self):
        a1 = [1,3,5]
        a2 = [2,4,6]
        l1 = LinkedList(a1)
        l2 = LinkedList(a2)
        r = mergeTwoLists(l1,l2)
        lr = LinkedList(r)
        print(lr.len())