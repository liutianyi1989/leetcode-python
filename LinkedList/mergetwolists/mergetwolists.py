from LinkedList.base.linkedlist import *

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    p1 = l1.head
    p2 = l2.head

    helper = ListNode(0)
    pre = helper
    while None != p1 and None != p2:
        if p1.val < p2.val:
            pre.next = p1
            p1 = p1.next
        else:
            pre.next = p2
            p2 = p2.next
        pre = pre.next

    if None != p1 :
        pre.next = p1
    elif None != p2:
        pre.next = p2

    return helper.next
