class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    #构造函数，传入list
    def __init__(self, data):
        self.head = ListNode(0)
        cur = self.head
        for i in data:
            newNode = ListNode(i)
            cur.next = newNode
            cur = cur.next

    #获取链表长度
    def len(self):
        len = 0
        cur = self.head.next
        while None != cur:
            len = len+1
            cur = cur.next
        return len